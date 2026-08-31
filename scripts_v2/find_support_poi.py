"""沿每日路線查出單車店與醫院（機械故障與傷病時的求助點）。

單車店半徑較小（爆胎後能牽車或慢騎的距離），醫院半徑較大（叫車或救護
可到的距離）。查得結果投影回沿線里程，方便「我在第 N 公里，最近的在哪」。

OSM 標籤：shop=bicycle；amenity=hospital / clinic（emergency=yes 者另外標記）。
"""
import json, io, os, math, time, urllib.request, urllib.parse

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OVERPASS = 'https://overpass-api.de/api/interpreter'
BIKE_RADIUS_M = 5000       # 爆胎後可牽可慢騎的合理距離
HOSP_RADIUS_M = 10000      # 傷病時叫車／救護可及的距離
SAMPLE_EVERY_M = 2500


def haversine(a, b):
    R = 6371000.0
    p1, p2 = math.radians(a[1]), math.radians(b[1])
    h = (math.sin((p2 - p1) / 2) ** 2
         + math.cos(p1) * math.cos(p2) * math.sin(math.radians(b[0] - a[0]) / 2) ** 2)
    return 2 * R * math.asin(math.sqrt(h))


def fetch(samples):
    coords = ','.join(f'{p[1]:.5f},{p[0]:.5f}' for p in samples)
    q = (f'[out:json][timeout:120];('
         f'node["shop"="bicycle"](around:{BIKE_RADIUS_M},{coords});'
         f'way["shop"="bicycle"](around:{BIKE_RADIUS_M},{coords});'
         f'node["amenity"~"^(hospital|clinic)$"](around:{HOSP_RADIUS_M},{coords});'
         f'way["amenity"~"^(hospital|clinic)$"](around:{HOSP_RADIUS_M},{coords});'
         f');out center tags;')
    req = urllib.request.Request(
        OVERPASS, data=urllib.parse.urlencode({'data': q}).encode(),
        headers={'User-Agent': 'tokyo-cycling-trip-planner/1.0'})
    with urllib.request.urlopen(req, timeout=180) as r:
        return json.load(r).get('elements', [])


def spread_by_km(items, want):
    """沿里程均勻取樣，避免都心動輒上百筆全部塞進頁面。"""
    if len(items) <= want:
        return items
    lo, hi = items[0]['km'], items[-1]['km']
    span = max(hi - lo, 0.1)
    out, used = [], set()
    for i in range(want):
        target = lo + span * i / (want - 1)
        best = min((x for x in items if id(x) not in used),
                   key=lambda x: (abs(x['km'] - target), x['off_km']), default=None)
        if best is not None:
            used.add(id(best))
            out.append(best)
    out.sort(key=lambda x: x['km'])
    return out


def main(shape_dir):
    import sys
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from find_bailout_stations import route_points, cumulative_km, project_to_km

    out = {}
    for day in range(1, 20):
        try:
            pts = route_points(os.path.join(shape_dir, f'day{day}.json'))
            cum = cumulative_km(pts)
            picked, last = [pts[0]], 0.0
            for p, c in zip(pts, cum):
                if (c - last) * 1000 >= SAMPLE_EVERY_M:
                    picked.append(p); last = c
            els = fetch(picked)
            bikes, hosps, seen = [], [], set()
            for e in els:
                t = e.get('tags', {})
                name = t.get('name') or t.get('name:ja')
                la = e.get('lat') or (e.get('center') or {}).get('lat')
                lo = e.get('lon') or (e.get('center') or {}).get('lon')
                if not name or la is None or name in seen:
                    continue
                seen.add(name)
                km, off = project_to_km(la, lo, pts, cum)
                rec = {'name': name, 'km': round(km, 1), 'off_km': round(off / 1000, 1),
                       'lat': round(la, 5), 'lon': round(lo, 5),
                       'tel': t.get('phone') or t.get('contact:phone', ''),
                       'hours': t.get('opening_hours', ''),
                       'web': t.get('website') or t.get('contact:website', '')}
                if t.get('shop') == 'bicycle':
                    rec['brand'] = t.get('brand', '')
                    if off <= BIKE_RADIUS_M:
                        bikes.append(rec)
                else:
                    rec['kind'] = t.get('amenity')
                    rec['emergency'] = t.get('emergency') == 'yes'
                    if off <= HOSP_RADIUS_M and t.get('amenity') == 'hospital':
                        hosps.append(rec)
            bikes.sort(key=lambda x: x['km'])
            hosps.sort(key=lambda x: x['km'])
            out[str(day)] = {'bike_shops': spread_by_km(bikes, 10),
                             'bike_total': len(bikes),
                             'hospitals': spread_by_km(hosps, 8),
                             'hospital_total': len(hosps)}
            print(f'Day {day:>2}: 單車店 {len(bikes):>3} ｜ 醫院 {len(hosps):>3}'
                  + (f' ｜ 最近單車店 {bikes[0]["name"]}' if bikes else ' ｜ ⚠️ 沿線無單車店'))
        except Exception as e:
            print(f'Day {day:>2}: 失敗 {str(e)[:60]}')
            out[str(day)] = {'error': str(e)}
        time.sleep(8)
    dest = os.path.join(ROOT, 'data/support_poi.json')
    io.open(dest, 'w', encoding='utf-8').write(json.dumps(out, ensure_ascii=False, indent=1))
    print(f'\n寫出 {dest}')


if __name__ == '__main__':
    import sys
    main(sys.argv[1])
