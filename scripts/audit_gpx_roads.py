#!/usr/bin/env python3
"""把 19 天的 GPX 逐段對照 OSM 道路分級，抓出實際跑在幹道上的路段。

起因：day1_track.gpx 的 km62–70 跑在日野バイパス（國道20號），但行程文案寫
「100% 堤防自行車道」。路線是 apply_real_cycleway_day1.py 拿手寫座標餵給 OSRM
產生的，座標本身就不在河濱道上，規劃器只能沿最近的道路連，沒人驗證。

做法：沿軌跡每 SAMPLE_M 公尺取樣，用 Overpass 的 around 一次撈出取樣點附近
所有 highway，再對每個取樣點找最近的 way，讀它的 highway 分級與 bicycle 標籤。
比逐點反向地理編碼省三個數量級的請求，而且拿到的是分級不是地名。

用法：
    python scripts/audit_gpx_roads.py            # 全部 19 天
    python scripts/audit_gpx_roads.py 1 4 5      # 只掃指定日
輸出：data/route_audit.json（機器讀）＋ stdout 摘要（人讀）
Overpass 回應會快取在 .cache/overpass/，重跑不會重打 API。
"""

import json
import math
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from collections import defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CACHE_DIR = os.path.join(ROOT, ".cache", "overpass")
OUT_JSON = os.path.join(ROOT, "data", "route_audit.json")

SAMPLE_M = 200          # 取樣間距
SNAP_M = 25             # 第一輪吸附半徑
SNAP_WIDE_M = 60        # 吸附不到時放寬（河濱道在 OSM 上常缺標籤）
CHUNK = 60              # 每次 Overpass 查詢帶幾個取樣點（太多會 timeout）
MIN_RUN_M = 300         # 連續幹道路段短於此不回報
ATTEMPTS = 8            # 公共 Overpass 常丟 504，要有耐心
ENDPOINTS = [
    "https://overpass-api.de/api/interpreter",
    "https://overpass.kumi.systems/api/interpreter",
    "https://overpass.private.coffee/api/interpreter",
]


class OverpassDown(RuntimeError):
    """Overpass 重試到底還是失敗。跳過這天，不要讓整批掃描陣亡。"""

# OSM highway 分級 → 我們關心的四類。
# 判斷標準是「載著行李騎 80km 的體感」，不是法規。
DEDICATED = {"cycleway"}
FOOTISH = {"path", "footway", "pedestrian", "bridleway", "steps"}
CALM = {"residential", "living_street", "unclassified", "service", "track",
        "tertiary", "tertiary_link", "road"}
ARTERIAL = {"secondary", "secondary_link", "primary", "primary_link",
            "trunk", "trunk_link"}
FORBIDDEN = {"motorway", "motorway_link"}
# 這些絕不可能是實際騎乘路面：高架高速會壓在平面道路上方，
# 而下河堤的階梯常落在軌跡 20m 內，兩者都會搶走吸附結果。
NOT_RIDEABLE = FORBIDDEN | {"steps"}
BIKE_OK = {"yes", "designated", "permissive", "official"}

CAT_LABEL = {
    "dedicated": "專用道",
    "calm": "生活道路",
    "arterial": "幹道",
    "forbidden": "禁行/高速",
    "footway_unclear": "步道(單車標示不明)",
    "bicycle_no": "明文禁行單車",
    "unknown": "查無道路",
}


def haversine(p, q):
    """p, q = (lat, lon) → 公尺"""
    r = 6371000.0
    la1, lo1 = math.radians(p[0]), math.radians(p[1])
    la2, lo2 = math.radians(q[0]), math.radians(q[1])
    a = (math.sin((la2 - la1) / 2) ** 2
         + math.cos(la1) * math.cos(la2) * math.sin((lo2 - lo1) / 2) ** 2)
    return 2 * r * math.asin(math.sqrt(a))


def local_xy(p, origin):
    """以 origin 為原點的等距長方投影，公尺。取樣點附近幾百公尺內誤差可忽略。"""
    m_per_deg_lat = 111132.0
    m_per_deg_lon = 111320.0 * math.cos(math.radians(origin[0]))
    return ((p[1] - origin[1]) * m_per_deg_lon, (p[0] - origin[0]) * m_per_deg_lat)


