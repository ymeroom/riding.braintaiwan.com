import sys, re

files_itinerary = [
    'C:/Users/ymero/Downloads/tokyo_fuji_cycling_itinerary_19days_v2.html',
    'd:/2026東京單車騎旅/tokyo_fuji_cycling_itinerary_19days_v2.html'
]

for path in files_itinerary:
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Fix Day 6 & Day 7 in Master Summary Table
    # Fix Day 6 row
    day6_row_new = '''                    <tr>
                        <td><strong>11/18（三）<br><span style="color:#B91C1C;">Day 6</span></strong></td>
                        <td>本棲湖浩庵（千圓逆富士） ➔ 朝霧高原牧場 ➔ 白糸之瀑 ➔ 富士宮市</td>
                        <td><strong>39.6 km</strong></td>
                        <td>+151m / -933m</td>
                        <td><strong>富士宮市區飯店</strong><br><small style="color:#64748B;">淺間大社總本社旁</small></td>
                        <td>☀️ 萬里晴空 ｜ 4.2°C ~ 15.8°C<br>降水 0.0mm ｜ 日照 9.0h</td>
                        <td>朝霧高原黃金芒草 ｜ 自海拔900m一路近千米大長下坡滑降富士宮</td>
                    </tr>'''

    # Fix Day 7 row
    day7_row_new = '''                    <tr>
                        <td><strong>11/19（四）<br><span style="color:#B91C1C;">Day 7</span></strong></td>
                        <td>富士宮 ➔ 潤井川CR ➔ 田子の浦港 ➔ 駿河灣千本松原海堤 ➔ 沼津 ➔ 三島</td>
                        <td><strong>41.3 km</strong></td>
                        <td>+32m / -118m</td>
                        <td><strong>三島市區飯店</strong><br><small style="color:#64748B;">三嶋大社周邊</small></td>
                        <td>☀️ 快晴 ｜ 2.2°C ~ 13.9°C<br>降水 0.0mm ｜ 日照 8.3h</td>
                        <td>田子之浦富士絕景 ｜ 全平緩海堤專用道（+32m/-118m），零紅綠燈狂飆沼津</td>
                    </tr>'''

    # Replace in summary table
    html = re.sub(r'<tr>\s*<td><strong>11/18（三）[\s\S]*?<\/tr>', day6_row_new, html)
    html = re.sub(r'<tr>\s*<td><strong>11/19（四）[\s\S]*?<\/tr>', day7_row_new, html)

    # 2. Fix Day 6 Card stats
    html = re.sub(
        r'<div class="day-card" id="day-6">[\s\S]*?(?=<div class="day-card" id="day-7">)',
        '''<div class="day-card" id="day-6">
            <div class="day-header">
                <span class="day-num">Day 6</span> 11/18（三）本棲湖浩庵 ➔ 朝霧高原牧場 ➔ 白糸之瀑 ➔ 富士宮市（宿 淺間大社旁飯店）
            </div>
            <div class="day-body">
                <div class="foliage-box">
                    <strong>🍂 歷史紅葉情報（朝霧高原 / 白糸之瀑）：</strong> 朝霧高原芒草金黃萬頃，白糸之瀑水氣如絹、紅葉環繞。
                </div>
                <div class="weather-box">
                    <strong>☀️ 去年實測天氣（2025/11/18 JMA 富士宮/白糸觀測所）：</strong><br>
                    天氣：<strong>萬里晴空（降水量 0.0 mm，日照時數 9.0 小時）</strong><br>
                    氣溫：最低 <strong>4.2°C</strong> ｜ 最高 <strong>15.8°C</strong> ｜ 朝霧高原下坡段風大，需著防風外套與保暖手套
                </div>
                <div class="route-stat">
                    <span>📏 里程：<strong>39.6 km</strong></span>
                    <span>⛰️ 爬升/下降：<strong>+151m / -933m</strong> (海拔 899m ➔ 115m，千米大長下坡！)</span>
                    <span>⏱️ 預估騎乘時間：<strong>2.0 ~ 2.5 小時</strong></span>
                    <span>🏨 推薦住宿：<strong>富士宮市區商務溫泉飯店</strong>（富士山本宮淺間大社總本社旁）</span>
                </div>
                <p><strong>🚲 高原俯衝與下行騎行導引：</strong></p>
                <ol style="margin-left: 20px; color: #475569; font-size: 14.5px;">
                    <li><strong>本棲湖千圓逆富士晨景：</strong> 清晨在浩庵門前欣賞平靜如鏡的千圓日幣逆富士倒影。</li>
                    <li><strong>朝霧高原暢快巡航：</strong> 沿國道 139 號與平坦側道南下，右側是廣袤的牧場牛群，左側是近在咫尺的壯麗富士西側山壁。</li>
                    <li><strong>白糸之瀑與千米長下坡：</strong> 探訪天下名瀑「白糸之瀑」，隨後沿潤井川河谷連續滑降近 800 公尺，輕鬆抵達富士宮市。</li>
                    <li><strong>富士宮市區慶祝：</strong> 參拜世界遺產「富士山本宮淺間大社」，品嚐日本 B 級美食冠軍「富士宮炒麵（富士宮やきそば）」，休整放鬆。</li>
                </ol>
            </div>
        </div>\n\n        ''',
        html
    )

    # 3. Fix Day 7 Card stats
    html = re.sub(
        r'<div class="day-card" id="day-7">[\s\S]*?(?=<div class="day-card" id="day-8">)',
        '''<div class="day-card" id="day-7">
            <div class="day-header">
                <span class="day-num">Day 7</span> 11/19（四）富士宮 ➔ 潤井川CR ➔ 田子の浦港 ➔ 駿河灣千本松原海岸海堤專用道 ➔ 沼津港 ➔ 三島
            </div>
            <div class="day-body">
                <div class="foliage-box">
                    <strong>🍂 歷史景觀情報（田子の浦港 / 駿河灣海堤）：</strong> 晴空萬里，回頭可清晰遠眺巨大雪冠富士山，海天一色。
                </div>
                <div class="weather-box">
                    <strong>☀️ 去年實測天氣（2025/11/19 JMA 三島/沼津觀測所）：</strong><br>
                    天氣：<strong>快晴（降水量 0.0 mm，日照時數 8.3 小時）</strong><br>
                    氣溫：最低 <strong>2.2°C</strong> ｜ 最高 <strong>13.9°C</strong> ｜ 沿海風勢平穩，陽光溫暖
                </div>
                <div class="route-stat">
                    <span>📏 里程：<strong>41.3 km</strong></span>
                    <span>⛰️ 爬升/下降：<strong>+32m / -118m</strong> (海拔 119m ➔ 2m ➔ 26m，平緩水岸微下坡)</span>
                    <span>⏱️ 預估騎乘時間：<strong>2.5 ~ 3.0 小時</strong></span>
                    <span>🏨 推薦住宿：<strong>三島市區飯店</strong>（三嶋大社周邊，品嚐三島名物鰻魚飯）</span>
                </div>
                <p><strong>🚲 在地車友黃金海堤走法導引：</strong></p>
                <ol style="margin-left: 20px; color: #475569; font-size: 14.5px;">
                    <li><strong>潤井川自行車道緩降：</strong> 由富士宮（海拔 119m）出發，沿著潤井川專用道一路輕鬆滑降至駿河灣出海口「田子の浦港」。</li>
                    <li><strong>切入全封閉太平洋岸自行車道：</strong> 進入「千本松原海岸堤防專用道路（縣道 380 號千本街道）」，整整 15 公里完全封閉、零汽機車干擾，右手是蔚藍太平洋，左手是千本黑松，回頭則是巨大雪白富士山！</li>
                    <li><strong>沼津港海鮮大餐：</strong> 中午抵達熱鬧的沼津港，大口享用新鮮捕撈的深海魚海鮮丼。</li>
                    <li><strong>平坦巡航至三島：</strong> 下午沿平坦道路騎抵富士山泉之都「三島市」，漫步三嶋大社與源兵衛川清泉，為隔天進駐伊豆半島做好完美準備！</li>
                </ol>
            </div>
        </div>\n\n        ''',
        html
    )

    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)

print("Successfully fixed Day 6 and Day 7 stats and cards in itinerary HTML!")
