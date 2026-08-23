import sys, re

files_itinerary = [
    'C:/Users/ymero/Downloads/tokyo_fuji_cycling_itinerary_19days_v2.html',
    'd:/2026東京單車騎旅/tokyo_fuji_cycling_itinerary_19days_v2.html'
]

btn_html = '''<a href="tokyo_cycling_19days_map_demo.html" target="_blank" class="meta-tag" style="background: #2563EB; color: #FFFFFF; font-weight: 700; text-decoration: none;">🗺️ 19日 全路線互動地圖與標高 Demo ➔</a>
            <a href="suno_cycling_soundtrack_19days.html" target="_blank" class="meta-tag" style="background: #F59E0B; color: #1E293B; font-weight: 700; text-decoration: none;">🎵 19日 Suno AI 音樂詞庫 ➔</a>'''

for path in files_itinerary:
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()

    # Update header meta tags
    html = re.sub(r'<a href="suno_cycling_soundtrack_19days\.html"[\s\S]*?<\/a>', btn_html, html)

    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)

print("Linked 19-day map demo in itinerary HTML header!")
