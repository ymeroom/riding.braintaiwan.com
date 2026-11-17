#!/usr/bin/env python3
"""Re-plan one day on the road: BRouter route through the timeline stops, then update
dayN_track.gpx, data/trip.json (original kept under original_plan) and the day card +
summary row in index.html. Weather/clothing blocks are left alone.

    python3 scripts_v2/replan_day.py spec.json

spec.json:
{
  "day": 6, "route_line": "A ➔ B ➔ C", "change": "11/17 晚改線：…（一句話說明）",
  "timeline": [{"name": "起點：A", "type": "start", "time": "08:30", "coord": [lon, lat], "desc": "…"}, …],
  "hotel": {"name": "…", "addr": "…", "booked": true, "bike": "…", "map_query": "…"},   (optional)
  "lunch_note": "…"                                                                      (optional)
}
Afterwards run build_sketches.py, build_daily.py and build_print.js, and the safety gate.
"""
import html
import json
import re
import sys
import urllib.parse
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import rebuild_routes_brouter as R  # noqa: E402

E = html.escape
ICON = dict(start="🚩", scenic="🌄", rest="☕", end="🏁", pivot="🔀", waypoint="📍")


def main():
    spec = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    n, tl = spec["day"], spec["timeline"]
    coords, props = R.brouter([(p["coord"][1], p["coord"][0]) for p in tl], "trekking")
    cum = [0.0]
    for i in range(1, len(coords)):
        cum.append(cum[-1] + R.hav((coords[i - 1][1], coords[i - 1][0]), (coords[i][1], coords[i][0])) / 1000)
    j = 0
    for p in tl:
        k = min(range(j, len(coords)), key=lambda i: R.hav((p["coord"][1], p["coord"][0]), (coords[i][1], coords[i][0])))
        j = k
        p["km"] = round(cum[k], 1)
    km = round(cum[-1], 1)
    tl[-1]["km"] = km
    gain = int(float(props["filtered ascend"]))
    loss = gain - int(float(props["plain-ascend"]))
    ele = [c[2] for c in coords]

    name = f"Day {n}: {spec['route_line']}"
    with open(ROOT / f"day{n}_track.gpx", "w", encoding="utf-8") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n<gpx version="1.1" creator="TokyoCycling2026 (BRouter trekking)" '
                'xmlns="http://www.topografix.com/GPX/1/1">\n'
                f"  <metadata>\n    <name>{E(name)}</name>\n    <desc>{km} km | +{gain}m / -{loss}m</desc>\n  </metadata>\n"
                f"  <trk>\n    <name>{E(name)}</name>\n    <trkseg>\n")
        for c in coords:
            f.write(f'      <trkpt lat="{c[1]:.6f}" lon="{c[0]:.6f}"><ele>{c[2]:.1f}</ele></trkpt>\n')
        f.write("    </trkseg>\n  </trk>\n</gpx>\n")

    tp = ROOT / "data/trip.json"
    T = json.loads(tp.read_text(encoding="utf-8"))
    d = [x for x in T["days"] if x["day"] == n][0]
    old_route = d["route_line"]
    old_hotel = dict(d.get("hotel") or {})
    d.setdefault("original_plan", {"route_line": d["route_line"], "timeline": d["timeline"],
                                   "planned_km": d.get("planned_km"), "meals": d.get("meals"), "hotel": old_hotel})
    d.update(route_line=spec["route_line"], planned_km=km, route_gain=gain, timeline=tl)
    h = spec.get("hotel")
    if h:
        q = urllib.parse.quote(h.get("map_query") or h["name"])
        d["hotel"] = dict(old_hotel, name=h["name"], addr=h["addr"], booked=h.get("booked", False), bike=h.get("bike", ""),
                          url=f"https://www.google.com/maps/search/?api=1&query={q}", tel=h.get("tel"))
    if spec.get("lunch_note") is not None:
        d["meals"] = dict(d.get("meals") or {}, lunch=[], lunch_note=spec["lunch_note"])
    tp.write_text(json.dumps(T, ensure_ascii=False, indent=1), encoding="utf-8")

    ip = ROOT / "index.html"
    s = ip.read_text(encoding="utf-8")
    i = s.index(f'<div class="day-card" id="day-{n}"')
    j = s.index('<div class="day-card" id="day-', i + 10) if n < 19 else len(s)
    c = s[i:j]
    c = re.sub(r'(<div class="day-title"><span class="day-num">Day \d+</span> \S+ ).*?(</div>)',
               lambda m: m.group(1) + E(spec["route_line"]) + m.group(2), c, count=1)
    gap = (f'<div class="km-gap">🔄 <strong>{E(spec["change"])}</strong> <strong>{km} km</strong>、爬升約 <strong>{gain} m</strong>、'
           f'下降約 {loss} m（BRouter 重算，海拔 {min(ele):.0f}–{max(ele):.0f} m）。上面的里程與爬升是原計畫的 NAVITIME 數字。</div>')
    if 'class="km-gap"' in c:
        c = re.sub(r'<div class="km-gap">.*?</div>', lambda m: gap, c, count=1, flags=re.S)
    else:
        k = c.index('<div class="day-stats">')
        k = c.index("</div>", k) + 6
        c = c[:k] + "\n" + gap + c[k:]
    a = c.index('<ul class="tl-list">')
    b = c.index("</ul>", a) + 5
    lis = "".join(f'''
                    <li class="tl-item tl-{p['type']}">
                        <span class="tl-km">{p['km']:.1f} km</span>
                        <span class="tl-icon">{ICON.get(p['type'], '📍')}</span>
                        <div><strong>{E(p['name'])}</strong>（預定 {p['time']}）<br>{E(p['desc'])}</div>
                    </li>''' for p in tl)
    c = c[:a] + '<ul class="tl-list">' + lis + "\n                </ul>" + c[b:]
    if h:
        status = ('<div class="booking-status status-booked">✅ 已訂房</div>' if h.get("booked")
                  else '<div class="booking-status status-pending">🔍 尚未訂房 — 需儘早確認</div>')
        box = (f'<div class="hotel-box">\n                <div class="hotel-name">🏨 住宿：{E(h["name"])}</div>\n'
               f'                <div class="hotel-address">地址：{E(h["addr"])}</div>\n                {status}\n'
               f'                <div class="bike-store-info">🚲 {E(h.get("bike", ""))}</div>\n'
               f'                <div class="hotel-actions"><a href="{E(d["hotel"]["url"])}" target="_blank" rel="noopener" class="hotel-link">📍 在 Google Maps 查看旅館位置 ↗</a></div>\n            </div>')
        c, nb = re.subn(r'<div class="hotel-box">.*?</div>\s*</div>', lambda m: box, c, count=1, flags=re.S)
        assert nb == 1, "hotel box not found"
    s = s[:i] + c + s[j:]

    r = s.index(f'onclick="scrollToDay({n})"')
    re_ = s.index("</tr>", r)
    row = s[r:re_]
    tds = list(re.finditer(r"<td>.*?</td>", row, re.S))
    rep = {1: f"<td>🔄 {E(spec['route_line'])}</td>"}
    km_td = re.sub(r'<br><small style="color:#B45309;">.*?</small>', "", tds[2].group(0))
    rep[2] = km_td.replace("</td>", f'<br><small style="color:#B45309;">新路線 {km} km</small></td>')
    el_td = re.sub(r'<small style="color:#B45309;">.*?</small><br>', "", tds[3].group(0))
    rep[3] = el_td.replace("<br>", f'<br><small style="color:#B45309;">新路線 +{gain}m / -{loss}m</small><br>', 1)
    if h:
        rep[4] = (f'<td><strong>{E(h["name"])}</strong><br><a href="{E(d["hotel"]["url"])}" target="_blank" rel="noopener" '
                  f'class="map-link">📍 {E(h["addr"])} ↗</a></td>')
    for idx in sorted(rep, reverse=True):
        t = tds[idx]
        row = row[:t.start()] + rep[idx] + row[t.end():]
    if h and h.get("booked"):
        row = row.replace('<span class="badge-pending">🔍 待訂房</span>', '<span class="badge-booked">✅ 🏨 已訂房</span>', 1)
    s = s[:r] + row + s[re_:]
    ip.write_text(s, encoding="utf-8")
    print(f"day {n}: {old_route[:30]}… → {km} km +{gain}/-{loss} m; stops:",
          [(p["name"][:12], p["km"]) for p in tl])


if __name__ == "__main__":
    main()
