import urllib.request, urllib.parse, json, sys
sys.stdout.reconfigure(encoding='utf-8')

# 1. Geocode Destination: 由加利旅館 (山梨県都留市上谷1丁目3-4)
query = '山梨県都留市上谷1丁目3-4'
url_geo = f'https://msearch.gsi.go.jp/address-search/AddressSearch?q={urllib.parse.quote(query)}'
req = urllib.request.Request(url_geo, headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req) as resp:
    data = json.loads(resp.read().decode('utf-8'))
    lon, lat = data[0]['geometry']['coordinates']

# Destination: 由加利旅館 (Yukari Ryokan, Tsuru)
dest_yukari = [lon, lat]

# Start: Mt. Takao Base Camp
takao_basecamp = [139.2705, 35.6323] # Alt: ~190m

# Also compare if starting from Fuchu (Old Day 2)
fuchu_station = [139.4795, 35.6675]

def get_stats(start_pt, start_name):
    if start_name == "Mt. Takao Base Camp":
        waypoints = [
            start_pt,
            [139.2780, 35.6150], # Machida Kaido bypass
            [139.2550, 35.5880], # Pref 515 Lake Tsukui
            [139.2080, 35.5810], # Pref 517
            [139.1450, 35.5800], # Pref 35 Akiyama entry
            [139.0400, 35.5680], # Pref 35 middle (Akiyama)
            dest_yukari
        ]
    else:
        waypoints = [
            start_pt,
            [139.4350, 35.6580],
            [139.3300, 35.6550],
            [139.2800, 35.6350],
            [139.2550, 35.5880],
            [139.1450, 35.5800],
            dest_yukari
        ]

    coord_str = ';'.join([f'{c[0]},{c[1]}' for c in waypoints])
    url_osrm = f'http://router.project-osrm.org/route/v1/bicycle/{coord_str}?overview=full&geometries=geojson'
    req_osrm = urllib.request.Request(url_osrm, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req_osrm) as resp:
        data = json.loads(resp.read().decode('utf-8'))
        r = data['routes'][0]
        dist_km = round(r['distance'] / 1000.0, 1)
        coords = r['geometry']['coordinates']

    elevs = []
    step = max(1, len(coords) // 40)
    sampled = coords[::step]
    if sampled[-1] != coords[-1]:
        sampled.append(coords[-1])

    for pt in sampled:
        gsi_url = f'https://cyberjapandata2.gsi.go.jp/general/dem/scripts/getelevation.php?lon={pt[0]}&lat={pt[1]}&outtype=JSON'
        try:
            req_gsi = urllib.request.Request(gsi_url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req_gsi, timeout=4) as g_resp:
                g_data = json.loads(g_resp.read().decode('utf-8'))
                elev = float(g_data.get('elevation', 0))
                elevs.append(elev)
        except:
            pass

    ascent = sum([max(0, elevs[i] - elevs[i-1]) for i in range(1, len(elevs))])
    descent = sum([max(0, elevs[i-1] - elevs[i]) for i in range(1, len(elevs))])

    return {
        "start": start_name,
        "dist_km": dist_km,
        "ascent": round(ascent),
        "descent": round(descent),
        "start_e": round(elevs[0]),
        "end_e": round(elevs[-1]),
        "max_e": round(max(elevs)),
        "min_e": round(min(elevs))
    }

res_from_takao = get_stats(takao_basecamp, "Mt. Takao Base Camp")
res_from_fuchu = get_stats(fuchu_station, "府中市 (原起點)")

print(f"由加利旅館 經緯度座標: {lon:.5f}, {lat:.5f} (海拔: {res_from_takao['end_e']}m)")
print("\n--- 方案 A：從 Mt. Takao Base Camp 出發 (強烈推薦) ---")
print(f"總里程: {res_from_takao['dist_km']} km")
print(f"累積爬升: +{res_from_takao['ascent']} m")
print(f"累積下降: -{res_from_takao['descent']} m")
print(f"起點海拔: {res_from_takao['start_e']} m (高尾山口)")
print(f"終點海拔: {res_from_takao['end_e']} m (都留市由加利旅館)")
print(f"最高海拔: {res_from_takao['max_e']} m (山梨縣道35號秋山隧道口)")

print("\n--- 方案 B：從 府中 出發 (原方案) ---")
print(f"總里程: {res_from_fuchu['dist_km']} km")
print(f"累積爬升: +{res_from_fuchu['ascent']} m")
print(f"累積下降: -{res_from_fuchu['descent']} m")
