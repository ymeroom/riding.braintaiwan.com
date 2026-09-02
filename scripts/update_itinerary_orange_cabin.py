import sys, re

files_itinerary = [
    'C:/Users/ymero/Downloads/tokyo_fuji_cycling_itinerary_19days_v2.html',
    'd:/2026東京單車騎旅/tokyo_fuji_cycling_itinerary_19days_v2.html'
]

for path in files_itinerary:
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()

    # Update Day 3 in summary table
    html = re.sub(
        r'<tr[^>]*>\s*<td[^>]*><strong>Day 3<\/strong><\/td>[\s\S]*?<\/tr>',
        '''<tr>
            <td><strong>Day 3</strong></td>
            <td>11/15（日）</td>
            <td>由加利旅館 ➔ 富士急行線農路 ➔ 新倉山五重塔 ➔ <strong>河口湖北岸（紅葉迴廊）</strong></td>
            <td><strong>22.2 km</strong></td>
            <td>+532m / -173m</td>
            <td><span class="badge badge-easy">輕鬆爬升</span></td>
            <td><strong>Orange Cabin Inn far from station</strong>（連住第1晚・紅葉迴廊旁）</td>
            <td>晴朗乾燥 0.0mm (4.5~15.1°C)</td>
            <td>由加利旅館出發，探訪新倉山五重塔絕景，下午入住紅葉迴廊旁木屋，晚上賞夜楓點燈</td>
        </tr>''',
        html
    )

    # Update Day 4 in summary table
    html = re.sub(
        r'<tr[^>]*>\s*<td[^>]*><strong>Day 4<\/strong><\/td>[\s\S]*?<\/tr>',
        '''<tr>
            <td><strong>Day 4</strong></td>
            <td>11/16（一）</td>
            <td>清晨獨享紅葉迴廊 ➔ 忍野八海 ➔ 山中湖紅葉祭 ➔ <strong>返回河口湖</strong></td>
            <td><strong>50.0 km</strong></td>
            <td>+500m / -500m</td>
            <td><span class="badge badge-easy">輕裝探索</span></td>
            <td><strong>Orange Cabin Inn far from station</strong>（連住第2晚・免換飯店）</td>
            <td>晴朗乾燥 0.0mm (3.2~14.6°C)</td>
            <td>清晨步行獨享無人紅葉迴廊，白天輕裝無負重暢遊忍野八海與山中湖，極度愜意</td>
        </tr>''',
        html
    )

    # Update Day 5 in summary table
    html = re.sub(
        r'<tr[^>]*>\s*<td[^>]*><strong>Day 5<\/strong><\/td>[\s\S]*?<\/tr>',
        '''<tr>
            <td><strong>Day 5</strong></td>
            <td>11/17（二）</td>
            <td>Orange Cabin ➔ 湖北View Line ➔ 西湖 ➔ 精進湖 ➔ 本棲湖逆富士 ➔ <strong>富士宮</strong></td>
            <td><strong>70.6 km</strong></td>
            <td>+250m / -991m</td>
            <td><span class="badge badge-easy">長下坡爽騎</span></td>
            <td>富士宮市區商務溫泉飯店（淺間大社總本社旁）</td>
            <td>晴朗乾燥 0.0mm (5.8~16.4°C)</td>
            <td>河口湖北岸出發，順訪西湖、精進湖、本棲湖浩庵逆富士，隨後從海拔900m一路暢快滑降至富士宮</td>
        </tr>''',
        html
    )

    # Update Day 3 Card details
    day3_card_old = r'<div class="day-card" id="day-3">[\s\S]*?(?=<div class="day-card" id="day-4">)'
    day3_card_new = '''<div class="day-card" id="day-3">
            <div class="day-header">
                <span class="day-num">Day 3</span> 11/15（日）由加利旅館 ➔ 富士急行生活農路 ➔ 新倉山淺間五重塔 ➔ 河口湖紅葉迴廊（宿 Orange Cabin Inn 連住第 1 晚）
            </div>
            <div class="day-body">
                <div class="foliage-box">
                    <strong>🍂 歷史紅葉情報（新倉山公園 / 河口湖北岸）：</strong> <strong>見頃最盛期！</strong> 紅葉與朱紅五重塔、雪白富士山構成全日本最經典明信片。
                </div>
                <div class="weather-box">
                    <strong>☀️ 去年實測天氣（2025/11/15 JMA 河口湖觀測所）：</strong><br>
                    天氣：<strong>萬里無雲（降水量 0.0 mm，日照時數 9.6 小時）</strong><br>
                    氣溫：最低 <strong>4.5°C</strong> ｜ 最高 <strong>15.1°C</strong> ｜ 傍晚紅葉迴廊點燈需備保暖外套
                </div>
                <div class="route-stat">
                    <span>📏 里程：<strong>22.2 km</strong> (休閒慢活半日騎)</span>
                    <span>⛰️ 爬升/下降：<strong>+532m / -173m</strong> (海拔 484m ➔ 845m)</span>
                    <span>⏱️ 預估騎乘時間：<strong>1.5 ~ 2.0 小時</strong></span>
                    <span>🏨 推薦住宿：<strong>Orange Cabin Inn far from station</strong>（山梨縣南都留郡富士河口湖町河口1916-3，步行 3 分鐘至紅葉迴廊！）</span>
                </div>
                <p><strong>🚲 騎行路線導引：</strong></p>
                <ol style="margin-left: 20px; color: #475569; font-size: 14.5px;">
                    <li><strong>由加利旅館愜意出發：</strong> 享用早餐後 09:30 出發，沿富士急行線西側生活農路（縣道 713 號）緩坡上行，完全無大型車輛壓力。</li>
                    <li><strong>新倉山淺間公園朝聖：</strong> 抵達新倉山腳，登上 398 階石階，親眼目睹五重塔、漫山紅葉與巨大富士山的世紀同框絕景！</li>
                    <li><strong>下午 14:00 入住 Orange Cabin Inn：</strong> 位於河口湖北岸久保田一竹美術館旁，木屋溫馨舒適。check-in 卸下行李後，傍晚直接漫步前往「河口湖紅葉迴廊」欣賞夜間點燈，完全免去塞車與尋找車位的困擾！</li>
                </ol>
            </div>
        </div>\n\n        '''
    html = re.sub(day3_card_old, day3_card_new, html)

    # Update Day 4 Card details
    day4_card_old = r'<div class="day-card" id="day-4">[\s\S]*?(?=<div class="day-card" id="day-5">)'
    day4_card_new = '''<div class="day-card" id="day-4">
            <div class="day-header">
                <span class="day-num">Day 4</span> 11/16（一）清晨獨享紅葉迴廊 ➔ 忍野八海 ➔ 山中湖旭日丘紅葉祭 ➔ 返回河口湖（宿 Orange Cabin Inn 連住第 2 晚）
            </div>
            <div class="day-body">
                <div class="foliage-box">
                    <strong>🍂 歷史紅葉情報（河口湖紅葉迴廊 / 山中湖旭日丘）：</strong> <strong>雙湖見頃最高峰！</strong> 滿天燃燒的深紅隧道。
                </div>
                <div class="weather-box">
                    <strong>☀️ 去年實測天氣（2025/11/16 JMA 河口湖/山中湖觀測所）：</strong><br>
                    天氣：<strong>全日大晴（降水量 0.0 mm，日照時數 9.1 小時）</strong><br>
                    氣溫：最低 <strong>3.2°C</strong> ｜ 最高 <strong>14.6°C</strong> ｜ 清晨晨光斜射紅葉迴廊，拍照光線最無敵
                </div>
                <div class="route-stat">
                    <span>📏 里程：<strong>50.0 km</strong> (輕裝無負重環湖)</span>
                    <span>⛰️ 爬升/下降：<strong>+500m / -500m</strong></span>
                    <span>⏱️ 預估騎乘時間：<strong>3.0 ~ 3.5 小時</strong></span>
                    <span>🏨 推薦住宿：<strong>Orange Cabin Inn far from station</strong>（連住第 2 晚，免打包行李！）</span>
                </div>
                <p><strong>🚲 騎行路線導引（在地車友私房玩法）：</strong></p>
                <ol style="margin-left: 20px; color: #475569; font-size: 14.5px;">
                    <li><strong>06:30-08:00 清晨獨享紅葉迴廊：</strong> 住宿就在旁邊的絕對優勢！在觀光大巴與人潮湧入前，悠閒散步或單車滑進紅葉迴廊，獨享無人深紅隧道與富士晨光！</li>
                    <li><strong>輕裝騎往忍野八海：</strong> 不需背負大件行李，單車輕快飛馳，品嚐清涼甘洌的神之湧泉與現烤草餅。</li>
                    <li><strong>山中湖旭日丘紅葉祭巡航：</strong> 沿山中湖專用自行車道漫騎，欣賞落葉紅毯與天鵝游弋，下午原路輕鬆返回 Orange Cabin Inn 連住休整。</li>
                </ol>
            </div>
        </div>\n\n        '''
    html = re.sub(day4_card_old, day4_card_new, html)

    # Update Day 5 Card details
    day5_card_old = r'<div class="day-card" id="day-5">[\s\S]*?(?=<div class="day-card" id="day-6">)'
    day5_card_new = '''<div class="day-card" id="day-5">
            <div class="day-header">
                <span class="day-num">Day 5</span> 11/17（二）Orange Cabin ➔ 湖北View Line ➔ 西湖 ➔ 精進湖 ➔ 本棲湖千圓逆富士 ➔ 朝霧高原 ➔ 富士宮
            </div>
            <div class="day-body">
                <div class="foliage-box">
                    <strong>🍂 歷史紅葉情報（西湖 / 本棲湖 / 朝霧高原）：</strong> 湖畔深秋蒼松與紅葉交織，朝霧高原芒草金黃萬頃。
                </div>
                <div class="weather-box">
                    <strong>☀️ 去年實測天氣（2025/11/17 JMA 富士宮觀測所）：</strong><br>
                    天氣：<strong>晴朗（降水量 0.0 mm，日照時數 8.8 小時）</strong><br>
                    氣溫：最低 <strong>5.8°C</strong> ｜ 最高 <strong>16.4°C</strong> ｜ 朝霧高原下坡需防風手套與風衣
                </div>
                <div class="route-stat">
                    <span>📏 里程：<strong>70.6 km</strong></span>
                    <span>⛰️ 爬升/下降：<strong>+250m / -991m</strong> (從海拔 850m 一路爽快滑降至 119m 富士宮！)</span>
                    <span>⏱️ 預估騎乘時間：<strong>3.5 ~ 4.0 小時</strong></span>
                    <span>🏨 推薦住宿：<strong>富士宮市區商務溫泉飯店</strong>（淺間大社總本社旁，品嚐富士宮炒麵）</span>
                </div>
                <p><strong>🚲 騎行路線導引：</strong></p>
                <ol style="margin-left: 20px; color: #475569; font-size: 14.5px;">
                    <li><strong>北岸出發直切湖北 View Line：</strong> 告別 Orange Cabin Inn，沿河口湖北岸景觀公路滑行，途經大石公園掃帚草。</li>
                    <li><strong>西湖、精進湖與本棲湖巡禮：</strong> 探訪西湖療癒之里、精進湖「子抱富士」，抵達本棲湖浩庵營地掏出千圓紙幣比對水鏡逆富士。</li>
                    <li><strong>超暢快千米長下坡：</strong> 翻過朝霧高原後，一路沿著寬闊平整的國道 139 號與潤井川河谷連續滑降近 1000 公尺，輕鬆抵達富士宮市！</li>
                </ol>
            </div>
        </div>\n\n        '''
    html = re.sub(day5_card_old, day5_card_new, html)

    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)

print("Successfully updated itinerary HTML for Day 3, 4, 5!")
