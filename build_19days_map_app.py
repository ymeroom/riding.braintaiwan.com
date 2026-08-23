import json, sys

with open("d:/2026東京單車騎旅/all_19days_route_data.json", "r", encoding="utf-8") as f:
    days_data = json.load(f)

json_data_str = json.dumps(days_data, ensure_ascii=False)

html_content = f'''<!DOCTYPE html>
<html lang="zh-TW">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>東京・富士五湖・伊豆・東京灣 19日秋季單車騎旅 ｜ 19天全路線地圖與標高剖面互動 Demo</title>
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
            --primary: #2563EB;
            --accent: #F59E0B;
            --success: #10B981;
            --danger: #EF4444;
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
            max-width: 1440px;
            margin: 0 auto;
        }}

        /* 橫幅頂部 */
        header {{
            background: linear-gradient(135deg, #1E1B4B 0%, #31102E 50%, #451A03 100%);
            border: 1px solid var(--border);
            border-radius: 16px;
            padding: 20px 24px;
            margin-bottom: 16px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            flex-wrap: wrap;
            gap: 16px;
        }}

        .header-title h1 {{
            font-size: 21px;
            font-weight: 800;
            color: #FFFFFF;
            margin-bottom: 4px;
        }}

        .header-title p {{
            font-size: 13px;
            color: #CBD5E1;
        }}

        .nav-links {{
            display: flex;
            gap: 10px;
            flex-wrap: wrap;
        }}

        .nav-btn {{
            background: rgba(255, 255, 255, 0.12);
            color: #FFFFFF;
            padding: 8px 14px;
            border-radius: 8px;
            text-decoration: none;
            font-size: 12.5px;
            font-weight: 600;
            display: inline-flex;
            align-items: center;
            gap: 6px;
            border: 1px solid rgba(255, 255, 255, 0.2);
            transition: all 0.15s ease;
        }}

        .nav-btn:hover {{
            background: rgba(255, 255, 255, 0.25);
            transform: translateY(-1px);
        }}

        .nav-btn.primary {{
            background: var(--primary);
            border-color: #3B82F6;
        }}

        /* 19天選擇器 Tab 列 */
        .days-nav-wrapper {{
            background: var(--card-bg);
            border: 1px solid var(--border);
            border-radius: 14px;
            padding: 12px 14px;
            margin-bottom: 16px;
            overflow-x: auto;
            white-space: nowrap;
            scrollbar-width: thin;
        }}

        .days-nav {{
            display: flex;
            gap: 8px;
        }}

        .day-tab {{
            background: #1E293B;
            border: 1px solid #334155;
            color: #94A3B8;
            padding: 7px 14px;
            border-radius: 8px;
            cursor: pointer;
            font-size: 12px;
            font-weight: 700;
            transition: all 0.15s ease;
            display: inline-flex;
            flex-direction: column;
            align-items: center;
            gap: 2px;
            min-width: 68px;
            user-select: none;
        }}

        .day-tab:hover {{
            background: #334155;
            color: #FFFFFF;
            border-color: #475569;
        }}

        .day-tab.active {{
            background: #2563EB;
            color: #FFFFFF;
            border-color: #60A5FA;
            box-shadow: 0 0 12px rgba(37, 99, 235, 0.5);
        }}

        .day-tab .tab-date {{
            font-size: 10px;
            font-weight: 500;
            opacity: 0.85;
        }}

        .day-tab.booked-tag {{
            border-bottom: 3px solid #10B981;
        }}

        /* KPI 指標列 */
        .stats-bar {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(170px, 1fr));
            gap: 12px;
            margin-bottom: 16px;
        }}

        .stat-box {{
            background: var(--card-bg);
            border: 1px solid var(--border);
            border-radius: 12px;
            padding: 12px 16px;
            text-align: center;
        }}

        .stat-box .val {{
            font-size: 19px;
            font-weight: 800;
            color: var(--accent);
            margin-bottom: 2px;
        }}

        .stat-box .lbl {{
            font-size: 11px;
            color: var(--text-muted);
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }}

        /* 主佈局：地圖 + 側邊欄 */
        .main-layout {{
            display: grid;
            grid-template-columns: 1fr 380px;
            gap: 16px;
            margin-bottom: 16px;
        }}

        @media (max-width: 1024px) {{
            .main-layout {{
                grid-template-columns: 1fr;
            }}
        }}

        #map {{
            height: 560px;
            border-radius: 14px;
            border: 1px solid var(--border);
            box-shadow: 0 8px 24px rgba(0, 0, 0, 0.4);
            z-index: 1;
        }}

        .sidebar {{
            background: var(--card-bg);
            border: 1px solid var(--border);
            border-radius: 14px;
            padding: 18px;
            display: flex;
            flex-direction: column;
            gap: 14px;
            max-height: 560px;
            overflow-y: auto;
        }}

        .sidebar-section-title {{
            font-size: 13.5px;
            font-weight: 700;
            color: #F8FAFC;
            display: flex;
            align-items: center;
            gap: 6px;
            border-bottom: 1px solid var(--border);
            padding-bottom: 6px;
        }}

        .hotel-card {{
            background: rgba(30, 41, 59, 0.7);
            border: 1px solid #334155;
            border-radius: 10px;
            padding: 12px;
        }}

        .hotel-name {{
            font-size: 14px;
            font-weight: 700;
            color: #38BDF8;
            margin-bottom: 4px;
        }}

        .hotel-addr {{
            font-size: 12px;
            color: #94A3B8;
            margin-bottom: 8px;
        }}

        .hotel-link {{
            color: #60A5FA;
            text-decoration: none;
            font-size: 12px;
            font-weight: 600;
            display: inline-flex;
            align-items: center;
            gap: 4px;
        }}
        .hotel-link:hover {{
            text-decoration: underline;
        }}

        .cue-list {{
            list-style: none;
            display: flex;
            flex-direction: column;
            gap: 8px;
            font-size: 12.5px;
        }}

        .cue-item {{
            display: flex;
            gap: 8px;
            align-items: flex-start;
            background: rgba(15, 23, 42, 0.6);
            border: 1px solid #1E293B;
            padding: 8px 10px;
            border-radius: 6px;
        }}

        .cue-num {{
            background: #2563EB;
            color: #FFFFFF;
            width: 18px;
            height: 18px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 10px;
            font-weight: 800;
            flex-shrink: 0;
            margin-top: 2px;
        }}

        .cue-text {{
            color: #CBD5E1;
            line-height: 1.4;
        }}

        .quick-nav-btns {{
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 8px;
            margin-top: auto;
        }}

        .app-btn {{
            background: #1E293B;
            border: 1px solid #334155;
            color: #F8FAFC;
            padding: 8px 10px;
            border-radius: 8px;
            font-size: 11.5px;
            font-weight: 700;
            text-decoration: none;
            text-align: center;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 4px;
            transition: all 0.15s ease;
        }}

        .app-btn:hover {{
            background: #334155;
            border-color: #64748B;
        }}

        .app-btn.gpx-btn {{
            grid-column: 1 / -1;
            background: #D97724;
            border-color: #F59E0B;
            color: #FFFFFF;
        }}
        .app-btn.gpx-btn:hover {{
            background: #B45309;
        }}

        /* 高程圖表區 */
        .chart-card {{
            background: var(--card-bg);
            border: 1px solid var(--border);
            border-radius: 14px;
            padding: 16px 20px;
            margin-bottom: 20px;
        }}

        .chart-header {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 12px;
        }}

        .chart-title {{
            font-size: 14px;
            font-weight: 700;
            color: #F8FAFC;
            display: flex;
            align-items: center;
            gap: 6px;
        }}

        .chart-container {{
            height: 200px;
            position: relative;
        }}

        /* 標籤小徽章 */
        .badge-booked {{
            background: #059669;
            color: #FFFFFF;
            padding: 2px 6px;
            border-radius: 4px;
            font-size: 10px;
            font-weight: 700;
            display: inline-block;
        }}
    </style>
</head>
<body>

<div class="container">
    <!-- 橫幅頂部 -->
    <header>
        <div class="header-title">
            <h1>東京・富士五湖・伊豆・東京灣 19日秋季單車騎旅</h1>
            <p>【全 19 天 OSRM 單車路網幾何 ＋ 日本國土地理院 GSI 1m DEM 實測高程互動地圖】</p>
        </div>
        <div class="nav-links">
            <a href="tokyo_fuji_cycling_itinerary_19days_v2.html" class="nav-btn primary">📋 返回 19日總行程表 ➔</a>
            <a href="suno_cycling_soundtrack_19days.html" target="_blank" class="nav-btn">🎵 19首 Suno 歌曲詞庫 ↗</a>
        </div>
    </header>

    <!-- 19 天選擇 Tab 列 -->
    <div class="days-nav-wrapper">
        <div class="days-nav" id="daysNav">
            <!-- Rendered via JS -->
        </div>
    </div>

    <!-- 核心數據指標欄 -->
    <div class="stats-bar">
        <div class="stat-box">
            <div class="val" id="kpiDist">-- km</div>
            <div class="lbl">實測騎行里程</div>
        </div>
        <div class="stat-box">
            <div class="val" id="kpiGain">+-- m</div>
            <div class="lbl">累積爬升 / 下降</div>
        </div>
        <div class="stat-box">
            <div class="val" id="kpiAlt">-- m</div>
            <div class="lbl">起點 ➔ 終點 (最高)</div>
        </div>
        <div class="stat-box">
            <div class="val" id="kpiWeather">☀️ 快晴</div>
            <div class="lbl">去年實測氣象 (JMA)</div>
        </div>
        <div class="stat-box">
            <div class="val" id="kpiFoliage" style="font-size: 15px;">見頃</div>
            <div class="lbl">紅葉 / 景觀情報</div>
        </div>
    </div>

    <!-- 主地圖與側邊導航欄 -->
    <div class="main-layout">
        <div id="map"></div>

        <div class="sidebar">
            <div class="sidebar-section-title">
                🏨 當日住宿與導航
            </div>
            <div class="hotel-card" id="hotelCard">
                <!-- Rendered via JS -->
            </div>

            <div class="sidebar-section-title">
                🚲 轉彎指引與避坑提醒 (Turn-by-Turn)
            </div>
            <ul class="cue-list" id="cueList">
                <!-- Rendered via JS -->
            </ul>

            <div class="quick-nav-btns">
                <a href="#" id="btnGoogle" target="_blank" class="app-btn">🗺️ Google Maps 導航 ↗</a>
                <a href="#" id="btnNavitime" target="_blank" class="app-btn">🗾 NAVITIME 導航 ↗</a>
                <button id="btnDownloadGPX" class="app-btn gpx-btn">💾 下載當日 GPX 軌跡檔 (Garmin/Wahoo)</button>
            </div>
        </div>
    </div>

    <!-- GSI DEM 數值高程剖面圖表 -->
    <div class="chart-card">
        <div class="chart-header">
            <div class="chart-title">
                📈 日本國土地理院 (GSI 1m DEM) 精確標高剖面 (滑鼠懸停查看公里與海拔)
            </div>
            <div style="font-size: 12px; color: #94A3B8;">
                X軸：騎行公里數 (km) ｜ Y軸：海拔高度 (m)
            </div>
        </div>
        <div class="chart-container">
            <canvas id="elevationChart"></canvas>
        </div>
    </div>
</div>

<script>
    // 19 Days Comprehensive Dataset
    const daysData = {json_data_str};

    let currentDayIdx = 0;
    let map, polylineLayer, startMarker, endMarker, hoverMarker;
    let elevationChart;

    // Initialize Leaflet Map
    function initMap() {{
        // Base layers
        const osm = L.tileLayer('https://{{s}}.tile.openstreetmap.org/{{z}}/{{x}}/{{y}}.png', {{
            maxZoom: 19,
            attribution: '© OpenStreetMap'
        }});

        const gsiStd = L.tileLayer('https://cyberjapandata.gsi.go.jp/xyz/std/{{z}}/{{x}}/{{y}}.png', {{
            maxZoom: 18,
            attribution: '© 國土地理院 標準地圖'
        }});

        const gsiPale = L.tileLayer('https://cyberjapandata.gsi.go.jp/xyz/pale/{{z}}/{{x}}/{{y}}.png', {{
            maxZoom: 18,
            attribution: '© 國土地理院 淡色地圖'
        }});

        const gsiRelief = L.tileLayer('https://cyberjapandata.gsi.go.jp/xyz/relief/{{z}}/{{x}}/{{y}}.png', {{
            maxZoom: 15,
            attribution: '© 國土地理院 標高地形圖'
        }});

        map = L.map('map', {{
            center: [35.6, 139.3],
            zoom: 10,
            layers: [osm]
        }});

        const baseLayers = {{
            "OpenStreetMap (標準)": osm,
            "國土地理院 (標準)": gsiStd,
            "國土地理院 (淡色)": gsiPale,
            "國土地理院 (標高地形)": gsiRelief
        }};

        L.control.layers(baseLayers, null, {{ position: 'topright' }}).addTo(map);
    }}

    // Render Day Navigation Tabs
    function renderDaysNav() {{
        const nav = document.getElementById('daysNav');
        nav.innerHTML = '';

        daysData.forEach((d, idx) => {{
            const tab = document.createElement('div');
            tab.className = `day-tab ${{idx === currentDayIdx ? 'active' : ''}} ${{d.booked ? 'booked-tag' : ''}}`;
            tab.innerHTML = `
                <span>Day ${{d.day}}</span>
                <span class="tab-date">${{d.date.split('（')[0]}}</span>
            `;
            tab.onclick = () => selectDay(idx);
            nav.appendChild(tab);
        }});
    }}

    // Select Day and Update Everything
    function selectDay(idx) {{
        currentDayIdx = idx;
        const d = daysData[idx];

        // Update Tabs Active state
        document.querySelectorAll('.day-tab').forEach((t, i) => {{
            t.classList.toggle('active', i === idx);
        }});

        // Update KPI Cards
        document.getElementById('kpiDist').innerText = `${{d.dist_km}} km`;
        document.getElementById('kpiGain').innerText = `+${{d.gain}}m / -${{d.loss}}m`;
        document.getElementById('kpiAlt').innerText = `${{d.start_e}}m ➔ ${{d.end_e}}m (${{d.peak_e}}m)`;
        document.getElementById('kpiWeather').innerText = d.weather.split('｜')[0];
        document.getElementById('kpiFoliage').innerText = d.foliage.split('｜')[0];

        // Update Sidebar Hotel
        const hotelCard = document.getElementById('hotelCard');
        hotelCard.innerHTML = `
            <div class="hotel-name">${{d.hotel}} ${{d.booked ? '<span class="badge-booked">✅ 已訂房</span>' : ''}}</div>
            <div class="hotel-addr">📍 ${{d.hotel_addr}}</div>
            <a href="${{d.hotel_url}}" target="_blank" class="hotel-link">在 Google Maps 中查看位置 ↗</a>
        `;

        // Update Cues
        const cueList = document.getElementById('cueList');
        cueList.innerHTML = '';
        d.cues.forEach((cue, i) => {{
            const li = document.createElement('li');
            li.className = 'cue-item';
            li.innerHTML = `
                <div class="cue-num">${{i + 1}}</div>
                <div class="cue-text">${{cue}}</div>
            `;
            cueList.appendChild(li);
        }});

        // Update Action URLs
        const startPt = d.coords[0];
        const endPt = d.coords[d.coords.length - 1];
        document.getElementById('btnGoogle').href = `https://www.google.com/maps/dir/?api=1&origin=${{startPt[1]}},${{startPt[0]}}&destination=${{endPt[1]}},${{endPt[0]}}&travelmode=bicycling`;
        document.getElementById('btnNavitime').href = `https://www.navitime.co.jp/bicycle/`;
        document.getElementById('btnDownloadGPX').onclick = () => downloadDayGPX(d);

        // Update Map Route
        updateMapRoute(d);

        // Update Elevation Chart
        updateElevationChart(d);
    }}

    // Update Leaflet Map Route Polyline & Markers
    function updateMapRoute(d) {{
        if (polylineLayer) map.removeLayer(polylineLayer);
        if (startMarker) map.removeLayer(startMarker);
        if (endMarker) map.removeLayer(endMarker);
        if (hoverMarker) map.removeLayer(hoverMarker);

        // Convert [lon, lat] to [lat, lon]
        const latlngs = d.coords.map(c => [c[1], c[0]]);

        polylineLayer = L.polyline(latlngs, {{
            color: '#3B82F6',
            weight: 5,
            opacity: 0.85,
            lineJoin: 'round'
        }}).addTo(map);

        // Start marker (Green)
        startMarker = L.circleMarker(latlngs[0], {{
            radius: 8,
            fillColor: '#10B981',
            color: '#FFFFFF',
            weight: 2,
            opacity: 1,
            fillOpacity: 1
        }}).bindPopup(`<b>起點</b><br>海拔: ${{d.start_e}}m`).addTo(map);

        // End marker (Red)
        endMarker = L.circleMarker(latlngs[latlngs.length - 1], {{
            radius: 8,
            fillColor: '#EF4444',
            color: '#FFFFFF',
            weight: 2,
            opacity: 1,
            fillOpacity: 1
        }}).bindPopup(`<b>終點: ${{d.hotel}}</b><br>海拔: ${{d.end_e}}m`).addTo(map);

        // Fit map bounds
        map.fitBounds(polylineLayer.getBounds(), {{ padding: [30, 30] }});
    }}

    // Update Chart.js Elevation Profile
    function updateElevationChart(d) {{
        const ctx = document.getElementById('elevationChart').getContext('2d');
        const labels = d.elev_profile.map(p => `${{p.km}} km`);
        const elevations = d.elev_profile.map(p => p.ele);

        if (elevationChart) {{
            elevationChart.destroy();
        }}

        // Gradient fill
        const gradient = ctx.createLinearGradient(0, 0, 0, 180);
        gradient.addColorStop(0, 'rgba(59, 130, 246, 0.45)');
        gradient.addColorStop(1, 'rgba(59, 130, 246, 0.02)');

        elevationChart = new Chart(ctx, {{
            type: 'line',
            data: {{
                labels: labels,
                datasets: [{{
                    label: '標高 (m)',
                    data: elevations,
                    borderColor: '#60A5FA',
                    borderWidth: 2.5,
                    fill: true,
                    backgroundColor: gradient,
                    tension: 0.25,
                    pointRadius: 0,
                    pointHoverRadius: 6,
                    pointHoverBackgroundColor: '#F59E0B',
                    pointHoverBorderColor: '#FFFFFF',
                    pointHoverBorderWidth: 2
                }}]
            }},
            options: {{
                responsive: true,
                maintainAspectRatio: false,
                interaction: {{
                    mode: 'index',
                    intersect: false
                }},
                plugins: {{
                    legend: {{ display: false }},
                    tooltip: {{
                        backgroundColor: 'rgba(15, 23, 42, 0.9)',
                        titleColor: '#F8FAFC',
                        bodyColor: '#38BDF8',
                        borderColor: '#334155',
                        borderWidth: 1,
                        padding: 10,
                        callbacks: {{
                            label: function(context) {{
                                return `海拔標高: ${{context.parsed.y}} m`;
                            }}
                        }}
                    }}
                }},
                scales: {{
                    x: {{
                        grid: {{ color: 'rgba(51, 65, 85, 0.4)' }},
                        ticks: {{ color: '#94A3B8', maxTicksLimit: 12 }}
                    }},
                    y: {{
                        grid: {{ color: 'rgba(51, 65, 85, 0.4)' }},
                        ticks: {{ color: '#94A3B8' }}
                    }}
                }},
                onHover: (e, activeElements) => {{
                    if (activeElements.length > 0) {{
                        const idx = activeElements[0].index;
                        const pt = d.elev_profile[idx];
                        if (pt && map) {{
                            if (hoverMarker) map.removeLayer(hoverMarker);
                            hoverMarker = L.circleMarker([pt.lat, pt.lon], {{
                                radius: 7,
                                fillColor: '#F59E0B',
                                color: '#FFFFFF',
                                weight: 2,
                                fillOpacity: 1
                            }}).addTo(map);
                        }}
                    }}
                }}
            }}
        }});
    }}

    // Download GPX for current Day
    function downloadDayGPX(d) {{
        let gpx = `<?xml version="1.0" encoding="UTF-8"?>\\n<gpx version="1.1" creator="TokyoCycling2026" xmlns="http://www.topografix.com/GPX/1/1">\\n  <metadata>\\n    <name>Day ${{d.day}}: ${{d.title}}</name>\\n    <desc>${{d.dist_km}} km | +${{d.gain}}m / -${{d.loss}}m</desc>\\n  </metadata>\\n  <trk>\\n    <name>Day ${{d.day}}: ${{d.title}}</name>\\n    <trkseg>\\n`;
        d.coords.forEach(pt => {{
            gpx += `      <trkpt lat="${{pt[1]}}" lon="${{pt[0]}}"></trkpt>\\n`;
        }});
        gpx += `    </trkseg>\\n  </trk>\\n</gpx>`;

        const blob = new Blob([gpx], {{ type: 'application/gpx+xml' }});
        const url = URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url;
        a.download = `day${{d.day}}_track.gpx`;
        document.body.appendChild(a);
        a.click();
        document.body.removeChild(a);
        URL.revokeObjectURL(url);
    }}

    // Initialize on page load
    window.onload = () => {{
        initMap();
        renderDaysNav();
        selectDay(0);
    }};
</script>

</body>
</html>'''

# Write to Downloads and Workspace
with open("C:/Users/ymero/Downloads/tokyo_cycling_19days_map_demo.html", "w", encoding="utf-8") as f:
    f.write(html_content)

with open("d:/2026東京單車騎旅/tokyo_cycling_19days_map_demo.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("Master 19-Day Interactive Map Demo generated successfully at tokyo_cycling_19days_map_demo.html!")
