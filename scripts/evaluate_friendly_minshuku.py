import urllib.request, json, sys
sys.stdout.reconfigure(encoding='utf-8')

akihabara = [139.7714, 35.6998] # Alt 3m
negoya = [139.26506, 35.577412] # Friendly Minshuku (Alt 201m)
tsuru_yukari = [138.90582, 35.55057] # Yukari Ryokan (Alt 484m)

# Day 1: Akihabara -> Tamagawa CR -> Fuchu -> Hashimoto -> Negoya 2367-6
d1_wps = [
    akihabara,
    [139.7088, 35.5412], # Rokugo Bridge
    [139.6268, 35.6115], # Futako-Tamagawa
    [139.4850, 35.6600], # Fuchu
    [139.3400, 35.5900], # Hashimoto / Sagamihara
    negoya
]

# Day 2: Negoya -> Pref 517 -> Pref 35 (Akiyama Kaido) -> Tsuru Yukari Ryokan
d2_wps = [
    negoya,
    [139.2080, 35.5810], # Pref 517
    [139.1450, 35.5840], # Pref 35 entry
    [139.0500, 35.5680], # Pref 35 mid
    [138.9700, 35.5650], # Pref 35 tunnel
    tsuru_yukari
]

def calc_stats(wps):
    coord_str = ';'.join([f'{c[0]},{c[1]}' for c in wps])
    url = f'http://router.project-osrm.org/route/v1/bicycle/{coord_str}?overview=full&geometries=geojson'
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req) as resp:
        data = json.loads(resp.read().decode('utf-8'))
        r = data['routes'][0]
        dist_km = round(r['distance'] / 1000.0, 1)
        coords = r['geometry']['coordinates']

    sampled = coords[::max(1, len(coords)//50)]
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

    gain = sum([max(0, elevs[i]-elevs[i-1]) for i in range(1, len(elevs)) if abs(elevs[i]-elevs[i-1])>=4])
    loss = sum([max(0, elevs[i-1]-elevs[i]) for i in range(1, len(elevs)) if abs(elevs[i-1]-elevs[i])>=4])
    return dist_km, round(gain), round(loss), round(elevs[0]), round(max(elevs)), round(elevs[-1])

d1_dist, d1_gain, d1_loss, d1_start, d1_max, d1_end = calc_stats(d1_wps)
d2_dist, d2_gain, d2_loss, d2_start, d2_max, d2_end = calc_stats(d2_wps)

print("=== 住宿點評估：フレンドリー民宿 (Friendly Minshuku) ===")
print("地址: 神奈川縣相模原市綠區根小屋 2367-6 (海拔 201m)")
print(f"Day 1: {d1_dist} km ｜ 爬升 +{d1_gain}m / -{d1_loss}m ｜ 海拔 {d1_start}m ➔ {d1_end}m")
print(f"Day 2: {d2_dist} km ｜ 爬升 +{d2_gain}m / -{d2_loss}m ｜ 海拔 {d2_start}m ➔ {d2_end}m (最高 {d2_max}m)")