def bearing(a, b):
    """a→b 的方位角（度）。"""
    la1, la2 = math.radians(a[0]), math.radians(b[0])
    dlo = math.radians(b[1] - a[1])
    y = math.sin(dlo) * math.cos(la2)
    x = math.cos(la1) * math.sin(la2) - math.sin(la1) * math.cos(la2) * math.cos(dlo)
    return math.degrees(math.atan2(y, x)) % 360


def bearing_gap(b1, b2):
    """兩方位角差，忽略正反向（道路不分來回）。0–90 度。"""
    d = abs(b1 - b2) % 180
    return min(d, 180 - d)


def point_seg_dist(p, a, b):
    """點到線段距離（公尺）。a、b 為 way 上相鄰兩節點。"""
    px, py = local_xy(p, p)
    ax, ay = local_xy(a, p)
    bx, by = local_xy(b, p)
    dx, dy = bx - ax, by - ay
    if dx == 0 and dy == 0:
        return math.hypot(px - ax, py - ay)
    t = ((px - ax) * dx + (py - ay) * dy) / (dx * dx + dy * dy)
    t = max(0.0, min(1.0, t))
    return math.hypot(px - (ax + t * dx), py - (ay + t * dy))


def read_gpx(path):
    pts = [(float(e.get("lat")), float(e.get("lon")))
           for e in ET.parse(path).getroot().iter() if e.tag.endswith("trkpt")]
    cum = [0.0]
    for i in range(1, len(pts)):
        cum.append(cum[-1] + haversine(pts[i - 1], pts[i]))
    return pts, cum


def resample(pts, cum, step):
    """沿軌跡等距取樣，回傳 [(累積公尺, (lat, lon))]。"""
    out, target, j = [], 0.0, 0
    while target <= cum[-1]:
        while j < len(cum) - 1 and cum[j + 1] < target:
            j += 1
        if j >= len(pts) - 1:
            out.append((target, pts[-1]))
            break
        span = cum[j + 1] - cum[j]
        f = 0.0 if span == 0 else (target - cum[j]) / span
        lat = pts[j][0] + f * (pts[j + 1][0] - pts[j][0])
        lon = pts[j][1] + f * (pts[j + 1][1] - pts[j][1])
        out.append((target, (lat, lon)))
        target += step
    return out


def bad_response(data):
    """Overpass 逾時會回 HTTP 200 帶 remark，不檢查就會把空結果當成『這裡沒有路』。"""
    remark = (data.get("remark") or "").lower()
    if "error" in remark or "timed out" in remark:
        return f"remark: {remark[:80]}"
    if not data.get("elements"):
        return "elements 為空"
    return None


def overpass(coords, tag):
    """撈出 coords 折線 SNAP_WIDE_M 內的所有 highway，附帶 geometry。"""
    os.makedirs(CACHE_DIR, exist_ok=True)
    cache = os.path.join(CACHE_DIR, f"{tag}.json")
    if os.path.exists(cache):
        with open(cache, encoding="utf-8") as f:
            cached = json.load(f)
        why = bad_response(cached)
        if why is None:
            return cached
        print(f"    快取 {tag} 無效（{why}），重抓", flush=True)

    flat = ",".join(f"{lat:.6f},{lon:.6f}" for lat, lon in coords)
    query = (f"[out:json][timeout:180];"
             f"way(around:{SNAP_WIDE_M},{flat})"
             f'["highway"]["highway"!~"^(elevator|construction|proposed)$"];'
             f"out tags geom;")
    body = urllib.parse.urlencode({"data": query}).encode()

    last = None
    for attempt in range(ATTEMPTS):
        url = ENDPOINTS[attempt % len(ENDPOINTS)]
        try:
            req = urllib.request.Request(
                url, data=body,
                headers={"User-Agent": "tokyo-cycling-route-audit/1.0 (personal trip planning)"})
            with urllib.request.urlopen(req, timeout=200) as resp:
                data = json.loads(resp.read().decode())
            why = bad_response(data)
            if why is not None:
                last = RuntimeError(why)
                print(f"    Overpass 回應無效（{why}），重試…", flush=True)
                time.sleep(15)
                continue
            with open(cache, "w", encoding="utf-8") as f:
                json.dump(data, f)
            time.sleep(2)  # 對公共 Overpass 客氣一點
            return data
        except (urllib.error.HTTPError, urllib.error.URLError, TimeoutError) as e:
            last = e
            wait = 10 * (attempt + 1)
            print(f"    Overpass {type(e).__name__}，{wait}s 後換節點重試…", flush=True)
            time.sleep(wait)
    raise OverpassDown(f"Overpass {ATTEMPTS} 次都失敗：{last}")


