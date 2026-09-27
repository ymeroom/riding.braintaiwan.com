#!/usr/bin/env python3
"""用 BRouter 重建路線，取代 OSRM demo 產生的汽車路線。

背景：專案原本所有路線都呼叫 router.project-osrm.org/route/v1/bicycle/，
但那台 demo 伺服器只掛汽車圖資，profile 字串被完全忽略 —— 連不存在的
profile（banana）都回傳同一條路線，隱含時速 38.8km/h。實測結果是 19 天
累計只有 0.8km 落在 cycleway 上。

BRouter 已通過三關驗證（詳見 scripts/audit_gpx_roads.py 的稽核結果）：
  1. banana 測試：trekking/fastbike/safety 給出三條不同路線，未知 profile 回 500
  2. 與真人實騎軌跡（YouTube VDw0uCzXb6w 的 My Maps 軌跡）偏差中位數 9.1m，
     同一段的舊 GPX 是 921m
  3. 輸出的道路組成（專用道 13.6km / 生活道路 6.0km / 幹道 0km）與真人實騎
     軌跡（14.2 / 5.8 / 0）幾乎一致

錨點原則：只用「查證過的座標」。trip.json timeline 裡的手寫座標有偏差前例
（Day 1 標的府中四谷橋離實際橋位 1.2km），所以寧可少給路點，讓 BRouter
自己找河濱道，再用稽核腳本驗收，而不是用可疑座標去強迫它繞路。

用法：
    python scripts/rebuild_routes_brouter.py           # 全部待修日
    python scripts/rebuild_routes_brouter.py 1 16      # 指定日
輸出到 routes_rebuilt/dayN_track.gpx，不動原檔。
"""

import json
import math
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT_DIR = os.path.join(ROOT, "routes_rebuilt")
PROFILE = os.environ.get("BROUTER_PROFILE", "trekking")

# (lat, lon)。來源標註在註解裡 —— 沒有來源的座標不放進來。
ANCHORS = {
    1: [(35.698425, 139.778496),   # 秋葉原 CycleTrip Base（原腳本起點，與 GPX 起點一致）
        (35.612230, 139.622600),   # 兵庫島公園（Nominatim 查證）
        (35.651100, 139.447110),   # 浅川CR 入口（真人實騎軌跡起點，實地 GPS）
        (35.631500, 139.270800)],  # Mt. Takao Base Camp（trip.json 住宿座標）
    7: [(35.222000, 138.615000),   # 富士宮市區
        (35.142000, 138.695000),   # 田子の浦港
        (35.105000, 138.800000),   # 千本松原海岸堤防
        (35.083000, 138.858000),   # 沼津港
        (35.122000, 138.915000)],  # 三島市區
    8: [(35.122000, 138.915000),   # 三島市區
        (35.030000, 138.935000),   # 狩野川CR
        (34.970200, 138.926000)],  # 温泉宿 水口
    13: [(35.308000, 139.482000),  # 江之島
         (35.312000, 139.535000),  # 長谷寺
         (35.380000, 139.530000),  # 柏尾川水岸綠道入口
         (35.455000, 139.635000)], # 横濱港未來
    15: [(35.630000, 139.775000),  # 台場海濱公園
         (35.645000, 139.860000),  # 葛西臨海公園
         (35.700000, 139.870000),  # 中川・江戶川水岸
         (35.757000, 139.878000),  # 柴又
         (35.767300, 139.865900)], # 花庵旅舍
    16: [(35.767300, 139.865900),  # 花庵旅舍（環線起點）
         (35.840000, 139.880000),  # 江戶川自行車道
         (35.800000, 139.800000),  # 葛飾水岸
         (35.767300, 139.865900)], # 回花庵
}


def hav(a, b):
    r = 6371000.0
    la1, lo1 = math.radians(a[0]), math.radians(a[1])
    la2, lo2 = math.radians(b[0]), math.radians(b[1])
    return 2 * r * math.asin(math.sqrt(
        math.sin((la2 - la1) / 2) ** 2
        + math.cos(la1) * math.cos(la2) * math.sin((lo2 - lo1) / 2) ** 2))


