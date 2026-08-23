import sys, re

files_itinerary = [
    'C:/Users/ymero/Downloads/tokyo_fuji_cycling_itinerary_19days_v2.html',
    'd:/2026東京單車騎旅/tokyo_fuji_cycling_itinerary_19days_v2.html'
]

for path in files_itinerary:
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()

    # Update hotel bike checklist
    html = re.sub(
        r'<li><strong>11/23 Izu Kansya \(伊豆観舎\)<\/strong>.*?<\/li>',
        '<li><strong>11/23 guest house MARUYA</strong>：熱海銀座町7-8，文青設計旅舍，步行3分鐘直達海灘看花火，設室內/玄關單車停放空間</li>',
        html
    )

    # Update summary table Day 11 and Day 12 rows
    d11_row = '''                    <tr>
                        <td><strong>11/23（一）<br><span style="color:#B91C1C;">Day 11</span></strong><br><span class="badge badge-mod" style="font-size:10px;">勤勞感謝日</span><br><span class="badge-booked">✅ 🏨 已訂房</span></td>
                        <td>Apt南熱海 ➔ 熱海梅園紅葉祭 ➔ 來宮神社 ➔ 熱海銀座 ➔ <strong>晚上 20:20 熱海海上花火大會</strong></td>
                        <td><strong>12.2 km</strong></td>
                        <td>+250m / -244m</td>
                        <td><strong>guest house MARUYA</strong><br><a href="https://www.google.com/maps/search/?api=1&query=%E9%9D%99%E5%B2%A1%E7%9C%8C%E7%86%B1%E6%B5%B7%E5%B8%82%E9%8A%80%E5%BA%A7%E7%94%BA7-8+guest+house+MARUYA" target="_blank" class="map-link">📍 靜岡縣熱海市銀座町7-8 ↗</a></td>
                        <td>☀️ 快晴 ｜ 10.4°C ~ 19.7°C<br>降水 0.0mm ｜ 日照 9.7h</td>
                        <td>🎆 <strong>熱海海上煙火祭特設日</strong> ｜ <strong>入住熱海銀座，步行 3 分鐘直達海灘特等席！散場零塞車</strong></td>
                    </tr>'''

    d12_row = '''                    <tr>
                        <td><strong>11/24（二）<br><span style="color:#B91C1C;">Day 12</span></strong></td>
                        <td>熱海銀座 ➔ 縣道740號柑橘道 ➔ 小田原城 ➔ 湘南海岸防風林 ➔ 江之島</td>
                        <td><strong>63.2 km</strong></td>
                        <td>+323m / -328m</td>
                        <td><strong>江之島 / 藤澤市區飯店</strong></td>
                        <td>☀️ 快晴 ｜ 8.9°C ~ 18.0°C<br>降水 0.0mm ｜ 日照 9.4h</td>
                        <td>灌籃高手湘南海岸 ｜ 熱海直接出發，小田原後一馬平川相模灣平路直達江之島</td>
                    </tr>'''

    html = re.sub(r'<tr>\s*<td><strong>11/23（一）[\s\S]*?<\/tr>', d11_row, html)
    html = re.sub(r'<tr>\s*<td><strong>11/24（二）[\s\S]*?<\/tr>', d12_row, html)

    # Update Day 11 Card
    html = re.sub(
        r'<div class="day-card" id="day-11">[\s\S]*?(?=<div class="day-card" id="day-12">)',
        '''<div class="day-card" id="day-11">
            <div class="day-header">
                <span class="day-num">Day 11</span> 11/23（一・勤勞感謝日）Apt南熱海 ➔ 熱海梅園最晚紅葉 ➔ 來宮神社 ➔ 熱海銀座 ➔ 晚上 20:20 熱海海上花火大會（宿 guest house MARUYA） <span class="badge-booked">✅ 🏨 已訂房</span>
            </div>
            <div class="day-body">
                <div class="foliage-box">
                    <strong>🍂 歷史紅葉與節慶情報（熱海梅園 / 海上花火）：</strong> <strong>熱海梅園日本最晚紅葉見頃！</strong> <strong>🎆 晚上 20:20-20:40 熱海海上花火大會特設場！</strong>
                </div>
                <div class="weather-box">
                    <strong>☀️ 去年實測天氣（2025/11/23 JMA 網代/熱海觀測所）：</strong><br>
                    天氣：<strong>快晴（降水量 0.0 mm，日照時數 9.7 小時）</strong><br>
                    氣溫：最低 <strong>10.4°C</strong> ｜ 最高 <strong>19.7°C</strong> ｜ 氣候溫和宜人
                </div>
                <div class="route-stat">
                    <span>📏 里程：<strong>12.2 km</strong> (超休閒花火漫遊日)</span>
                    <span>⛰️ 爬升/下降：<strong>+250m / -244m</strong> (輕鬆無負擔)</span>
                    <span>⏱️ 預估騎乘時間：<strong>1.0 ~ 1.5 小時</strong></span>
                    <span>🏨 鎖定住宿：<strong>guest house MARUYA</strong> <a href="https://www.google.com/maps/search/?api=1&query=%E9%9D%99%E5%B2%A1%E7%9C%8C%E7%86%B1%E6%B5%B7%E5%B8%82%E9%8A%80%E5%BA%A7%E7%94%BA7-8+guest+house+MARUYA" target="_blank" class="map-link">📍 靜岡縣熱海市銀座町7-8 ↗</a></span>
                </div>
                <p><strong>🚲 神仙級花火動線實戰導引：</strong></p>
                <ol style="margin-left: 20px; color: #475569; font-size: 14.5px;">
                    <li><strong>日間悠閒賞楓與參拜：</strong> 由南熱海下多賀出發，沿海岸平緩北上，前往「熱海梅園」欣賞日本最遲的紅葉祭與來宮神社兩千年大楠神木。</li>
                    <li><strong>下午 15:00 進駐熱海銀座 MARUYA：</strong> 抵達熱海市中心熱海銀座商店街 7-8 辦理入住，將單車與行李妥善安置在旅舍。</li>
                    <li><strong>晚上 20:20 海上花火特等席：</strong> 步行僅 3 分鐘（250m）直接抵達「熱海 Sun Beach 陽光海灘」，享受天然扇形海灣的高空巨型煙火與音浪回音！散場步行 3 分鐘直接回房休息或在銀座商店街居酒屋小酌，徹底免除所有交通癱瘓困擾！</li>
                </ol>
            </div>
        </div>\n\n        ''',
        html
    )

    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)

print("Updated itinerary HTML with guest house MARUYA!")
