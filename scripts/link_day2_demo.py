import sys
sys.stdout.reconfigure(encoding='utf-8')

for filepath in ['C:/Users/ymero/Downloads/tokyo_fuji_cycling_itinerary_19days_v2.html', 'd:/2026東京單車騎旅/tokyo_fuji_cycling_itinerary_19days_v2.html']:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    target = '<span class="day-num">Day 2</span> 11/14（六）府中 ➔ 淺川自行車道 ➔ 高尾 ➔ 秋山街道幽谷 ➔ 都留市</div>'
    target_alt = '<span class="day-num">Day 2</span> 11/14（六）'
    
    replacement = '<span class="day-num">Day 2</span> 11/14（六）Mt. Takao Base Camp ➔ 大垂水峠 ➔ 相模湖 ➔ 縣道35秋山街道 ➔ 都留 由加利旅館</div>\n                <div style="margin-top: 6px;"><a href="day2_route_map_demo.html" target="_blank" style="display: inline-flex; align-items: center; gap: 4px; background: #D97724; color: #FFFFFF; padding: 3px 10px; border-radius: 6px; font-size: 12px; font-weight: 700; text-decoration: none;">🗺️ 開啟 Day 2 具體地圖 Demo (NAVITIME/Leaflet/GPX) ➔</a></div>'
    
    if target in content and 'day2_route_map_demo.html' not in content:
        content = content.replace(target, replacement)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Linked day 2 demo in {filepath}")
