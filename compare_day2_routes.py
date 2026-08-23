import urllib.request, json, sys
sys.stdout.reconfigure(encoding='utf-8')

takao_basecamp = [139.2705, 35.6323]
dest_yukari = [138.90582, 35.55057]

routes = {
    "1. 原始大車主幹道 (國道20號/大垂水峠 ➔ 大月 ➔ 都留)": [
        takao_basecamp,
        [139.2300, 35.6200], # Otarumi Pass (392m)
        [139.1800, 35.6150], # Sagamiko
        [139.1100, 35.6300], # Uenohara
        [138.9400, 35.6100], # Otsuki
        dest_yukari
    ],
    "2. 經大垂水峠 ➔ 相模湖 ➔ 縣道35秋山街道 ➔ 都留": [
        takao_basecamp,
        [139.2300, 35.6200], # Otarumi Pass
        [139.1800, 35.6150], # Sagamiko
        [139.1450, 35.5800], # Pref 35 entry (Akiyama)
        [139.0400, 35.5680], # Pref 35 mid
        dest_yukari
    ],
    "3. 避大垂水：經國道413/三井大橋(北岸) ➔ 縣道35秋山街道 ➔ 都留": [
        takao_basecamp,
        [139.2780, 35.6150], # Machida Kaido
        [139.2600, 35.5900], # Rt 413 North shore
        [139.2000, 35.5850], # Pref 517 direct
        [139.1450, 35.5800], # Pref 35 entry
        [139.0400, 35.5680],
        dest_yukari
    ],
    "4. 避大垂水：經津久井湖南岸(縣道515/517深山連峰) ➔ 縣道35 ➔ 都留": [
        takao_basecamp,
        [139.2780, 35.6150], # Machida Kaido
        [139.2550, 35.5880], # Pref 515 south shore
        [139.2080, 35.5810], # Pref 517 south shore
        [139.1450, 35.5800], # Pref 35 entry
        [139.0400, 35.5680],
        dest_yukari
    ]
}

def analyze_route(name, waypoints):
    coord_str = ';'.join([f'{c[0]},{c[1]}' for c in waypoints])
    url = f'http://router.project-osrm.org/route/v1/bicycle/{coord_str}?overview=full&geometries=geojson'
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req) as resp:
        data = json.loads(resp.read().decode('utf-8'))
        r = data['routes'][0]
        dist_km = round(r['distance'] / 1000.0, 1)
        coords = r['geometry']['coordinates']

    sampled = coords[::max(1, len(coords)//60)]
    elevs = []
    for pt in sampled:
        gsi_url = f'https://cyberjapandata2.gsi.go.jp/general/dem/scripts/getelevation.php?lon={pt[0]}&lat={pt[1]}&outtype=JSON'
        try:
            req_gsi = urllib.request.Request(gsi_url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req_gsi, timeout=4) as g_resp:
                g_data = json.loads(g_resp.read().decode('utf-8'))
                elevs.append(float(g_data.get('elevation', 0)))
        except:
            pass

    # 5m threshold gain
    gain = 0
    loss = 0
    prev = elevs[0]
    for e in elevs[1:]:
        diff = e - prev
        if abs(diff) >= 5:
            if diff > 0:
                gain += diff
            else:
                loss += abs(diff)
            prev = e

    return dist_km, round(gain), round(loss), round(elevs[0]), round(max(elevs)), round(elevs[-1])

print("=== Day 2 各種路線走法里程與爬升真實比對 ===")
for name, wps in routes.items():
    dist, gain, loss, s_e, max_e, end_e = analyze_route(name, wps)
    print(f"\n【{name}】")
    print(f"  里程: {dist} km ｜ 爬升: +{gain} m ｜ 下降: -{loss} m")
    print(f"  起點海拔: {s_e}m ➔ 最高點: {max_e}m ➔ 終點: {end_e}m")
