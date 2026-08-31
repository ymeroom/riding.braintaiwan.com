"""策略 B：對「沒站區」找出 20 公里內實際存在的住宿點。

沿沒站區每隔數公里取一個抽樣點，查詢該點周圍 20 公里內的旅館、民宿、
青年旅舍與山莊，換算「從路線上這個位置出發要偏離多少公里」。
輸出讓騎士能直接判斷：在第 N 公里出狀況時，最近的落腳處在哪、多遠。
"""
import json, io, os, math, time, urllib.request, urllib.parse

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OVERPASS = 'https://overpass-api.de/api/interpreter'
MAX_DETOUR_KM = 20          # 使用者定義的策略 B 半徑
SAMPLE_EVERY_KM = 6         # 沒站區的抽樣間距
TOP_N = 4                   # 每個抽樣點保留幾個最近住宿

TOURISM = 'hotel|guest_house|hostel|motel|chalet|alpine_hut|apartment'


def haversine(a, b):
    R = 6371000.0
    p1, p2 = math.radians(a[1]), math.radians(b[1])
    h = (math.sin((p2 - p1) / 2) ** 2
         + math.cos(p1) * math.cos(p2) * math.sin(math.radians(b[0] - a[0]) / 2) ** 2)
    return 2 * R * math.asin(math.sqrt(h))


def query(lat, lon):
    q = (f'[out:json][timeout:90];'
         f'(node["tourism"~"^({TOURISM})$"](around:{MAX_DETOUR_KM * 1000},{lat:.5f},{lon:.5f});'
         f' way["tourism"~"^({TOURISM})$"](around:{MAX_DETOUR_KM * 1000},{lat:.5f},{lon:.5f}););'
         f'out center tags;')
    req = urllib.request.Request(
        OVERPASS, data=urllib.parse.urlencode({'data': q}).encode(),
        headers={'User-Agent': 'tokyo-cycling-trip-planner/1.0'})
    with urllib.request.urlopen(req, timeout=120) as r:
        return json.load(r).get('elements', [])


def main(shape_dir):
    import sys
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from find_bailout_stations import route_points, cumulative_km

    st = json.load(io.open(os.path.join(ROOT, 'data/bailout_stations.json'), encoding='utf-8'))
    out = {}
    for day in map(str, range(1, 20)):
        gaps = (st.get(day) or {}).get('gaps') or []
        if not gaps:
            continue
        pts = route_points(os.path.join(shape_dir, f'day{day}.json'))
        cum = cumulative_km(pts)
        day_out = []
        for g in gaps:
            samples = []
            k = g['from_km'] + SAMPLE_EVERY_KM / 2
            while k < g['to_km']:
                idx = min(range(len(cum)), key=lambda i: abs(cum[i] - k))
                samples.append((round(cum[idx], 1), pts[idx]))
                k += SAMPLE_EVERY_KM
            picks = []
            for km, p in samples:
                try:
                    els = query(p[1], p[0])
                except Exception as e:
                    print(f'  Day {day} {km}km 查詢失敗: {str(e)[:40]}')
                    time.sleep(30)
                    continue
                rows = []
                for e in els:
                    t = e.get('tags', {})
                    name = t.get('name') or t.get('name:ja')
                    if not name:
                        continue
                    la = e.get('lat') or (e.get('center') or {}).get('lat')
                    lo = e.get('lon') or (e.get('center') or {}).get('lon')
                    if la is None:
                        continue
                    d = haversine(p, [lo, la]) / 1000
                    rows.append({'name': name, 'kind': t.get('tourism'),
                                 'detour_km': round(d, 1),
                                 'lat': round(la, 5), 'lon': round(lo, 5),
                                 'phone': t.get('phone') or t.get('contact:phone', ''),
                                 'web': t.get('website') or t.get('contact:website', '')})
                rows.sort(key=lambda r: r['detour_km'])
                picks.append({'at_km': km, 'lodging': rows[:TOP_N]})
                print(f'  Day {day} 第 {km} km：{len(rows)} 處住宿，最近 '
                      + (f"{rows[0]['name']} {rows[0]['detour_km']}km" if rows else '無'))
                time.sleep(6)
            day_out.append({**g, 'samples': picks})
        out[day] = day_out
    dest = os.path.join(ROOT, 'data/bailout_lodging.json')
    io.open(dest, 'w', encoding='utf-8').write(json.dumps(out, ensure_ascii=False, indent=1))
    print(f'\n寫出 {dest}')


if __name__ == '__main__':
    import sys
    main(sys.argv[1])
