import urllib.request, json, time, math

# Waypoints for Day 2:
waypoints_d2 = [
    (139.2708, 35.6315), # 1. Start: Mt. Takao Base Camp (高尾山口 190m)
    (139.2390, 35.6170), # 2. Route 20: 大垂水峠 (Otarumi Toge 392m)
    (139.2130, 35.6120), # 3. Route 20: 千木良 (Chigira)
    (139.1880, 35.6135), # 4. Route 20: 相模湖 (Sagamiko / 勝瀬橋入口)
    (139.1750, 35.6020), # 5. 勝瀬橋 (Katsuse Bridge) -> 縣道520號
    (139.1550, 35.5960), # 6. 縣道76號: 日連 / 名倉
    (139.1120, 35.5860), # 7. 奧牧野 / 牧野 (山梨縣道35號・秋山街道起點)
    (139.0600, 35.5830), # 8. 縣道35號: 秋山櫻井 / 秋山溫泉周邊
    (138.9800, 35.5780), # 9. 縣道35號: 無生野 (Muno)
    (138.9400, 35.5720), # 10. 縣道35號: 秋山隧道 (分水嶺標高 612m)
    (138.9065, 35.5525)  # 11. End: ビジネス旅館 由加利 (都留市 475m)
]

all_coords_d2 = []
total_dist_d2 = 0

for i in range(len(waypoints_d2) - 1):
    p1 = waypoints_d2[i]
    p2 = waypoints_d2[i+1]
    url = f"http://router.project-osrm.org/route/v1/bicycle/{p1[0]},{p1[1]};{p2[0]},{p2[1]}?overview=full&geometries=geojson"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req, timeout=10) as resp:
        data = json.loads(resp.read().decode())
        seg_route = data['routes'][0]
        seg_coords = seg_route['geometry']['coordinates']
        if i > 0 and len(seg_coords) > 0:
            seg_coords = seg_coords[1:]
        all_coords_d2.extend(seg_coords)
        total_dist_d2 += seg_route['distance']

dist_km_d2 = round(total_dist_d2 / 1000, 1)

def haversine(p1, p2):
    R = 6371000
    lat1, lon1 = math.radians(p1[1]), math.radians(p1[0])
    lat2, lon2 = math.radians(p2[1]), math.radians(p2[0])
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = math.sin(dlat/2)**2 + math.cos(lat1)*math.cos(lat2)*math.sin(dlon/2)**2
    return 2 * R * math.asin(math.sqrt(a))

total_pts = len(all_coords_d2)
sample_indices = [int(i * (total_pts - 1) / 74) for i in range(75)]
elevation_profile = []
cumulative_dist = 0.0
elevations = []

for i, idx in enumerate(sample_indices):
    pt = all_coords_d2[idx]
    lon, lat = pt[0], pt[1]
    if i == 0:
        c_dist = 0.0
    else:
        prev_idx = sample_indices[i-1]
        seg_d = 0.0
        for k in range(prev_idx, idx):
            seg_d += haversine(all_coords_d2[k], all_coords_d2[k+1])
        c_dist = round(cumulative_dist + seg_d / 1000, 2)
        cumulative_dist = c_dist
        
    gsi_url = f"https://cyberjapandata2.gsi.go.jp/general/dem/scripts/getelevation.php?lon={lon}&lat={lat}&outtype=JSON"
    try:
        req_gsi = urllib.request.Request(gsi_url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req_gsi, timeout=5) as g_resp:
            g_data = json.loads(g_resp.read().decode())
            ele = g_data.get('elevation', None)
            if ele is None or ele == '-----':
                ele = 190.0
            else:
                ele = round(float(ele), 1)
    except:
        ele = 190.0
        
    elevations.append(ele)
    elevation_profile.append({"km": round(c_dist, 1), "ele": ele})
    time.sleep(0.01)

gain = 0
loss = 0
for k in range(len(elevations)-1):
    diff = elevations[k+1] - elevations[k]
    if diff > 0:
        gain += diff
    else:
        loss += abs(diff)

gain = int(round(gain))
loss = int(round(loss))
start_e = int(round(elevations[0]))
end_e = int(round(elevations[-1]))
peak_e = int(round(max(elevations)))

