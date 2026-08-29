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

kml_content = """<?xml version="1.0" encoding="UTF-8"?>
<kml xmlns="http://www.opengis.net/kml/2.2">
  <Document>
    <name>2026 東京單車騎旅 19 天行程</name>
    <description>所有每日目的地與停靠站</description>
"""

for day, loc in DAY_LOCATIONS.items():
    kml_content += f"""
    <Placemark>
      <name>{loc['name']}</name>
      <description>Day {day} 目的地</description>
      <Point>
        <coordinates>{loc['lon']},{loc['lat']},0</coordinates>
      </Point>
    </Placemark>
"""

kml_content += """
  </Document>
</kml>
"""

with open('19days_route.kml', 'w', encoding='utf-8') as f:
    f.write(kml_content)
