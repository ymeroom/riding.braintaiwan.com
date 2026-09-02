import sys, json, time, urllib.request
sys.stdout.reconfigure(encoding='utf-8')

days_waypoints = [
    {
        "day": 1,
        "title": "秋葉原 ➔ 銀座/品川 ➔ 國道15號 ➔ 六鄉橋 ➔ 多摩川自行車道 ➔ 府中/調布",
        "pts": [(139.7745, 35.6975), (139.7580, 35.6660), (139.7385, 35.6285), (139.7118, 35.5397), (139.6270, 35.6115), (139.5350, 35.6420), (139.4770, 35.6690)]
    },
    {
        "day": 2,
        "title": "府中 ➔ 淺川自行車道 ➔ 高尾 ➔ 津久井湖畔 (縣道515/517) ➔ 山梨縣道35號 (秋山街道) ➔ 都留",
        "pts": [(139.4770, 35.6690), (139.4150, 35.6560), (139.2820, 35.6425), (139.2800, 35.5890), (139.1850, 35.5870), (139.0850, 35.5680), (138.9050, 35.5530)]
    },
    {
        "day": 3,
        "title": "都留 ➔ 富士急行沿線裏道 ➔ 縣道713號 ➔ 富士吉田 (金鳥居) ➔ 山中湖",
        "pts": [(138.9050, 35.5530), (138.8650, 35.5180), (138.8030, 35.4910), (138.8050, 35.4780), (138.8780, 35.4090), (138.9020, 35.4240)]
    },
    {
        "day": 4,
        "title": "山中湖環湖 ➔ 忍野八海 ➔ 湖北View Line ➔ 河口湖 (紅葉迴廊/大石公園)",
        "pts": [(138.9020, 35.4240), (138.8710, 35.4260), (138.8320, 35.4600), (138.7690, 35.4980), (138.7660, 35.5250), (138.7460, 35.5230)]
    },
    {
        "day": 5,
        "title": "河口湖 ➔ 湖北View Line ➔ 西湖 ➔ 精進湖 ➔ 本棲湖 ➔ 折返河口湖",
        "pts": [(138.7460, 35.5230), (138.6650, 35.5030), (138.6070, 35.4880), (138.5770, 35.4740), (138.6850, 35.4950), (138.7500, 35.5100)]
    },
    {
        "day": 6,
        "title": "河口湖／富士吉田 彈性休整與深度賞楓 (新倉山/本町通/南岸)",
        "pts": [(138.7500, 35.5100), (138.8030, 35.4910), (138.8050, 35.5010), (138.7650, 35.5050), (138.7500, 35.5100)]
    },
    {
        "day": 7,
        "title": "河口湖 ➔ 朝霧高原 ➔ 富士宮 ➔ 田子の浦港 ➔ 駿河灣千本松原海堤 ➔ 沼津港 ➔ 三島",
        "pts": [(138.7500, 35.5100), (138.6950, 35.4750), (138.6000, 35.4050), (138.5870, 35.3130), (138.6110, 35.2260), (138.6950, 35.1430), (138.8350, 35.0930), (138.8580, 35.0820), (138.9110, 35.1270)]
    },
    {
        "day": 8,
        "title": "三島 ➔ 狩野川自行車專用道 ➔ 伊豆Gateway函南 ➔ 修善寺溫泉",
        "pts": [(138.9110, 35.1270), (138.9380, 35.0350), (138.9410, 34.9980), (138.9290, 34.9720)]
    },
    {
        "day": 9,
        "title": "修善寺 ➔ 縣道12號 ➔ 冷川峠 ➔ 伊豆高原 ➔ 城崎海岸",
        "pts": [(138.9290, 34.9720), (138.9880, 34.9780), (139.0430, 34.9770), (139.1000, 34.9200), (139.1350, 34.8900)]
    },
    {
        "day": 10,
        "title": "伊豆高原 ➔ 伊東溫泉 ➔ 宇佐美 ➔ 網代港舊道 ➔ 南熱海長濱 ➔ 熱海溫泉",
        "pts": [(139.1350, 34.8900), (139.0980, 34.9700), (139.0820, 35.0040), (139.0850, 35.0420), (139.0750, 35.0600), (139.0740, 35.0970)]
    },
    {
        "day": 11,
        "title": "熱海 ➔ 湯河原 ➔ 真鶴 ➔ 縣道740號柑橘山線 ➔ 早川漁港 ➔ 小田原城",
        "pts": [(139.0740, 35.0970), (139.1150, 35.1430), (139.1330, 35.1570), (139.1360, 35.2010), (139.1480, 35.2390), (139.1530, 35.2500)]
    },
    {
        "day": 12,
        "title": "小田原 ➔ 國道1號 ➔ 湘南海岸防風林道/國道134共用道 ➔ 茅崎 ➔ 江之島",
        "pts": [(139.1530, 35.2500), (139.2150, 35.2800), (139.3170, 35.3120), (139.4000, 35.3160), (139.4820, 35.3080)]
    },
    {
        "day": 13,
        "title": "江之島 ➔ 鎌倉高校前 ➔ 鶴岡八幡宮 ➔ 北鎌倉 ➔ 大船 ➔ 柏尾川步道 ➔ 戶塚 ➔ 橫濱港未來",
        "pts": [(139.4820, 35.3080), (139.5020, 35.3065), (139.5560, 35.3260), (139.5310, 35.3530), (139.5350, 35.4000), (139.5950, 35.4450), (139.6320, 35.4550)]
    },
    {
        "day": 14,
        "title": "橫濱 ➔ 鶴見 ➔ 羽田大鳥居 ➔ 築地/勝鬨 ➔ 豐洲大橋 ➔ 台場海濱公園",
        "pts": [(139.6320, 35.4550), (139.6800, 35.5100), (139.7460, 35.5480), (139.7680, 35.6600), (139.7820, 35.6480), (139.7750, 35.6290)]
    },
    {
        "day": 15,
        "title": "台場 ➔ 葛西臨海公園 ➔ 清砂大橋 ➔ 荒川右岸自行車專用道 ➔ 赤羽",
        "pts": [(139.7750, 35.6290), (139.8600, 35.6420), (139.8450, 35.6670), (139.8430, 35.7050), (139.8150, 35.7500), (139.7280, 35.7860)]
    },
    {
        "day": 16,
        "title": "赤羽 ➔ 荒川右岸 ➔ 入間川自行車道 ➔ 川越小江戶老街 ➔ 折返荒川中游",
        "pts": [(139.7280, 35.7860), (139.6050, 35.8450), (139.5600, 35.9100), (139.4830, 35.9230), (139.5600, 35.9100), (139.6800, 35.8000)]
    },
    {
        "day": 17,
        "title": "荒川中游 ➔ 葛飾水元公園 (水杉金黃林) ➔ 柴又帝釋天 ➔ 隅田川 ➔ 上野/淺草",
        "pts": [(139.6800, 35.8000), (139.8700, 35.7880), (139.8780, 35.7580), (139.7960, 35.7140), (139.7740, 35.7140)]
    },
    {
        "day": 18,
        "title": "上野 ➔ 東大銀杏 ➔ 明治神宮外苑銀杏大道 ➔ 皇居 ➔ 秋葉原",
        "pts": [(139.7740, 35.7140), (139.7620, 35.7120), (139.7180, 35.6730), (139.7550, 35.6810), (139.7745, 35.6975)]
    },
    {
        "day": 19,
        "title": "秋葉原市區巡禮 ➔ 還車 ➔ 京成 Skyliner 至成田機場",
        "pts": [(139.7745, 35.6975), (139.7680, 35.7000), (139.7745, 35.6975)]
    }
]