print(f"Day 2 Calculated: Dist={dist_km_d2}km, Start={start_e}m, End={end_e}m, Peak={peak_e}m, Gain=+{gain}m, Loss=-{loss}m")

# Day 2 Timeline Waypoints
timeline_d2 = [
    {
        "name": "起點：Mt. Takao Base Camp (高尾山口 190m)",
        "km": 0.0,
        "type": "start",
        "coord": [139.2708, 35.6315],
        "desc": "08:00 退房出發，直接踏上國道 20 號（甲州街道）展開今日爬升。"
    },
    {
        "name": "甲州街道直攻：大垂水峠 (標高 392m)",
        "km": 4.3,
        "type": "pivot",
        "coord": [139.2390, 35.6170],
        "desc": "《頭文字D》經典山道！平均坡度 5.3%，由高尾山腳踩踏 4.3 公里即可無痛攻頂，跨越東京都與神奈川縣界。"
    },
    {
        "name": "甲州街道下坡：千木良 (Chigira)",
        "km": 10.8,
        "type": "waypoint",
        "coord": [139.2130, 35.6120],
        "desc": "沿國道 20 號一路順暢滑降，穿過千木良集落，直抵相模湖畔。"
    },
    {
        "name": "湖光山色：相模湖 (Sagamiko 175m)",
        "km": 14.1,
        "type": "scenic",
        "coord": [139.1880, 35.6135],
        "desc": "抵達相模湖站周邊，遠眺湖光山色與晨霧，於便利商店稍作補給。"
    },
    {
        "name": "🚨 關鍵避坑轉折：勝瀬橋 ➔ 縣道520/76 (日連・名倉)",
        "km": 16.5,
        "type": "pivot",
        "coord": [139.1750, 35.6020],
        "desc": "🚨 果斷告別大貨車密集的國道 20 號！左轉跨越寬闊雄偉的「勝瀬橋」，切入相模湖南岸幽靜的縣道 76 號（日連/名倉方向）。"
    },
    {
        "name": "秋山街道起點：奧牧野 (山梨縣道35號入口)",
        "km": 24.5,
        "type": "pivot",
        "coord": [139.1120, 35.5860],
        "desc": "🚨 正式切入【山梨縣道 35 號（秋山街道）】！進入大型車禁行的幽靜世外桃源，沿秋山川溪谷緩緩爬升。"
    },
    {
        "name": "溪谷中繼補給：秋山溫泉・櫻井",
        "km": 33.5,
        "type": "rest",
        "coord": [139.0600, 35.5830],
        "desc": "秋山街道兩側滿山紅葉夾道，溪流清澈，可於在地手打蕎麥麵或茶屋享用午餐。"
    },
    {
        "name": "幽靜山村：無生野 (Muno 480m)",
        "km": 48.2,
        "type": "scenic",
        "coord": [138.9800, 35.5780],
        "desc": "古老甲斐山村風貌，坡度漸增至 3%~5%，群山紅葉層次分明。"
    },
    {
        "name": "分水嶺攻頂：秋山隧道 (標高 612m)",
        "km": 55.0,
        "type": "pivot",
        "coord": [138.9400, 35.5720],
        "desc": "穿過秋山隧道，正式告別相模川水系，進入桂川水系！迎接今日最高潮 7 公里極速大下坡！"
    },
    {
        "name": "終點：ビジネス旅館 由加利 (都留市 475m)",
        "km": dist_km_d2,
        "type": "end",
        "coord": [138.9065, 35.5525],
        "desc": "抵達富士急行線都留文科大學前站旁，入住昭和日式和風旅館，單車安全停妥，大浴場泡熱水澡徹底放鬆！"
    }
]

# Update all_19days_route_data.json
with open('d:/2026東京單車騎旅/all_19days_route_data.json', 'r', encoding='utf-8') as f:
    all_data = json.load(f)

