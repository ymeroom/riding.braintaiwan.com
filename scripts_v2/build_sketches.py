#!/usr/bin/env python3
"""Build the Japanese hand-drawn itinerary sketches (sketches/dayN.html + sketches/index.html).

Four styles per day: ① 絵巻 ② 旅のしおり ③ 鳥瞰図 ④ 木版.
Reads data/trip.json and dayN_track.gpx only; never touches index.html.
Day 1 uses the hand-drawn SVGs in sketches/_hand/ when present.

    python3 scripts_v2/build_sketches.py
"""
import html
import json
import math
import random
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "sketches"
HAND = OUT / "_hand"

E = html.escape
KD = "〇一二三四五六七八九"

# ---------------------------------------------------------------- helpers

def kanji_digits(n):
    return "".join(KD[int(c)] for c in str(int(n)))


def kanji_num(n):
    n = int(n)
    if n == 0:
        return "〇"
    out = ""
    for unit, ch in ((1000, "千"), (100, "百"), (10, "十")):
        q, n = divmod(n, unit)
        if q:
            out += ("" if q == 1 else KD[q]) + ch
    if n:
        out += KD[n]
    return out


EMOJI = re.compile("[\U0001F000-\U0001FFFF☀-➿️‍]")


def short(name, limit=11):
    s = re.split(r"[➔→]", name)[0] if "：" not in re.split(r"[➔→]", name)[0] or True else name
    s = EMOJI.sub("", s).strip()
    s = re.sub(r"【[^】]*】", "", s)
    if "：" in s:
        s = s.split("：", 1)[1]
    s = re.sub(r"^(晚上|清晨|早上)\s*\d{1,2}:\d{2}\s*", "", s)
    s = re.sub(r"\s*[（(][^）)]*[）)]?", "", s)
    s = s.replace("終點", "").replace("起點", "").strip(" ・/")
    if " / " in s:
        s = s.split(" / ")[0]
    if re.fullmatch(r"[\x00-\x7f]+", s):
        limit = int(limit * 1.7)
    if len(s) > limit:
        s = s[:limit].rstrip() + "…"
    return s or name[:limit]


MOTIF_RULES = [
    ("fireworks", "花火"), ("pagoda", "五重塔"), ("sea", "城崎|城ケ崎"), ("castle", "城"),
    ("waterfall", "瀑"), ("plane", "機場|Skyliner"), ("onsen", "溫泉|温泉|之湯|名湯"),
    ("ginkgo", "銀杏|大學"), ("conifer", "水杉|樹海|松原|林蔭|風穴|冰穴"),
    ("torii", "寺|神社|神宮|明神|帝釋天|雷門|淺草"), ("pass", "峠"), ("bridge", "橋"),
    ("inn", "旅館|飯店|旅舍|HOSTEL|Hostel|Inn|Base|Camp|浩庵|水口|MARUYA|Apt|seaview|宿|guest house"),
    ("maple", "紅葉|楓"), ("lake", "湖|湧泉|八海"), ("sea", "海|灣|港|濱|浜|江之島|台場|羽田"),
    ("susuki", "牧場|高原|芒"), ("river", "川|水岸|CR|自行車道|專用道|綠道"),
    ("town", "市區|站|街|銀座|秋葉原|品川|三島|富士宮|國道|縣道"),
]
DESC_OK = {"sea", "lake", "river", "bridge", "susuki", "maple", "conifer", "onsen", "waterfall"}


def motif_of(p):
    for m, pat in MOTIF_RULES:
        if re.search(pat, p["name"]):
            return m
    for m, pat in MOTIF_RULES:
        if m in DESC_OK and re.search(pat, p.get("desc", "")):
            return m
    return "trees"


# ---------------------------------------------------------------- motifs
# Unit box: base-centre at (0,0), about 100 wide, up to ~100 tall (y negative is up).
# Every shape is stroked with pal['ink'] so a monochrome palette works for stamps.

def _g(body, x, y, s):
    return f'<g transform="translate({x:.1f} {y:.1f}) scale({s:.2f})">{body}</g>'


