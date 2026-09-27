#!/usr/bin/env python3
"""重建路線後，把高度剖面與逐日 demo 頁一起補正。

apply_rebuilt_routes.py 只改了距離、爬升與 timeline 里程，但下列東西仍是舊
汽車路線的資料：
  data/trip.json               每日 elev_profile（46–49 點，含 km/ele/lon/lat）
  all_19days_route_data.json   elev_profile／elevation_profile
  dayN_route_map_demo.html     chartLabels／chartData 與五張統計卡片

高度一律重新向國土地理院（GSI）DEM 取值，不用 BRouter 附的 SRTM ——
SRTM 在都市河濱會差很多（Day 1 起點 SRTM 說 16m，GSI 是 2.7m，實際約 3m）。

用法：python scripts/resync_elevation_and_demos.py [--dry-run] [days...]
"""

import json
import math
import os
import re
import sys
import time
import urllib.request
import xml.etree.ElementTree as ET

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DRY = "--dry-run" in sys.argv
DAYS = [int(a) for a in sys.argv[1:] if a.isdigit()] or [1, 7, 8, 13, 15, 16]
GSI = ("https://cyberjapandata2.gsi.go.jp/general/dem/scripts/getelevation.php"
       "?lon={lon:.6f}&lat={lat:.6f}&outtype=JSON")


def hav(a, b):
    r = 6371000.0
    la1, lo1 = math.radians(a[0]), math.radians(a[1])
    la2, lo2 = math.radians(b[0]), math.radians(b[1])
    return 2 * r * math.asin(math.sqrt(
        math.sin((la2 - la1) / 2) ** 2
        + math.cos(la1) * math.cos(la2) * math.sin((lo2 - lo1) / 2) ** 2))


def track(day):
    pts = [(float(e.get("lat")), float(e.get("lon")))
           for e in ET.parse(os.path.join(ROOT, f"day{day}_track.gpx")).getroot().iter()
           if e.tag.endswith("trkpt")]
    cum = [0.0]
    for i in range(1, len(pts)):
        cum.append(cum[-1] + hav(pts[i - 1], pts[i]))
    return pts, cum


def gsi_elev(lat, lon):
    try:
        req = urllib.request.Request(GSI.format(lon=lon, lat=lat),
                                     headers={"User-Agent": "trip-planning/1.0"})
        with urllib.request.urlopen(req, timeout=20) as r:
            v = json.loads(r.read().decode()).get("elevation")
        return round(float(v), 1) if v not in (None, "-----") else None
    except Exception:                                    # noqa: BLE001
        return None


def build_profile(day, n):
    pts, cum = track(day)
    total = cum[-1]
    prof = []
    for i in range(n):
        j = min(range(len(cum)), key=lambda k: abs(cum[k] - total * i / (n - 1)))
        lat, lon = pts[j]
        ele = gsi_elev(lat, lon)
        prof.append({"km": round(cum[j] / 1000, 1), "ele": ele,
                     "lon": round(lon, 6), "lat": round(lat, 6)})
        time.sleep(0.25)
    ok = [p["ele"] for p in prof if p["ele"] is not None]
    for p in prof:                       # 補洞，避免圖表斷線
        if p["ele"] is None:
            p["ele"] = ok[0] if ok else 0
    print(f"  GSI {len(ok)}/{n} 點成功  {prof[0]['ele']}m ➔ {prof[-1]['ele']}m",
          flush=True)
    return prof, total / 1000


def patch_demo(day, prof, km, gain, loss):
    fp = os.path.join(ROOT, f"day{day}_route_map_demo.html")
    if not os.path.exists(fp):
        print(f"  （無 day{day}_route_map_demo.html）")
        return
    s = open(fp, encoding="utf-8").read()
    labels = [f"{p['km']}km" for p in prof]
    data = [p["ele"] for p in prof]
    s2 = re.sub(r"const chartLabels = \[.*?\];",
                "const chartLabels = " + json.dumps(labels) + ";", s, flags=re.S)
    s2 = re.sub(r"const chartData = \[.*?\];",
                "const chartData = " + json.dumps(data) + ";", s2, flags=re.S)

    # 五張卡片：1 距離、2 爬升/下降、3 起訖海拔、4 各頁自訂（不動）、5 騎乘時間
    vals = list(re.finditer(r'(<div class="val">)(.*?)(</div>)', s2, re.S))
    if len(vals) >= 5:
        hrs = km / 18
        new = {0: f"{km:.1f} km",
               1: f"+{gain:.0f} m / -{loss:.0f} m",
               2: f"{prof[0]['ele']:.0f}m ➔ {prof[-1]['ele']:.0f}m",
               4: f"~{hrs:.1f} – {hrs * 1.12:.1f} hr"}
        out, last = [], 0
        for i, m in enumerate(vals):
            if i in new:
                out.append(s2[last:m.start(2)]); out.append(new[i]); last = m.end(2)
        out.append(s2[last:])
        s2 = "".join(out)
        print(f"  卡片 → {new[0]} / {new[1]} / {new[2]} / {new[4]}")
    else:
        print(f"  ⚠ 卡片數 {len(vals)} 不符預期，只更新圖表")
    if not DRY and s2 != s:
        open(fp, "w", encoding="utf-8", newline="").write(s2)


def main():
    trip_path = os.path.join(ROOT, "data", "trip.json")
    all_path = os.path.join(ROOT, "all_19days_route_data.json")
    trip = json.load(open(trip_path, encoding="utf-8"))
    tdays = trip["days"] if isinstance(trip, dict) else trip
    alld = json.load(open(all_path, encoding="utf-8"))

    for day in DAYS:
        rec = next(d for d in tdays if d["day"] == day)
        n = len(rec.get("elev_profile") or []) or 47
        print(f"Day {day}（{n} 點剖面）", flush=True)
        prof, km = build_profile(day, n)
        gain = rec.get("nav", {}).get("gain") or 0
        loss = rec.get("nav", {}).get("loss") or 0
        patch_demo(day, prof, km, gain, loss)
        if not DRY:
            rec["elev_profile"] = prof
            arec = next((d for d in alld if d["day"] == day), None)
            if arec is not None:
                short = [{"km": p["km"], "ele": p["ele"]} for p in prof]
                if "elev_profile" in arec:
                    arec["elev_profile"] = short
                if "elevation_profile" in arec:
                    arec["elevation_profile"] = short

    if not DRY:
        json.dump(trip, open(trip_path, "w", encoding="utf-8"),
                  ensure_ascii=False, indent=1)
        json.dump(alld, open(all_path, "w", encoding="utf-8"),
                  ensure_ascii=False, indent=1)
        print("\n已寫入 trip.json / all_19days_route_data.json")
        print("接著請重跑：python scripts/sync_embedded_day_data.py"
              "（19 日地圖內嵌的是 all_19days 的副本）")
    else:
        print("\n（--dry-run，未寫入）")


if __name__ == "__main__":
    main()
