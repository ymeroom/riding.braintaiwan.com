#!/usr/bin/env python3
"""Turn a trip photo into a Japanese woodblock-style illustration (no cropping).

    python3 scripts_v2/photo_to_woodblock.py <photo> <out.jpg> --title 本栖湖 --sub "十一月十八日 夜明" \
        --seal 本栖 --fonts <dir with yuji.ttf / klee.ttf>

Look: mean-shift flattening → colours pulled toward a limited woodblock palette (藍・縹・空・金・朱・墨)
→ ink outlines from edges → washi paper grain → ink frame, vertical title cartouche and red seal.
Needs numpy, Pillow and OpenCV (opencv-python-headless). Output has no EXIF.
"""
import argparse
import numpy as np
import cv2
from PIL import Image, ImageDraw, ImageFont, ImageOps

PALETTE = np.array([  # RGB
    (0x1D, 0x1D, 0x1B),  # 墨
    (0x1F, 0x3A, 0x5F),  # 藍
    (0x3D, 0x5A, 0x7A),  # 縹
    (0x8E, 0xA3, 0xB8),  # 空(淡)
    (0xB9, 0xCF, 0xE0),  # 空
    (0xF3, 0xEA, 0xD5),  # 生成(雪・雲)
    (0xE9, 0xC4, 0x6A),  # 金
    (0xD9, 0xA4, 0x41),  # 黄土
    (0xC8, 0x44, 0x2F),  # 朱
    (0x2E, 0x3D, 0x33),  # 山(深緑)
    (0x5B, 0x4A, 0x3A),  # 焦茶
    (0x6E, 0x8F, 0x45),  # 草色
    (0x9F, 0xBF, 0x5A),  # 若草・萌黄
    (0xC9, 0xD6, 0x5E),  # 黄緑（外套・銀杏）
    (0xE8, 0xBE, 0x96),  # 肌（明）
    (0xC4, 0x8A, 0x62),  # 肌（影）
    (0xE8, 0xA0, 0x9A),  # 鴇色（紅富士・朝焼け）
    (0x8C, 0x5E, 0x6E),  # 紅藤（朝の山肌）
], dtype=np.float32)


def remove_stamp(a):
    """Inpaint the phone's bright date stamp in the bottom-right corner."""
    h, w = a.shape[:2]
    roi = a[int(h * 0.86):, int(w * 0.74):]
    m = (cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY) > 170).astype(np.uint8) * 255
    m = cv2.dilate(m, np.ones((7, 7), np.uint8))
    mask = np.zeros((h, w), np.uint8)
    mask[int(h * 0.86):, int(w * 0.74):] = m
    return cv2.inpaint(a, mask, 9, cv2.INPAINT_TELEA)


