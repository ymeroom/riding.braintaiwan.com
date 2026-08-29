import io
with io.open('index.html', 'r', encoding='utf-8') as f: 
    html = f.read()

# Replace existing link text and append the new Google Maps button
html = html.replace('🗺️ 19日 全路線互動地圖與標高 Demo ➔</a>', '🗺️ 19日 全路線地圖 (NAVITIME) ➔</a>\n            <a href="google_maps_19days.html" target="_blank" class="meta-tag" style="background: #10B981; color: #FFFFFF; font-weight: 700; text-decoration: none; box-shadow: 0 0 10px rgba(16, 185, 129, 0.4);">🗺️ 19日 全行程路線 (Google地圖版) ➔</a>')

with io.open('index.html', 'w', encoding='utf-8') as f: 
    f.write(html)