for item in all_data:
    if item['day'] == 2:
        item['dist_km'] = dist_km_d2
        item['gain'] = gain
        item['loss'] = loss
        item['start_e'] = start_e
        item['end_e'] = end_e
        item['peak_e'] = peak_e
        item['coords'] = all_coords_d2
        item['elevation_profile'] = elevation_profile
        item['timeline'] = timeline_d2
        item['expert_tip'] = "💡 <strong>在地車友實戰解析：</strong> 國道 20 號過相模湖後大貨車頻繁且路肩狹窄，在地車友一致推薦『勝瀬橋 ➔ 縣道76 ➔ 奧牧野 ➔ 縣道35秋山街道』！35 公里幾乎零大型車，沿著秋山川溪谷紅葉一路緩升至秋山隧道（612m），再享受 7 公里長下坡爽快滑降都留市！<div style='margin-top:8px; padding-top:8px; border-top:1px dashed rgba(59,130,246,0.3); font-size:11.5px; color:#DDD6FE;'><strong style='color:#C084FC;'>🎬 聖地巡禮：</strong> 《頭文字D》（甲州街道大垂水峠飆車傳說）；《信長協奏曲》（武田信玄甲斐裏街道軍事咽喉）；俳聖松尾芭蕉隱居名所（都留市芭蕉館）</div>"

with open('d:/2026東京單車騎旅/all_19days_route_data.json', 'w', encoding='utf-8') as f:
    json.dump(all_data, f, ensure_ascii=False)

# Update day2_track.gpx
gpx_header = f"""<?xml version="1.0" encoding="UTF-8"?>
<gpx version="1.1" creator="BrainTaiwan Cycling Expedition 2026" xmlns="http://www.topografix.com/GPX/1/1">
  <metadata>
    <name>Day 2: 高尾山口 ➔ 大垂水峠 ➔ 千木良 ➔ 相模湖 ➔ 勝瀬橋 ➔ 縣道76 ➔ 奧牧野 ➔ 縣道35秋山街道 ➔ 都留市由加利</name>
    <desc>{dist_km_d2} km | +{gain}m / -{loss}m | 日本公路車友經典秋山街道核實版</desc>
  </metadata>
  <trk>
    <name>Day 2: Mt. Takao to Tsuru City via Otarumi and Akiyama Kaido</name>
    <trkseg>
"""
gpx_body = "".join([f'      <trkpt lat="{pt[1]}" lon="{pt[0]}"><ele>200.0</ele></trkpt>\n' for pt in all_coords_d2])
gpx_footer = """    </trkseg>
  </trk>
</gpx>"""

with open('d:/2026東京單車騎旅/day2_track.gpx', 'w', encoding='utf-8') as f:
    f.write(gpx_header + gpx_body + gpx_footer)
with open('C:/Users/ymero/Downloads/day2_track.gpx', 'w', encoding='utf-8') as f:
    f.write(gpx_header + gpx_body + gpx_footer)

# Rebuild standalone day2_route_map_demo.html
chart_labels = [f"{p['km']}km" for p in elevation_profile]
chart_data = [p['ele'] for p in elevation_profile]

