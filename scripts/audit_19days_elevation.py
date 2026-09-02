import urllib.request, urllib.parse, json, sys, time
sys.stdout.reconfigure(encoding='utf-8')

# Geocoding function via GSI
def geocode_gsi(address):
    url = f"https://msearch.gsi.go.jp/address-search/AddressSearch?q={urllib.parse.quote(address)}"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req, timeout=5) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            if data:
                return data[0]['geometry']['coordinates']
    except Exception as e:
        print(f"Geocoding error for {address}: {e}")
    return None

# GSI Elevation fetcher
def get_gsi_elevation(lon, lat):
    url = f"https://cyberjapandata2.gsi.go.jp/general/dem/scripts/getelevation.php?lon={lon}&lat={lat}&outtype=JSON"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req, timeout=4) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            return float(data.get('elevation', 0))
    except:
        return 0.0

# Precise Route Calculation using OSRM + GSI DEM
def calculate_day_metrics(wps, day_num, name):
    coord_str = ';'.join([f'{c[0]},{c[1]}' for c in wps])
    url = f'http://router.project-osrm.org/route/v1/bicycle/{coord_str}?overview=full&geometries=geojson'
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req, timeout=10) as resp:
        data = json.loads(resp.read().decode('utf-8'))
        r = data['routes'][0]
        dist_km = round(r['distance'] / 1000.0, 1)
        coords = r['geometry']['coordinates']

    # Sample coordinates along the route for GSI elevation
    sample_rate = max(1, len(coords) // 45)
    sampled = coords[::sample_rate]
    if coords[-1] not in sampled:
        sampled.append(coords[-1])

    elevs = []
    for pt in sampled:
        e = get_gsi_elevation(pt[0], pt[1])
        elevs.append(e)
        time.sleep(0.02) # Gentle rate limit for GSI

    # Filter minor noise threshold (> 3m)
    gain = sum([max(0, elevs[i]-elevs[i-1]) for i in range(1, len(elevs)) if abs(elevs[i]-elevs[i-1]) >= 3.5])
    loss = sum([max(0, elevs[i-1]-elevs[i]) for i in range(1, len(elevs)) if abs(elevs[i-1]-elevs[i]) >= 3.5])
    start_e = round(elevs[0]) if elevs else 0
    peak_e = round(max(elevs)) if elevs else 0
    end_e = round(elevs[-1]) if elevs else 0

    return {
        "day": day_num,
        "name": name,
        "dist_km": dist_km,
        "gain": round(gain),
        "loss": round(loss),
        "start_e": start_e,
        "peak_e": peak_e,
        "end_e": end_e
    }

# Key Waypoints for all 19 days
cycletrip_base = [139.7785, 35.6985] # Akihabara (5m)
rokugo_bridge = [139.7120, 35.5390] # Rokugo (3m)
tamagawa_fuchu = [139.4850, 35.6600] # Fuchu (40m)
asakawa_junction = [139.4000, 35.6550] # Asakawa junction (75m)
takao_basecamp = [139.2708, 35.6315] # Mt. Takao Base Camp (190m)

otarumi_pass = [139.2450, 35.6150] # Otarumi Pass (392m)
sagamiko = [139.1900, 35.6130] # Sagami Lake (205m)
akiyama_highway = [139.0600, 35.5800] # Pref 35 Akiyama (350m)
tsuru_yukari = [138.90582, 35.55057] # Yukari Ryokan (484m)

oshino_hakkai = [138.8320, 35.4600] # Oshino (930m)
yamanakako = [138.8800, 35.4050] # Yamanakako Asahigaoka (990m)
arakurayama = [138.8020, 35.5010] # Arakurayama Pagoda (850m)
orange_cabin = [138.7610, 35.5280] # Orange Cabin Inn (845m)

oishi_park = [138.7450, 35.5230] # Oishi Park (835m)
saiko_iyashi = [138.6750, 35.5000] # Saiko Iyashi no Sato (910m)
shojiko = [138.6080, 35.4850] # Shojiko (900m)
motosuko_kouan = [138.564758, 35.473095] # Motosuko Kouan (905m)

asagiri_plateau = [138.5750, 35.4000] # Asagiri (830m)
shiraito_falls = [138.5880, 35.3120] # Shiraito (450m)
fujinomiya_center = [138.6150, 35.2220] # Fujinomiya (115m)

tagonoura_port = [138.6950, 35.1420] # Tagonoura (2m)
senbonmatsubara = [138.8000, 35.1050] # Senbonmatsubara (3m)
numazu_port = [138.8580, 35.0830] # Numazu (3m)
mishima_center = [138.9150, 35.1220] # Mishima (25m)

shuzenji_mizuguchi = [138.92598, 34.97020] # Onsen Yado Mizuguchi (99m)
hiekawa_pass = [139.0200, 34.9600] # Hiekawa Pass (380m)
ippeki_lake = [139.1000, 34.9200] # Ippeki Lake (170m)
jogasaki_coast = [139.1300, 34.8900] # Jogasaki Coast (25m)
kawana_seaview = [139.12343, 34.96987] # kawana seaview standard (36m)

usami_beach = [139.0800, 35.0080] # Usami (5m)
ajiro_old_street = [139.0880, 35.0420] # Ajiro (5m)
apt_minami_atami = [139.08211, 35.04507] # Apt南熱海 (下多賀440, 4m)
izu_kansya = [139.06842, 35.05392] # Izu Kansya (下多賀1473-11, 9m)
atami_baien = [139.0550, 35.0980] # Atami Plum Garden (85m)
atami_sun_beach = [139.0750, 35.0970] # Atami Sun Beach (3m)

pref740_mikan = [139.1450, 35.1550] # Pref 740 Mikan Highway (150m)
odawara_castle = [139.1550, 35.2500] # Odawara Castle (15m)
shonan_cr = [139.3100, 35.3200] # Shonan Coastal Path (5m)
enoshima_island = [139.4820, 35.3080] # Enoshima (5m)

kamakura_hase = [139.5350, 35.3120] # Kamakura Hasedera (15m)
kashio_river_cr = [139.5300, 35.3800] # Kashio River (12m)
yokohama_minatomirai = [139.6350, 35.4550] # Minato Mirai (4m)

toyosu_bridge = [139.7820, 35.6500] # Toyosu Bridge (8m)
odaiba_marine_park = [139.7750, 35.6300] # Odaiba (4m)

kasai_rinkai_park = [139.8600, 35.6450] # Kasai (3m)
shibamata_taishakuten = [139.8780, 35.7570] # Shibamata (2m)
hostel_hana_an = [139.86586, 35.76727] # Hostel Hana An Kanamachi (1m)

mizumoto_park = [139.8700, 35.7870] # Mizumoto Park (1m)
kawagoe_kitain = [139.4850, 35.9180] # Kawagoe Kitain (18m)
asakusa_kaminarimon = [139.7980, 35.7130] # Asakusa Kaminarimon (3m)

todai_hongo = [139.7620, 35.7120] # Todai Hongo (22m)
imperial_palace = [139.7550, 35.6850] # Imperial Palace (12m)
jingu_gaien = [139.7180, 35.6740] # Meiji Jingu Gaien (32m)
kanda_myojin = [139.7680, 35.7020] # Kanda Myojin (15m)

days_wps = [
    (1, "Day 1: 秋葉原 ➔ 多摩川CR ➔ 淺川CR ➔ 高尾山口", [cycletrip_base, rokugo_bridge, tamagawa_fuchu, asakawa_junction, takao_basecamp]),
    (2, "Day 2: 高尾山口 ➔ 大垂水峠 ➔ 相模湖 ➔ 縣道35秋山街道 ➔ 都留", [takao_basecamp, otarumi_pass, sagamiko, akiyama_highway, tsuru_yukari]),
    (3, "Day 3 (好天氣): 都留 ➔ 忍野八海 ➔ 山中湖 ➔ 新倉山 ➔ 河口湖", [tsuru_yukari, [138.8600, 35.5200], oshino_hakkai, yamanakako, arakurayama, orange_cabin]),
    (4, "Day 4: 河口湖 ➔ 湖北View Line ➔ 西湖 ➔ 精進湖 ➔ 本棲湖浩庵", [orange_cabin, oishi_park, saiko_iyashi, shojiko, motosuko_kouan]),
    (5, "Day 5: 富士五湖核心緩衝日 (精進湖/樹海/鳴澤/溫泉休整)", [motosuko_kouan, shojiko, [138.6900, 35.4800], motosuko_kouan]),
    (6, "Day 6: 本棲湖浩庵 ➔ 朝霧高原 ➔ 白糸之瀑 ➔ 富士宮", [motosuko_kouan, asagiri_plateau, shiraito_falls, fujinomiya_center]),
    (7, "Day 7: 富士宮 ➔ 潤井川CR ➔ 田子の浦 ➔ 駿河灣千本松原海堤 ➔ 沼津 ➔ 三島", [fujinomiya_center, tagonoura_port, senbonmatsubara, numazu_port, mishima_center]),
    (8, "Day 8: 三島 ➔ 狩野川自行車道 ➔ 修善寺溫泉水口", [mishima_center, [138.9350, 35.0300], shuzenji_mizuguchi]),
    (9, "Day 9: 修善寺 ➔ 冷川峠 ➔ 一碧湖 ➔ 城崎海岸 ➔ 伊東川奈", [shuzenji_mizuguchi, hiekawa_pass, ippeki_lake, jogasaki_coast, kawana_seaview]),
    (10, "Day 10: 伊東川奈 ➔ 宇佐美 ➔ 網代舊街 ➔ Apt南熱海 (下多賀440)", [kawana_seaview, usami_beach, ajiro_old_street, apt_minami_atami]),
    (11, "Day 11: 南熱海換宿 ➔ 熱海梅園紅葉 ➔ 晚上海上煙火 ➔ Izu Kansya", [apt_minami_atami, izu_kansya, atami_baien, atami_sun_beach, izu_kansya]),
    (12, "Day 12: 南熱海 ➔ 縣道740柑橘道 ➔ 小田原城 ➔ 湘南海岸 ➔ 江之島", [izu_kansya, atami_sun_beach, pref740_mikan, odawara_castle, shonan_cr, enoshima_island]),
    (13, "Day 13: 江之島 ➔ 鎌倉長谷寺 ➔ 柏尾川水岸綠道 ➔ 橫濱港未來", [enoshima_island, kamakura_hase, kashio_river_cr, yokohama_minatomirai]),
    (14, "Day 14: 橫濱 ➔ 第一京濱/羽田 ➔ 豐洲大橋 ➔ 台場海濱公園", [yokohama_minatomirai, [139.7350, 35.5450], toyosu_bridge, odaiba_marine_park]),
    (15, "Day 15: 台場 ➔ 葛西臨海公園 ➔ 中川水岸 ➔ 柴又 ➔ 金町花庵旅舍", [odaiba_marine_park, kasai_rinkai_park, shibamata_taishakuten, hostel_hana_an]),
    (16, "Day 16: 金町出發 ➔ 江戶川CR / 荒川 ➔ 小江戶川越 / 葛飾老街 ➔ 返回金町", [hostel_hana_an, [139.8800, 35.8400], kawagoe_kitain, [139.8000, 35.8000], hostel_hana_an]),
    (17, "Day 17: 金町花庵 ➔ 水元公園水杉林 ➔ 柴又 ➔ 淺草雷門", [hostel_hana_an, mizumoto_park, shibamata_taishakuten, asakusa_kaminarimon]),
    (18, "Day 18: 淺草 ➔ 東大本鄉銀杏 ➔ 皇居 ➔ 神宮外苑銀杏大道 ➔ 秋葉原", [asakusa_kaminarimon, todai_hongo, imperial_palace, jingu_gaien, cycletrip_base]),
    (19, "Day 19: 秋葉原市區 ➔ 神田明神 ➔ CycleTrip還車 ➔ 日暮里搭車", [cycletrip_base, kanda_myojin, cycletrip_base, [139.7710, 35.7280]])
]

print("=== 開始執行全 19 天 OSRM 單車路網 ＋ 日本國土地理院 (GSI DEM 1m) 標高大核實 ===\n")
results = []
for day_num, name, wps in days_wps:
    res = calculate_day_metrics(wps, day_num, name)
    results.append(res)
    print(f"Day {res['day']:02d}: 里程 = {res['dist_km']:>5.1f} km ｜ 爬升 = +{res['gain']:>4d} m / 下降 = -{res['loss']:>4d} m ｜ 海拔 = {res['start_e']:>4d}m ➔ {res['end_e']:>4d}m (最高 {res['peak_e']:>4d}m) ｜ {name}")

# Total summary
total_dist = sum([r['dist_km'] for r in results])
total_gain = sum([r['gain'] for r in results])
print("\n" + "="*80)
print(f"19 天全程總里程核實：{total_dist:.1f} km ｜ 全程累積爬升總核實：+{total_gain} m")
print("="*80)

# Save result as json for update
with open("d:/2026東京單車騎旅/audit_results_19days.json", "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=2)
print("Audit results saved to d:/2026東京單車騎旅/audit_results_19days.json")
