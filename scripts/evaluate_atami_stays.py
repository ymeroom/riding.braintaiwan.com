import urllib.request, urllib.parse, json, sys
sys.stdout.reconfigure(encoding='utf-8')

def geocode(address):
    url = f"https://msearch.gsi.go.jp/address-search/AddressSearch?q={urllib.parse.quote(address)}"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req) as resp:
        data = json.loads(resp.read().decode('utf-8'))
        lon, lat = data[0]['geometry']['coordinates']

    gsi_url = f"https://cyberjapandata2.gsi.go.jp/general/dem/scripts/getelevation.php?lon={lon}&lat={lat}&outtype=JSON"
    req_gsi = urllib.request.Request(gsi_url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req_gsi) as resp:
        elev = json.loads(resp.read().decode('utf-8'))['elevation']

    return lon, lat, float(elev)

# Geocode Day 10 and Day 11 lodgings
lon1, lat1, elev1 = geocode("静岡県熱海市下多賀440")
lon2, lat2, elev2 = geocode("静岡県熱海市下多賀1473-11")

stay10 = [lon1, lat1] # Apt南熱海-網代
stay11 = [lon2, lat2] # Izu Kansya (伊豆観舎)

# Key points
ito_onsen = [139.0980, 34.9700] # Day 9 end / Day 10 start (Ito)
usami = [139.0800, 35.0080] # Usami
ajiro_old_street = [139.0880, 35.0420] # Ajiro bypass
atami_sun_beach = [139.0750, 35.0970] # Atami Beach (Fireworks venue)
atami_baien = [139.0550, 35.0980] # Atami Plum Garden (Momiji)
odawara = [139.1550, 35.2500] # Odawara Castle
enoshima = [139.4820, 35.3080] # Enoshima

def calc_route(wps, name):
    coord_str = ';'.join([f'{c[0]},{c[1]}' for c in wps])
    url = f'http://router.project-osrm.org/route/v1/bicycle/{coord_str}?overview=full&geometries=geojson'
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req) as resp:
        data = json.loads(resp.read().decode('utf-8'))
        r = data['routes'][0]
        dist_km = round(r['distance'] / 1000.0, 1)
        coords = r['geometry']['coordinates']

    sampled = coords[::max(1, len(coords)//40)]
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

# Day 10: Ito -> Usami -> Ajiro old street -> Apt南熱海-網代 (下多賀440)
d10_dist, d10_gain, d10_loss, d10_s, d10_m, d10_e = calc_route([ito_onsen, usami, ajiro_old_street, stay10], "Day 10")

# Day 11: Apt南熱海 (下多賀440) -> Izu Kansya (下多賀1473-11) + Daytime Atami sightseeing (Atami Baien, Sun Beach)
d11_dist, d11_gain, d11_loss, d11_s, d11_m, d11_e = calc_route([stay10, stay11, atami_baien, atami_sun_beach, stay11], "Day 11")

# Day 12: Izu Kansya (下多賀1473-11) -> Atami Beach -> Pref 740 -> Odawara -> Enoshima
d12_dist, d12_gain, d12_loss, d12_s, d12_m, d12_e = calc_route([stay11, atami_sun_beach, [139.1450, 35.1550], odawara, [139.3100, 35.3200], enoshima], "Day 12")

print("=== 住宿點詳細定位 ===")
print(f"1. 11/22 (Day 10) Apt南熱海-網代 (下多賀440): 經緯度 [{lon1:.5f}, {lat1:.5f}], 海拔 {elev1:.1f}m")
print(f"2. 11/23 (Day 11) Izu Kansya (下多賀1473-11): 經緯度 [{lon2:.5f}, {lat2:.5f}], 海拔 {elev2:.1f}m")

print("\n=== 路線數據與騎行分析 ===")
print(f"Day 10 (伊東 ➔ 網代舊街 ➔ Apt南熱海-網代): 里程 = {d10_dist} km ｜ 爬升 = +{d10_gain}m / -{d10_loss}m ｜ 海拔 {d10_s}m ➔ {d10_e}m")
print(f"Day 11 (下多賀換宿 ➔ 熱海梅園紅葉 ➔ 晚上海上煙火祭 ➔ Izu Kansya): 里程 = {d11_dist} km ｜ 爬升 = +{d11_gain}m / -{d11_loss}m ｜ 輕裝機動")
print(f"Day 12 (Izu Kansya ➔ 縣道740 ➔ 小田原城 ➔ 湘南海岸 ➔ 江之島): 里程 = {d12_dist} km ｜ 爬升 = +{d12_gain}m / -{d12_loss}m ｜ 海拔 {d12_s}m ➔ {d12_e}m")