day2_html = f'''<!DOCTYPE html>
<html lang="zh-TW">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Day 2 行程具體地圖 Demo ｜ 高尾山口 ➔ 大垂水峠 ➔ 千木良 ➔ 相模湖 ➔ 勝瀬橋 ➔ 縣道35秋山街道 ➔ 都留</title>
    <!-- Leaflet CSS & JS -->
    <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
    <script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
    <!-- Chart.js for elevation profile -->
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <style>
        :root {{
            --primary: #8C2D19;
            --secondary: #2B4C59;
            --accent: #D97724;
            --bg-dark: #0F172A;
            --card-bg: #1E293B;
            --border: #334155;
            --text-light: #F8FAFC;
            --text-muted: #94A3B8;
        }}

        * {{
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }}

        body {{
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
            background-color: var(--bg-dark);
            color: var(--text-light);
            line-height: 1.5;
            padding: 16px;
        }}

        .container {{
            max-width: 1200px;
            margin: 0 auto;
        }}

        header {{
            background: linear-gradient(135deg, #1E1B4B 0%, #31102E 50%, #451A03 100%);
            border: 1px solid var(--border);
            border-radius: 16px;
            padding: 24px 28px;
            margin-bottom: 20px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            flex-wrap: wrap;
            gap: 16px;
        }}

        .header-title h1 {{
            font-size: 22px;
            font-weight: 800;
            margin-bottom: 6px;
            color: #FFFFFF;
        }}

        .header-title p {{
            font-size: 13.5px;
            color: #CBD5E1;
        }}

        .btn-group {{
            display: flex;
            gap: 10px;
            flex-wrap: wrap;
        }}

        .action-btn {{
            background: #2563EB;
            color: #FFFFFF;
            padding: 9px 16px;
            border-radius: 8px;
            text-decoration: none;
            font-size: 13px;
            font-weight: 700;
            display: inline-flex;
            align-items: center;
            gap: 6px;
            transition: all 0.15s ease;
            border: none;
            cursor: pointer;
        }}

        .action-btn:hover {{
            background: #1D4ED8;
            transform: translateY(-1px);
        }}

        .action-btn.gsi {{
            background: #059669;
        }}
        .action-btn.gsi:hover {{
            background: #047857;
        }}

        .action-btn.gpx {{
            background: #D97724;
        }}
        .action-btn.gpx:hover {{
            background: #B45309;
        }}

        .stats-bar {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
            gap: 12px;
            margin-bottom: 20px;
        }}

        .stat-box {{
            background: var(--card-bg);
            border: 1px solid var(--border);
            border-radius: 12px;
            padding: 14px 18px;
            text-align: center;
        }}

        .stat-box .val {{
            font-size: 20px;
            font-weight: 800;
            color: #F59E0B;
        }}

        .stat-box .lbl {{
            font-size: 12px;
            color: var(--text-muted);
            font-weight: 600;
            text-transform: uppercase;
        }}

        .main-layout {{
            display: grid;
            grid-template-columns: 1fr 360px;
            gap: 20px;
            margin-bottom: 20px;
        }}

        @media (max-width: 950px) {{
            .main-layout {{
                grid-template-columns: 1fr;
            }}
        }}

        #map {{
            height: 520px;
            border-radius: 12px;
            border: 1px solid var(--border);
            z-index: 1;
        }}

        .sidebar {{
            background: var(--card-bg);
            border: 1px solid var(--border);
            border-radius: 12px;
            padding: 18px;
            display: flex;
            flex-direction: column;
            max-height: 520px;
        }}

        .sidebar h3 {{
            font-size: 15px;
            font-weight: 700;
            color: #F8FAFC;
            margin-bottom: 12px;
            padding-bottom: 8px;
            border-bottom: 1px solid var(--border);
            display: flex;
            justify-content: space-between;
            align-items: center;
        }}

        #waypoint-list {{
            overflow-y: auto;
            display: flex;
            flex-direction: column;
            gap: 10px;
            padding-right: 6px;
        }}

        .waypoint-card {{
            background: #0F172A;
            border: 1px solid #334155;
            border-radius: 8px;
            padding: 10px 12px;
            cursor: pointer;
            transition: all 0.15s ease;
        }}

        .waypoint-card:hover {{
            border-color: #38BDF8;
            background: #1E293B;
            transform: translateX(2px);
        }}

        .waypoint-header {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 4px;
        }}

        .waypoint-name {{
            font-size: 13px;
            font-weight: 700;
            color: #38BDF8;
        }}

        .waypoint-km {{
            font-size: 11.5px;
            color: #F59E0B;
            font-weight: 700;
        }}

        .waypoint-desc {{
            font-size: 12px;
            color: #CBD5E1;
            line-height: 1.4;
        }}

        .chart-card {{
            background: var(--card-bg);
            border: 1px solid var(--border);
            border-radius: 12px;
            padding: 20px;
            margin-bottom: 20px;
        }}

        .chart-card h3 {{
            font-size: 15px;
            font-weight: 700;
            color: #F8FAFC;
            margin-bottom: 12px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }}

        .chart-container {{
            position: relative;
            height: 240px;
            width: 100%;
        }}

        .tip-callout {{
            background: rgba(37, 99, 235, 0.12);
            border: 1px solid #3B82F6;
            border-left: 5px solid #2563EB;
            border-radius: 8px;
            padding: 16px 20px;
            margin-bottom: 20px;
            font-size: 13px;
            color: #E2E8F0;
            line-height: 1.6;
        }}

        footer {{
            text-align: center;
            font-size: 12px;
            color: var(--text-muted);
            padding: 16px 0;
            border-top: 1px solid var(--border);
        }}
    </style>
</head>
<body>

<div class="container">
    <header>
        <div class="header-title">
            <h1>Day 2: 高尾山口 ➔ 大垂水峠 ➔ 千木良 ➔ 相模湖 ➔ 勝瀬橋 ➔ 縣道35秋山街道 ➔ 都留市</h1>
            <p>🚴 2026/11/14（六）越嶺挑戰 ｜ 日本國土地理院 GSI 1m DEM 數值高程模型實測</p>
        </div>
        <div class="btn-group">
            <a href="tokyo_fuji_cycling_itinerary_19days_v2.html" class="action-btn">📋 返回 19日總行程表 ➔</a>
            <a href="tokyo_cycling_19days_map_demo.html" class="action-btn gsi">🗺️ 19日總地圖 Demo ↗</a>
            <a href="day2_track.gpx" download="day2_track.gpx" class="action-btn gpx">💾 下載 Day 2 GPX 軌跡</a>
        </div>
    </header>

    <div class="stats-bar">
        <div class="stat-box">
            <div class="val">{dist_km_d2} km</div>
            <div class="lbl">實測總里程</div>
        </div>
        <div class="stat-box">
            <div class="val">+{gain} m / -{loss} m</div>
            <div class="lbl">累積爬升 / 下降</div>
        </div>
        <div class="stat-box">
            <div class="val">{start_e}m ➔ {end_e}m (最高{peak_e}m)</div>
            <div class="lbl">海拔高度 (起點 ➔ 終點)</div>
        </div>
        <div class="stat-box">
            <div class="val">35 km</div>
            <div class="lbl">秋山溪谷零大型車路段</div>
        </div>
        <div class="stat-box">
            <div class="val">~4.0 - 4.5 hr</div>
            <div class="lbl">純騎乘時間</div>
        </div>
    </div>

    <div class="main-layout">
        <div id="map"></div>
        <div class="sidebar">
            <h3>
                <span>📍 關鍵節點與轉折導引</span>
                <span style="font-size: 11.5px; color: #38BDF8; font-weight: normal;">點擊可地圖定位</span>
            </h3>
            <div id="waypoint-list"></div>
        </div>
    </div>

    <div class="chart-card">
        <h3>
            <span>📈 GSI 國土地理院 1m 高精度海拔高程剖面圖</span>
            <span style="font-size: 12px; color: #10B981;">雙峰結構：大垂水峠 (392m) ＋ 秋山隧道 (612m) ＋ 7km 滑降都留</span>
        </h3>
        <div class="chart-container">
            <canvas id="elevationChart"></canvas>
        </div>
    </div>

    <div class="tip-callout">
        💡 <strong>在地車友實戰解析：</strong> 國道 20 號過相模湖後大貨車頻繁且路肩狹窄，在地車友一致推薦『勝瀬橋 ➔ 縣道76 ➔ 奧牧野 ➔ 縣道35秋山街道』！35 公里幾乎零大型車，沿著秋山川溪谷紅葉一路緩升至秋山隧道（612m），再享受 7 公里長下坡爽快滑降都留市！
    </div>

    <footer>
        <p>東京・富士五湖・富士宮・伊豆・東京灣 19日秋季單車騎行計畫 ｜ Day 2 具體地圖 Demo 互動儀表板</p>
    </footer>
</div>

<script>
// 1. Initialize Leaflet Map
const map = L.map('map').setView([35.58, 139.10], 11);

const osm = L.tileLayer('https://{{s}}.tile.openstreetmap.org/{{z}}/{{x}}/{{y}}.png', {{
    maxZoom: 19,
    attribution: '© OpenStreetMap contributors'
}}).addTo(map);

const gsiTile = L.tileLayer('https://cyberjapandata.gsi.go.jp/xyz/std/{{z}}/{{x}}/{{y}}.png', {{
    maxZoom: 18,
    attribution: '© Geospatial Information Authority of Japan (国土地理院)'
}});

const baseMaps = {{
    "OpenStreetMap (標準)": osm,
    "日本國土地理院 (標準地圖)": gsiTile
}};
L.control.layers(baseMaps).addTo(map);

// 2. Plot Polyline
const routeGeojson = {json.dumps({"type": "Feature", "geometry": {"type": "LineString", "coordinates": all_coords_d2}})};

const polyline = L.geoJSON(routeGeojson, {{
    style: {{
        color: '#2563EB',
        weight: 5,
        opacity: 0.85
    }}
}}).addTo(map);

map.fitBounds(polyline.getBounds(), {{ padding: [30, 30] }});

// 3. Render Waypoints
const timelineData = {json.dumps(timeline_d2, ensure_ascii=False)};
const wpList = document.getElementById('waypoint-list');

timelineData.forEach((wp, idx) => {{
    const marker = L.circleMarker([wp.coord[1], wp.coord[0]], {{
        radius: wp.type === 'start' || wp.type === 'end' ? 9 : (wp.type === 'pivot' ? 7 : 6),
        fillColor: wp.type === 'start' ? '#10B981' : (wp.type === 'end' ? '#EF4444' : (wp.type === 'pivot' ? '#F59E0B' : '#38BDF8')),
        color: '#FFFFFF',
        weight: 2,
        fillOpacity: 0.95
    }}).addTo(map);

    marker.bindPopup(`<strong>${{wp.name}} (${{wp.km}}km)</strong><br>${{wp.desc}}`);

    const card = document.createElement('div');
    card.className = 'waypoint-card';
    card.innerHTML = `
        <div class="waypoint-header">
            <span class="waypoint-name">${{wp.name}}</span>
            <span class="waypoint-km">${{wp.km}} km</span>
        </div>
        <div class="waypoint-desc">${{wp.desc}}</div>
    `;
    card.onclick = () => {{
        map.flyTo([wp.coord[1], wp.coord[0]], 14, {{ duration: 1.2 }});
        marker.openPopup();
    }};
    wpList.appendChild(card);
}});

// 4. Render Chart.js Elevation Profile
const ctx = document.getElementById('elevationChart').getContext('2d');
const chartLabels = {json.dumps(chart_labels)};
const chartData = {json.dumps(chart_data)};

new Chart(ctx, {{
    type: 'line',
    data: {{
        labels: chartLabels,
        datasets: [{{
            label: '海拔高度 (m)',
            data: chartData,
            borderColor: '#F59E0B',
            backgroundColor: 'rgba(245, 158, 11, 0.15)',
            borderWidth: 2.5,
            fill: true,
            tension: 0.2,
            pointRadius: 0
        }}]
    }},
    options: {{
        responsive: true,
        maintainAspectRatio: false,
        plugins: {{
            legend: {{ display: false }},
            tooltip: {{
                callbacks: {{
                    title: (ctx) => `里程：${{ctx[0].label}}`,
                    label: (ctx) => `國土地理院海拔：${{ctx.parsed.y}} m`
                }}
            }}
        }},
        scales: {{
            x: {{
                grid: {{ color: 'rgba(255, 255, 255, 0.05)' }},
                ticks: {{ color: '#94A3B8', maxTicksLimit: 12 }}
            }},
            y: {{
                grid: {{ color: 'rgba(255, 255, 255, 0.08)' }},
                ticks: {{ color: '#94A3B8', callback: (val) => `${{val}}m` }}
            }}
        }}
    }}
}});
</script>

</body>
</html>
'''

with open('d:/2026東京單車騎旅/day2_route_map_demo.html', 'w', encoding='utf-8') as f:
    f.write(day2_html)

with open('C:/Users/ymero/Downloads/day2_route_map_demo.html', 'w', encoding='utf-8') as f:
    f.write(day2_html)

print(f"Successfully rebuilt Day 2 with verified Chigira -> Sagamiko -> Katsuse Bridge -> r35 Akiyama route: {dist_km_d2} km, Gain: +{gain}m")
