import urllib.request, json, sys
sys.stdout.reconfigure(encoding='utf-8')

hana_an = [139.86586, 35.76727] # 花庵旅舍 (金町)
odaiba = [139.7900, 35.6300] # 台場
kasai = [139.8600, 35.6450] # 葛西臨海公園
shibamata = [139.8780, 35.7570] # 柴又帝釋天
mizumoto = [139.8700, 35.7870] # 水元公園
asakusa = [139.7980, 35.7130] # 淺草雷門

# Day 15: Odaiba -> Kasai Rinkai Park -> Arakawa/Edogawa -> Shibamata -> Hana An (Kanamachi)
wps_d15 = [odaiba, kasai, shibamata, hana_an]

# Day 17: Hana An (Kanamachi) -> Mizumoto Park Metasequoia forest -> Shibamata -> Asakusa
wps_d17 = [hana_an, mizumoto, shibamata, asakusa]

def calc_route(wps, name):
    coord_str = ';'.join([f'{c[0]},{c[1]}' for c in wps])
    url = f'http://router.project-osrm.org/route/v1/bicycle/{coord_str}?overview=full&geometries=geojson'
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req) as resp:
        data = json.loads(resp.read().decode('utf-8'))
        r = data['routes'][0]
        dist_km = round(r['distance'] / 1000.0, 1)
        coords = r['geometry']['coordinates']

    sampled = coords[::max(1, len(coords)//30)]
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

d15_dist, d15_gain, d15_loss, d15_s, d15_m, d15_e = calc_route(wps_d15, "Day 15")
d17_dist, d17_gain, d17_loss, d17_s, d17_m, d17_e = calc_route(wps_d17, "Day 17")

print(f"Day 15 (台場 ➔ 葛西 ➔ 柴又 ➔ 花庵旅舍 金町): {d15_dist} km ｜ 爬升 +{d15_gain}m / -{d15_loss}m ｜ 海拔 {d15_s}m ➔ {d15_e}m")
print(f"Day 17 (花庵旅舍 ➔ 水元公園水杉林 ➔ 柴又 ➔ 淺草): {d17_dist} km ｜ 爬升 +{d17_gain}m / -{d17_loss}m ｜ 海拔 {d17_s}m ➔ {d17_e}m")
