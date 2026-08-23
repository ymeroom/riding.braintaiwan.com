import urllib.request, json, sys
sys.stdout.reconfigure(encoding='utf-8')

# Coordinates
akihabara = [139.7714, 35.6998] # Alt: ~3m
takao_basecamp = [139.2705, 35.6323] # Mt. Takao Base Camp (Takaosanguchi, Alt: ~205m)
fuchu_station = [139.4795, 35.6675] # Fuchu (Alt: ~54m)
tsuru = [138.9056, 35.5539] # Tsuru (Alt: ~508m)

# Day 1 Option A: via Rokugo Bridge + Tamagawa CR + Asakawa CR
d1_optA = [
    akihabara,
    [139.7088, 35.5412], # Rokugo Bridge
    [139.6268, 35.6115], # Futako-Tamagawa
    [139.4850, 35.6600], # Fuchu Tamagawa
    [139.4350, 35.6580], # Asakawa CR entry (Hino)
    [139.3300, 35.6550], # Asakawa CR (Hachioji)
    takao_basecamp
]

# Day 1 Option B: via Futako-Tamagawa direct entry (Akihabara -> Roppongi -> Futako-Tamagawa -> Tamagawa CR -> Asakawa CR -> Takao)
d1_optB = [
    akihabara,
    [139.7300, 35.6600], # Roppongi / Meguro
    [139.6268, 35.6115], # Futako-Tamagawa entry
    [139.4850, 35.6600], # Fuchu Tamagawa
    [139.4350, 35.6580], # Asakawa CR entry
    [139.3300, 35.6550], # Asakawa CR
    takao_basecamp
]

# Day 1 Option C: via Inokashira / Kanda River / Koshu Kaido to Asakawa CR (Shortest direct)
d1_optC = [
    akihabara,
    [139.7000, 35.6900], # Shinjuku
    [139.6000, 35.6800], # Suginami
    [139.4350, 35.6580], # Asakawa CR entry (Hino)
    [139.3300, 35.6550], # Asakawa CR
    takao_basecamp
]

# Day 2 Current (from Fuchu): Fuchu -> Asakawa -> Takao -> Tsukui Lake (515/517) -> Rt 35 Akiyama -> Tsuru
d2_current = [
    fuchu_station,
    [139.4350, 35.6580],
    [139.3300, 35.6550],
    [139.2800, 35.6350], # Takao
    [139.2550, 35.5880], # Tsukui Lake (515/517)
    [139.1450, 35.5800], # Akiyama entry
    tsuru
]

# Day 2 New (from Mt. Takao Base Camp): Takao Base Camp -> Machida Kaido -> Tsukui Lake (515/517) -> Rt 35 Akiyama -> Tsuru
d2_new = [
    takao_basecamp,
    [139.2780, 35.6150], # Machida Kaido / Otarumi bypass
    [139.2550, 35.5880], # Tsukui Lake (515/517)
    [139.1450, 35.5800], # Akiyama entry
    tsuru
]

