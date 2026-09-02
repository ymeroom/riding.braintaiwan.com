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

lon_mizuguchi, lat_mizuguchi, elev_mizuguchi = geocode("静岡県伊豆市修善寺3463-17")
lon_kawana, lat_kawana, elev_kawana = geocode("静岡県伊東市新井484-30")

print(f"11/20 (Day 8) Onsen Yado Mizuguchi (修善寺3463-17): 經緯度 [{lon_mizuguchi:.5f}, {lat_mizuguchi:.5f}], 海拔 {elev_mizuguchi:.1f}m")
print(f"11/21 (Day 9) kawana seaview standard (伊東市新井484-30): 經緯度 [{lon_kawana:.5f}, {lat_kawana:.5f}], 海拔 {elev_kawana:.1f}m")

# Day 8: Mishima -> Kano River CR -> Mizuguchi (Shuzenji)
mishima = [138.9150, 35.1220] # 25m
wps_d8 = [mishima, [138.9350, 35.0300], [lon_mizuguchi, lat_mizuguchi]]

# Day 9: Mizuguchi -> Hiekawa Pass -> Ippeki Lake -> Jogasaki -> Kawana seaview (Arai 484-30)
jogasaki = [139.1300, 34.8900]
wps_d9 = [[lon_mizuguchi, lat_mizuguchi], [139.0200, 34.9600], [139.1000, 34.9200], jogasaki, [lon_kawana, lat_kawana]]

def calc(wps):
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

d8_dist, d8_gain, d8_loss, d8_s, d8_m, d8_e = calc(wps_d8)
d9_dist, d9_gain, d9_loss, d9_s, d9_m, d9_e = calc(wps_d9)

print(f"Day 8 (三島 ➔ 狩野川CR ➔ 温泉宿 水口): 里程={d8_dist}km, 爬升=+{d8_gain}m, 下降=-{d8_loss}m, 海拔: {d8_s}m ➔ {d8_e}m")
print(f"Day 9 (水口 ➔ 冷川峠 ➔ 一碧湖 ➔ 城崎海岸 ➔ kawana seaview): 里程={d9_dist}km, 爬升=+{d9_gain}m, 下降=-{d9_loss}m, 海拔: {d9_s}m ➔ {d9_e}m")
