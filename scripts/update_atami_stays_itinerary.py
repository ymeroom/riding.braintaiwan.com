import sys, re

files_itinerary = [
    'C:/Users/ymero/Downloads/tokyo_fuji_cycling_itinerary_19days_v2.html',
    'd:/2026東京單車騎旅/tokyo_fuji_cycling_itinerary_19days_v2.html'
]

for path in files_itinerary:
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Update Master Summary Table for Day 10, Day 11, Day 12
    # Day 10 row
    day10_row_new = '''                    <tr>
                        <td><strong>11/22（日）<br><span style="color:#B91C1C;">Day 10</span></strong><br><span class="badge badge-mod" style="font-size:10px;">三連休中日</span></td>
                        <td>伊東 ➔ 宇佐美 ➔ 避開危險隧道（走網代舊街） ➔ 南熱海・下多賀</td>
                        <td><strong>15.1 km</strong></td>
                        <td>+330m / -326m</td>
                        <td><strong>Apt南熱海-網代</strong><br><small style="color:#64748B;">下多賀440（長浜海灘海景）</small></td>
                        <td>☀️ 快晴 ｜ 7.6°C ~ 19.2°C<br>降水 0.0mm ｜ 日照 9.3h</td>
                        <td>🔥 <strong>網代港海景第一排</strong> ｜ 避開三連休熱海塞車潮，悠閒入住南熱海海景公寓</td>
                    </tr>'''

    # Day 11 row
    day11_row_new = '''                    <tr>
                        <td><strong>11/23（一）<br><span style="color:#B91C1C;">Day 11</span></strong><br><span class="badge badge-mod" style="font-size:10px;">勤勞感謝日</span></td>
                        <td>南熱海換宿 ➔ 熱海梅園紅葉祭 ➔ <strong>晚上 20:20 熱海海上花火大會</strong></td>
                        <td><strong>17.7 km</strong></td>
                        <td>+340m / -336m</td>
                        <td><strong>Izu Kansya</strong><br><small style="color:#64748B;">下多賀1473-11（南熱海）</small></td>
                        <td>☀️ 快晴 ｜ 10.4°C ~ 19.7°C<br>降水 0.0mm ｜ 日照 9.7h</td>
                        <td>🎆 <strong>熱海海上煙火祭特設日</strong> ｜ 白天賞日本最晚紅葉，晚上直擊震撼高空煙火</td>
                    </tr>'''

    # Day 12 row
    day12_row_new = '''                    <tr>
                        <td><strong>11/24（二）<br><span style="color:#B91C1C;">Day 12</span></strong></td>
                        <td>南熱海 ➔ 縣道740號柑橘道 ➔ 小田原城 ➔ 湘南海岸防風林 ➔ 江之島</td>
                        <td><strong>68.4 km</strong></td>
                        <td>+302m / -303m</td>
                        <td><strong>江之島 / 藤澤市區飯店</strong></td>
                        <td>☀️ 快晴 ｜ 8.9°C ~ 18.0°C<br>降水 0.0mm ｜ 日照 9.4h</td>
                        <td>灌籃高手湘南海岸 ｜ 小田原後一馬平川相模灣平路，順暢直達江之島</td>
                    </tr>'''

    # Replace in summary table
    html = re.sub(r'<tr>\s*<td><strong>11/22（日）[\s\S]*?<\/tr>', day10_row_new, html)
    html = re.sub(r'<tr>\s*<td><strong>11/23（一）[\s\S]*?<\/tr>', day11_row_new, html)
    html = re.sub(r'<tr>\s*<td><strong>11/24（二）[\s\S]*?<\/tr>', day12_row_new, html)

    # 2. Update Day 10 Card details
    day10_card_new = '''<div class="day-card" id="day-10">
            <div class="day-header">
                <span class="day-num">Day 10</span> 11/22（日・三連休中日）伊東 ➔ 避開危險長隧道（網代港舊街道）➔ 南熱海（宿 Apt南熱海-網代）
            </div>
            <div class="day-body">
                <div class="foliage-box">
                    <strong>🍂 歷史景觀情報（南熱海・網代灣）：</strong> 溫暖海風吹拂，相模灣水面湛藍，沿岸柑橘結實纍纍。
                </div>
                <div class="weather-box">
                    <strong>☀️ 去年實測天氣（2025/11/22 JMA 熱海觀測所）：</strong><br>
                    天氣：<strong>快晴（降水量 0.0 mm，日照時數 9.3 小時）</strong><br>
                    氣溫：最低 <strong>7.6°C</strong> ｜ 最高 <strong>19.2°C</strong> ｜ 沿海極度溫暖舒適
                </div>
                <div class="route-stat">
                    <span>📏 里程：<strong>15.1 km</strong> (避開塞車極短程休閒日)</span>
                    <span>⛰️ 爬升/下降：<strong>+330m / -326m</strong></span>
                    <span>⏱️ 預估騎乘時間：<strong>1.0 ~ 1.5 小時</strong></span>
                    <span>🏨 推薦住宿：<strong>Apt南熱海-網代</strong>（靜岡縣熱海市下多賀440，長浜海灘海景第一排）</span>
                </div>
                <p><strong>🚲 在地車友避開三連休車潮實戰導引：</strong></p>
                <ol style="margin-left: 20px; color: #475569; font-size: 14.5px;">
                    <li><strong>果斷繞開國道 135 號連環暗黑隧道：</strong> 在宇佐美與網代路段，切入在地漁港舊生活道，完全避開狹窄隧道與大型車輛。</li>
                    <li><strong>早早抵達南熱海入住海景公寓：</strong> 15 公里輕鬆短程，下午 13:30 即可入住「Apt南熱海-網代（下多賀440）」，在陽台欣賞長浜海灘的寧靜海景與落日。</li>
                    <li><strong>三連休避坑智慧：</strong> 避開熱海市中心擠爆的車流，在安靜的南熱海海鮮餐廳品嚐網代名物「竹筴魚生魚片定食（アジフライ）」。</li>
                </ol>
            </div>
        </div>\n\n        '''
    html = re.sub(r'<div class="day-card" id="day-10">[\s\S]*?(?=<div class="day-card" id="day-11">)', day10_card_new, html)

    # 3. Update Day 11 Card details
    day11_card_new = '''<div class="day-card" id="day-11">
            <div class="day-header">
                <span class="day-num">Day 11</span> 11/23（一・勤勞感謝日）南熱海換宿 ➔ 熱海梅園最晚紅葉祭 ➔ 晚上 20:20 熱海海上花火大會（宿 Izu Kansya）
            </div>
            <div class="day-body">
                <div class="foliage-box">
                    <strong>🍂 歷史紅葉情報（熱海梅園）：</strong> <strong>見頃最盛期！</strong> 全日本最晚紅葉祭，深紅楓葉與早開白梅同框奇蹟。
                </div>
                <div class="weather-box">
                    <strong>☀️ 去年實測天氣（2025/11/23 JMA 熱海觀測所）：</strong><br>
                    天氣：<strong>快晴（降水量 0.0 mm，日照時數 9.7 小時）</strong><br>
                    氣溫：最低 <strong>10.4°C</strong> ｜ 最高 <strong>19.7°C</strong> ｜ 晚上海邊觀看煙火微涼需薄外套
                </div>
                <div class="route-stat">
                    <span>📏 里程：<strong>17.7 km</strong> (輕裝探索與煙火機動)</span>
                    <span>⛰️ 爬升/下降：<strong>+340m / -336m</strong></span>
                    <span>⏱️ 預估騎乘時間：<strong>1.5 ~ 2.0 小時</strong></span>
                    <span>🏨 推薦住宿：<strong>Izu Kansya</strong>（靜岡縣熱海市下多賀1473-11，南熱海溫泉聚落）</span>
                </div>
                <p><strong>🚲 熱海花火大會神級機動玩法：</strong></p>
                <ol style="margin-left: 20px; color: #475569; font-size: 14.5px;">
                    <li><strong>南熱海短距換宿：</strong> 上午由下多賀440移步至「Izu Kansya（下多賀1473-11）」，卸下行李。</li>
                    <li><strong>日間熱海名勝巡禮：</strong> 輕裝前往「熱海梅園」欣賞日本最晚紅葉祭、來宮神社 2000 年大楠樹祈福、熱海城俯瞰相模灣。</li>
                    <li><strong>🎆 晚上 20:20～20:40 直擊「熱海海上花火大會」：</strong>
                        <br>・【交通神招】：可騎單車或自伊豆多賀站搭乘 JR 伊東線（僅 1 站 5 分鐘）直達熱海陽光海灘第一排，欣賞震撼回音的巨型海上高空煙火！
                        <br>・【免塞車離場】：煙火結束後搭電車或騎車 15 分鐘輕鬆回到南熱海 Izu Kansya 泡湯安歇，完全不受熱海市區大塞車影響！
                    </li>
                </ol>
            </div>
        </div>\n\n        '''
    html = re.sub(r'<div class="day-card" id="day-11">[\s\S]*?(?=<div class="day-card" id="day-12">)', day11_card_new, html)

    # 4. Update Day 12 Card details
    day12_card_new = '''<div class="day-card" id="day-12">
            <div class="day-header">
                <span class="day-num">Day 12</span> 11/24（二）南熱海 ➔ 避開江之浦隧道（縣道740號柑橘道）➔ 小田原城 ➔ 湘南海岸 ➔ 江之島
            </div>
            <div class="day-body">
                <div class="foliage-box">
                    <strong>🍂 歷史紅葉情報（小田原城 / 湘南海岸）：</strong> 小田原城護城河楓紅倒影，湘南海岸深邃海藍與烏帽子岩。
                </div>
                <div class="weather-box">
                    <strong>☀️ 去年實測天氣（2025/11/24 JMA 小田原/江之島觀測所）：</strong><br>
                    天氣：<strong>快晴（降水量 0.0 mm，日照時數 9.4 小時）</strong><br>
                    氣溫：最低 <strong>8.9°C</strong> ｜ 最高 <strong>18.0°C</strong> ｜ 相模灣海風和煦，順暢巡航
                </div>
                <div class="route-stat">
                    <span>📏 里程：<strong>68.4 km</strong></span>
                    <span>⛰️ 爬升/下降：<strong>+302m / -303m</strong> (小田原過後一馬平川！)</span>
                    <span>⏱️ 預估騎乘時間：<strong>3.5 ~ 4.0 小時</strong></span>
                    <span>🏨 推薦住宿：<strong>江之島 / 藤澤市區飯店</strong>（品嚐江之島吻仔魚海鮮丼）</span>
                </div>
                <p><strong>🚲 騎行路線導引：</strong></p>
                <ol style="margin-left: 20px; color: #475569; font-size: 14.5px;">
                    <li><strong>南熱海出發切入縣道 740 號：</strong> 由 Izu Kansya 出發穿過熱海市區，至真鶴站前左轉切入「縣道 740 號柑橘景觀道」，徹底避開國道 135 號險惡的江之浦暗黑隧道，俯瞰相模灣蔚藍海景與蜜柑山坡。</li>
                    <li><strong>小田原城休整享用午餐：</strong> 參觀難攻不落的小田原城天守閣與護城河楓紅，品嚐早川漁港酥脆炸竹筴魚。</li>
                    <li><strong>湘南海岸順暢平路衝刺：</strong> 小田原過後沿國道 1 號與湘南防風林自行車道一馬平川，一路巡航至茅崎烏帽子岩，傍晚抵達江之島！</li>
                </ol>
            </div>
        </div>\n\n        '''
    html = re.sub(r'<div class="day-card" id="day-12">[\s\S]*?(?=<div class="day-card" id="day-13">)', day12_card_new, html)

    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)

print("Successfully updated Day 10, Day 11, Day 12 in itinerary HTML!")