def query_osrm_and_gsi(coords_list, name=""):
    coord_str = ';'.join([f'{c[0]},{c[1]}' for c in coords_list])
    url = f'http://router.project-osrm.org/route/v1/bicycle/{coord_str}?overview=full&geometries=geojson'
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req) as resp:
        data = json.loads(resp.read().decode('utf-8'))
        r = data['routes'][0]
        dist_km = round(r['distance'] / 1000.0, 1)
        coords = r['geometry']['coordinates']
        
    # Sample GSI elevation
    elevs = []
    step = max(1, len(coords) // 30)
    for pt in coords[::step]:
        lon, lat = pt[0], pt[1]
        try:
            gsi_url = f"https://cyberjapandata2.gsi.go.jp/general/dem/scripts/getelevation.php?lon={lon}&lat={lat}&outtype=JSON"
            req_gsi = urllib.request.Request(gsi_url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req_gsi, timeout=3) as g_resp:
                g_data = json.loads(g_resp.read().decode('utf-8'))
                e = float(g_data.get('elevation', 0))
                elevs.append(e)
        except:
            pass
            
    ascent = 0
    descent = 0
    for i in range(1, len(elevs)):
        diff = elevs[i] - elevs[i-1]
        if diff > 0:
            ascent += diff
        else:
            descent += abs(diff)
            
    ascent = round(ascent)
    descent = round(descent)
    min_e = round(min(elevs)) if elevs else 0
    max_e = round(max(elevs)) if elevs else 0
    start_e = round(elevs[0]) if elevs else 0
    end_e = round(elevs[-1]) if elevs else 0
    
    return {
        "name": name,
        "dist_km": dist_km,
        "ascent": ascent,
        "descent": descent,
        "min_e": min_e,
        "max_e": max_e,
        "start_e": start_e,
        "end_e": end_e
    }

print("=== 1. 當前原方案 (Day 1 宿府中 ➔ Day 2 騎至都留) ===")
res_d1_curr = query_osrm_and_gsi([akihabara, [139.7088, 35.5412], [139.6268, 35.6115], fuchu_station], "原 Day 1 (秋葉原 ➔ 府中)")
res_d2_curr = query_osrm_and_gsi(d2_current, "原 Day 2 (府中 ➔ 高尾 ➔ 都留)")
print(f"原 Day 1: {res_d1_curr['dist_km']} km ｜ 爬升 +{res_d1_curr['ascent']}m / -{res_d1_curr['descent']}m ｜ 海拔 {res_d1_curr['start_e']}m ➔ {res_d1_curr['end_e']}m")
print(f"原 Day 2: {res_d2_curr['dist_km']} km ｜ 爬升 +{res_d2_curr['ascent']}m / -{res_d2_curr['descent']}m ｜ 海拔 {res_d2_curr['start_e']}m ➔ {res_d2_curr['end_e']}m (最高 {res_d2_curr['max_e']}m)")

print("\n=== 2. 新方案 (Day 1 宿 Mt. Takao Base Camp ➔ Day 2 騎至都留) ===")
# Let's test the best bike path route for Day 1 (via Tamagawa & Asakawa CR)
res_d1_new_optA = query_osrm_and_gsi(d1_optA, "新 Day 1 (水岸全封閉方案：六鄉橋 ➔ 多摩川CR ➔ 淺川CR ➔ 高尾)")
res_d1_new_optB = query_osrm_and_gsi(d1_optB, "新 Day 1 (黃金折衷方案：二子玉川 ➔ 多摩川CR ➔ 淺川CR ➔ 高尾)")
res_d1_new_optC = query_osrm_and_gsi(d1_optC, "新 Day 1 (市區直達方案：都心 ➔ 井之頭/甲州 ➔ 淺川CR ➔ 高尾)")

res_d2_new = query_osrm_and_gsi(d2_new, "新 Day 2 (高尾 Base Camp ➔ 津久井湖 ➔ 縣道35 ➔ 都留)")

print(f"新 Day 1 方案 A (水岸無車流): {res_d1_new_optA['dist_km']} km ｜ 爬升 +{res_d1_new_optA['ascent']}m / -{res_d1_new_optA['descent']}m ｜ 海拔 {res_d1_new_optA['start_e']}m ➔ {res_d1_new_optA['end_e']}m")
print(f"新 Day 1 方案 B (市區切入CR): {res_d1_new_optB['dist_km']} km ｜ 爬升 +{res_d1_new_optB['ascent']}m / -{res_d1_new_optB['descent']}m ｜ 海拔 {res_d1_new_optB['start_e']}m ➔ {res_d1_new_optB['end_e']}m")
print(f"新 Day 1 方案 C (市區最短線): {res_d1_new_optC['dist_km']} km ｜ 爬升 +{res_d1_new_optC['ascent']}m / -{res_d1_new_optC['descent']}m ｜ 海拔 {res_d1_new_optC['start_e']}m ➔ {res_d1_new_optC['end_e']}m")
print(f"新 Day 2 (高尾出發): {res_d2_new['dist_km']} km ｜ 爬升 +{res_d2_new['ascent']}m / -{res_d2_new['descent']}m ｜ 海拔 {res_d2_new['start_e']}m ➔ {res_d2_new['end_e']}m (最高 {res_d2_new['max_e']}m)")
