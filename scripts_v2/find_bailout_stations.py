"""沿每日 NAVITIME 路線找出可輪行的車站，並標出「沒站區」。

撤退策略（依使用者定義）：
  A. 有火車站 → 裝攜車袋（輪行袋）搭到下一站／下一個住宿點
  B. 沒火車站 → 在 20 公里內找下一個區域訂住宿

作法：對每日路線幾何取樣，用 Overpass API 的 around 過濾器查詢沿線
3 公里內的鐵路車站，換算成沿線里程後排序；相鄰兩站里程差超過門檻的
區段即為「沒站區」，套用策略 B。
"""
import json, io, os, math, time, urllib.request, urllib.parse, collections

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OVERPASS = 'https://overpass-api.de/api/interpreter'
SEARCH_RADIUS_M = 3000      # 離路線多遠仍算「沿線可撤退」
GAP_THRESHOLD_KM = 12.0     # 相鄰站距超過此值視為沒站區
SAMPLE_EVERY_M = 1500       # 路線取樣間距


def haversine(a, b):
    R = 6371000.0
    p1, p2 = math.radians(a[1]), math.radians(b[1])
    h = (math.sin((p2 - p1) / 2) ** 2
         + math.cos(p1) * math.cos(p2) * math.sin(math.radians(b[0] - a[0]) / 2) ** 2)
    return 2 * R * math.asin(math.sqrt(h))


def route_points(shape_path, route_no='2'):
    """取 NAVITIME 指定路線偏好的有序座標（預設 2 = 坡少，與網站數據同源）。"""
    geo = json.load(io.open(shape_path, encoding='utf-8'))
    feats = [f for f in geo['features'] if f['properties'].get('route_no') == route_no]
    if not feats:
        feats = [f for f in geo['features'] if f['properties'].get('route_no') == '1']
    pts = []
    for f in feats:
        for c in f['geometry']['coordinates']:
            if not pts or pts[-1] != c:
                pts.append(c)
    return pts


def cumulative_km(pts):
    out, acc = [0.0], 0.0
    for i in range(len(pts) - 1):
        acc += haversine(pts[i], pts[i + 1])
        out.append(acc / 1000)
    return out


def sample(pts, cum, every_m=SAMPLE_EVERY_M):
    picked, last = [pts[0]], 0.0
    for p, c in zip(pts, cum):
        if (c - last) * 1000 >= every_m:
            picked.append(p)
            last = c
    if picked[-1] != pts[-1]:
        picked.append(pts[-1])
    return picked


def overpass_stations(samples):
    coords = ','.join(f'{p[1]:.5f},{p[0]:.5f}' for p in samples)
    q = (f'[out:json][timeout:90];'
         f'node["railway"="station"](around:{SEARCH_RADIUS_M},{coords});'
         f'out body;')
    req = urllib.request.Request(
        OVERPASS, data=urllib.parse.urlencode({'data': q}).encode(),
        headers={'User-Agent': 'tokyo-cycling-trip-planner/1.0'})
    with urllib.request.urlopen(req, timeout=120) as r:
        return json.load(r).get('elements', [])


def project_to_km(lat, lon, pts, cum):
    """把車站投影到路線上，回傳沿線里程與離線距離。"""
    best = (1e9, 0.0)
    for p, c in zip(pts, cum):
        d = haversine([lon, lat], p)
        if d < best[0]:
            best = (d, c)
    return best[1], best[0]


def analyse(day, shape_dir):
    pts = route_points(os.path.join(shape_dir, f'day{day}.json'))
    cum = cumulative_km(pts)
    total = cum[-1]
    els = overpass_stations(sample(pts, cum))
    seen, stations = set(), []
    for e in els:
        t = e.get('tags', {})
        name = t.get('name') or t.get('name:ja') or ''
        if not name or name in seen:
            continue
        seen.add(name)
        km, off = project_to_km(e['lat'], e['lon'], pts, cum)
        stations.append({
            'name': name,
            'name_en': t.get('name:en', ''),
            'operator': t.get('operator', ''),
            'km': round(km, 1),
            'off_km': round(off / 1000, 1),
            'lat': round(e['lat'], 5), 'lon': round(e['lon'], 5),
        })
    stations.sort(key=lambda s: s['km'])

    # 找沒站區：起點、各站、終點之間的里程缺口
    marks = [0.0] + [s['km'] for s in stations] + [round(total, 1)]
    gaps = []
    for i in range(len(marks) - 1):
        span = marks[i + 1] - marks[i]
        if span >= GAP_THRESHOLD_KM:
            before = stations[i - 1]['name'] if 0 < i <= len(stations) else '當日起點'
            after = stations[i]['name'] if i < len(stations) else '當日終點'
            gaps.append({'from_km': round(marks[i], 1), 'to_km': round(marks[i + 1], 1),
                         'span_km': round(span, 1), 'after': before, 'before': after})
    return {'total_km': round(total, 1), 'stations': stations, 'gaps': gaps}


def main(shape_dir):
    out = {}
    for d in range(1, 20):
        try:
            out[str(d)] = analyse(d, shape_dir)
            s, g = out[str(d)]['stations'], out[str(d)]['gaps']
            print(f'Day {d:>2}: {len(s):>2} 站 ｜ {len(g)} 個沒站區 ｜ '
                  + (', '.join(x['name'] for x in s[:6]) + ('…' if len(s) > 6 else '')))
        except Exception as e:
            print(f'Day {d:>2}: 失敗 {e}')
            out[str(d)] = {'error': str(e)}
        time.sleep(4)  # 尊重 Overpass 公用服務
    dest = os.path.join(ROOT, 'data/bailout_stations.json')
    io.open(dest, 'w', encoding='utf-8').write(json.dumps(out, ensure_ascii=False, indent=1))
    print(f'\n寫出 {dest}')


if __name__ == '__main__':
    import sys
    main(sys.argv[1])
