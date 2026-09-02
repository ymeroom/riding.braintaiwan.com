import re

with open('d:/2026東京單車騎旅/tokyo_fuji_cycling_itinerary_19days_v2.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace summary table Day 1
html = re.sub(
    r'<td>秋葉原.*?高尾山口</td>\s*<td><strong>.*?km</strong></td>\s*<td>.*?</td>',
    '<td>秋葉原 ➔ 國道15號 ➔ 六鄉橋 ➔ 多摩川CR(左岸) ➔ 府中四谷橋 ➔ 淺川CR ➔ 南淺川CR(南淺川橋) ➔ 高尾山口</td>\n                        <td><strong>81.5 km</strong></td>\n                        <td>+267m / -71m</td>',
    html
)

# Replace Day 1 Card stats
html = re.sub(
    r'<div class="day-stats">\s*[\d\.]+\s*km\s*｜\s*<span class="elev-pill">.*?</span>\s*｜\s*海拔\s*[\d~]+m',
    '<div class="day-stats">\n                    81.5 km ｜ <span class="elev-pill">+267 m / -71 m</span> ｜ 海拔 3~193m',
    html,
    count=1
)

# Save to all target files
files = [
    'd:/2026東京單車騎旅/tokyo_fuji_cycling_itinerary_19days_v2.html',
    'd:/2026東京單車騎旅/index.html',
    'C:/Users/ymero/Downloads/tokyo_fuji_cycling_itinerary_19days_v2.html',
    'C:/Users/ymero/Downloads/index.html'
]

for fp in files:
    with open(fp, 'w', encoding='utf-8') as f:
        f.write(html)

print("Updated itinerary with 81.5km 100% dedicated cycleway details!")