def motif(kind, x, y, s, P):
    k, sw = P["ink"], P.get("sw", 2.2) / max(s, 0.4)
    S = f'stroke="{k}" stroke-width="{sw:.2f}" stroke-linejoin="round" stroke-linecap="round"'
    b = ""
    if kind == "inn":
        b = (f'<path d="M-30 0V-40H30V0Z" fill="{P["wall"]}" {S}/><path d="M-40 -38L0 -64L40 -38Z" fill="{P["roof"]}" {S}/>'
             f'<path d="M-8 0V-20H8V0" fill="{P["roof"]}" {S}/><path d="M16 -30h8v8h-8z" fill="{P["gold"]}" {S}/>')
    elif kind == "town":
        b = (f'<path d="M-48 0V-46H-20V0Z" fill="{P["wall"]}" {S}/><path d="M-18 0V-72H14V0Z" fill="{P["wall2"]}" {S}/>'
             f'<path d="M16 0V-38H46V0Z" fill="{P["wall"]}" {S}/>'
             f'<path d="M-42 -36h16M-42 -24h16M-12 -62h20M-12 -50h20M-12 -38h20M-12 -26h20M22 -28h18M22 -16h18" fill="none" {S}/>')
    elif kind == "bridge":
        b = (f'<path d="M-52 0H52V-10H-52Z" fill="{P["water"]}" {S}/><path d="M-52 -18H52" fill="none" {S} stroke-width="{sw*1.8:.2f}"/>'
             f'<path d="M-46 -18Q0 -66 46 -18" fill="none" stroke="{P["red"]}" stroke-width="{sw*2:.2f}"/>'
             f'<path d="M-24 -18V-38M0 -18V-44M24 -18V-38" fill="none" stroke="{P["red"]}" stroke-width="{sw:.2f}"/>')
    elif kind == "lake":
        b = (f'<ellipse cx="0" cy="-10" rx="52" ry="13" fill="{P["water"]}" {S}/>'
             f'<path d="M-30 -10q6-4 12 0t12 0M8 -8q6-4 12 0t12 0" fill="none" stroke="{P["paper"]}" stroke-width="{sw:.2f}"/>'
             f'<path d="M-50 -14q-2-18 -8-26M-46 -14q2-20 8-30M44 -16q2-16 8-24" fill="none" {S}/>')
    elif kind == "sea":
        b = (f'<path d="M-54 0V-26Q-27 -34 0 -26T54 -26V0Z" fill="{P["water"]}" {S}/>'
             f'<path d="M-44 -16q8-6 16 0t16 0M4 -12q8-6 16 0t16 0" fill="none" stroke="{P["paper"]}" stroke-width="{sw:.2f}"/>'
             f'<path d="M10 -30V-66L32 -32Z" fill="{P["wall"]}" {S}/><path d="M2 -30H38L32 -24H8Z" fill="{P["roof"]}" {S}/>')
    elif kind == "river":
        b = (f'<path d="M-54 -4Q-20 -20 0 -10T54 -14V-2Q20 4 0 2T-54 6Z" fill="{P["water"]}" {S}/>'
             f'<path d="M-30 -4q6-4 12 0M10 -6q6-4 12 0" fill="none" stroke="{P["paper"]}" stroke-width="{sw:.2f}"/>'
             f'<path d="M-40 -14q-2-16 -8-24M-34 -14q2-18 8-26M34 -18q-2-16 -8-24" fill="none" {S}/>')
    elif kind == "pass":
        b = (f'<path d="M-54 0L-6 -74L54 0Z" fill="{P["green"]}" {S}/><path d="M-6 -74L8 -52L-2 -56L-12 -50Z" fill="{P["paper"]}" {S}/>'
             f'<path d="M30 0V-34" fill="none" {S}/><path d="M18 -44H46V-30H18Z" fill="{P["wall"]}" {S}/>'
             f'<text x="32" y="-33" font-size="12" text-anchor="middle" fill="{k}" font-family="Klee One,Noto Serif TC,serif">峠</text>')
    elif kind == "torii":
        b = (f'<path d="M-24 0V-52M24 0V-52" fill="none" stroke="{P["red"]}" stroke-width="{sw*3:.2f}"/>'
             f'<path d="M-40 -60Q0 -54 40 -60L36 -52H-36Z" fill="{P["ink2"]}" {S}/><path d="M-32 -44H32V-38H-32Z" fill="{P["red"]}" {S}/>'
             f'<path d="M-30 0V-4H-18V0ZM18 0V-4H30V0Z" fill="{P["ink2"]}" {S}/>')
    elif kind == "pagoda":
        t = ""
        for i in range(5):
            w, yy = 30 - i * 4, -i * 16
            t += f'<path d="M{-w-8} {yy-8}L{w+8} {yy-8}L{w} {yy-14}H{-w}Z" fill="{P["ink2"]}" {S}/><path d="M{-w+6} {yy}V{yy-8}H{w-6}V{yy}Z" fill="{P["red"]}" {S}/>'
        b = t + f'<path d="M0 -86V-104" fill="none" {S}/>'
    elif kind == "castle":
        b = (f'<path d="M-46 0L-38 -26H38L46 0Z" fill="{P["grey"]}" {S}/><path d="M-30 -26V-46H30V-26Z" fill="{P["wall"]}" {S}/>'
             f'<path d="M-40 -44L0 -58L40 -44Z" fill="{P["ink2"]}" {S}/><path d="M-18 -56V-72H18V-56Z" fill="{P["wall"]}" {S}/>'
             f'<path d="M-28 -70L0 -84L28 -70Z" fill="{P["ink2"]}" {S}/><path d="M-8 -84l-4-6M8 -84l4-6" fill="none" {S}/>')
    elif kind == "waterfall":
        b = (f'<path d="M-50 0V-70Q-30 -84 -14 -74V0Z" fill="{P["green"]}" {S}/><path d="M50 0V-66Q30 -82 14 -74V0Z" fill="{P["green"]}" {S}/>'
             f'<path d="M-14 -74H14V-6H-14Z" fill="{P["paper"]}" {S}/><path d="M-8 -70V-8M0 -72V-6M8 -70V-8" fill="none" stroke="{P["water"]}" stroke-width="{sw:.2f}"/>'
             f'<ellipse cx="0" cy="-4" rx="30" ry="6" fill="{P["water"]}" {S}/>')
    elif kind == "onsen":
        b = (f'<path d="M-34 -16A34 16 0 0 0 34 -16Z" fill="{P["ink2"]}" {S}/>'
             f'<path d="M-16 -24c-8-10 8-14 0-26M0 -24c-8-10 8-14 0-26M16 -24c-8-10 8-14 0-26" fill="none" stroke="{P["red"]}" stroke-width="{sw*1.4:.2f}"/>')
    elif kind == "fireworks":
        rays = "".join(f'M{math.cos(a)*10:.1f} {-50+math.sin(a)*10:.1f}L{math.cos(a)*34:.1f} {-50+math.sin(a)*34:.1f}' for a in [i * math.pi / 8 for i in range(16)])
        bg = "" if P.get("bare") else f'<circle cx="0" cy="-50" r="44" fill="{P["night"]}" {S}/>'
        b = (bg + f'<path d="{rays}" fill="none" stroke="{P["gold"]}" stroke-width="{sw*1.2:.2f}"/>'
             f'<circle cx="0" cy="-50" r="6" fill="{P["red"]}" stroke="none"/>'
             + ("" if P.get("bare") else f'<path d="M-50 0V-8Q0 -14 50 -8V0Z" fill="{P["water"]}" {S}/>'))
    elif kind == "plane":
        b = (f'<path d="M-46 -40Q-10 -46 36 -44Q48 -42 46 -38Q30 -34 -40 -34Z" fill="{P["wall"]}" {S}/>'
             f'<path d="M-4 -40L16 -64H24L14 -40ZM-2 -36L14 -18H22L14 -36ZM-40 -40L-46 -56H-38L-30 -40Z" fill="{P["ink2"]}" {S}/>'
             f'<path d="M-50 0H50" fill="none" {S}/>')
    elif kind == "ginkgo":
        b = (f'<path d="M-3 0V-30H3V0Z" fill="{P["trunk"]}" {S}/><path d="M0 -26L-34 -44Q-30 -90 0 -96Q30 -90 34 -44Z" fill="{P["gold"]}" {S}/>'
             f'<path d="M30 0V-20" fill="none" {S}/><path d="M30 -16L14 -30Q18 -56 30 -58Q42 -56 46 -30Z" fill="{P["gold"]}" {S}/>')
    elif kind == "conifer":
        b = "".join(f'<path d="M{cx-14} {-8}L{cx} {-h}L{cx+14} -8Z" fill="{P["green_d"]}" {S}/><path d="M{cx} 0V-8" fill="none" {S}/>'
                    for cx, h in ((-30, 62), (0, 84), (30, 56)))
    elif kind == "susuki":
        b = (f'<path d="M-40 0q4-40 -12-70M-28 0q2-44 14-76M-16 0q6-36 26-58M8 0q0-30 -18-52M20 0q4-40 -12-70M34 0q2-44 14-76" fill="none" stroke="{P["gold_d"]}" stroke-width="{sw:.2f}"/>'
             + "".join(f'<ellipse cx="{cx}" cy="{cy}" rx="4" ry="11" transform="rotate({r} {cx} {cy})" fill="{P["gold"]}" {S}/>'
                       for cx, cy, r in ((-52, -70, -20), (-14, -76, 20), (10, -58, 45), (-10, -52, -30), (8, -70, -20), (48, -76, 20))))
    elif kind == "maple":
        b = (f'<path d="M-3 0V-28H3V0Z" fill="{P["trunk"]}" {S}/><circle cx="-16" cy="-40" r="20" fill="{P["red"]}" {S}/>'
             f'<circle cx="14" cy="-46" r="22" fill="{P["orange"]}" {S}/><circle cx="0" cy="-64" r="18" fill="{P["red"]}" {S}/>')
    else:  # trees
        b = (f'<path d="M-23 0V-24M23 0V-20" fill="none" {S}/><circle cx="-22" cy="-40" r="20" fill="{P["green"]}" {S}/>'
             f'<circle cx="22" cy="-34" r="16" fill="{P["green_d"]}" {S}/><circle cx="2" cy="-54" r="18" fill="{P["green"]}" {S}/>')
    return _g(b, x, y, s)


