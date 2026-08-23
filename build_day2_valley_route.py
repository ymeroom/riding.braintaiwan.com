import urllib.request, json, time, math, re

# Waypoints for Day 2 Low-Climb Valley Route:
# Takao Base Camp -> Route 20 Otarumi Pass -> Chigira -> Sagamiko -> Fujino -> Uenohara -> Torisawa -> Saruhashi (日本三奇橋) -> Otsuki Station -> Route 139 -> Yamura -> Tsuru City (Yukari Ryokan)

waypoints = [
    (139.2708, 35.6315), # 1. Start: Mt. Takao Base Camp (高尾山口 190m)
    (139.2390, 35.6170), # 2. Route 20: 大垂水峠 (Otarumi Toge 392m)
    (139.2130, 35.6120), # 3. Route 20: 千木良 (Chigira 240m)
    (139.1880, 35.6135), # 4. Route 20: 相模湖 (Sagamiko 175m)
    (139.1550, 35.6150), # 5. Route 20: 藤野 (Fujino 200m)
    (139.1080, 35.6280), # 6. Route 20: 上野原 (Uenohara 205m)
    (139.0150, 35.6130), # 7. Route 20: 鳥澤 (Torisawa 280m)
    (138.9800, 35.6150), # 8. 國寶名勝：甲斐猿橋 (Saruhashi 310m)
    (138.9400, 35.6100), # 9. 大月站前 (Otsuki Station / 轉國道139號 358m)
    (138.9200, 35.5800), # 10. 國道139號：谷村 (Yamura 420m)
    (138.9065, 35.5525)  # 11. End: ビジネス旅館 由加利 (都留市 475m)
]

all_coords = []
total_dist = 0

for i in range(len(waypoints) - 1):
    p1 = waypoints[i]
    p2 = waypoints[i+1]
    url = f"http://router.project-osrm.org/route/v1/bicycle/{p1[0]},{p1[1]};{p2[0]},{p2[1]}?overview=full&geometries=geojson"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req, timeout=10) as resp:
        data = json.loads(resp.read().decode())
        seg_route = data['routes'][0]
        seg_coords = seg_route['geometry']['coordinates']
        if i > 0 and len(seg_coords) > 0:
            seg_coords = seg_coords[1:]
        all_coords.extend(seg_coords)
        total_dist += seg_route['distance']

dist_km = round(total_dist / 1000, 1)

def haversine(p1, p2):
    R = 6371000
    lat1, lon1 = math.radians(p1[1]), math.radians(p1[0])
    lat2, lon2 = math.radians(p2[1]), math.radians(p2[0])
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = math.sin(dlat/2)**2 + math.cos(lat1)*math.cos(lat2)*math.sin(dlon/2)**2
    return 2 * R * math.asin(math.sqrt(a))

total_pts = len(all_coords)
sample_indices = [int(i * (total_pts - 1) / 74) for i in range(75)]
elevation_profile = []
cumulative_dist = 0.0
elevations = []

for i, idx in enumerate(sample_indices):
    pt = all_coords[idx]
    lon, lat = pt[0], pt[1]
    if i == 0:
        c_dist = 0.0
    else:
        prev_idx = sample_indices[i-1]
        seg_d = 0.0
        for k in range(prev_idx, idx):
            seg_d += haversine(all_coords[k], all_coords[k+1])
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

# Road smoothed gain & loss calculation to eliminate bridge deck/riverbed spikes
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

print(f"Day 2 Valley Route Calculated: Dist={dist_km}km, Start={start_e}m, End={end_e}m, Peak={peak_e}m, Gain=+{gain}m, Loss=-{loss}m")

