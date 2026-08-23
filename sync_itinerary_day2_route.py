import re

with open('d:/2026東京單車騎旅/tokyo_fuji_cycling_itinerary_19days_v2.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace summary table Day 2
html = re.sub(
    r'<td>高尾山口 ➔ <strong>甲州街道.*?都留</td>\s*<td><strong>.*?km</strong></td>\s*<td>.*?</td>',
    '<td>高尾山口 ➔ <strong>甲州街道(國道20)</strong> ➔ 大垂水峠(392m) ➔ 千木良 ➔ 相模湖 ➔ 勝瀬橋 ➔ 縣道35秋山街道 ➔ 都留</td>\n                        <td><strong>68.5 km</strong></td>\n                        <td>+1258m / -970m</td>',
    html
)

# Replace Day 2 Card title and stats
old_d2_title = """<div class="day-title"><span class="day-num">Day 2</span> 11/14（六）府中 ➔ 淺川自行車道 ➔ 高尾／津久井湖畔 ➔ 縣道35號秋山街道 ➔ 都留</div>"""
new_d2_title = """<div class="day-title"><span class="day-num">Day 2</span> 11/14（六）高尾山口 ➔ 甲州街道(國道20) ➔ 大垂水峠(392m) ➔ 千木良 ➔ 相模湖 ➔ 勝瀬橋 ➔ 縣道35號秋山街道 ➔ 都留</div>"""
html = html.replace(old_d2_title, new_d2_title)

# Replace Day 2 Card stats
old_d2_stats = """68.5 km ｜ <span class="elev-pill">+580 m / -385 m</span> ｜ 海拔 54~612m"""
new_d2_stats = """68.5 km ｜ <span class="elev-pill">+1258 m / -970 m</span> ｜ 海拔 193~612m"""
html = html.replace(old_d2_stats, new_d2_stats)

# Replace Day 2 Route description
old_d2_route = """<div class="route-step"><span class="step-label">路線：</span>府中 ➔ 淺川自行車道 ➔ 八王子／高尾 ➔ 經町田街道／國道 413 號 ➔ 城山湖／津久井湖畔（神奈川縣道 515/517 號） ➔ 接山梨縣道 35 號（秋山街道） ➔ 都留市</div>"""
new_d2_route = """<div class="route-step"><span class="step-label">路線：</span>Mt. Takao Base Camp ➔ 國道 20 號（甲州街道） ➔ 攻頂【大垂水峠（標高392m）】 ➔ 順暢滑降經【千木良】 ➔ 相模湖站前 ➔ 🚨 左轉跨越【勝瀬橋】切入縣道520/76號（日連・名倉） ➔ 抵達【奧牧野】正式切入【山梨縣道35號（秋山街道）】 ➔ 秋山溫泉 ➔ 無生野 ➔ 攻頂【秋山隧道（分水嶺標高612m）】 ➔ 7公里長下坡爽快滑降 ➔ 都留市 ビジネス旅館 由加利</div>"""
html = html.replace(old_d2_route, new_d2_route)

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

print("Updated itinerary with verified Day 2 Route 20 Chigira -> Sagamiko -> Katsuse Bridge -> r35 Akiyama route!")
