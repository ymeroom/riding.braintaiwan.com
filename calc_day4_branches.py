import urllib.request, urllib.parse, json, sys
sys.stdout.reconfigure(encoding='utf-8')

# Geocoding function
def geocode(address):
    url = f"https://msearch.gsi.go.jp/address-search/AddressSearch?q={urllib.parse.quote(address)}"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req) as resp:
        data = json.loads(resp.read().decode('utf-8'))
        return data[0]['geometry']['coordinates']

# Locations
orange_cabin = [138.7610, 35.5280] # Start (845m)
arakurayama = [138.8020, 35.5010] # 五重塔 (850m)
oshino_hakkai = [138.8320, 35.4600] # 忍野八海 (930m)
yamanakako = [138.8800, 35.4050] # 山中湖旭日丘 (990m)
saiko = [138.6750, 35.5000] # 西湖 (910m)
shojiko = [138.6080, 35.4850] # 精進湖 (900m)

# Destinations
kouan = geocode("山梨県南巨摩郡身延町中之倉2926") # 浩庵
kagelow = geocode("山梨県南都留郡富士河口湖町船津3111-1") # kagelow
fujimi205 = geocode("山梨県富士吉田市大明見6-10-14") # 富士見旅館205

print(f"浩庵座標: {kouan}")
print(f"kagelow座標: {kagelow}")
print(f"富士見旅館205座標: {fujimi205}")

# Function to calculate route & GSI elevation stats
def calculate_route_stats(wps, name):
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
    start_e = round(elevs[0]) if elevs else 0
    end_e = round(elevs[-1]) if elevs else 0
    max_e = round(max(elevs)) if elevs else 0
    min_e = round(min(elevs)) if elevs else 0

    return {
        "name": name,
        "dist_km": dist_km,
        "gain": round(gain),
        "loss": round(loss),
        "start_e": start_e,
        "end_e": end_e,
        "max_e": max_e,
        "min_e": min_e
    }

# 1. 情境 A：Day 3 已完山中湖 ➔ Day 4 走五重塔往西騎 ➔ 宿本棲湖浩庵
# Orange Cabin -> Arakurayama -> Kawaguchiko North Shore (Oishi) -> Saiko -> Shojiko -> Kouan
wps_A = [
    orange_cabin,
    arakurayama,
    [138.7450, 35.5230], # Oishi Park
    saiko,
    shojiko,
    kouan
]
res_A = calculate_route_stats(wps_A, "情境 A：走五重塔 ➔ 西進本棲湖浩庵")

# 2. 情境 B：Day 3 沒騎山中湖 ➔ Day 4 騎山中湖
# Orange Cabin -> Oshino Hakkai -> Yamanakako loop
# Option B1: -> kagelow (河口湖船津)
wps_B1 = [
    orange_cabin,
    oshino_hakkai,
    yamanakako,
    [138.8400, 35.4200], # Yamanakako west
    kagelow
]
res_B1 = calculate_route_stats(wps_B1, "選項 B1：山中湖 ➔ 宿 kagelow (河口湖船津)")

# Option B2: -> 富士見旅館205 (富士吉田大明見)
wps_B2 = [
    orange_cabin,
    oshino_hakkai,
    yamanakako,
    fujimi205
]
res_B2 = calculate_route_stats(wps_B2, "選項 B2：山中湖 ➔ 宿 富士見旅館205 (富士吉田)")

# Option B3: -> 本棲湖浩庵 (經山中湖後，長征至本棲湖浩庵)
wps_B3 = [
    orange_cabin,
    oshino_hakkai,
    yamanakako,
    [138.7600, 35.5000], # Kawaguchiko
    saiko,
    shojiko,
    kouan
]
res_B3 = calculate_route_stats(wps_B3, "選項 B3：山中湖 ➔ 長征至本棲湖浩庵")

print("\n=======================================================")
print("【情境 A：Day 3 已騎山中湖 ➔ Day 4 走五重塔往西至本棲湖浩庵】")
print(f"路線: Orange Cabin ➔ 新倉山五重塔 ➔ 西湖 ➔ 精進湖 ➔ 本棲湖浩庵")
print(f"總里程: {res_A['dist_km']} km ｜ 爬升: +{res_A['gain']} m ｜ 下降: -{res_A['loss']} m ｜ 海拔: {res_A['start_e']}m ➔ {res_A['end_e']}m (最高 {res_A['max_e']}m)")

print("\n=======================================================")
print("【情境 B：Day 3 沒騎山中湖 ➔ Day 4 騎山中湖後的三種住宿選項】")
print(f"\n1. 選項 B1 ➔ 宿 kagelow 河口湖卡吉羅旅舍 (船津3111-1):")
print(f"   總里程: {res_B1['dist_km']} km ｜ 爬升: +{res_B1['gain']} m ｜ 下降: -{res_B1['loss']} m ｜ 海拔: {res_B1['start_e']}m ➔ {res_B1['end_e']}m")

print(f"\n2. 選項 B2 ➔ 宿 富士見旅館205 (富士吉田大明見6-10-14):")
print(f"   總里程: {res_B2['dist_km']} km ｜ 爬升: +{res_B2['gain']} m ｜ 下降: -{res_B2['loss']} m ｜ 海拔: {res_B2['start_e']}m ➔ {res_B2['end_e']}m")

print(f"\n3. 選項 B3 ➔ 宿 本栖湖畔 民宿 浩庵 (身延町中之倉2926):")
print(f"   總里程: {res_B3['dist_km']} km ｜ 爬升: +{res_B3['gain']} m ｜ 下降: -{res_B3['loss']} m ｜ 海拔: {res_B3['start_e']}m ➔ {res_B3['end_e']}m")