def classify(tags):
    hw = tags.get("highway", "")
    bike = (tags.get("bicycle") or "").lower()
    if bike == "no":
        return "bicycle_no"
    if hw in DEDICATED:
        return "dedicated"
    if hw in FOOTISH:
        # 日本河濱堤防道常是 path/footway；有 bicycle=designated 才算專用道
        return "dedicated" if bike in BIKE_OK else "footway_unclear"
    if tags.get("cycleway") in ("track", "lane") or tags.get("cycleway:both") in ("track", "lane"):
        return "calm"   # 幹道但有自行車道 → 降級為可接受
    if hw in FORBIDDEN:
        return "forbidden"
    if hw in ARTERIAL:
        return "arterial"
    if hw in CALM:
        return "calm"
    return "calm"


def audit_day(day, gpx_path):
    pts, cum = read_gpx(gpx_path)
    total_km = cum[-1] / 1000
    samples = resample(pts, cum, SAMPLE_M)
    print(f"Day {day:2d}  {os.path.basename(gpx_path):18s} {total_km:6.2f}km  "
          f"{len(samples)} 取樣點", flush=True)

    ways = []
    for i in range(0, len(samples), CHUNK):
        chunk = samples[i:i + CHUNK]
        data = overpass([c[1] for c in chunk], f"day{day}_{i:04d}")
        for el in data.get("elements", []):
            geom = el.get("geometry") or []
            if len(geom) >= 2:
                ways.append((el.get("tags", {}),
                             [(g["lat"], g["lon"]) for g in geom]))
        print(f"    chunk {i // CHUNK + 1}: {len(ways)} ways 累計", flush=True)

    # 網格空間索引：沒有它的話每個取樣點都要掃過全部 ways，19 天跑不完。
    # 格子邊長 ~0.003 度（約 330m），查詢時取 3x3 格，足以覆蓋 SNAP_WIDE_M。
    CELL = 0.003
    grid = defaultdict(list)
    for tags, geom in ways:
        for k in range(len(geom) - 1):
            a, b = geom[k], geom[k + 1]
            seg = (tags, a, b)
            for pt in (a, b):
                grid[(int(pt[0] / CELL), int(pt[1] / CELL))].append(seg)

    results = []
    for idx, (dist_m, p) in enumerate(samples):
        # 取樣點的行進方向：用來排除「剛好在旁邊但走向完全不同」的路，
        # 例如跨越軌跡的橋、垂直的巷子。
        nb = samples[idx + 1][1] if idx + 1 < len(samples) else samples[idx - 1][1]
        track_b = bearing(p, nb) if nb != p else None

        ci, cj = int(p[0] / CELL), int(p[1] / CELL)
        seen = set()
        # 分兩層候選：高速公路（含匝道）永遠不可能是實際騎乘路面，
        # 只有在完全找不到別的路時才拿它來回報，避免高架壓在平面道路上造成誤判。
        best = (1e9, None)
        best_mw = (1e9, None)
        for di in (-1, 0, 1):
            for dj in (-1, 0, 1):
                for seg in grid.get((ci + di, cj + dj), ()):
                    key = id(seg)
                    if key in seen:
                        continue
                    seen.add(key)
                    tags, a, b = seg
                    d = point_seg_dist(p, a, b)
                    if track_b is not None and bearing_gap(track_b, bearing(a, b)) > 40:
                        d += 1000          # 走向不符 → 重罰而非直接剔除
                    if tags.get("highway") in NOT_RIDEABLE:
                        if d < best_mw[0]:
                            best_mw = (d, tags)
                    elif d < best[0]:
                        best = (d, tags)
        if best[1] is None:
            best = best_mw
        d, tags = best
        if tags is None or d > SNAP_WIDE_M:
            cat, name, hw = "unknown", "", ""
        else:
            cat = classify(tags)
            name = tags.get("name") or tags.get("name:ja") or tags.get("ref") or ""
            hw = tags.get("highway", "")
            if d > SNAP_M and cat == "arterial":
                # 吸附距離偏遠的幹道多半是「旁邊有條大路」而非真的騎在上面
                cat = "arterial_maybe"
        results.append({"km": round(dist_m / 1000, 2), "cat": cat,
                        "name": name, "highway": hw, "snap_m": round(d, 1)})

    by_cat = defaultdict(float)
    for r in results:
        by_cat[r["cat"]] += SAMPLE_M / 1000

    runs, cur = [], None
    for r in results:
        if r["cat"] in ("arterial", "forbidden", "bicycle_no"):
            if cur is None:
                cur = {"from_km": r["km"], "to_km": r["km"], "cat": r["cat"],
                       "names": {}}
            cur["to_km"] = r["km"]
            if r["name"]:
                cur["names"][r["name"]] = cur["names"].get(r["name"], 0) + 1
        elif cur is not None:
            runs.append(cur)
            cur = None
    if cur is not None:
        runs.append(cur)
    runs = [r for r in runs
            if (r["to_km"] - r["from_km"]) * 1000 + SAMPLE_M >= MIN_RUN_M]
    for r in runs:
        r["km_len"] = round(r["to_km"] - r["from_km"] + SAMPLE_M / 1000, 1)
        r["names"] = sorted(r["names"], key=r["names"].get, reverse=True)[:3]

    return {"day": day, "gpx": os.path.basename(gpx_path),
            "total_km": round(total_km, 2),
            "by_cat_km": {k: round(v, 1) for k, v in sorted(by_cat.items())},
            "arterial_runs": runs, "samples": results}