def get_elevation(lon, lat):
    try:
        url = f"https://cyberjapandata2.gsi.go.jp/general/dem/scripts/getelevation.php?lon={lon:.5f}&lat={lat:.5f}&outtype=JSON"
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=5) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            elev = data.get('elevation')
            if elev is not None and elev != '-----':
                return float(elev)
    except Exception as e:
        pass
    return None

def get_osrm_route(pts):
    coords_str = ";".join([f"{lon:.5f},{lat:.5f}" for lon, lat in pts])
    url = f"https://routing.openstreetmap.de/routed-bike/route/v1/driving/{coords_str}?overview=full&geometries=geojson"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req, timeout=10) as resp:
        data = json.loads(resp.read().decode('utf-8'))
        route = data['routes'][0]
        dist_km = route['distance'] / 1000.0
        coords = route['geometry']['coordinates']
        return dist_km, coords

print("Calculating exact distance and elevation profiles...")
results = []

for item in days_waypoints:
    day_num = item['day']
    title = item['title']
    pts = item['pts']
    
    try:
        dist_km, coords = get_osrm_route(pts)
    except Exception as e:
        print(f"Day {day_num} routing fallback: {e}")
        # fallback simple estimation
        dist_km = 40.0
        coords = pts
        
    # sample coordinates for elevation (every ~200-500m or at least 30-50 points)
    step = max(1, len(coords) // 30)
    sample_coords = coords[::step]
    if coords[-1] != sample_coords[-1]:
        sample_coords.append(coords[-1])
        
    elevations = []
    for lon, lat in sample_coords:
        elev = get_elevation(lon, lat)
        if elev is not None:
            elevations.append(elev)
        time.sleep(0.04) # be polite to GSI API
        
    # Calculate elevation gain / loss with threshold filter to prevent noise
    ascent = 0.0
    descent = 0.0
    if len(elevations) >= 2:
        for i in range(1, len(elevations)):
            diff = elevations[i] - elevations[i-1]
            if abs(diff) >= 2.0: # 2m threshold
                if diff > 0:
                    ascent += diff
                else:
                    descent += abs(diff)
        min_elev = min(elevations)
        max_elev = max(elevations)
        start_elev = elevations[0]
        end_elev = elevations[-1]
    else:
        min_elev, max_elev, start_elev, end_elev = 0, 0, 0, 0
        
    results.append({
        "day": day_num,
        "title": title,
        "dist_km": round(dist_km, 1),
        "ascent_m": round(ascent),
        "descent_m": round(descent),
        "min_elev": round(min_elev),
        "max_elev": round(max_elev),
        "start_elev": round(start_elev),
        "end_elev": round(end_elev)
    })
    print(f"Day {day_num:2d}: {dist_km:5.1f} km | 爬升: +{round(ascent):4d} m | 下降: -{round(descent):4d} m | 海拔: {round(min_elev):4d}m ~ {round(max_elev):4d}m | {title[:30]}...")

with open("d:/2026東京單車騎旅/route_stats.json", "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=2)

print("\nFinished! Results saved to route_stats.json")