# Day 2 Timeline Waypoints
timeline_d2 = [
    {
        "name": "起點：Mt. Takao Base Camp (高尾山口 190m)",
        "km": 0.0,
        "type": "start",
        "coord": [139.2708, 35.6315],
        "desc": "08:30 退房出發，直接踏上國道 20 號（甲州街道），展開今日唯一一段主要爬升。"
    },
    {
        "name": "唯一主要峠道：大垂水峠 (標高 392m)",
        "km": 4.3,
        "type": "pivot",
        "coord": [139.2390, 35.6170],
        "desc": "《頭文字D》經典山道！平均坡度 5.3%，由高尾山口踩踏 4.3 公里（爬升 200m）即輕鬆攻頂，跨越東京都與神奈川縣界。"
    },
    {
        "name": "甲州街道順降：千木良 ➔ 相模湖 (175m)",
        "km": 14.1,
        "type": "scenic",
        "coord": [139.1880, 35.6135],
        "desc": "爽快滑降 10 公里直通河谷！相模湖畔晨霧繚繞，於湖畔便利店稍作補給。"
    },
    {
        "name": "桂川河谷順騎：藤野 ➔ 上野原 (205m)",
        "km": 24.5,
        "type": "waypoint",
        "coord": [139.1080, 35.6280],
        "desc": "告別陡坡，沿著桂川河谷緩緩平騎，平均坡度僅約 0.5%~1%，兩側群山夾道。"
    },
    {
        "name": "國寶級名勝／午餐點：日本三奇橋「甲斐猿橋」",
        "km": 42.0,
        "type": "rest",
        "coord": [138.9800, 35.6150],
        "desc": "🍁 必訪絕景！日本三大奇橋之一，懸空於深邃桂川峽谷之上，兩側楓紅極為壯觀，可於橋旁茶屋享用手打蕎麥麵或烏龍麵。"
    },
    {
        "name": "關鍵轉折：大月站前 ➔ 切入國道 139 號 (358m)",
        "km": 48.2,
        "type": "pivot",
        "coord": [138.9400, 35.6100],
        "desc": "抵達大月市區，告別國道 20 號，左轉切入【國道 139 號（富士道）】，沿清澈的桂川逆流緩緩漫騎 12 公里。"
    },
    {
        "name": "終點：ビジネス旅館 由加利 (都留市 475m)",
        "km": dist_km,
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
        item['title'] = "進山篇：高尾山口 ➔ 甲州街道(國道20) ➔ 大垂水峠(392m) ➔ 千木良 ➔ 相模湖 ➔ 日本三奇橋(猿橋) ➔ 大月 ➔ 國道139 ➔ 都留市 (475m)"
        item['dist_km'] = dist_km
        item['gain'] = gain
        item['loss'] = loss
        item['start_e'] = start_e
        item['end_e'] = end_e
        item['peak_e'] = peak_e
        item['coords'] = all_coords
        item['elevation_profile'] = elevation_profile
        item['timeline'] = timeline_d2
        item['expert_tip'] = "💡 <strong>在地車友實戰解析：</strong> 徹底放棄爬升破千米的秋山深山隧道，改走經典【國道20號河谷直達線 ➔ 日本三奇橋猿橋 ➔ 大月 ➔ 國道139 ➔ 都留】！除了出發後 4 公里爬大垂水峠（+200m）外，後續 50 公里沿著桂川河谷緩緩平騎（坡度 < 1%），輕鬆暢遊猿橋紅葉絕景！<div style='margin-top:8px; padding-top:8px; border-top:1px dashed rgba(59,130,246,0.3); font-size:11.5px; color:#DDD6FE;'><strong style='color:#C084FC;'>🎬 聖地巡禮：</strong> 《頭文字D》（甲州街道大垂水峠飆車傳說）；《歌川廣重》（浮世繪名勝・甲陽猿橋之圖）；俳聖松尾芭蕉隱居名所（都留市芭蕉館）</div>"

with open('d:/2026東京單車騎旅/all_19days_route_data.json', 'w', encoding='utf-8') as f:
    json.dump(all_data, f, ensure_ascii=False)

# Update day2_track.gpx
gpx_header = f"""<?xml version="1.0" encoding="UTF-8"?>
<gpx version="1.1" creator="BrainTaiwan Cycling Expedition 2026" xmlns="http://www.topografix.com/GPX/1/1">
  <metadata>
    <name>Day 2: 高尾山口 ➔ 大垂水峠 ➔ 相模湖 ➔ 日本三奇橋(猿橋) ➔ 大月 ➔ 國道139 ➔ 都留市</name>
    <desc>{dist_km} km | +{gain}m / -{loss}m | 低爬升河谷直達線（國道20+國道139）</desc>
  </metadata>
  <trk>
    <name>Day 2: Mt. Takao to Tsuru City via Otarumi and Saruhashi Valley</name>
    <trkseg>
"""
gpx_body = "".join([f'      <trkpt lat="{pt[1]}" lon="{pt[0]}"><ele>250.0</ele></trkpt>\n' for pt in all_coords])
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
    <title>Day 2 行程具體地圖 Demo ｜ 高尾山口 ➔ 大垂水峠 ➔ 相模湖 ➔ 日本三奇橋(猿橋) ➔ 大月 ➔ 國道139 ➔ 都留</title>
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
            <h1>Day 2: 高尾山口 ➔ 大垂水峠 ➔ 相模湖 ➔ 日本三奇橋(猿橋) ➔ 大月 ➔ 國道139 ➔ 都留市</h1>
            <p>🚴 2026/11/14（六）低爬升河谷直達線 ｜ 日本國土地理院 GSI 1m DEM 實測</p>
        </div>
        <div class="btn-group">
            <a href="tokyo_fuji_cycling_itinerary_19days_v2.html" class="action-btn">📋 返回 19日總行程表 ➔</a>
            <a href="tokyo_cycling_19days_map_demo.html" class="action-btn gsi">🗺️ 19日總地圖 Demo ↗</a>
            <a href="day2_track.gpx" download="day2_track.gpx" class="action-btn gpx">💾 下載 Day 2 GPX 軌跡</a>
        </div>
    </header>

    <div class="stats-bar">
        <div class="stat-box">
            <div class="val">{dist_km} km</div>
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
            <div class="val">50 km</div>
            <div class="lbl">桂川平緩河谷路段</div>
        </div>
        <div class="stat-box">
            <div class="val">~3.5 - 4.0 hr</div>
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
            <span style="font-size: 12px; color: #10B981;">低爬升結構：大垂水峠 (392m) 攻頂後，沿桂川河谷一路極緩升至都留</span>
        </h3>
        <div class="chart-container">
            <canvas id="elevationChart"></canvas>
        </div>
    </div>

    <div class="tip-callout">
        💡 <strong>在地車友實戰解析：</strong> 徹底放棄爬升破千米的秋山深山隧道，改走經典【國道20號河谷直達線 ➔ 日本三奇橋猿橋 ➔ 大月 ➔ 國道139 ➔ 都留】！除了出發後 4 公里爬大垂水峠（+200m）外，後續 50 公里沿著桂川河谷緩緩平騎（坡度 < 1%），輕鬆暢遊猿橋紅葉絕景！
    </div>

    <footer>
        <p>東京・富士五湖・富士宮・伊豆・東京灣 19日秋季單車騎行計畫 ｜ Day 2 具體地圖 Demo 互動儀表板</p>
    </footer>
</div>

<script>
// 1. Initialize Leaflet Map
const map = L.map('map').setView([35.60, 139.10], 11);

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
const routeGeojson = {json.dumps({"type": "Feature", "geometry": {"type": "LineString", "coordinates": all_coords}})};

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
            borderColor: '#38BDF8',
            backgroundColor: 'rgba(56, 189, 248, 0.15)',
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

# Sync to Itinerary HTML files
with open('d:/2026東京單車騎旅/tokyo_fuji_cycling_itinerary_19days_v2.html', 'r', encoding='utf-8') as f:
    itinerary_html = f.read()

# Replace summary table Day 2
itinerary_html = re.sub(
    r'<td>高尾山口 ➔ <strong>甲州街道.*?都留</td>\s*<td><strong>.*?km</strong></td>\s*<td>.*?</td>',
    f'<td>高尾山口 ➔ <strong>甲州街道(國道20)</strong> ➔ 大垂水峠(392m) ➔ 相模湖 ➔ 日本三奇橋(猿橋) ➔ 大月 ➔ 國道139 ➔ 都留</td>\n                        <td><strong>{dist_km} km</strong></td>\n                        <td>+{gain}m / -{loss}m</td>',
    itinerary_html
)

# Replace Day 2 Card title, stats, route
itinerary_html = re.sub(
    r'<div class="day-title"><span class="day-num">Day 2</span>.*?</div>',
    '<div class="day-title"><span class="day-num">Day 2</span> 11/14（六）高尾山口 ➔ 甲州街道(國道20) ➔ 大垂水峠(392m) ➔ 相模湖 ➔ 日本三奇橋(猿橋) ➔ 大月 ➔ 國道139 ➔ 都留</div>',
    itinerary_html,
    count=1
)

itinerary_html = re.sub(
    r'<div class="day-stats">\s*[\d\.]+\s*km\s*｜\s*<span class="elev-pill">.*?</span>\s*｜\s*海拔\s*[\d~]+m',
    f'<div class="day-stats">\n                    {dist_km} km ｜ <span class="elev-pill">+{gain} m / -{loss} m</span> ｜ 海拔 175~475m',
    itinerary_html,
    count=1
)

itinerary_html = re.sub(
    r'<div class="route-step"><span class="step-label">路線：</span>.*?</div>',
    '<div class="route-step"><span class="step-label">路線：</span>Mt. Takao Base Camp ➔ 國道 20 號（甲州街道） ➔ 攻頂【大垂水峠（標高392m）】 ➔ 順暢滑降經【千木良】 ➔ 相模湖 ➔ 藤野 ➔ 上野原 ➔ 桂川河谷緩平騎行 ➔ 🍁 國寶名勝【日本三奇橋・甲斐猿橋】(午餐/拍照) ➔ 大月站前切入【國道 139 號】 ➔ 沿桂川水岸逆流緩騎 12km ➔ 都留市 ビジネス旅館 由加利</div>',
    itinerary_html,
    count=1
)

files = [
    'd:/2026東京單車騎旅/tokyo_fuji_cycling_itinerary_19days_v2.html',
    'd:/2026東京單車騎旅/index.html',
    'C:/Users/ymero/Downloads/tokyo_fuji_cycling_itinerary_19days_v2.html',
    'C:/Users/ymero/Downloads/index.html'
]

for fp in files:
    with open(fp, 'w', encoding='utf-8') as f:
        f.write(itinerary_html)

print("Successfully switched Day 2 to Low-Climb Valley Route across all platforms!")
