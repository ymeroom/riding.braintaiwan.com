import urllib.request, json, sys
sys.stdout.reconfigure(encoding='utf-8')

# Exact coordinates
tsuru_yukari = [138.90582, 35.55057] # 484m
orange_cabin = [138.7610, 35.5280] # Near Kubota Itchiku / Momiji corridor (~845m)
arakurayama = [138.8020, 35.5010] # Arakurayama Pagoda (~850m)
oshino_hakkai = [138.8320, 35.4600] # ~930m
yamanakako_asahigaoka = [138.8800, 35.4050] # ~990m
oishi_park = [138.7450, 35.5230] # ~835m
saiko_iyashi = [138.6750, 35.5000] # ~910m
shojiko = [138.6080, 35.4850] # ~900m
motosuko_koan = [138.5770, 35.4720] # ~905m
fujinomiya = [138.6150, 35.2220] # ~120m

# Day 3: Tsuru (Yukari) -> Pref 713 rural road -> Arakurayama Pagoda -> Fujiyoshida -> Kawaguchiko North Shore (Orange Cabin)
d3_wps = [tsuru_yukari, [138.8600, 35.5200], arakurayama, [138.7680, 35.5150], orange_cabin]

# Day 4: Light ride: Orange Cabin -> Oshino Hakkai -> Yamanakako loop -> return Orange Cabin
d4_wps = [orange_cabin, [138.7750, 35.4950], oshino_hakkai, yamanakako_asahigaoka, [138.8400, 35.4200], oshino_hakkai, orange_cabin]

# Day 5: Orange Cabin -> Kohoku View Line -> Oishi Park -> Saiko -> Shojiko -> Motosuko Koan -> Asagiri -> Fujinomiya
d5_wps = [orange_cabin, oishi_park, saiko_iyashi, shojiko, motosuko_koan, [138.5700, 35.4000], [138.5850, 35.3100], fujinomiya]

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

d3_dist, d3_gain, d3_loss, d3_s, d3_m, d3_e = calc(d3_wps)
d4_dist, d4_gain, d4_loss, d4_s, d4_m, d4_e = calc(d4_wps)
d5_dist, d5_gain, d5_loss, d5_s, d5_m, d5_e = calc(d5_wps)

print("=== 住宿連住規劃：Orange Cabin Inn far from station (河口湖北岸紅葉迴廊旁) ===")
print(f"Day 3 (都留 由加利 ➔ 新倉山五重塔 ➔ 河口湖 Orange Cabin): {d3_dist} km ｜ 爬升 +{d3_gain}m / -{d3_loss}m ｜ 起點 {d3_s}m ➔ 終點 {d3_e}m")
print(f"Day 4 (輕裝探索：清晨紅葉迴廊 ➔ 忍野八海 ➔ 山中湖 ➔ 返回 Orange Cabin): {d4_dist} km ｜ 爬升 +{d4_gain}m / -{d4_loss}m ｜ 輕裝免背行李")
print(f"Day 5 (Orange Cabin 出發 ➔ 湖北 View Line ➔ 西湖 ➔ 精進湖 ➔ 本棲湖逆富士 ➔ 朝霧 ➔ 富士宮): {d5_dist} km ｜ 爬升 +{d5_gain}m / -{d5_loss}m ｜ 海拔 {d5_s}m ➔ {d5_e}m")
