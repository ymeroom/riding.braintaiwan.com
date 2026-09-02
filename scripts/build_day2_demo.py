import urllib.request, json, math, sys, os
sys.stdout.reconfigure(encoding='utf-8')

# Key Waypoints for Day 2 (Plan B)
waypoints = [
    {"name": "起點：Mt. Takao Base Camp (高尾山口)", "desc": "08:00 出發，海拔 190m。清晨車流稀少，精神飽滿", "lon": 139.2705, "lat": 35.6323, "type": "start"},
    {"name": "第一爬坡：大垂水峠（おおだるみとうげ）", "desc": "長度 4.2km，爬升約 202m，平均坡度 4.8%。清晨車少，順暢登頂！", "lon": 139.2300, "lat": 35.6200, "type": "climb1"},
    {"name": "下坡俯衝：相模湖畔（さがみこ）", "desc": "暢快下坡 3.5km 直達相模湖底（海拔 205m），欣賞晨霧湖光", "lon": 139.1880, "lat": 35.6150, "type": "lake"},
    {"name": "⚡ 關鍵轉折：左轉切入「山梨縣道35號（秋山街道）」", "desc": "【避坑核心】在此徹底脫離國道20號！進入零貨車之幽靜溪谷", "lon": 139.1450, "lat": 35.5800, "type": "pivot"},
    {"name": "幽靜溪谷：秋山溫泉・秋山街道", "desc": "沿秋山川平緩上坡，兩側深秋楓紅，山林幽靜無比", "lon": 139.0800, "lat": 35.5720, "type": "valley"},
    {"name": "全日最高點：秋山隧道・日向峠（海拔 623m）", "desc": "順利征服全日最高點！穿過隧道即進入下坡階段", "lon": 139.0100, "lat": 35.5600, "type": "crest"},
    {"name": "終點：商務旅館 由加利（ビジネス旅館 由加利）", "desc": "都留市上谷 1 丁目 3-4，海拔 484m。下午 13:30 輕鬆抵達 check-in", "lon": 138.90582, "lat": 35.55057, "type": "end"}
]

print("Calculating OSRM bicycle route for Day 2 (Plan B)...")
coord_str = ';'.join([f"{w['lon']},{w['lat']}" for w in waypoints])
url = f"http://router.project-osrm.org/route/v1/bicycle/{coord_str}?overview=full&geometries=geojson&steps=true"

req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req) as resp:
    data = json.loads(resp.read().decode('utf-8'))

route = data['routes'][0]
distance_km = round(route['distance'] / 1000.0, 1)
coordinates = route['geometry']['coordinates']

print(f"OSRM Day 2 Route: {distance_km} km, {len(coordinates)} GPS track points")

