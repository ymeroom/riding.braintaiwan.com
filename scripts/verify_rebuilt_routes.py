#!/usr/bin/env python3
"""驗收 routes_rebuilt/ 底下 BRouter 重建的路線：跟舊的汽車路線並排比較道路組成。

結果寫入 data/route_audit_rebuilt.json（逐日落地，中途掛掉不會全失）。
稽核快取用 900+day 編號，不會覆蓋舊路線的 Overpass 快取。
"""

import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import audit_gpx_roads as a  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "data", "route_audit_rebuilt.json")
DAYS = [int(x) for x in sys.argv[1:]] or [1, 7, 8, 13, 15, 16]


def ded_art(cats):
    ded = cats.get("dedicated", 0) + cats.get("footway_unclear", 0)
    art = (cats.get("arterial", 0) + cats.get("bicycle_no", 0)
           + cats.get("forbidden", 0) + cats.get("arterial_maybe", 0))
    return ded, art


def main():
    old = {d["day"]: d for d in json.load(
        open(os.path.join(ROOT, "data", "route_audit.json"), encoding="utf-8"))["days"]}
    results = {}
    if os.path.exists(OUT):
        results = {int(k): v for k, v in json.load(open(OUT, encoding="utf-8")).items()}

    for day in DAYS:
        gpx = os.path.join(ROOT, "routes_rebuilt", f"day{day}_track.gpx")
        if not os.path.exists(gpx):
            print(f"Day {day}: 找不到 {gpx}，跳過", flush=True)
            continue
        try:
            r = a.audit_day(900 + day, gpx)
        except a.OverpassDown as e:
            print(f"Day {day}: {e} — 跳過", flush=True)
            continue
        r["day"] = day
        results[day] = r
        with open(OUT, "w", encoding="utf-8") as f:
            json.dump({str(k): v for k, v in sorted(results.items())},
                      f, ensure_ascii=False, indent=1)
        nd, na = ded_art(r["by_cat_km"])
        od, oa = ded_art(old[day]["by_cat_km"])
        print(f"  Day {day}: 舊 {old[day]['total_km']}km 專用道{od:.1f}/幹道{oa:.1f}"
              f"  →  新 {r['total_km']}km 專用道{nd:.1f}/幹道{na:.1f}", flush=True)

    print("\n=== 驗收表 ===")
    print(f"{'Day':>4} | {'舊km':>6} {'舊專用':>6} {'舊幹道':>6} | "
          f"{'新km':>6} {'新專用':>6} {'新幹道':>6} | 判定")
    for day in sorted(results):
        r = results[day]
        nd, na = ded_art(r["by_cat_km"])
        od, oa = ded_art(old[day]["by_cat_km"])
        ok = "✅ 改善" if (nd > od and na < oa) else (
            "△ 部分改善" if nd > od or na < oa else "❌ 沒改善")
        print(f"{day:>4} | {old[day]['total_km']:>6.1f} {od:>6.1f} {oa:>6.1f} | "
              f"{r['total_km']:>6.1f} {nd:>6.1f} {na:>6.1f} | {ok}")
    print(f"\n{OUT}")


if __name__ == "__main__":
    main()
