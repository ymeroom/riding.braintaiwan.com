import sys
sys.stdout.reconfigure(encoding='utf-8')

for filepath in ['C:/Users/ymero/Downloads/tokyo_fuji_cycling_itinerary_19days_v2.html', 'd:/2026東京單車騎旅/tokyo_fuji_cycling_itinerary_19days_v2.html']:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    target = '<span class="day-num">Day 1</span> 11/13（五）秋葉原取車 ➔ 國道15號平坦水岸 ➔ 六鄉橋 ➔ 多摩川自行車道 ➔ 府中／調布</div>'
    replacement = target + '\n                <div style="margin-top: 6px;"><a href="day1_route_map_demo.html" target="_blank" style="display: inline-flex; align-items: center; gap: 4px; background: #2563EB; color: #FFFFFF; padding: 3px 10px; border-radius: 6px; font-size: 12px; font-weight: 700; text-decoration: none;">🗺️ 開啟 Day 1 具體地圖 Demo (NAVITIME/Leaflet/GPX) ➔</a></div>'
    
    if target in content and 'day1_route_map_demo.html' not in content:
        content = content.replace(target, replacement)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Linked map demo in {filepath}")
