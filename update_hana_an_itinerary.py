import sys, re

files_itinerary = [
    'C:/Users/ymero/Downloads/tokyo_fuji_cycling_itinerary_19days_v2.html',
    'd:/2026東京單車騎旅/tokyo_fuji_cycling_itinerary_19days_v2.html'
]

for path in files_itinerary:
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Update Master Summary Table for Day 15, Day 16, Day 17
    day15_row_new = '''                    <tr>
                        <td><strong>11/27（五）<br><span style="color:#B91C1C;">Day 15</span></strong><br><span class="badge-booked">✅ 🏨 已訂房</span></td>
                        <td>台場 ➔ 葛西臨海公園 ➔ 中川水岸綠道 ➔ 柴又 ➔ 葛飾金町</td>
                        <td><strong>27.6 km</strong></td>
                        <td>+7m / -15m</td>
                        <td><strong>花庵旅舍 (Hostel Hana An)</strong><br><a href="https://www.google.com/maps/search/?api=1&query=%E6%9D%B1%E4%BA%AC%E9%83%BD%E8%91%9B%E9%A3%BE%E5%8D%80%E9%87%91%E7%94%BA4-23-11+%E8%8A%B1%E5%BA%B5%E6%97%85%E8%88%8D" target="_blank" class="map-link">📍 東京都葛飾區金町4-23-11 ↗</a></td>
                        <td>☀️ 晴/多雲 ｜ 7.3°C ~ 16.2°C<br>降水 0.0mm ｜ 日照 3.7h</td>
                        <td>葛西海風與中川秋草 ｜ 避開市中心擁擠人潮，入住水元公園旁清幽下町旅舍</td>
                    </tr>'''

    day16_row_new = '''                    <tr>
                        <td><strong>11/28（六）<br><span style="color:#B91C1C;">Day 16</span></strong><br><span class="badge-booked">✅ 🏨 已訂房</span></td>
                        <td>金町出發 ➔ <strong>【輕裝免行李】</strong> 江戶川CR / 荒川 ➔ 小江戶川越 / 葛飾老街 ➔ 返回金町</td>
                        <td><strong>35.0 ~ 50.0 km</strong></td>
                        <td>+25m / -25m</td>
                        <td><strong>花庵旅舍 (Hostel Hana An)</strong><br><small style="color:#64748B;">連住第2晚・免換飯店</small></td>
                        <td>☀️ 快晴 ｜ 8.4°C ~ 19.8°C<br>降水 0.0mm ｜ 日照 9.1h</td>
                        <td>🔥 <strong>江戶老街與水岸金秋</strong> ｜ 週末免收行李輕裝暢快巡航，夜晚悠閒漫步下町居酒屋</td>
                    </tr>'''

    day17_row_new = '''                    <tr>
                        <td><strong>11/29（日）<br><span style="color:#B91C1C;">Day 17</span></strong></td>
                        <td>金町退房 ➔ <strong>水元公園（萬棵水杉黃金森林見頃）</strong> ➔ 柴又帝釋天 ➔ 淺草/上野</td>
                        <td><strong>16.6 ~ 25.0 km</strong></td>
                        <td>+9m / -9m</td>
                        <td><strong>淺草 / 上野 / 東京市區飯店</strong></td>
                        <td>☀️ 晴/多雲 ｜ 9.0°C ~ 15.3°C<br>降水 0.0mm ｜ 日照 5.2h</td>
                        <td>🔥 <strong>水元公園水杉見頃最高峰</strong> ｜ 清晨5分鐘直達無人水杉金黃森林，極致震撼</td>
                    </tr>'''

    html = re.sub(r'<tr>\s*<td><strong>11/27（五）[\s\S]*?<\/tr>', day15_row_new, html)
    html = re.sub(r'<tr>\s*<td><strong>11/28（六）[\s\S]*?<\/tr>', day16_row_new, html)
    html = re.sub(r'<tr>\s*<td><strong>11/29（日）[\s\S]*?<\/tr>', day17_row_new, html)

    # 2. Update Day 15 & Day 16 Card Details
    day15_card_new = '''<div class="day-card" id="day-15">
            <div class="day-header">
                <span class="day-num">Day 15</span> 11/27（五）台場 ➔ 葛西臨海公園 ➔ 中川水岸自行車道 ➔ 柴又 ➔ 葛飾金町（宿 花庵旅舍 連住第 1 晚） <span class="badge-booked">✅ 🏨 已訂房</span>
            </div>
            <div class="day-body">
                <div class="foliage-box">
                    <strong>🍂 歷史景觀情報（葛西臨海公園 / 葛飾下町）：</strong> 葛西海濱芒草金黃，東京灣天際線晴朗遼闊。
                </div>
                <div class="weather-box">
                    <strong>☀️ 去年實測天氣（2025/11/27 JMA 江戶川觀測所）：</strong><br>
                    天氣：<strong>晴/多雲（降水量 0.0 mm，日照時數 3.7 小時）</strong><br>
                    氣溫：最低 <strong>7.3°C</strong> ｜ 最高 <strong>16.2°C</strong> ｜ 水岸平原無風好騎
                </div>
                <div class="route-stat">
                    <span>📏 里程：<strong>27.6 km</strong> (超平坦水岸愜意騎)</span>
                    <span>⛰️ 爬升/下降：<strong>+7m / -15m</strong> (全日平路)</span>
                    <span>⏱️ 預估騎乘時間：<strong>1.5 ~ 2.0 小時</strong></span>
                    <span>🏨 鎖定住宿：<strong>花庵旅舍 (Hostel Hana An)</strong> <a href="https://www.google.com/maps/search/?api=1&query=%E6%9D%B1%E4%BA%AC%E9%83%BD%E8%91%9B%E9%A3%BE%E5%8D%80%E9%87%91%E7%94%BA4-23-11+%E8%8A%B1%E5%BA%B5%E6%97%85%E8%88%8D" target="_blank" class="map-link">📍 東京都葛飾區金町4-23-11 ↗</a></span>
                </div>
                <p><strong>🚲 在地水岸下町騎行導引：</strong></p>
                <ol style="margin-left: 20px; color: #475569; font-size: 14.5px;">
                    <li><strong>東京灣水岸暢快巡航：</strong> 由台場出發，沿平整開闊的灣岸專用道穿越「葛西臨海公園」，眺望東京灣與巨大的鑽石與花大摩天輪。</li>
                    <li><strong>中川與江戶川幽靜綠道：</strong> 切入中川水岸自行車道，避開市區繁雜車潮，一路平整北上抵達充滿江戶人情味的葛飾區。</li>
                    <li><strong>入住金町花庵旅舍：</strong> 下午入住位於寧靜街區的「花庵旅舍（金町4-23-11）」，單車進出方便，走路或騎車 5 分鐘即可抵達柴又老街品嚐草糰子與鰻魚飯！</li>
                </ol>
            </div>
        </div>\n\n        '''

    day16_card_new = '''<div class="day-card" id="day-16">
            <div class="day-header">
                <span class="day-num">Day 16</span> 11/28（六）金町出發 ➔ 江戶川自行車道 / 荒川 ➔ 輕裝漫遊小江戶 ➔ 返回金町（宿 花庵旅舍 連住第 2 晚） <span class="badge-booked">✅ 🏨 已訂房</span>
            </div>
            <div class="day-body">
                <div class="foliage-box">
                    <strong>🍂 歷史紅葉情報（江戶川沿線 / 川越喜多院）：</strong> <strong>見頃最盛期！</strong> 江戶古寺紅葉與藏造老街黑瓦交織。
                </div>
                <div class="weather-box">
                    <strong>☀️ 去年實測天氣（2025/11/28 JMA 葛飾/埼玉觀測所）：</strong><br>
                    天氣：<strong>快晴（降水量 0.0 mm，日照時數 9.1 小時）</strong><br>
                    氣溫：最低 <strong>8.4°C</strong> ｜ 最高 <strong>19.8°C</strong> ｜ 週末陽光溫暖
                </div>
                <div class="route-stat">
                    <span>📏 里程：<strong>35.0 ~ 50.0 km</strong> (輕裝無負重漫騎)</span>
                    <span>⛰️ 爬升/下降：<strong>+25m / -25m</strong> (一馬平川)</span>
                    <span>⏱️ 預估騎乘時間：<strong>2.5 ~ 3.0 小時</strong></span>
                    <span>🏨 鎖定住宿：<strong>花庵旅舍 (Hostel Hana An)</strong>（連住第 2 晚，免打包行李！）</span>
                </div>
                <p><strong>🚲 輕裝無行李水岸探秘導引：</strong></p>
                <ol style="margin-left: 20px; color: #475569; font-size: 14.5px;">
                    <li><strong>完全免打包行李的極致輕鬆：</strong> 週末這天所有行李都安心留在金町花庵旅舍，單車以最輕快的純車狀態出發！</li>
                    <li><strong>江戶川與水岸綠道暢遊：</strong> 沿著寬闊平整的江戶川專用車道漫騎，或順訪三鄉、流山白壁古鎮，享受遠離都會喧囂的純粹騎行樂趣。</li>
                    <li><strong>傍晚返回金町休整：</strong> 傍晚回到花庵旅舍，在金町在地商店街品嚐熱騰騰的日式拉麵與居酒屋串燒。</li>
                </ol>
            </div>
        </div>\n\n        '''

    html = re.sub(r'<div class="day-card" id="day-15">[\s\S]*?(?=<div class="day-card" id="day-16">)', day15_card_new, html)
    html = re.sub(r'<div class="day-card" id="day-16">[\s\S]*?(?=<div class="day-card" id="day-17">)', day16_card_new, html)

    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)

print("Successfully updated Day 15 & Day 16 with Hostel Hana An in Kanamachi!")