def save(existing):
    os.makedirs(os.path.dirname(OUT_JSON), exist_ok=True)
    with open(OUT_JSON, "w", encoding="utf-8") as f:
        json.dump({"generated": time.strftime("%Y-%m-%d %H:%M"),
                   "sample_m": SAMPLE_M, "snap_m": SNAP_M,
                   "snap_wide_m": SNAP_WIDE_M,
                   "days": [existing[k] for k in sorted(existing)]},
                  f, ensure_ascii=False, indent=1)


def main():
    days = [int(a) for a in sys.argv[1:]] or list(range(1, 20))
    existing = {}
    if os.path.exists(OUT_JSON):
        with open(OUT_JSON, encoding="utf-8") as f:
            existing = {d["day"]: d for d in json.load(f).get("days", [])}

    report, failed = [], []
    for day in days:
        gpx = os.path.join(ROOT, f"day{day}_track.gpx")
        if not os.path.exists(gpx):
            print(f"Day {day}: 找不到 {gpx}，跳過")
            continue
        try:
            d = audit_day(day, gpx)
        except OverpassDown as e:
            print(f"Day {day}: {e} — 跳過，稍後重跑這天即可（已完成的 chunk 有快取）")
            failed.append(day)
            continue
        report.append(d)
        existing[day] = d
        save(existing)   # 逐日落地：跑一小時後才寫檔，中途掛掉就全沒了

    print("\n=== 摘要 ===")
    for d in report:
        parts = " ".join(f"{CAT_LABEL.get(k, k)} {v}km"
                         for k, v in d["by_cat_km"].items() if v >= 0.5)
        print(f"\nDay {d['day']:2d} ({d['total_km']}km)  {parts}")
        for r in d["arterial_runs"]:
            names = "／".join(r["names"]) or "（無名稱）"
            print(f"   ⚠ km{r['from_km']:.1f}–{r['to_km']:.1f} "
                  f"({r['km_len']}km) {names}")
    if failed:
        print(f"\n未完成（Overpass 掛掉）：{failed} → "
              f"python scripts/audit_gpx_roads.py {' '.join(map(str, failed))}")
    print(f"\n完整結果：{OUT_JSON}")


if __name__ == "__main__":
    main()
