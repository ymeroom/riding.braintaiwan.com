#!/usr/bin/env python3
"""把 HTML 裡內嵌的逐日資料快照，從 data/trip.json 重新同步。

為什麼不重跑 scripts_v2/build_site.py：
index.html 在產生之後又被多個一次性腳本直接修改過，那些改動從沒回寫進
templates/index_template.html。實測模板裡完全沒有 live-cams（index 有 2 處）、
war-room（6 處）、sp-chip（38 處），重跑產生器會把這些功能整段洗掉。

所以這支腳本只換掉三個內嵌資料區塊，不碰其他任何內容：
    index.html                         const TRIP_DAYS = [...]
    day1_route_map_demo.html           const timelineData = [...]
    tokyo_cycling_19days_map_demo.html const daysData = [...]

用法：python scripts/sync_embedded_day_data.py [--dry-run]
"""

import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DRY = "--dry-run" in sys.argv


def load(name):
    return json.load(open(os.path.join(ROOT, name), encoding="utf-8"))


def replace_block(path, pattern, payload, label):
    fp = os.path.join(ROOT, path)
    s = open(fp, encoding="utf-8").read()
    m = re.search(pattern, s, re.S)
    if not m:
        print(f"⚠ {path}: 找不到 {label} 區塊，跳過")
        return False
    new = s[:m.start(1)] + payload + s[m.end(1):]
    if new == s:
        print(f"= {path}: {label} 無變化")
        return False
    print(f"{'(dry) ' if DRY else ''}✓ {path}: {label} 已更新 "
          f"（{len(m.group(1))} → {len(payload)} 字元）")
    if not DRY:
        open(fp, "w", encoding="utf-8", newline="").write(new)
    return True


def main():
    trip = load("data/trip.json")
    tdays = trip["days"] if isinstance(trip, dict) else trip
    alld = load("all_19days_route_data.json")

    # 1) index.html 的 TRIP_DAYS：{day,date,iso,route,hist,pts:[{n,km,lat,lon}]}
    payload = []
    for d in tdays:
        payload.append({
            "day": d["day"], "date": d["date"],
            "iso": d.get("iso") or "",
            "route": (d.get("route_line") or "")[:40],
            "hist": {"lo": d["weather_hist"]["lo"], "hi": d["weather_hist"]["hi"],
                     "rain": d["weather_hist"]["rain"],
                     "icon": d["weather_hist"]["icon"],
                     "text": d["weather_hist"]["text"]} if d.get("weather_hist") else {},
            "pts": [{"n": t["name"], "km": t["km"],
                     "lat": t["coord"][1], "lon": t["coord"][0]}
                    for t in d.get("timeline", [])],
        })
    # iso 欄位原檔已有，別被上面覆蓋成空字串
    old_iso = {}
    s_idx = open(os.path.join(ROOT, "index.html"), encoding="utf-8").read()
    m = re.search(r"const TRIP_DAYS = (\[.*?\]);", s_idx, re.S)
    if m:
        for rec in json.loads(m.group(1)):
            old_iso[rec["day"]] = rec.get("iso", "")
        for rec in payload:
            rec["iso"] = old_iso.get(rec["day"], rec["iso"])
    replace_block("index.html", r"const TRIP_DAYS = (\[.*?\]);",
                  json.dumps(payload, ensure_ascii=False, separators=(",", ":")),
                  "TRIP_DAYS")

    # 2) day1_route_map_demo.html 的 timelineData：trip.json 的 timeline 原樣
    day1 = next(d for d in tdays if d["day"] == 1)
    replace_block("day1_route_map_demo.html", r"const timelineData = (\[.*?\]);",
                  json.dumps(day1["timeline"], ensure_ascii=False),
                  "timelineData")

    # 3) tokyo_cycling_19days_map_demo.html 的 daysData
    replace_block("tokyo_cycling_19days_map_demo.html", r"const daysData = (\[.*?\]);",
                  json.dumps(alld, ensure_ascii=False),
                  "daysData")

    if DRY:
        print("\n（--dry-run，未寫入）")


if __name__ == "__main__":
    main()
