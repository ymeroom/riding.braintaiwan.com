import re

with open('d:/2026東京單車騎旅/tokyo_fuji_cycling_itinerary_19days_v2.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update Day 1 in summary table
# Old Day 1 row in table
old_table_d1 = """<td>秋葉原 ➔ 銀座/品川 ➔ 國道15號 ➔ 六鄉橋 ➔ 多摩川CR ➔ 府中(50km) ➔ 高尾山口</td>
                        <td><strong>89.7 km</strong></td>
                        <td>+243m / -62m</td>"""

new_table_d1 = """<td>秋葉原 ➔ 國道15號 ➔ 六鄉橋 ➔ 多摩川CR ➔ 府中四谷橋 ➔ 淺川CR ➔ 南淺川橋 ➔ 高尾山口</td>
                        <td><strong>82.4 km</strong></td>
                        <td>+259m / -69m</td>"""

html = html.replace(old_table_d1, new_table_d1)

# 2. Update Day 1 card
old_card_title = """<div class="day-title"><span class="day-num">Day 1</span> 11/13（五）秋葉原取車 ➔ 國道15號平坦水岸 ➔ 六鄉橋 ➔ 多摩川自行車道 ➔ 府中／調布</div>"""
new_card_title = """<div class="day-title"><span class="day-num">Day 1</span> 11/13（五）秋葉原取車 ➔ 國道15號 ➔ 六鄉橋 ➔ 多摩川CR ➔ 府中四谷橋 ➔ 淺川CR ➔ 南淺川橋 ➔ 高尾山口</div>"""
html = html.replace(old_card_title, new_card_title)

# Update stats in day card
old_card_stats = """50.4 km ｜ <span class="elev-pill">+62 m / -13 m</span> ｜ 海拔 2~54m"""
new_card_stats = """82.4 km ｜ <span class="elev-pill">+259 m / -69 m</span> ｜ 海拔 3~193m"""
html = html.replace(old_card_stats, new_card_stats)

# Update route step description in day card
old_route_desc = """<div class="route-step"><span class="step-label">路線：</span>CycleTrip Base (09:30 取車) ➔ 銀座／新橋 ➔ 國道 15 號（第一京濱，寬路肩）➔ 六鄉橋切入【多摩川自行車專用道】 ➔ 沿多摩川左岸逆流緩上 ➔ 二子玉川 ➔ 府中／調布</div>"""
new_route_desc = """<div class="route-step"><span class="step-label">路線：</span>CycleTrip Base (09:30 取車) ➔ 銀座／新橋 ➔ 國道 15 號（第一京濱，路肩寬闊）➔ 六鄉橋切入【多摩川自行車專用道（左岸）】 ➔ 二子玉川 ➔ 府中四谷橋切入【淺川自行車專用道 (浅川ゆったりロード)】 ➔ 八王子市役所／鶴巻橋切入【南淺川自行車道】 ➔ 陵南公園／南淺川橋 ➔ 國道20號甲州街道 ➔ 高尾山口 Mt. Takao Base Camp</div>"""
html = html.replace(old_route_desc, new_route_desc)

# Save to all locations
files = [
    'd:/2026東京單車騎旅/tokyo_fuji_cycling_itinerary_19days_v2.html',
    'd:/2026東京單車騎旅/index.html',
    'C:/Users/ymero/Downloads/tokyo_fuji_cycling_itinerary_19days_v2.html',
    'C:/Users/ymero/Downloads/index.html'
]

for fp in files:
    with open(fp, 'w', encoding='utf-8') as f:
        f.write(html)

print("Updated Day 1 itinerary descriptions with exact 82.4km Asakawa route!")