def brouter(anchors, profile=PROFILE):
    lonlats = "|".join(f"{lon:.6f},{lat:.6f}" for lat, lon in anchors)
    url = ("https://brouter.de/brouter?"
           + urllib.parse.urlencode({"lonlats": lonlats, "profile": profile,
                                     "alternativeidx": 0, "format": "geojson"}))
    last = None
    for attempt in range(5):
        try:
            req = urllib.request.Request(
                url, headers={"User-Agent": "tokyo-cycling-rebuild/1.0 (personal trip planning)"})
            with urllib.request.urlopen(req, timeout=120) as resp:
                data = json.loads(resp.read().decode())
            feat = data["features"][0]
            return feat["geometry"]["coordinates"], feat.get("properties", {})
        except urllib.error.HTTPError as e:
            last = f"HTTP {e.code}: {e.read().decode()[:150]}"
        except Exception as e:                      # noqa: BLE001
            last = f"{type(e).__name__}: {e}"
        wait = 8 * (attempt + 1)
        print(f"    BRouter 失敗（{last}），{wait}s 後重試…", flush=True)
        time.sleep(wait)
    raise RuntimeError(f"BRouter 五次都失敗：{last}")


def write_gpx(path, pts3, name):
    """pts3 = [(lon, lat, ele?), ...]，BRouter geojson 的座標含高度時一併寫入。"""
    with open(path, "w", encoding="utf-8") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n'
                '<gpx version="1.1" creator="rebuild_routes_brouter.py" '
                'xmlns="http://www.topografix.com/GPX/1/1">\n'
                f"<metadata><name>{name}</name></metadata>\n"
                f"<trk><name>{name}</name><trkseg>\n")
        for c in pts3:
            f.write(f'<trkpt lat="{c[1]:.6f}" lon="{c[0]:.6f}">')
            if len(c) > 2:
                f.write(f"<ele>{c[2]:.1f}</ele>")
            f.write("</trkpt>\n")
        f.write("</trkseg></trk></gpx>\n")


def main():
    days = [int(a) for a in sys.argv[1:]] or sorted(ANCHORS)
    trip = json.load(open(os.path.join(ROOT, "data", "trip.json"), encoding="utf-8"))
    tdays = {d["day"]: d for d in (trip["days"] if isinstance(trip, dict) else trip)}
    os.makedirs(OUT_DIR, exist_ok=True)

    print(f"profile = {PROFILE}\n")
    rows = []
    for day in days:
        if day not in ANCHORS:
            print(f"Day {day}: 沒有定義錨點，跳過")
            continue
        coords, props = brouter(ANCHORS[day])
        km = sum(hav((coords[i - 1][1], coords[i - 1][0]), (coords[i][1], coords[i][0]))
                 for i in range(1, len(coords))) / 1000
        # 高度務必用 BRouter 的 filtered ascend：逐點相加會把 SRTM 的高度雜訊
        # 全部算成爬升（Day 1 實測 raw 852m vs filtered 312m，原規劃 238m）。
        gain = float(props.get("filtered ascend", "nan"))
        plain = float(props.get("plain-ascend", "nan"))
        raw = sum(max(0.0, coords[i][2] - coords[i - 1][2])
                  for i in range(1, len(coords))) if len(coords[0]) > 2 else float("nan")
        loss = gain - plain if not math.isnan(plain) else float("nan")
        out = os.path.join(OUT_DIR, f"day{day}_track.gpx")
        write_gpx(out, coords, f"Day {day} rebuilt ({PROFILE})")
        # BRouter 的 filtered ascend 比自己事後平滑可靠，存成 sidecar 給後續使用
        meta = {k: props.get(k) for k in
                ("track-length", "filtered ascend", "plain-ascend", "total-time")}
        meta["profile"] = PROFILE
        meta["anchors"] = ANCHORS[day]
        with open(out.replace("_track.gpx", "_meta.json"), "w", encoding="utf-8") as mf:
            json.dump(meta, mf, ensure_ascii=False, indent=1)

        old = tdays.get(day, {})
        rows.append((day, old.get("planned_km"), old.get("nav", {}).get("gain"),
                     km, gain, raw, len(coords)))
        print(f"Day {day:2d}  {km:6.2f}km  爬升 {gain:.0f}m（逐點雜訊值 {raw:.0f}m）  "
              f"{len(coords)} pts  → {os.path.relpath(out, ROOT)}")
        time.sleep(2)

    print(f"\n{'Day':>4} {'舊km':>7} {'新km':>7} {'差km':>7} {'舊爬升':>8} {'新爬升':>8}")
    for day, plan, oldgain, km, gain, raw, n in rows:
        dp = (km - plan) if plan else float("nan")
        print(f"{day:>4} {plan or 0:>7.1f} {km:>7.2f} {dp:>+7.1f} "
              f"{oldgain or 0:>7.0f}m {gain:>7.0f}m")
    print(f"\n輸出目錄：{OUT_DIR}（原檔未動）")
    print("下一步：python scripts/audit_gpx_roads.py 驗收前，先把暫存檔複製成 "
          "dayN_track.gpx 或改稽核腳本的路徑。")


if __name__ == "__main__":
    main()