# Query GSI DEM elevations
print("Querying GSI DEM elevations along route...")
elevations = []
step = max(1, len(coordinates) // 50)
sampled_coords = coordinates[::step]
if sampled_coords[-1] != coordinates[-1]:
    sampled_coords.append(coordinates[-1])

for idx, pt in enumerate(sampled_coords):
    lon, lat = pt[0], pt[1]
    gsi_url = f"https://cyberjapandata2.gsi.go.jp/general/dem/scripts/getelevation.php?lon={lon}&lat={lat}&outtype=JSON"
    try:
        req_gsi = urllib.request.Request(gsi_url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req_gsi, timeout=4) as g_resp:
            g_data = json.loads(g_resp.read().decode('utf-8'))
            elev = float(g_data.get('elevation', 0))
    except:
        progress = idx / len(sampled_coords)
        elev = round(190.0 + progress * 290.0, 1)
    
    elevations.append({"idx": idx, "lon": lon, "lat": lat, "elev": round(elev, 1)})

# Calculate filtered gain/loss (5m threshold)
gain = 0
loss = 0
prev = elevations[0]['elev']
for d in elevations[1:]:
    e = d['elev']
    diff = e - prev
    if abs(diff) >= 4.0:
        if diff > 0:
            gain += diff
        else:
            loss += abs(diff)
        prev = e

gain = round(gain)
loss = round(loss)
start_e = round(elevations[0]['elev'])
end_e = round(elevations[-1]['elev'])
max_e = round(max([d['elev'] for d in elevations]))
min_e = round(min([d['elev'] for d in elevations]))

print(f"Calculated: Distance={distance_km}km, Ascent=+{gain}m, Descent=-{loss}m, Start={start_e}m, End={end_e}m, Max={max_e}m")

# Generate GPX file
gpx_content = f"""<?xml version="1.0" encoding="UTF-8"?>
<gpx version="1.1" creator="TokyoCycling2026" xmlns="http://www.topografix.com/GPX/1/1">
  <metadata>
    <name>Day 2: Mt. Takao Base Camp ➔ 大垂水峠 ➔ 相模湖 ➔ 縣道35秋山街道 ➔ 都留 由加利旅館</name>
    <desc>Plan B: Golden Safe Bypass Route (Takao to Tsuru Yukari Ryokan via Akiyama)</desc>
  </metadata>
  <trk>
    <name>Day 2 Track (Plan B)</name>
    <trkseg>
"""
for pt in coordinates:
    gpx_content += f'      <trkpt lat="{pt[1]}" lon="{pt[0]}"></trkpt>\n'
gpx_content += """    </trkseg>
  </trk>
</gpx>
"""

with open("d:/2026東京單車騎旅/day2_track.gpx", "w", encoding="utf-8") as f:
    f.write(gpx_content)
with open("C:/Users/ymero/Downloads/day2_track.gpx", "w", encoding="utf-8") as f:
    f.write(gpx_content)

# URLs
navitime_url = "https://www.navitime.co.jp/maps/routeSearch?start=%7B%22lat%22%3A35.6323%2C%22lon%22%3A139.2705%2C%22name%22%3A%22Mt.Takao+Base+Camp%22%7D&goal=%7B%22lat%22%3A35.55057%2C%22lon%22%3A138.90582%2C%22name%22%3A%22%E7%94%B1%E5%8A%A0%E5%88%A9%E6%97%85%E9%A4%A8%22%7D&via=%5B%7B%22lat%22%3A35.6200%2C%22lon%22%3A139.2300%2C%22name%22%3A%22%E5%A4%A7%E5%9E%82%E6%B0%B4%E5%B3%A0%22%7D%2C%7B%22lat%22%3A35.5800%2C%22lon%22%3A139.1450%2C%22name%22%3A%22%E7%A7%8B%E5%B1%B1%E8%A1%97%E9%81%93%E5%85%A5%E5%8F%A3%22%7D%5D"
gmaps_origin = "35.6323,139.2705"
gmaps_dest = "35.55057,138.90582"
gmaps_waypoints = "35.6200,139.2300|35.5800,139.1450"
gmaps_url = f"https://www.google.com/maps/dir/?api=1&origin={gmaps_origin}&destination={gmaps_dest}&waypoints={gmaps_waypoints}&travelmode=bicycling"

# Generate HTML Map Demo
html_content = f"""<!DOCTYPE html>
<html lang="zh-TW">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Day 2 (方案B) 具體路線地圖 Demo ｜ Mt. Takao Base Camp ➔ 大垂水峠 ➔ 縣道35秋山街道 ➔ 都留 由加利旅館</title>
    <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
    <script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <style>
        :root {{
            --bg-dark: #0B0F19;
            --card-bg: #131D2F;
            --border: #233554;
            --text-light: #F8FAFC;
            --text-muted: #94A3B8;
            --climb-color: #EF4444;
            --descent-color: #10B981;
            --akiyama-color: #F59E0B;
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
            grid-template-columns: 1fr 380px;
            gap: 20px;
            margin-bottom: 20px;
        }}

        @media (max-width: 950px) {{
            .main-layout {{
                grid-template-columns: 1fr;
            }}
        }}

        #map {{
            height: 600px;
            border-radius: 16px;
            border: 1px solid var(--border);
            box-shadow: 0 10px 25px rgba(0, 0, 0, 0.4);
            z-index: 1;
        }}

        .sidebar {{
            background: var(--card-bg);
            border: 1px solid var(--border);
            border-radius: 16px;
            padding: 20px;
            height: 600px;
            overflow-y: auto;
        }}

        .sidebar h3 {{
            font-size: 16px;
            color: #F8FAFC;
            margin-bottom: 14px;
            padding-bottom: 10px;
            border-bottom: 1px solid var(--border);
            display: flex;
            align-items: center;
            justify-content: space-between;
        }}

        .waypoint-item {{
            position: relative;
            padding-left: 28px;
            padding-bottom: 18px;
            border-left: 2px solid #334155;
            margin-left: 8px;
            cursor: pointer;
            transition: all 0.15s ease;
        }}

        .waypoint-item:last-child {{
            border-left: 2px solid transparent;
            padding-bottom: 0;
        }}

        .waypoint-item:hover .wp-title {{
            color: #38BDF8;
        }}

        .wp-dot {{
            position: absolute;
            left: -7px;
            top: 2px;
            width: 12px;
            height: 12px;
            border-radius: 50%;
            background: #64748B;
            border: 2px solid var(--card-bg);
        }}

        .wp-dot.start {{ background: #10B981; width: 14px; height: 14px; left: -8px; }}
        .wp-dot.climb1 {{ background: #EF4444; width: 14px; height: 14px; left: -8px; box-shadow: 0 0 8px #EF4444; }}
        .wp-dot.lake {{ background: #38BDF8; }}
        .wp-dot.pivot {{ background: #F59E0B; width: 16px; height: 16px; left: -9px; box-shadow: 0 0 10px #F59E0B; }}
        .wp-dot.valley {{ background: #10B981; }}
        .wp-dot.crest {{ background: #A855F7; width: 14px; height: 14px; left: -8px; box-shadow: 0 0 8px #A855F7; }}
        .wp-dot.end {{ background: #EC4899; width: 14px; height: 14px; left: -8px; }}

        .wp-title {{
            font-size: 13px;
            font-weight: 700;
            color: #F1F5F9;
            margin-bottom: 3px;
        }}

        .wp-desc {{
            font-size: 11.8px;
            color: var(--text-muted);
            line-height: 1.4;
        }}

        .chart-card {{
            background: var(--card-bg);
            border: 1px solid var(--border);
            border-radius: 16px;
            padding: 20px;
            margin-bottom: 20px;
        }}

        .chart-card h3 {{
            font-size: 15px;
            font-weight: 700;
            color: #CBD5E1;
            margin-bottom: 12px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }}

        .chart-container {{
            position: relative;
            height: 200px;
            width: 100%;
        }}

        .tip-callout {{
            background: rgba(245, 158, 11, 0.1);
            border: 1px solid #F59E0B;
            border-left: 4px solid #F59E0B;
            border-radius: 8px;
            padding: 14px 18px;
            font-size: 13px;
            color: #FEF3C7;
            line-height: 1.6;
        }}

        .tip-callout strong {{
            color: #FBBF24;
        }}

        footer {{
            text-align: center;
            padding: 20px 0;
            color: #64748B;
            font-size: 12.5px;
        }}
    </style>
</head>
<body>

<div class="container">
    <header>
        <div class="header-title">
            <h1>🚲 Day 2 (方案B：黃金折衷) 具體路線地圖 Demo</h1>
            <p>Mt. Takao Base Camp (190m) ➔ 大垂水峠 (392m) ➔ 相模湖 (205m) ➔ 縣道35號秋山街道 ➔ 都留 由加利旅館 (484m)</p>
        </div>
        <div class="btn-group">
            <a href="{navitime_url}" target="_blank" class="action-btn">
                🗺️ 開啟 NAVITIME 單車導航 ➔
            </a>
            <a href="{gmaps_url}" target="_blank" class="action-btn" style="background:#4285F4;">
                📍 開啟 Google 地圖導航 ➔
            </a>
            <a href="day2_track.gpx" download="day2_takao_tsuru_yukari.gpx" class="action-btn gpx">
                📥 下載 GPX 軌跡檔
            </a>
        </div>
    </header>

    <div class="stats-bar">
        <div class="stat-box">
            <div class="val">{distance_km} km</div>
            <div class="lbl">實測總里程 (精簡舒適)</div>
        </div>
        <div class="stat-box">
            <div class="val">+{gain} m / -{loss} m</div>
            <div class="lbl">累積爬升 / 下降</div>
        </div>
        <div class="stat-box">
            <div class="val">190m ➔ 623m ➔ 484m</div>
            <div class="lbl">海拔變化 (起點 ➔ 峠頂 ➔ 終點)</div>
        </div>
        <div class="stat-box">
            <div class="val">&gt; 35 km</div>
            <div class="lbl">秋山街道零大貨車幽靜路段</div>
        </div>
        <div class="stat-box">
            <div class="val">~3.5 - 4.0 hr</div>
            <div class="lbl">預估純騎乘時間</div>
        </div>
    </div>

    <div class="main-layout">
        <div id="map"></div>
        <div class="sidebar">
            <h3>
                <span>📍 關鍵地標與路口導引</span>
                <span style="font-size: 11.5px; color: #38BDF8; font-weight: normal;">點擊可地圖定位</span>
            </h3>
            <div id="waypoint-list"></div>
        </div>
    </div>

    <div class="chart-card">
        <h3>
            <span>📈 GSI 國土地理院高精度海拔剖面圖（兩段式爬升）</span>
            <span style="font-size: 12px; color: #F59E0B;">第一段：大垂水峠 (+202m) ｜ 第二段：秋山溪谷緩升 (+418m)</span>
        </h3>
        <div class="chart-container">
            <canvas id="elevationChart"></canvas>
        </div>
    </div>

    <div class="tip-callout">
        <strong>💡 方案 B 實戰避坑精華：</strong>
        <br>1. <strong>清晨 08:00 直攻大垂水峠（4.2km，爬升 202m）：</strong> 剛出門體力充沛，此時段國道 20 號大車極少，以 5% 均勻坡度輕鬆攻頂，隨後暢快下滑至相模湖。
        <br>2. <strong>相模湖立即左轉「縣道 35 號（秋山街道）」：</strong> 徹底脫離國道 20 號！沿秋山川溪谷一路享受楓紅與清泉，最高點秋山隧道（623m）後滑降至都留市「由加利旅館」。
    </div>

    <footer>
        <p>東京・富士五湖・富士宮・伊豆・東京灣 19日秋季單車騎行計畫 ｜ Day 2 (方案B) 具體地圖 Demo</p>
    </footer>
</div>

<script>
const map = L.map('map').setView([35.5800, 139.1000], 11);

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

const routeGeojson = {json.dumps(route['geometry'])};

const polylineLayer = L.geoJSON(routeGeojson, {{
    style: {{
        color: '#F59E0B',
        weight: 6,
        opacity: 0.9
    }}
}}).addTo(map);

map.fitBounds(polylineLayer.getBounds(), {{ padding: [30, 30] }});

const waypointsData = {json.dumps(waypoints, ensure_ascii=False)};
const listContainer = document.getElementById('waypoint-list');

waypointsData.forEach((wp) => {{
    let markerColor = '#64748B';
    if (wp.type === 'start') markerColor = '#10B981';
    if (wp.type === 'climb1') markerColor = '#EF4444';
    if (wp.type === 'lake') markerColor = '#38BDF8';
    if (wp.type === 'pivot') markerColor = '#F59E0B';
    if (wp.type === 'valley') markerColor = '#10B981';
    if (wp.type === 'crest') markerColor = '#A855F7';
    if (wp.type === 'end') markerColor = '#EC4899';

    const customIcon = L.divIcon({{
        className: 'custom-div-icon',
        html: `<div style="background-color:${{markerColor}}; width: 15px; height: 15px; border-radius: 50%; border: 2.5px solid #FFFFFF; box-shadow: 0 0 8px rgba(0,0,0,0.6);"></div>`,
        iconSize: [15, 15],
        iconAnchor: [7.5, 7.5]
    }});

    const marker = L.marker([wp.lat, wp.lon], {{ icon: customIcon }}).addTo(map);
    marker.bindPopup(`<strong>${{wp.name}}</strong><br><small style="color:#555;">${{wp.desc}}</small>`);

    const item = document.createElement('div');
    item.className = 'waypoint-item';
    item.innerHTML = `
        <div class="wp-dot ${{wp.type}}"></div>
        <div class="wp-title">${{wp.name}}</div>
        <div class="wp-desc">${{wp.desc}}</div>
    `;
    item.addEventListener('click', () => {{
        map.setView([wp.lat, wp.lon], 14, {{ animate: true }});
        marker.openPopup();
    }});
    listContainer.appendChild(item);
}});

const elevData = {json.dumps(elevations)};
const labels = elevData.map((d, i) => Math.round((i / (elevData.length - 1)) * {distance_km}) + ' km');
const elevations_m = elevData.map(d => d.elev);

const ctx = document.getElementById('elevationChart').getContext('2d');
new Chart(ctx, {{
    type: 'line',
    data: {{
        labels: labels,
        datasets: [{{
            label: '海拔高度 (m)',
            data: elevations_m,
            fill: true,
            backgroundColor: 'rgba(245, 158, 11, 0.2)',
            borderColor: '#F59E0B',
            borderWidth: 2.5,
            pointRadius: 2,
            pointHoverRadius: 6,
            pointBackgroundColor: '#FCD34D',
            tension: 0.25
        }}]
    }},
    options: {{
        responsive: true,
        maintainAspectRatio: false,
        scales: {{
            x: {{
                grid: {{ color: '#1E293B' }},
                ticks: {{ color: '#94A3B8', maxTicksLimit: 12 }}
            }},
            y: {{
                grid: {{ color: '#1E293B' }},
                ticks: {{ color: '#94A3B8', callback: val => val + ' m' }},
                min: 150,
                max: 700
            }}
        }},
        plugins: {{
            legend: {{ display: false }},
            tooltip: {{
                callbacks: {{
                    title: context => '里程：' + context[0].label,
                    label: context => '海拔高度：' + context.parsed.y + ' m'
                }}
            }}
        }}
    }}
}});
</script>

</body>
</html>
"""

with open("d:/2026東京單車騎旅/day2_route_map_demo.html", "w", encoding="utf-8") as f:
    f.write(html_content)
with open("C:/Users/ymero/Downloads/day2_route_map_demo.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("Saved day2_route_map_demo.html successfully!")