PAL_EMAKI = dict(ink="#3a2f22", ink2="#4a3a2a", paper="#efe6cf", water="#3f6b8f", wall="#f4ead2", wall2="#d8cdb2",
                 roof="#5b4632", red="#b8442c", orange="#d9902f", gold="#dcb85e", gold_d="#a57f3b", green="#6f8a55",
                 green_d="#465a2e", grey="#9a9282", trunk="#5a3d22", night="#27405f")
PAL_MAP = dict(PAL_EMAKI, water="#5e8fb3", green="#7f9a5c", wall="#fbf7ef")
PAL_WOOD = dict(ink="#1d1d1b", ink2="#1d1d1b", paper="#efe2c6", water="#27405f", wall="#efe2c6", wall2="#d9c79f",
                roof="#1d1d1b", red="#c8442f", orange="#d9a441", gold="#d9a441", gold_d="#1d1d1b", green="#3d5a7a",
                green_d="#1f3a5f", grey="#8ea3b8", trunk="#1d1d1b", night="#1f3a5f")


def stamp_pal(c):
    return {k: ("none" if k not in ("ink",) else c) for k in PAL_EMAKI} | {"paper": "none", "sw": 3.4}


# ---------------------------------------------------------------- data

def load_days():
    trip = json.loads((ROOT / "data/trip.json").read_text(encoding="utf-8"))
    return trip["days"]


def load_gpx(n):
    f = ROOT / f"day{n}_track.gpx"
    if not f.exists():
        return [], []
    s = f.read_text(encoding="utf-8")
    pts = [(float(a), float(b)) for a, b in re.findall(r'<trkpt[^>]*lat="([\d.\-]+)"[^>]*lon="([\d.\-]+)"', s)]
    if not pts:
        pts = [(float(b), float(a)) for a, b in re.findall(r'<trkpt[^>]*lon="([\d.\-]+)"[^>]*lat="([\d.\-]+)"', s)]
    ele = [float(x) for x in re.findall(r"<ele>([\d.\-]+)</ele>", s)]
    return pts, ele


def rdp(P, eps):
    if len(P) < 3:
        return P
    a, b = P[0], P[-1]
    dmax, idx = 0, 0
    den = math.hypot(b[1] - a[1], b[0] - a[0])
    for i in range(1, len(P) - 1):
        p = P[i]
        if den < 1e-9:  # closed loop: distance to the shared endpoint
            d = math.hypot(p[0] - a[0], p[1] - a[1])
        else:
            d = abs((b[1] - a[1]) * (a[0] - p[0]) - (a[1] - p[1]) * (b[0] - a[0])) / den
        if d > dmax:
            dmax, idx = d, i
    if dmax > eps:
        return rdp(P[: idx + 1], eps)[:-1] + rdp(P[idx:], eps)
    return [a, b]


def flags(d):
    text = d["route_line"] + d.get("foliage", "") + " ".join(p["name"] for p in d["timeline"])
    return dict(
        fuji=bool(re.search("富士|湖|朝霧|田子", text)),
        sea=bool(re.search("海岸|海灣|海堤|海景|海濱|港|湘南|江之島|台場|網代|熱海|伊東|駿河", d["route_line"])),
        mount=d["nav"]["max_e"] > 300,
        momiji=bool(re.search("紅葉|楓|🔥", d.get("foliage", ""))),
        ginkgo="銀杏" in d.get("foliage", "") + d["route_line"],
        night="花火" in d["route_line"],
    )


def est_times(d):
    tl = d["timeline"]
    km_tot = max(p["km"] for p in tl) or 1
    hours = km_tot / 15 + d["nav"]["gain"] / 450
    start = 9.5 if d["day"] == 1 else 9.0
    out, lunch_added = [], False
    for p in tl:
        t = start + hours * p["km"] / km_tot
        if lunch_added:
            t += 1
        out.append(t)
        if not lunch_added and p["km"] > km_tot * 0.35 and km_tot > 20:
            lunch_added = True
    return [f"{int(t)%24:02d}:{int(round((t%1)*60/5)*5)%60:02d}" for t in out]


def endpoints(d):
    parts = [re.sub(r"【[^】]*】|[（(][^）)]*[）)]?", "", x).strip() for x in re.split(r"➔", d["route_line"])]
    return short(parts[0], 10), short(parts[-1], 10)


def label(d, i, limit=11):
    p = d["timeline"][i]
    t = short(p["name"], limit)
    if re.search(r"[A-Za-z]{3}", t) and i in (0, len(d["timeline"]) - 1):
        a, b = endpoints(d)
        return a if i == 0 else b
    return t


RANK = ["fireworks", "pagoda", "castle", "torii", "waterfall", "ginkgo", "bridge", "pass", "onsen", "lake",
        "conifer", "susuki", "maple", "sea", "plane", "river", "town", "inn", "trees"]


def hero_motif(d):
    fol = d.get("foliage", "") + d.get("subtitle", "")
    for pat, m in (("花火", "fireworks"), ("水杉", "conifer"), ("銀杏", "ginkgo")):
        if pat in fol:
            return m
    ms = [motif_of(p) for p in d["timeline"]]
    return min(ms, key=RANK.index)


TYPE_JA = dict(start="出発", end="到着", pivot="乗り換え", scenic="絶景", rest="休憩", waypoint="通過", warning="注意")
WEEK = dict(zip("一二三四五六日", "月火水木金土日"))


def date_ja(d):
    m = re.match(r"(\d+)/(\d+)（(.)）", d["date"])
    return int(m.group(1)), int(m.group(2)), WEEK.get(m.group(3), m.group(3))


# ---------------------------------------------------------------- ① 絵巻

