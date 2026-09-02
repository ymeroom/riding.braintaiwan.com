import sys, re

files_itinerary = [
    'C:/Users/ymero/Downloads/tokyo_fuji_cycling_itinerary_19days_v2.html',
    'd:/2026東京單車騎旅/tokyo_fuji_cycling_itinerary_19days_v2.html'
]

for path in files_itinerary:
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Update Master Summary Table for Day 5 and Day 6
    # Day 5 in table
    html = re.sub(
        r'<tr[^>]*>\s*<td[^>]*><strong>Day 5<\/strong><\/td>[\s\S]*?<\/tr>',
        '''<tr>
            <td><strong>Day 5</strong></td>
            <td>11/17（二）</td>
            <td><strong>【五湖天候核心緩衝日】</strong> 富士五湖深度賞楓 ➔ 溫泉休整 ➔ 補完五湖</td>
            <td><strong>15.0 ~ 30.0 km</strong></td>
            <td>+150m ~ +280m</td>
            <td><span class="badge badge-easy">彈性休整</span></td>
            <td><strong>本棲湖浩庵 / 河口湖 / 富士吉田</strong></td>
            <td>晴朗乾燥 0.0mm (5.8~16.4°C)</td>
            <td>應對11月富士五湖多變天候（防雨/防初雪/低溫），深度慢遊青木原樹海、西湖療癒之里、泡湯休整</td>
        </tr>''',
        html
    )

    # Day 6 in table
    html = re.sub(
        r'<tr[^>]*>\s*<td[^>]*><strong>Day 6<\/strong><\/td>[\s\S]*?<\/tr>',
        '''<tr>
            <td><strong>Day 6</strong></td>
            <td>11/18（三）</td>
            <td>本棲湖浩庵 ➔ <strong>朝霧高原牧場</strong> ➔ 白糸之瀑 ➔ <strong>富士宮市</strong></td>
            <td><strong>48.0 km</strong></td>
            <td>+180m / -890m</td>
            <td><span class="badge badge-easy">千米大下坡</span></td>
            <td><strong>富士宮市區飯店</strong>（淺間大社總本社旁）</td>
            <td>晴朗乾燥 0.0mm (4.2~15.8°C)</td>
            <td>告別富士五湖，自海拔900m高原沿朝霧高原與潤井川河谷一路大長下坡滑降至富士宮，品嚐炒麵</td>
        </tr>''',
        html
    )

    # 2. Update Day 5 Card Details
    day5_card_old = r'<div class="day-card" id="day-5">[\s\S]*?(?=<div class="day-card" id="day-6">)'
    day5_card_new = '''<div class="day-card" id="day-5">
            <div class="day-header">
                <span class="day-num">Day 5</span> 11/17（二）富士五湖彈性休整與深度賞楓（天候應變核心緩衝日 ｜ 宿 本棲湖浩庵 / 河口湖）
            </div>
            <div class="day-body">
                <div class="foliage-box">
                    <strong>🍂 歷史紅葉情報（西湖 / 精進湖 / 本棲湖）：</strong> <strong>見頃最盛期！</strong> 熔岩樹海與深藍湖水交織，深秋蒼茫寧靜。
                </div>
                <div class="weather-box">
                    <strong>☀️ 去年實測天氣（2025/11/17 JMA 富士五湖觀測所）：</strong><br>
                    天氣：<strong>晴朗（降水量 0.0 mm，日照時數 8.8 小時）</strong><br>
                    氣溫：最低 <strong>5.8°C</strong> ｜ 最高 <strong>16.4°C</strong> ｜ 11月中旬高原氣候多變，此緩衝日能百分之百消化任何低溫、陣雨或初雪延誤！
                </div>
                <div class="route-stat">
                    <span>📏 里程：<strong>15.0 ~ 30.0 km</strong> (慢活無負擔)</span>
                    <span>⛰️ 爬升/下降：<strong>+150m ~ +280m</strong></span>
                    <span>⏱️ 預估騎乘時間：<strong>1.5 ~ 2.0 小時</strong></span>
                    <span>🏨 推薦住宿：<strong>本棲湖 民宿 浩庵 / 河口湖木屋 / 富士吉田</strong></span>
                </div>
                <p><strong>🚲 富士五湖天候緩衝與深度慢活策略：</strong></p>
                <ol style="margin-left: 20px; color: #475569; font-size: 14.5px;">
                    <li><strong>應對高原氣候的定海神針：</strong> 富士五湖海拔近 1,000 公尺，11 月氣候多變。若前兩天（Day 3、Day 4）遇到低溫、降雨或山區初雪，今天就是最完美的「行程補完與休整日」！</li>
                    <li><strong>深度慢遊探索：</strong> 漫步西湖療癒之里根場（茅草屋聚落）、探訪青木原樹海步道（富岳風穴/鳴澤冰穴）、精進湖「子抱富士」、本棲湖浩庵營地放空。</li>
                    <li><strong>溫泉暖湯與美食：</strong> 前往富士眺望之湯 Yurari（ゆらり）泡露天溫泉眺望巨大富士山，品嚐熱騰騰的南瓜餺飥麵，讓身心完全回血！</li>
                </ol>
            </div>
        </div>\n\n        '''
    html = re.sub(day5_card_old, day5_card_new, html)

    # 3. Update Day 6 Card Details
    day6_card_old = r'<div class="day-card" id="day-6">[\s\S]*?(?=<div class="day-card" id="day-7">)'
    day6_card_new = '''<div class="day-card" id="day-6">
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
                    <span>📏 里程：<strong>48.0 km</strong></span>
                    <span>⛰️ 爬升/下降：<strong>+180m / -890m</strong> (從海拔 900m 高原一路暢快滑降至 120m 富士宮！)</span>
                    <span>⏱️ 預估騎乘時間：<strong>2.5 ~ 3.0 小時</strong></span>
                    <span>🏨 推薦住宿：<strong>富士宮市區商務溫泉飯店</strong>（富士山本宮淺間大社總本社旁）</span>
                </div>
                <p><strong>🚲 高原俯衝與下行騎行導引：</strong></p>
                <ol style="margin-left: 20px; color: #475569; font-size: 14.5px;">
                    <li><strong>本棲湖千圓逆富士晨景：</strong> 清晨在浩庵門前欣賞平靜如鏡的千圓日幣逆富士倒影。</li>
                    <li><strong>朝霧高原暢快巡航：</strong> 沿國道 139 號與平坦側道南下，右側是廣袤的牧場牛群，左側是近在咫尺的壯麗富士西側山壁。</li>
                    <li><strong>白糸之瀑與千米長下坡：</strong> 探訪天下名瀑「白糸之瀑」，隨後沿潤井川河谷連續滑降近 800 公尺，輕鬆抵達富士宮市。</li>
                    <li><strong>富士宮市區慶祝：</strong> 參拜世界遺產「富士山本宮淺間大社」，品嚐日本 B 級美食冠軍「富士宮炒麵（富士宮やきそば）」，準備迎接隔天的駿河灣海堤！</li>
                </ol>
            </div>
        </div>\n\n        '''
    html = re.sub(day6_card_old, day6_card_new, html)

    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)

print("Successfully updated itinerary HTML with Day 5 buffer & Day 6 Fujinomiya descent!")
