import json

DAY_LOCATIONS = {
    1: {'lat': 35.628, 'lon': 139.270, 'name': 'Day 1: 高尾/八王子'},
    2: {'lat': 35.626, 'lon': 139.119, 'name': 'Day 2: 上野原/相模湖'},
    3: {'lat': 35.498, 'lon': 138.769, 'name': 'Day 3: 富士河口湖'},
    4: {'lat': 35.418, 'lon': 138.868, 'name': 'Day 4: 山中湖'},
    5: {'lat': 35.308, 'lon': 138.934, 'name': 'Day 5: 御殿場'},
    6: {'lat': 35.232, 'lon': 139.106, 'name': 'Day 6: 箱根'},
    7: {'lat': 35.257, 'lon': 139.155, 'name': 'Day 7: 小田原'},
    8: {'lat': 35.095, 'lon': 139.073, 'name': 'Day 8: 熱海'},
    9: {'lat': 34.971, 'lon': 139.098, 'name': 'Day 9: 伊東'},
    10: {'lat': 34.679, 'lon': 138.945, 'name': 'Day 10: 下田'},
    11: {'lat': 34.976, 'lon': 138.932, 'name': 'Day 11: 伊豆'},
    12: {'lat': 35.101, 'lon': 138.859, 'name': 'Day 12: 沼津'},
    13: {'lat': 35.161, 'lon': 138.676, 'name': 'Day 13: 富士'},
    14: {'lat': 34.975, 'lon': 138.382, 'name': 'Day 14: 靜岡'},
    15: {'lat': 35.319, 'lon': 139.550, 'name': 'Day 15: 鎌倉'},
    16: {'lat': 35.443, 'lon': 139.638, 'name': 'Day 16: 橫濱'},
    17: {'lat': 35.689, 'lon': 139.691, 'name': 'Day 17: 東京'},
    19: {'lat': 35.776, 'lon': 140.318, 'name': 'Day 19: 成田'}
}

markers_js = ''
latlngs_js = ''
for day, loc in DAY_LOCATIONS.items():
    markers_js += f"""
        L.marker([{loc['lat']}, {loc['lon']}]).addTo(map)
         .bindPopup('<b>{loc['name']}</b>');
    """
    latlngs_js += f"[{loc['lat']}, {loc['lon']}],\n"

html = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>19 Days Itinerary on Google Maps</title>
    <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
    <style>
        body {{ margin: 0; padding: 0; }}
        #map {{ width: 100vw; height: 100vh; }}
        .header-overlay {{
            position: absolute;
            top: 15px; left: 50%;
            transform: translateX(-50%);
            z-index: 1000;
            background: rgba(255,255,255,0.95);
            padding: 12px 24px;
            border-radius: 30px;
            font-family: sans-serif;
            font-weight: bold;
            font-size: 15px;
            color: #1e293b;
            box-shadow: 0 4px 15px rgba(0,0,0,0.15);
            white-space: nowrap;
        }}
    </style>
</head>
<body>
    <div class="header-overlay">🚴 2026 東京單車騎旅 19 天全路線 (Google 地圖版)</div>
    <div id="map"></div>

    <script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
    <script>
        var map = L.map('map').setView([35.3606, 139.273], 9);

        // Load Google Maps Tile Layer
        L.tileLayer('http://mt0.google.com/vt/lyrs=m&hl=zh-TW&x={{x}}&y={{y}}&z={{z}}', {{
            maxZoom: 20,
            attribution: '&copy; Google Maps'
        }}).addTo(map);

        {markers_js}

        var routeCoords = [
            {latlngs_js}
        ];
        var polyline = L.polyline(routeCoords, {{color: '#E11D48', weight: 4, opacity: 0.8}}).addTo(map);
        map.fitBounds(polyline.getBounds(), {{padding: [50, 50]}});
    </script>
</body>
</html>
"""

with open('google_maps_19days.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('google_maps_19days.html generated')