def v1(d, F, rnd):
    tl = d["timeline"]
    n = len(tl)
    W, H, G = max(1300, 300 * n + 300), 540, 430
    step = (W - 420) / max(n - 1, 1)
    xs = [W - 220 - i * step for i in range(n)]
    o = [f'<svg viewBox="0 0 {W} {H}" style="width:{W*0.83:.0f}px" role="img" aria-label="Day {d["day"]} 絵巻">',
         f'<rect width="{W}" height="{H}" fill="#eee1c3"/><rect width="{W}" height="{H}" filter="url(#grain)"/><g filter="url(#rough)">',
         f'<path d="M0 14H{W}M0 22H{W}M0 518H{W}M0 526H{W}" stroke="#8a6a3c" stroke-width="2" fill="none"/>']
    # gold clouds
    cl = '<g fill="#dcb85e" stroke="#a9853a" stroke-width="1.6" opacity=".92">'
    x = -40
    while x < W:
        w = rnd.randint(260, 460)
        y = rnd.choice((34, 44, 56))
        cl += f'<path d="M{x} {y}H{x+w}a22 22 0 0 1 0 44H{x+w*0.4:.0f}a18 18 0 0 0 0 36H{x}a18 18 0 0 1 0-36H{x+30}a22 22 0 0 0 0-44Z"/>'
        x += w + rnd.randint(140, 300)
    x = -60
    while x < W:
        w = rnd.randint(300, 520)
        cl += f'<path d="M{x} 482H{x+w}a20 20 0 0 0 0-40H{x+w+120}a22 22 0 0 1 0 44V540H{x}Z"/>'
        x += w + rnd.randint(260, 420)
    o.append(cl + "</g>")
    # back terrain
    if F["mount"]:
        pts = " ".join(f"{x:.0f},{G - 120 - rnd.randint(0, 120)}" for x in range(-40, W + 120, 140))
        o.append(f'<polygon points="-40,{G} {pts} {W+40},{G}" fill="#a9b6a0" stroke="#5f6e55" stroke-width="2" opacity=".85"/>')
    if F["fuji"]:
        fx = xs[min(n - 1, n // 2)] - step / 2
        o.append(f'<path d="M{fx-170} {G-40}L{fx} {G-300}L{fx+170} {G-40}Z" fill="#9fb2c2" stroke="#55697a" stroke-width="2"/>'
                 f'<path d="M{fx-46} {G-230}L{fx} {G-300}L{fx+46} {G-230}L{fx+24} {G-240}L{fx+8} {G-224}L{fx-10} {G-242}L{fx-26} {G-226}Z" fill="#fbfbf7" stroke="#55697a" stroke-width="1.6"/>')
    if F["sea"]:
        o.append(f'<path d="M0 {G+18}H{W}V{H-40}H0Z" fill="#3f6b8f" opacity=".85"/>')
    o.append(f'<path d="M0 {G}H{W}" stroke="#7a6a4c" stroke-width="2"/>')
    # scenes
    for i, p in enumerate(tl):
        m = motif_of(p)
        o.append(motif(m, xs[i], G - 4, 1.55, PAL_EMAKI))
        if m not in ("trees", "conifer", "maple") and F["momiji"]:
            o.append(motif("maple", xs[i] + 80, G - 4, 0.8, PAL_EMAKI))
    # route
    rp = f"M{W-150} {G+8}" + "".join(f"Q{x+step/2:.0f} {G+14+(8 if j%2 else -4)} {x:.0f} {G+8}" for j, x in enumerate(xs[1:] + [90]))
    o.append(f'<path d="{rp}" fill="none" stroke="#b8442c" stroke-width="3.2" stroke-dasharray="10 8" stroke-linecap="round"/></g>')
    o.append(f'<use href="#bike" x="{(xs[0]+xs[1])/2 if n>1 else xs[0]-80:.0f}" y="{G-38}" width="44" height="42" color="#2b2622"/>')
    # cartouche
    o.append(f'<g filter="url(#rough)"><rect x="{W-74}" y="40" width="54" height="270" fill="#f6efdc" stroke="#3a2f22" stroke-width="2"/>'
             f'<rect x="{W-68}" y="46" width="42" height="258" fill="none" stroke="#3a2f22"/></g>'
             f'<text x="{W-47}" y="62" font-family="Yuji Syuku,Noto Serif TC,serif" font-size="23" fill="#2b2622" style="writing-mode:vertical-rl" letter-spacing="2">単車旅絵巻 第{kanji_num(d["day"])}日</text>')
    o.append('<g font-family="Klee One,Noto Serif TC,serif" fill="#2b2622" font-size="19" style="writing-mode:vertical-rl">')
    for i, p in enumerate(tl):
        o.append(f'<text x="{xs[i]+64:.0f}" y="{150 if i%2==0 else 175}">{E(label(d, i))}</text>')
    o.append('</g><g font-family="Klee One,Noto Serif TC,serif" fill="#7a4f1c" font-size="14" text-anchor="middle">')
    for i, p in enumerate(tl):
        o.append(f'<text x="{xs[i]:.0f}" y="512">{kanji_digits(round(p["km"]))}粁</text>')
    o.append(f'</g><text x="40" y="70" font-family="Klee One,Noto Serif TC,serif" font-size="20" fill="#2b2622">{E(d.get("subtitle",""))}</text></svg>')
    return "".join(o)


# ---------------------------------------------------------------- ② 旅のしおり

def v2(d, F, rnd):
    tl = d["timeline"]
    n = len(tl)
    top, row = 270, 82
    tl_end = top + row * (n - 1)
    H = tl_end + 250
    mo, da, wd = date_ja(d)
    times = est_times(d)
    nav = d["nav"]
    wh = d.get("weather_hist", {})
    o = [f'<svg viewBox="0 0 600 {H}" role="img" aria-label="Day {d["day"]} 旅のしおり">',
         f'<rect width="600" height="{H}" fill="#fdfbf5"/><rect width="600" height="{H}" fill="url(#grid)"/>',
         f'<rect width="600" height="{H}" filter="url(#grain)" opacity=".5"/>',
         '<rect x="30" y="-6" width="130" height="34" fill="url(#tape1)" opacity=".9" transform="rotate(-6 95 11)"/>',
         '<rect x="440" y="-4" width="130" height="34" fill="url(#tape2)" opacity=".9" transform="rotate(5 505 13)"/>',
         '<g font-family="Klee One,Noto Serif TC,serif" fill="#2b2622">',
         '<text x="40" y="78" font-size="18" fill="#b8442c" letter-spacing="3">旅のしおり</text>',
         f'<text x="40" y="122" font-size="40" font-weight="600">Day {d["day"]}　{E(d.get("subtitle",""))}</text>',
         f'<text x="40" y="156" font-size="18">{mo}月{da}日（{wd}）{E(label(d,0,9))} → {E(label(d,n-1,12))}</text></g>',
         '<path d="M40 170q130 6 260 0t240 2" stroke="#b8442c" stroke-width="2.4" fill="none" filter="url(#rough)"/>',
         '<g filter="url(#rough)" fill="none" stroke-width="2"><ellipse cx="105" cy="214" rx="66" ry="26" stroke="#27405f"/>'
         '<ellipse cx="260" cy="214" rx="72" ry="26" stroke="#27405f"/><ellipse cx="452" cy="214" rx="108" ry="26" stroke="#d08a2b"/></g>',
         '<g font-family="Klee One,Noto Serif TC,serif" font-size="19" text-anchor="middle" fill="#2b2622">'
         f'<text x="105" y="221">{max(p["km"] for p in tl):.1f} km</text><text x="260" y="221">登り {nav["gain"]} m</text>'
         f'<text x="452" y="221" font-size="16">去年 {E(wh.get("text",""))} {wh.get("lo","")}–{wh.get("hi","")}°C</text></g>',
         f'<path d="M100 {top-10}V{tl_end+10}" stroke="#2b2622" stroke-width="2" stroke-dasharray="3 7" stroke-linecap="round"/>']
    cols = dict(start="#b8442c", end="#b8442c", pivot="#5e8fb3", scenic="#e0b13c", rest="#9fbf6a", warning="#d08a2b")
    o.append('<g filter="url(#rough)" stroke="#2b2622" stroke-width="2">')
    for i, p in enumerate(tl):
        r = 12 if p["type"] in ("start", "end") else 9
        o.append(f'<circle cx="100" cy="{top+row*i}" r="{r}" fill="{cols.get(p["type"],"#fdfbf5")}"/>')
    o.append('</g><g font-family="Klee One,Noto Serif TC,serif" fill="#2b2622">')
    for i, p in enumerate(tl):
        y = top + row * i
        o.append(f'<text x="78" y="{y+6}" font-size="17" fill="#6e6458" text-anchor="end">{times[i]}</text>'
                 f'<text x="124" y="{y+6}" font-size="21" font-weight="600">{E(short(p["name"],12))}</text>'
                 f'<text x="124" y="{y+30}" font-size="15" fill="#6e6458">{p["km"]:.1f} km ・ {TYPE_JA.get(p["type"],"")}</text>')
    o.append(f'<text x="40" y="{tl_end+50}" font-size="13" fill="#6e6458">※ 時刻は目安（平均 15 km/h＋登り＋昼休み）</text></g>')
    # stamps: start, best scenic, end
    mid = next((i for i, p in enumerate(tl) if p["type"] == "scenic"), n // 2)
    picks = [(0, "#b8442c", -8), (mid, "#27405f", 7), (n - 1, "#3f6b3a", -4)] if n > 2 else [(0, "#b8442c", -8), (n - 1, "#3f6b3a", -4)]
    used = set()
    for idx, col, rot in picks:
        if idx in used:
            continue
        used.add(idx)
        cy = min(max(top + row * idx + 20, 300), tl_end - 10)
        p = tl[idx]
        o.append(f'<g filter="url(#stamp)" transform="rotate({rot} 482 {cy})"><g fill="none" stroke="{col}" stroke-width="3">'
                 f'<circle cx="482" cy="{cy}" r="56"/><circle cx="482" cy="{cy}" r="47" stroke-width="1.5"/></g>'
                 + motif(motif_of(p), 482, cy + 24, 0.5, stamp_pal(col)) +
                 f'<g font-family="Klee One,Noto Serif TC,serif" fill="{col}" text-anchor="middle"><text x="482" y="{cy-30}" font-size="13" font-weight="600">{E(label(d,idx,7))}</text>'
                 f'<text x="482" y="{cy+40}" font-size="10">{mo}.{da} 第{kanji_num(d["day"])}日</text></g></g>')
    # notes
    ny = tl_end + 76
    meals = d.get("meals") or {}
    lunch = [short(x["name"], 14) for x in meals.get("lunch", [])][:2]
    dinner = [short(x["name"], 14) for x in meals.get("dinner", [])][:2]
    hotel = short(d.get("hotel", {}).get("name", ""), 16)
    o.append(f'<g transform="rotate(-2 200 {ny+60})"><rect x="40" y="{ny}" width="300" height="130" fill="#f7e7a1" filter="url(#rough)"/>'
             f'<rect x="150" y="{ny-9}" width="80" height="22" fill="url(#tape2)" opacity=".85"/><g font-family="Klee One,Noto Serif TC,serif" fill="#2b2622">'
             f'<text x="58" y="{ny+38}" font-size="17" font-weight="600">昼ごはん</text>')
    for j, t in enumerate(lunch or ["沿途で調達"]):
        o.append(f'<text x="58" y="{ny+64+j*24}" font-size="15">□ {E(t)}</text>')
    o.append(f'</g></g><g transform="rotate(2 470 {ny+60})"><rect x="362" y="{ny+6}" width="208" height="122" fill="#f6d7cf" filter="url(#rough)"/>'
             f'<g font-family="Klee One,Noto Serif TC,serif" fill="#2b2622"><text x="378" y="{ny+40}" font-size="17" font-weight="600">今夜の宿・晩ごはん</text>'
             f'<text x="378" y="{ny+66}" font-size="14">{E(hotel)}</text>')
    for j, t in enumerate(dinner[:2]):
        o.append(f'<text x="378" y="{ny+90+j*22}" font-size="13.5" fill="#6e6458">{"AB"[j]} {E(t)}</text>')
    o.append("</g></g></svg>")
    return "".join(o)


# ---------------------------------------------------------------- ③ 鳥瞰図

def v3(d, F, rnd):
    pts, _ = load_gpx(d["day"])
    tl = d["timeline"]
    if not pts:
        pts = [(p["coord"][1], p["coord"][0]) for p in tl]
    allp = pts + [(p["coord"][1], p["coord"][0]) for p in tl]
    k = math.cos(math.radians(sum(a for a, _ in allp) / len(allp)))
    lo0, lo1 = min(b for _, b in allp), max(b for _, b in allp)
    la0, la1 = min(a for a, _ in allp), max(a for a, _ in allp)
    MX, MY, MW, MH = 70, 220, 860, 450
    span_x, span_y = max((lo1 - lo0) * k, 1e-4), max(la1 - la0, 1e-4)
    sc = min(MW / span_x, MH / span_y)
    ox = MX + (MW - span_x * sc) / 2
    oy = MY + (MH - span_y * sc) / 2

    def P(la, lo):
        return ox + (lo - lo0) * k * sc, oy + (la1 - la) * sc

    simp = rdp(pts, max(span_x, span_y) / 400)
    poly = " ".join(f"{x:.0f},{y:.0f}" for x, y in (P(a, b) for a, b in simp))
    mo, da, wd = date_ja(d)
    o = [f'<svg viewBox="0 0 1000 720" role="img" aria-label="Day {d["day"]} 鳥瞰図">',
         '<rect width="1000" height="720" fill="url(#sky3)"/><rect y="190" width="1000" height="530" fill="#ece3c6"/>',
         '<rect width="1000" height="720" filter="url(#grain)" opacity=".7"/><g filter="url(#rough)">']
    hz = " ".join(f"{x},{190 - rnd.randint(10, 60 if F['mount'] else 25)}" for x in range(0, 1081, 90))
    o.append(f'<polygon points="0,200 {hz} 1000,200" fill="#a9b9c4" stroke="#6d7f8c" stroke-width="1.5"/>')
    if F["fuji"]:
        o.append('<path d="M150 200L235 82L320 200Z" fill="#9fb2c2" stroke="#55697a" stroke-width="1.8"/>'
                 '<path d="M210 116L235 82L260 116L250 112L242 122L232 110L222 120Z" fill="#fbfbf7" stroke="#55697a" stroke-width="1.4"/>')
    o.append("</g>")
    o.append(f'<polyline points="{poly}" fill="none" stroke="#fdfbf5" stroke-width="8" stroke-linejoin="round" stroke-linecap="round"/>'
             f'<polyline points="{poly}" fill="none" stroke="#b8442c" stroke-width="3.6" stroke-dasharray="9 6" stroke-linejoin="round" stroke-linecap="round" filter="url(#rough)"/>')
    # icons + labels (labels that cannot be placed go to a numbered legend)
    placed, legend = [], []
    for p in tl:
        ix, iy = P(p["coord"][1], p["coord"][0])
        placed.append((ix - 28, iy + 2, 56))
        placed.append((ix - 28, iy - 20, 56))
    lab = ['<g font-family="Klee One,Noto Serif TC,serif" fill="#2b2622" font-size="17">']
    for i, p in enumerate(tl):
        x, y = P(p["coord"][1], p["coord"][0])
        o.append(motif(motif_of(p), x, y - 8, 0.55, PAL_MAP))
        se = p["type"] in ("start", "end")
        o.append(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{8 if se else 5}" fill="{"#b8442c" if se else "#fdfbf5"}" stroke="#2b2622" stroke-width="2"/>')
        t = short(p["name"], 10) + (" スタート" if p["type"] == "start" else " ゴール" if p["type"] == "end" else "")
        w = len(t) * 16 + 4
        spot = None
        for lx, ly in ((x + 16, y + 24), (x - 16 - w, y + 24), (x - w / 2, y + 30), (x + 22, y - 6), (x - 22 - w, y - 6),
                       (x - w / 2, y - 66), (x + 16, y + 46), (x - 16 - w, y + 46)):
            if lx < 10 or lx + w > 990 or ly < 214 or ly > 712:
                continue
            if all(lx + w < px or lx > px + pw or abs(ly - py) > 21 for px, py, pw in placed) and \
               not (30 < lx + w and lx < 410 and ly < 100):
                spot = (lx, ly)
                break
        if spot is None:
            legend.append((i, t))
            o.append(f'<text x="{x+10:.0f}" y="{y-8:.0f}" font-family="Klee One,serif" font-size="15" font-weight="600" fill="#b8442c" paint-order="stroke" stroke="#ece3c6" stroke-width="4">{"①②③④⑤⑥⑦⑧⑨⑩⑪⑫"[len(legend)-1]}</text>')
            continue
        placed.append((spot[0], spot[1], w))
        wt = ' font-weight="600"' if se else ""
        lab.append(f'<text x="{spot[0]:.0f}" y="{spot[1]:.0f}"{wt} paint-order="stroke" stroke="#ece3c6" stroke-width="4">{E(t)}</text>')
    o.append("".join(lab) + "</g>")
    if legend:
        lh = 28 + 24 * len(legend)
        o.append(f'<g filter="url(#rough)"><rect x="440" y="24" width="300" height="{lh}" fill="#f6efdc" stroke="#2b2622" stroke-width="1.6"/></g>'
                 '<g font-family="Klee One,Noto Serif TC,serif" font-size="16" fill="#2b2622">'
                 + "".join(f'<text x="456" y="{54+24*j}"><tspan fill="#b8442c" font-weight="600">{"①②③④⑤⑥⑦⑧⑨⑩⑪⑫"[j]}</tspan> {E(t)}</text>' for j, (_, t) in enumerate(legend))
                 + '</g>')
    o.append('<g transform="translate(930 110)" filter="url(#rough)" stroke="#2b2622" stroke-width="1.8"><circle r="30" fill="#f6efdc"/>'
             '<path d="M0-26L7 0L0 26L-7 0Z" fill="#fdfbf5"/><path d="M0-26L7 0L-7 0Z" fill="#b8442c"/></g>'
             '<text x="930" y="70" text-anchor="middle" font-family="Klee One,serif" font-size="14" fill="#2b2622">北</text>'
             '<g filter="url(#rough)"><rect x="30" y="24" width="380" height="70" fill="#f6efdc" stroke="#2b2622" stroke-width="2"/></g>'
             f'<g font-family="Klee One,Noto Serif TC,serif" fill="#2b2622"><text x="48" y="58" font-size="26" font-weight="600">第{kanji_num(d["day"])}日 {E(d.get("subtitle",""))} 鳥瞰図</text>'
             f'<text x="48" y="82" font-size="14" fill="#6e6458">{max(p["km"] for p in tl):.1f} km ・ 標高 {d["nav"]["min_e"]} → {d["nav"]["max_e"]} m ・ {mo}月{da}日</text></g></svg>')
    return "".join(o)


# ---------------------------------------------------------------- ④ 木版

def v4(d, F, rnd):
    tl = d["timeline"]
    mo, da, wd = date_ja(d)
    sub = d.get("subtitle", "").replace("篇", "")
    km = max(p["km"] for p in tl)
    hero = hero_motif(d)
    sky_top, sky_mid = ("#0f1d33", "#27405f") if F["night"] else ("#27405f", "#7d93ab")
    o = [f'<svg viewBox="0 0 600 860" role="img" aria-label="Day {d["day"]} 木版">',
         f'<defs><linearGradient id="bk{d["day"]}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{sky_top}"/>'
         f'<stop offset=".32" stop-color="{sky_mid}"/><stop offset=".58" stop-color="{"#3d5a7a" if F["night"] else "#efe2c6"}"/></linearGradient>'
         f'<clipPath id="fr{d["day"]}"><rect x="18" y="18" width="564" height="824"/></clipPath></defs>',
         f'<rect width="600" height="860" fill="#efe2c6"/><g clip-path="url(#fr{d["day"]})">',
         f'<rect x="18" y="18" width="564" height="600" fill="url(#bk{d["day"]})"/>']
    if F["night"]:
        bare = dict(PAL_WOOD, bare=1)
        o.append(motif("fireworks", 300, 360, 2.4, bare) + motif("fireworks", 140, 300, 1.2, dict(bare, gold="#c8442f", red="#d9a441"))
                 + motif("fireworks", 420, 250, 1.0, bare))
    else:
        o.append(f'<circle cx="{rnd.randint(240,380)}" cy="{rnd.randint(170,220)}" r="62" fill="#c8442f"/>')
    if F["mount"] or F["fuji"]:
        o.append('<path d="M18 420L120 330L200 370L280 320L360 390L460 350L582 380V620H18Z" fill="#8ea3b8"/>')
    if F["fuji"]:
        fx = rnd.choice((170, 230))
        o.append(f'<path d="M{fx-150} 430L{fx} 250L{fx+150} 430Z" fill="#a9b9cc"/><path d="M{fx-38} 297L{fx} 250L{fx+38} 297L{fx+20} 290L{fx+6} 304L{fx-10} 288L{fx-24} 300Z" fill="#f6efdc"/>')
    if F["mount"]:
        o.append('<path d="M18 600C60 520 120 470 190 470C250 470 300 520 360 560C400 588 440 600 480 610V660H18Z" fill="#1f3a5f"/>')
    elif not F["sea"]:
        sk = ""
        x = 18
        while x < 582:
            w = rnd.randint(30, 70)
            h = rnd.randint(60, 190)
            sk += f"M{x} 640V{640-h}H{x+w}V640Z"
            x += w + rnd.randint(0, 12)
        o.append(f'<path d="{sk}" fill="#3d5a7a"/>')
    if F["sea"]:
        if not F["mount"]:
            o.append('<path d="M18 470C70 440 120 430 170 450C220 470 250 520 330 556H18Z" fill="#3d5a7a"/>'
                     '<path d="M582 500C540 490 500 500 470 530L440 556H582Z" fill="#8ea3b8"/>')
        o.append('<path d="M18 560Q300 540 582 556V700H18Z" fill="url(#seigaiha)"/>')
        o.append('<g fill="#1d1d1b"><path d="M548 640V520" stroke="#1d1d1b" stroke-width="6"/>'
                 '<path d="M470 528Q520 500 580 512Q560 530 500 534Z"/><path d="M490 560Q540 540 590 552Q570 568 510 570Z"/>'
                 '<path d="M500 492Q540 470 584 480Q566 498 520 500Z"/></g>')
    o.append('<path d="M18 640C120 624 240 626 340 634C440 642 520 628 582 620V700H18Z" fill="#d9a441"/>')
    if not F["sea"]:
        o.append('<path d="M18 700C140 680 260 690 360 702C460 714 530 700 582 690V760H18Z" fill="url(#seigaiha)"/>')
    else:
        o.append('<path d="M18 700H582V760H18Z" fill="#d9a441"/>')
    if not (F["night"] and hero == "fireworks"):
        o.append(motif(hero, 150, 640, 1.9, PAL_WOOD))
    o.append('<use href="#bike" x="300" y="584" width="58" height="54" color="#1d1d1b"/>')
    leafc = "#d9a441" if F["ginkgo"] else "#c8442f"
    if F["momiji"] or F["ginkgo"]:
        for _ in range(6):
            x, y, s = rnd.randint(40, 440), rnd.randint(60, 300), rnd.randint(14, 26)
            o.append(f'<use href="#leaf" x="{x}" y="{y}" width="{s}" height="{s+2}" fill="{leafc}" transform="rotate({rnd.randint(-40,40)} {x+s/2} {y+s/2})"/>')
    o.append('<rect x="18" y="760" width="564" height="82" fill="#1d1d1b"/></g>'
             '<rect x="18" y="18" width="564" height="824" fill="none" stroke="#1d1d1b" stroke-width="6"/>')
    th = max(110, 52 * len(sub) + 30)
    o.append(f'<rect x="500" y="46" width="62" height="{th}" fill="#efe2c6" stroke="#c8442f" stroke-width="3"/>'
             f'<text x="531" y="66" font-family="Yuji Syuku,Noto Serif TC,serif" font-size="44" fill="#1d1d1b" style="writing-mode:vertical-rl" letter-spacing="8">{E(sub)}</text>'
             f'<text x="470" y="56" font-family="Yuji Syuku,Noto Serif TC,serif" font-size="19" fill="#f6efdc" style="writing-mode:vertical-rl" letter-spacing="3">{E(label(d,0,7))}ヨリ{E(label(d,len(tl)-1,8))}ヘ</text>'
             f'<rect x="510" y="{62+th}" width="42" height="42" fill="#c8442f" filter="url(#stamp)"/>'
             f'<text x="531" y="{91+th}" font-family="Yuji Syuku,Noto Serif TC,serif" font-size="{20 if d["day"]<11 else 15}" fill="#efe2c6" text-anchor="middle">{"初日" if d["day"]==1 else "結" if d["day"]==19 else kanji_num(d["day"])}</text>'
             '<g font-family="Klee One,Noto Serif TC,serif" fill="#efe2c6">'
             f'<text x="40" y="794" font-size="18" font-weight="600" letter-spacing="1">第{kanji_num(d["day"])}日 ・ {kanji_num(mo)}月{kanji_num(da)}日 ・ {kanji_num(round(km))}粁 ・ 登 {kanji_num(d["nav"]["gain"])}米</text>'
             f'<text x="40" y="824" font-size="14" fill="#d9a441">{E(" → ".join(label(d,i,6) for i in range(0,len(tl),max(1,len(tl)//4))))}</text></g></svg>')
    return "".join(o)


# ---------------------------------------------------------------- page

CSS = """
:root{--paper:#f3ecdf;--card:#fbf7ef;--ink:#2b2622;--muted:#6e6458;--shu:#b8442c;--line:#dccfb8;
--f-hand:"Klee One","Noto Serif TC","Hiragino Mincho ProN",serif;--f-body:-apple-system,"PingFang TC","Noto Sans TC","Microsoft JhengHei",sans-serif;color-scheme:light}
*{box-sizing:border-box}html{-webkit-text-size-adjust:100%}
body{margin:0;background:var(--paper);color:var(--ink);font-family:var(--f-body);line-height:1.6}
.wrap{max-width:860px;margin:0 auto;padding:24px max(16px,env(safe-area-inset-right,0px)) 56px max(16px,env(safe-area-inset-left,0px));display:flex;flex-direction:column;gap:34px}
a{color:var(--shu)}
.top{display:flex;justify-content:space-between;gap:8px;flex-wrap:wrap;font-size:14px}
h1{font-family:var(--f-hand);font-weight:600;font-size:clamp(24px,6vw,34px);margin:4px 0 0;text-wrap:balance}
.lead{margin:4px 0 0;color:var(--muted);font-size:14.5px}
nav.v{display:flex;flex-wrap:wrap;gap:8px;margin-top:12px}
nav.v a,.days a{font-family:var(--f-hand);font-size:15px;color:var(--ink);text-decoration:none;border:1.5px solid var(--ink);border-radius:999px;padding:2px 12px;background:var(--card)}
nav.v a:hover,.days a:hover,.days a.on{background:var(--ink);color:var(--card)}
.days{display:flex;flex-wrap:wrap;gap:6px}.days a{font-size:13px;padding:1px 9px}
section{display:flex;flex-direction:column;gap:8px;scroll-margin-top:12px}
h2{font-family:var(--f-hand);font-weight:600;font-size:21px;margin:0}
.tag{font-family:var(--f-hand);font-size:13px;letter-spacing:.12em;color:var(--shu)}
.plate{background:var(--card);border:1px solid var(--line);border-radius:4px;padding:10px}
.plate svg{display:block;width:100%;height:auto}
.scroll{overflow-x:auto;-webkit-overflow-scrolling:touch}.scroll svg{max-width:none}
.portrait{max-width:520px}.hint{font-size:12.5px;color:var(--muted)}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(150px,1fr));gap:14px}
.grid a{display:flex;flex-direction:column;gap:4px;text-decoration:none;color:var(--ink);font-family:var(--f-hand);font-size:14px}
.grid svg{width:100%;height:auto;display:block;border:1px solid var(--line)}
footer{border-top:1px dashed var(--line);padding-top:14px;color:var(--muted);font-size:13.5px}
"""
FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
         '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Klee+One:wght@400;600&family=Yuji+Syuku&family=Noto+Serif+TC:wght@500&display=swap">')
EXTRA_DEFS = ('<linearGradient id="sky3" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#cfe0e8"/><stop offset="1" stop-color="#f2ead6"/></linearGradient>')


def defs_block():
    defs = (HAND / "defs.svg").read_text(encoding="utf-8").strip()
    defs = defs.replace("</defs>", EXTRA_DEFS + "</defs>")
    return f'<svg width="0" height="0" style="position:absolute" aria-hidden="true">{defs}</svg>'


def head(title, desc):
    return (f'<!doctype html><html lang="zh-Hant"><head><meta charset="utf-8">'
            f'<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">'
            f'<title>{E(title)}</title><meta name="description" content="{E(desc)}">{FONTS}<style>{CSS}</style></head><body>')


def hand(n, v):
    f = HAND / f"day{n}_v{v}.svg"
    return f.read_text(encoding="utf-8") if f.exists() else None


def day_page(d, days):
    n = d["day"]
    F = flags(d)
    plates = []
    for v, fn in ((1, v1), (2, v2), (3, v3), (4, v4)):
        svg = hand(n, v) or fn(d, F, random.Random(n * 10 + v))
        if v == 1:
            svg = svg.replace('<svg viewBox="0 0 1800 540"', '<svg viewBox="0 0 1800 540" style="width:1500px"', 1)
        plates.append(svg)
    mo, da, wd = date_ja(d)
    km = max(p["km"] for p in d["timeline"])
    chips = "".join(f'<a href="day{x["day"]}.html"{" class=on" if x["day"]==n else ""}>{x["day"]}</a>' for x in days)
    prev_ = f'<a href="day{n-1}.html">← Day {n-1}</a>' if n > 1 else '<span></span>'
    next_ = f'<a href="day{n+1}.html">Day {n+1} →</a>' if n < len(days) else '<span></span>'
    note45 = '<p class="lead">※ Day 4／5 的 GPX 仍是舊規劃，鳥瞰圖軌跡以舊路線為準。</p>' if n in (4, 5) else ""
    h = [head(f"Day {n} 手繪行程圖", f"Day {n} {d['date']} {d.get('subtitle','')}：繪卷、旅のしおり、鳥瞰圖、木版畫"), defs_block(),
         '<div class="wrap"><header><div class="top"><a href="../index.html#day-%d">← 回 Day %d 行程</a><a href="index.html">全部 19 天 ↗</a></div>' % (n, n),
         f'<div class="tag">東京單車騎旅 ・ 手繪行程圖</div><h1>Day {n}　{E(d.get("subtitle",""))}</h1>',
         f'<p class="lead">{mo}/{da}（{d["date"][-2]}）{E(d["route_line"])}<br>{km:.1f} km、爬升 {d["nav"]["gain"]} m。時刻與畫面為示意。</p>{note45}',
         '<nav class="v" aria-label="版本"><a href="#v1">① 繪卷</a><a href="#v2">② 旅のしおり</a><a href="#v3">③ 鳥瞰圖</a><a href="#v4">④ 木版畫</a></nav></header>',
         f'<section id="v1"><div class="tag">① 繪卷</div><div class="plate scroll" tabindex="0" aria-label="繪卷，可左右捲動">{plates[0]}</div><div class="hint">← 左右滑動，由右往左讀。</div></section>',
         f'<section id="v2"><div class="tag">② 旅のしおり</div><div class="plate portrait">{plates[1]}</div></section>',
         f'<section id="v3"><div class="tag">③ 鳥瞰圖</div><div class="plate">{plates[2]}</div></section>',
         f'<section id="v4"><div class="tag">④ 木版畫</div><div class="plate portrait">{plates[3]}</div></section>',
         '<script>document.querySelectorAll(".scroll").forEach(function(e){e.scrollLeft=e.scrollWidth})</script>'
         f'<footer><div class="top">{prev_}{next_}</div><div class="days" style="margin-top:10px">{chips}</div></footer></div></body></html>']
    return "".join(h), plates[3]


def main():
    days = load_days()
    OUT.mkdir(exist_ok=True)
    cards = []
    for d in days:
        page, poster = day_page(d, days)
        (OUT / f"day{d['day']}.html").write_text(page, encoding="utf-8")
        poster = re.sub(r'id="(bk|fr)(\d+)"', r'id="g\1\2"', poster).replace('url(#bk', 'url(#gbk').replace('url(#fr', 'url(#gfr')
        cards.append(f'<a href="day{d["day"]}.html">{poster}<span>Day {d["day"]} {E(d["date"])} {E(d.get("subtitle",""))}</span></a>')
    idx = [head("手繪行程圖 19 天", "東京單車騎旅 19 天日式手繪行程圖：繪卷、旅のしおり、鳥瞰圖、木版畫"), defs_block(),
           '<div class="wrap"><header><div class="top"><a href="../index.html">← 回行程網站</a></div>',
           '<div class="tag">東京單車騎旅 ・ 手繪行程圖</div><h1>19 日手繪行程</h1>',
           '<p class="lead">每天四種日式手繪風格：① 繪卷 ② 旅のしおり ③ 鳥瞰圖 ④ 木版畫。點海報進入當天。</p></header>',
           f'<div class="grid">{"".join(cards)}</div></div></body></html>']
    (OUT / "index.html").write_text("".join(idx), encoding="utf-8")
    print("wrote", len(days) + 1, "pages to", OUT)


if __name__ == "__main__":
    main()
