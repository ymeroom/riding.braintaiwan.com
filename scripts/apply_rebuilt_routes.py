#!/usr/bin/env python3
"""把 routes_rebuilt/ 驗收過的路線換上，並同步 trip.json / all_19days_route_data.json。

原檔由 git 追蹤，所以不另外備份；要回復用 git checkout。

同步的欄位：
  trip.json      planned_km、nav.km/gain/loss、timeline 每個路點的 km
  all_19days...  dist_km、gain、loss

timeline 的 km 用「把該路點座標投影到新軌跡上最近點」重算。投影距離超過
SNAP_WARN 公尺的會印警告而不靜默寫入 —— trip.json 的手寫座標有偏差前例
（Day 1 標的府中四谷橋離實際橋位 1.2km），投影距離就是偏差的體溫計。

用法：
    python scripts/apply_rebuilt_routes.py --dry-run     # 只看會改什麼
    python scripts/apply_rebuilt_routes.py               # 實際寫入
"""

import json
import math
import os
import shutil
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REBUILT = os.path.join(ROOT, "routes_rebuilt")
SNAP_WARN = 500

# Day 1 採用變體 B（含六郷橋）：trip.json 的 route_line 明確寫「六鄉橋 ➔ 多摩川
# 自行車道」，變體 A 會跳過六郷橋、少掉 15km 的多摩川下游段。
SOURCES = {
    1: "day1_variantB_track.gpx",
    7: "day7_track.gpx",
    8: "day8_track.gpx",
    13: "day13_track.gpx",
    15: "day15_track.gpx",
    16: "day16_track.gpx",
}


def hav(a, b):
    r = 6371000.0
    la1, lo1 = math.radians(a[0]), math.radians(a[1])
    la2, lo2 = math.radians(b[0]), math.radians(b[1])
    return 2 * r * math.asin(math.sqrt(
        math.sin((la2 - la1) / 2) ** 2
        + math.cos(la1) * math.cos(la2) * math.sin((lo2 - lo1) / 2) ** 2))


def read_track(path):
    import xml.etree.ElementTree as ET
    pts, eles = [], []
    for e in ET.parse(path).getroot().iter():
        if e.tag.endswith("trkpt"):
            pts.append((float(e.get("lat")), float(e.get("lon"))))
            ele = next((c for c in e if c.tag.endswith("ele")), None)
            eles.append(float(ele.text) if ele is not None else None)
    cum = [0.0]
    for i in range(1, len(pts)):
        cum.append(cum[-1] + hav(pts[i - 1], pts[i]))
    return pts, eles, cum


def smooth_gain(eles, window=8):
    """先做移動平均再算爬升。SRTM 高度雜訊會讓逐點相加膨脹 2–3 倍
    （Day 1 實測 raw 852m vs BRouter filtered 312m）。"""
    vals = [e for e in eles if e is not None]
    if len(vals) < window * 2:
        return None, None
    sm = []
    for i in range(len(vals)):
        lo, hi = max(0, i - window), min(len(vals), i + window + 1)
        sm.append(sum(vals[lo:hi]) / (hi - lo))
    gain = sum(max(0.0, sm[i] - sm[i - 1]) for i in range(1, len(sm)))
    loss = sum(max(0.0, sm[i - 1] - sm[i]) for i in range(1, len(sm)))
    return round(gain), round(loss)


def main():
    dry = "--dry-run" in sys.argv
    trip_path = os.path.join(ROOT, "data", "trip.json")
    all_path = os.path.join(ROOT, "all_19days_route_data.json")
    trip = json.load(open(trip_path, encoding="utf-8"))
    tdays = trip["days"] if isinstance(trip, dict) else trip
    alld = json.load(open(all_path, encoding="utf-8"))

    for day, src in sorted(SOURCES.items()):
        gpx = os.path.join(REBUILT, src)
        if not os.path.exists(gpx):
            print(f"Day {day}: 找不到 {src}，跳過")
            continue
        pts, eles, cum = read_track(gpx)
        km = round(cum[-1] / 1000, 2)
        # 爬升優先採用 BRouter 的 filtered ascend（sidecar），它的濾波比事後
        # 自己平滑可靠；沒有 sidecar 才退回自算。
        meta_path = gpx.replace("_track.gpx", "_meta.json")
        gain = loss = None
        if os.path.exists(meta_path):
            meta = json.load(open(meta_path, encoding="utf-8"))
            if meta.get("filtered ascend") is not None:
                gain = int(float(meta["filtered ascend"]))
                plain = meta.get("plain-ascend")
                loss = gain - int(float(plain)) if plain is not None else None
        if gain is None:
            gain, loss = smooth_gain(eles)
            print("  （無 BRouter sidecar，改用自行平滑的爬升值）")

        rec = next(d for d in tdays if d["day"] == day)
        arec = next((d for d in alld if d["day"] == day), None)
        print(f"\n=== Day {day} ({src}) ===")
        print(f"  距離 {rec.get('planned_km')}km → {km}km"
              f"   爬升 {rec.get('nav', {}).get('gain')}m → {gain}m")

        # timeline 每個路點重新投影。第一／最後一個直接綁到軌跡頭尾 ——
        # 環線（Day 16 起終點同座標）投影會把終點算回 km0。
        tl = rec.get("timeline", [])
        for idx, t in enumerate(tl):
            p = (t["coord"][1], t["coord"][0])
            if idx == 0:
                best, newkm = 0, 0.0
            elif idx == len(tl) - 1:
                best, newkm = len(pts) - 1, km
            else:
                best = min(range(len(pts)), key=lambda i: hav(p, pts[i]))
                newkm = round(cum[best] / 1000, 1)
            snap = hav(p, pts[best])
            note = ""
            if snap > SNAP_WARN and 0 < idx < len(tl) - 1:
                # 座標本身有誤（trip.json 的手寫座標有 1.2km 偏差前例）。
                # 把它移到新軌跡上最近的點，地圖標記才會落在路線上。
                note = f"  ⚠ 原座標偏 {snap:.0f}m，已移到軌跡上"
                if not dry:
                    t["coord"] = [round(pts[best][1], 5), round(pts[best][0], 5)]
                    t.setdefault("_coord_fixed", "2026-09-27 由重建軌跡投影校正")
            print(f"    {t['name'][:26]:28s} km{t['km']:<6} → km{newkm:<6} "
                  f"(投影 {snap:5.0f}m){note}")
            if not dry:
                t["km"] = newkm

        if not dry:
            rec["planned_km"] = km
            nav = rec.setdefault("nav", {})
            nav["km"], nav["gain"], nav["loss"] = km, gain, loss
            rec["route_source"] = f"BRouter trekking（{src}），2026-09-27 重建"
            if arec:
                arec["dist_km"], arec["gain"], arec["loss"] = km, gain, loss
            shutil.copyfile(gpx, os.path.join(ROOT, f"day{day}_track.gpx"))
            print(f"  → 已換上 day{day}_track.gpx")

    if not dry:
        json.dump(trip, open(trip_path, "w", encoding="utf-8"),
                  ensure_ascii=False, indent=1)
        json.dump(alld, open(all_path, "w", encoding="utf-8"),
                  ensure_ascii=False, indent=1)
        total = sum((d.get("planned_km") or 0) for d in tdays)
        tgain = sum((d.get("nav", {}).get("gain") or 0) for d in tdays)
        print(f"\n已寫入 trip.json / all_19days_route_data.json")
        print(f"19 天新總計：{total:.1f}km ／ 爬升 {tgain:.0f}m")
    else:
        print("\n（--dry-run，未寫入任何檔案）")


if __name__ == "__main__":
    main()
