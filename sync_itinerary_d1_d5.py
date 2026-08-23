import sys, re

files_itinerary = [
    'C:/Users/ymero/Downloads/tokyo_fuji_cycling_itinerary_19days_v2.html',
    'd:/2026東京單車騎旅/tokyo_fuji_cycling_itinerary_19days_v2.html'
]

for path in files_itinerary:
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()

    # Update Day 1, 2, 3, 4 in summary table
    d1_row = '''                    <tr>
                        <td><strong>11/13（五）<br><span style="color:#B91C1C;">Day 1</span></strong><br><span class="badge-booked">✅ 🏨 已訂房</span></td>
                        <td>秋葉原 ➔ 銀座/品川 ➔ 國道15號 ➔ 六鄉橋 ➔ 多摩川CR ➔ 府中(50km) ➔ 高尾山口</td>
                        <td><strong>89.7 km</strong></td>
                        <td>+243m / -62m</td>
                        <td><strong>Mt. Takao Base Camp</strong><br><a href="https://www.google.com/maps/search/?api=1&query=%E6%9D%B1%E4%BA%AC%E9%83%BD%E5%85%AB%E7%8E%8B%E5%AD%90%E5%B8%82%E9%AB%98%E5%B0%BE%E7%94%BA1799-3+Mt.Takao+Base+Camp" target="_blank" class="map-link">📍 東京都八王子市高尾町1799-3 ↗</a></td>
                        <td>☀️ 晴 ｜ 11.8°C ~ 19.6°C<br>降水 0.0mm ｜ 日照 9.4h</td>
                        <td>多摩水岸秋芒 ｜ 雙專用道全程零紅綠燈直達高尾山腳（海拔190m）</td>
                    </tr>'''

    d2_row = '''                    <tr>
                        <td><strong>11/14（六）<br><span style="color:#B91C1C;">Day 2</span></strong><br><span class="badge-booked">✅ 🏨 已訂房</span></td>
                        <td>高尾山口 ➔ <strong>甲州街道(國道20)</strong> ➔ 大垂水峠(392m) ➔ 相模湖 ➔ 縣道35秋山街道 ➔ 都留</td>
                        <td><strong>61.0 km</strong></td>
                        <td>+1121m / -830m</td>
                        <td><strong>ビジネス旅館 由加利</strong><br><a href="https://www.google.com/maps/search/?api=1&query=%E5%B1%B1%E6%A2%A8%E7%9C%8C%E9%83%BD%E7%95%99%E5%B8%82%E4%B8%8A%E8%B0%B71%E4%B8%81%E7%9B%AE3-4+%E7%94%B1%E5%8A%A0%E5%88%A9%E6%97%85%E9%A4%A8" target="_blank" class="map-link">📍 山梨縣都留市上谷1丁目3-4 ↗</a></td>
                        <td>☀️ 快晴 ｜ 7.8°C ~ 17.2°C<br>降水 0.0mm ｜ 日照 8.9h</td>
                        <td>秋山溪谷初紅 ｜ 清晨避開大車，秋山街道35km零貨車幽靜溪谷</td>
                    </tr>'''

    d3_row = '''                    <tr>
                        <td><strong>11/15（日）<br><span style="color:#B91C1C;">Day 3</span></strong><br><span class="badge-booked">✅ 🏨 已訂房</span></td>
                        <td>由加利 ➔ <strong>【晴】山中湖完整環湖+忍野 / 【陰雨】新倉山五重塔直達</strong> ➔ 河口湖</td>
                        <td><strong>22.2 ~ 70.5 km</strong></td>
                        <td>+532m ~ +1030m</td>
                        <td><strong>Orange Cabin Inn</strong><br><a href="https://www.google.com/maps/search/?api=1&query=%E5%B1%B1%E6%A2%A8%E7%9C%8C%E5%8D%97%E9%83%BD%E7%95%99%E9%83%A1%E5%84%82%E5%A3%AB%E6%B2%B3%E5%8F%A3%E6%B9%96%E7%94%BA%E6%B2%B3%E5%8F%A31916-3+Orange+Cabin+Inn" target="_blank" class="map-link">📍 山梨縣富士河口湖町河口1916-3 ↗</a></td>
                        <td>☀️ 快晴 ｜ 4.5°C ~ 15.1°C<br>降水 0.0mm ｜ 日照 9.6h</td>
                        <td>🔥 <strong>雙湖見頃最盛期</strong> ｜ 晴天環山中湖、陰雨天直取五重塔，晚賞夜楓點燈</td>
                    </tr>'''

    d4_row = '''                    <tr>
                        <td><strong>11/16（一）<br><span style="color:#B91C1C;">Day 4</span></strong></td>
                        <td>清晨紅葉迴廊 ➔ <strong>【去過山中湖】爬五重塔往西騎本棲湖 / 【未去】補騎山中湖 / 附近漫遊</strong></td>
                        <td><strong>30.0 ~ 52.7 km</strong></td>
                        <td>+250m ~ +629m</td>
                        <td><strong>本棲湖 民宿 浩庵 / 機動</strong><br><small style="color:#64748B;">（身延町中之倉2926 / 河口湖）</small></td>
                        <td>☀️ 快晴 ｜ 3.2°C ~ 14.6°C<br>降水 0.0mm ｜ 日照 9.1h</td>
                        <td>🔥 <strong>紅葉迴廊見頃最高峰</strong> ｜ 依前日天候靈活啟動分支，西進逆富士或深度漫遊</td>
                    </tr>'''

    html = re.sub(r'<tr>\s*<td><strong>11/13（五）[\s\S]*?<\/tr>', d1_row, html)
    html = re.sub(r'<tr>\s*<td><strong>11/14（六）[\s\S]*?<\/tr>', d2_row, html)
    html = re.sub(r'<tr>\s*<td><strong>11/15（日）[\s\S]*?<\/tr>', d3_row, html)
    html = re.sub(r'<tr>\s*<td><strong>11/16（一）[\s\S]*?<\/tr>', d4_row, html)

    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)

print("Updated itinerary HTML with exact Day 1-5 logic!")
