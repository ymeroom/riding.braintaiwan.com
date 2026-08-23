import re

with open('d:/2026東京單車騎旅/tokyo_fuji_cycling_itinerary_19days_v2.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Update Day 1 stats in table and card
html = re.sub(
    r'<td>秋葉原.*?高尾山口</td>\s*<td><strong>.*?km</strong></td>\s*<td>.*?</td>',
    '<td>秋葉原 ➔ 國道15號 ➔ 六鄉橋 ➔ 多摩川CR(左岸) ➔ 府中四谷橋 ➔ 淺川CR ➔ 南淺川CR(南淺川橋) ➔ 高尾山口</td>\n                        <td><strong>81.5 km</strong></td>\n                        <td>+245m / -55m</td>',
    html
)

html = re.sub(
    r'<div class="day-stats">\s*81\.5\s*km\s*｜\s*<span class="elev-pill">.*?</span>\s*｜\s*海拔\s*[\d~]+m',
    '<div class="day-stats">\n                    81.5 km ｜ <span class="elev-pill">+245 m / -55 m</span> ｜ 海拔 3~193m（多摩川＋淺川水岸純平路）',
    html,
    count=1
)

# Update Day 2 stats in table and card
html = re.sub(
    r'<td>高尾山口 ➔ <strong>甲州街道.*?都留</td>\s*<td><strong>.*?km</strong></td>\s*<td>.*?</td>',
    '<td>高尾山口 ➔ <strong>甲州街道(國道20)</strong> ➔ 大垂水峠(392m) ➔ 相模湖 ➔ 日本三奇橋(猿橋) ➔ 大月 ➔ 國道139 ➔ 都留</td>\n                        <td><strong>60.4 km</strong></td>\n                        <td>+510m / -230m</td>',
    html
)

html = re.sub(
    r'<div class="day-stats">\s*60\.4\s*km\s*｜\s*<span class="elev-pill">.*?</span>\s*｜\s*海拔\s*[\d~]+m.*?</div>',
    '<div class="day-stats">\n                        60.4 km ｜ <span class="elev-pill">+510 m / -230 m</span> ｜ 海拔 175~475m（NAVITIME 實測低爬升河谷直達線）\n                    </div>',
    html,
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
        f.write(html)

print("Updated itinerary cards and tables with NAVITIME-aligned elevations!")