def stylize(img, k=18, pull=0.35, stamp=True):
    a = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
    if stamp:
        a = remove_stamp(a)
    a = cv2.pyrMeanShiftFiltering(a, sp=12, sr=22)
    for _ in range(2):
        a = cv2.bilateralFilter(a, 9, 60, 60)
    rgb = cv2.cvtColor(a, cv2.COLOR_BGR2RGB).astype(np.float32)
    # k-means flat regions
    Z = rgb.reshape(-1, 3)
    crit = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 20, 1.0)
    _, lab, cen = cv2.kmeans(Z, k, None, crit, 3, cv2.KMEANS_PP_CENTERS)
    # pull each centre toward the nearest woodblock colour
    d = ((cen[:, None, :] - PALETTE[None, :, :]) ** 2).sum(-1)
    near = PALETTE[d.argmin(1)]
    cen2 = cen * (1 - pull) + near * pull
    flat = cen2[lab.flatten()].reshape(rgb.shape)
    # ink outlines
    gray = cv2.cvtColor(a, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(cv2.GaussianBlur(gray, (5, 5), 0), 30, 90)
    edges = cv2.dilate(edges, np.ones((2, 2), np.uint8))
    ink = cv2.GaussianBlur(edges.astype(np.float32) / 255, (3, 3), 0)[..., None] * 0.75
    out = flat * (1 - ink) + PALETTE[0] * ink
    # washi grain + slight warm wash
    rng = np.random.default_rng(7)
    grain = cv2.GaussianBlur(rng.normal(0, 1, out.shape[:2]).astype(np.float32), (0, 0), 1.2)
    fib = cv2.GaussianBlur(rng.normal(0, 1, out.shape[:2]).astype(np.float32), (0, 0), 6)
    out = out + (grain * 6 + fib * 4)[..., None]
    out = out * 0.94 + np.array([243, 234, 213], np.float32) * 0.06
    return Image.fromarray(np.clip(out, 0, 255).astype(np.uint8))


def frame(img, title, sub, seal, fonts):
    W0, H = img.size
    W = max(W0, H)  # size the frame and lettering by the long side so portrait photos get a readable cartouche
    pad = int(W * 0.035)
    canvas = Image.new("RGB", (W0 + 2 * pad, H + 2 * pad), (239, 226, 198))
    canvas.paste(img, (pad, pad))
    d = ImageDraw.Draw(canvas)
    lw = max(6, W // 300)
    d.rectangle([pad - lw, pad - lw, pad + W0 + lw - 1, pad + H + lw - 1], outline=(29, 29, 27), width=lw)
    big = ImageFont.truetype(f"{fonts}/yuji.ttf", int(W * 0.05))
    small = ImageFont.truetype(f"{fonts}/yuji.ttf", int(W * 0.022))
    # vertical title cartouche (top-left, over the sky)
    cw = int(W * 0.075)
    x0, y0 = pad + int(W * 0.03), pad + int(H * 0.05)
    ch = int(W * 0.05) * len(title) + int(W * 0.05)
    d.rectangle([x0, y0, x0 + cw, y0 + ch], fill=(239, 226, 198), outline=(200, 68, 47), width=max(3, W // 600))
    y = y0 + int(W * 0.025)
    for t in title:
        bb = d.textbbox((0, 0), t, font=big)
        d.text((x0 + (cw - (bb[2] - bb[0])) / 2 - bb[0], y), t, font=big, fill=(29, 29, 27))
        y += int(W * 0.05)
    # subtitle column
    sx = x0 + cw + int(W * 0.012)
    y = y0 + int(W * 0.01)
    for t in sub:
        if t == " ":
            y += int(W * 0.012)
            continue
        bb = d.textbbox((0, 0), t, font=small)
        d.text((sx, y), t, font=small, fill=(246, 239, 220), stroke_width=2, stroke_fill=(29, 29, 27))
        y += int(W * 0.025)
    # red seal under the cartouche
    s = int(W * 0.05)
    sy = y0 + ch + int(W * 0.012)
    d.rectangle([x0 + (cw - s) // 2, sy, x0 + (cw - s) // 2 + s, sy + s], fill=(200, 68, 47))
    sf = ImageFont.truetype(f"{fonts}/yuji.ttf", int(s * 0.42))
    for i, t in enumerate(seal[:2]):
        bb = d.textbbox((0, 0), t, font=sf)
        d.text((x0 + (cw - (bb[2] - bb[0])) / 2 - bb[0], sy + s * 0.06 + i * s * 0.45), t, font=sf, fill=(239, 226, 198))
    return canvas


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("photo")
    ap.add_argument("out")
    ap.add_argument("--title", default="本栖湖")
    ap.add_argument("--sub", default="")
    ap.add_argument("--seal", default="富士")
    ap.add_argument("--fonts", required=True)
    ap.add_argument("--width", type=int, default=2000)
    ap.add_argument("--k", type=int, default=18, help="number of flat colours")
    ap.add_argument("--pull", type=float, default=0.35, help="0–1, how far colours move toward the palette (lower for faces)")
    ap.add_argument("--no-stamp", action="store_true", help="photo has no date stamp; skip the inpainting")
    a = ap.parse_args()
    img = ImageOps.exif_transpose(Image.open(a.photo)).convert("RGB")
    img.thumbnail((a.width, a.width))
    art = frame(stylize(img, k=a.k, pull=a.pull, stamp=not a.no_stamp), a.title, a.sub, a.seal, a.fonts)
    clean = Image.new("RGB", art.size)
    clean.paste(art)
    clean.save(a.out, "JPEG", quality=85, optimize=True, progressive=True)
    print("wrote", a.out, clean.size)


if __name__ == "__main__":
    main()
