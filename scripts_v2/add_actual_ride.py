#!/usr/bin/env python3
"""Publish one day's actual ride (from a Garmin FIT point dump) to the site.

    python3 scripts_v2/add_actual_ride.py <day> <points.json>

<points.json> is a list of [lat, lon, ele, dist_m, iso_time, temp, speed] produced
locally from the FIT file (see HANDOFF 8.7). The summary for the day must already be
in data/actual_rides.json. This script:
  1. writes actual/day<N>_actual.gpx (RDP-simplified, lat/lon/ele only: no time, no HR)
  2. overlays it on day<N>_route_map_demo.html (red dashed line + layer toggle + summary box)
  3. adds the summary block to the day card in index.html (after the daily-link)
Re-running replaces earlier injections. Run the safety gate on index.html afterwards.
"""
import html
import json
import math
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
E = html.escape


def rdp(Q, eps):
    if len(Q) < 3:
        return Q
    keep, stack = {0, len(Q) - 1}, [(0, len(Q) - 1)]
    while stack:
        i, j = stack.pop()
        a, b = Q[i], Q[j]
        den = math.hypot(b[0] - a[0], b[1] - a[1])
        dmax, idx = 0, None
        for k in range(i + 1, j):
            p = Q[k]
            d = (math.hypot(p[0] - a[0], p[1] - a[1]) if den < 1e-12
                 else abs((b[1] - a[1]) * (a[0] - p[0]) - (a[1] - p[1]) * (b[0] - a[0])) / den)
            if d > dmax:
                dmax, idx = d, k
        if idx is not None and dmax > eps:
            keep.add(idx)
            stack += [(i, idx), (idx, j)]
    return [Q[k] for k in sorted(keep)]


def main():
    n, src = int(sys.argv[1]), sys.argv[2]
    r = json.loads((ROOT / "data/actual_rides.json").read_text(encoding="utf-8"))[str(n)]
    pts = [(round(p[0], 6), round(p[1], 6), round(p[2] or 0, 1)) for p in json.load(open(src)) if p[0]]
    s = rdp(pts, 0.00004)
    (ROOT / "actual").mkdir(exist_ok=True)
    gpx = ROOT / f"actual/day{n}_actual.gpx"
    with open(gpx, "w", encoding="utf-8") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n<gpx version="1.1" creator="TokyoCycling2026 (actual ride, simplified)" '
                'xmlns="http://www.topografix.com/GPX/1/1">\n'
                f'  <metadata><name>Day {n} 實騎：{E(r["route_line"])}</name><desc>{r["km"]} km | +{r["gain"]}m</desc></metadata>\n'
                f'  <trk><name>Day {n} 實騎</name><trkseg>\n')
        for a, b, c in s:
            f.write(f'    <trkpt lat="{a}" lon="{b}"><ele>{c}</ele></trkpt>\n')
        f.write("  </trkseg></trk>\n</gpx>\n")

    summary = (f'<strong>{r["km"]} km</strong> ・ 騎乘 <strong>{E(r["moving"])}</strong>（全程 {E(r["elapsed"])}）・ 爬升 <strong>{r["gain"]} m</strong> ・ '
               f'{E(r["start"])} {E(r["start_place"])} → {E(r["end"])} {E(r["end_place"])}')
    stops = "、".join(r.get("stops", []))

    # map overlay
    mp = ROOT / f"day{n}_route_map_demo.html"
    m = mp.read_text(encoding="utf-8")
    m = re.sub(r"\n// 2b\. Actual ride.*?// end actual ride\n", "\n", m, flags=re.S)
    m = re.sub(r'\n        <div class="actual-ride".*?</div><!-- /actual-ride -->', "", m, flags=re.S)
    anchor = "map.fitBounds(polyline.getBounds(), { padding: [30, 30] });"
    assert m.count(anchor) == 1, "map anchor not found"
    coords = json.dumps([[b, a] for a, b, _ in s], separators=(",", ":"))
    js = (anchor + f"""
// 2b. Actual ride (Garmin, simplified; no heart rate or timestamps)
const actualCoords = {coords};
const actualLine = L.polyline(actualCoords.map(c => [c[1], c[0]]), {{ color: '#DC2626', weight: 5, opacity: 0.9, dashArray: '10 6' }})
    .addTo(map).bindPopup({json.dumps(f'<strong>{r["date"]} 實騎路線</strong><br>{r["km"]} km ・ 騎乘 {r["moving"]} ・ 爬升 {r["gain"]} m', ensure_ascii=False)});
L.control.layers(null, {{ "計畫路線（藍）": polyline, "{r['date']} 實騎路線（紅虛線）": actualLine }}, {{ collapsed: false, position: 'bottomleft' }}).addTo(map);
map.fitBounds(polyline.getBounds().extend(actualLine.getBounds()), {{ padding: [30, 30] }});
// end actual ride
""")
    m = m.replace(anchor, js)
    box = (f'\n        <div class="actual-ride" style="margin:12px 0;padding:12px 14px;border:2px solid #DC2626;border-radius:10px;background:#FEF2F2;color:#1F2937;font-size:14px;line-height:1.7;">'
           f'<strong style="color:#B91C1C;">🚴 {E(r["date"])} 實騎紀錄</strong>（地圖上的紅色虛線；藍線是原計畫）<br>{summary}<br>{E(r["route_note"])}<br>'
           f'<small>{"休息：" + E(stops) + "。" if stops else ""}資料來源：{E(r["source"])}。 <a href="actual/day{n}_actual.gpx" download>下載實騎 GPX</a></small></div><!-- /actual-ride -->')
    assert m.count('<div id="map"></div>') == 1
    m = m.replace('<div id="map"></div>', '<div id="map"></div>' + box)
    mp.write_text(m, encoding="utf-8")

    # day card in index.html
    ip = ROOT / "index.html"
    s_ = ip.read_text(encoding="utf-8")
    i = s_.index(f'<div class="day-card" id="day-{n}"')
    j = s_.index('<div class="day-card" id="day-', i + 10) if n < 19 else len(s_)
    card = s_[i:j]
    card = re.sub(r'\n            <div class="actual-ride".*?</div>', "", card, flags=re.S)
    k = card.index(f'href="daily/day{n}.html"')
    k = card.index("</a>", k) + 4
    blk = (f'\n            <div class="actual-ride" style="display:block; margin:0 0 12px; padding:10px 12px; border:2px solid #DC2626; border-radius:8px; background:#FEF2F2; color:#1F2937; font-size:13.5px; line-height:1.7;">'
           f'<strong style="color:#B91C1C;">🚴 {E(r["date"])} 實騎紀錄</strong>：{summary}<br>{E(r["route_note"])}<br>'
           f'<a href="day{n}_route_map_demo.html#map" style="font-weight:700;">🗺️ 看實騎路線地圖（紅虛線＝實騎、藍線＝計畫）</a> ・ <a href="actual/day{n}_actual.gpx" download>下載實騎 GPX</a></div>')
    card = card[:k] + blk + card[k:]
    ip.write_text(s_[:i] + card + s_[j:], encoding="utf-8")
    print(f"day {n}: {len(pts)} -> {len(s)} points; map, card and GPX written")


if __name__ == "__main__":
    main()
