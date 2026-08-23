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
            <td>由加利旅館 ➔ <strong>【晴天】衝山中湖+忍野八海 / 【陰天】走新倉山五重塔</strong> ➔ 河口湖</td>
            <td><strong>22.2 ~ 54.9 km</strong></td>
            <td>+532m ~ +775m</td>
            <td><span class="badge badge-easy">晴雨雙軌</span></td>
            <td><strong>Orange Cabin Inn far from station</strong>（紅葉迴廊旁）</td>
            <td>晴朗乾燥 0.0mm (4.5~15.1°C)</td>
            <td>天候極佳時直攻海拔千米山中湖與忍野八海；天候不佳時走新倉山五重塔精簡直達木屋</td>
        </tr>''',
        html
    )

    # Update Day 4 in summary table
    html = re.sub(
        r'<tr[^>]*>\s*<td[^>]*><strong>Day 4<\/strong><\/td>[\s\S]*?<\/tr>',
        '''<tr>
            <td><strong>Day 4</strong></td>
            <td>11/16（一）</td>
            <td>清晨獨享紅葉迴廊 ➔ 富士五湖深度漫活 / 彈性探索 ➔ <strong>當日動態推進</strong></td>
            <td><strong>25.0 ~ 50.0 km</strong></td>
            <td>+250m ~ +500m</td>
            <td><span class="badge badge-easy">機動彈性</span></td>
            <td><strong>當日視天候與體力機動決定</strong>（連住 Orange Cabin 或彈性推進）</td>
            <td>晴朗乾燥 0.0mm (3.2~14.6°C)</td>
            <td>清晨必賞無人紅葉迴廊，白天深度慢遊河口湖/西湖/天空鳥居，住宿保留最高自由度</td>
        </tr>''',
        html
    )

    # Update Day 3 Card details
    day3_card_old = r'<div class="day-card" id="day-3">[\s\S]*?(?=<div class="day-card" id="day-4">)'
    day3_card_new = '''<div class="day-card" id="day-3">
            <div class="day-header">
                <span class="day-num">Day 3</span> 11/15（日）由加利旅館 ➔ 晴雨雙軌決策（好天氣衝山中湖＋忍野八海 / 天氣差走新倉山五重塔）➔ 河口湖（宿 Orange Cabin Inn）
            </div>
            <div class="day-body">
                <div class="foliage-box">
                    <strong>🍂 歷史紅葉情報（山中湖旭日丘 / 河口湖北岸）：</strong> <strong>見頃最盛期！</strong> 雙湖楓紅如火，富士雪冠清晰可見。
                </div>
                <div class="weather-box">
                    <strong>☀️ 去年實測天氣（2025/11/15 JMA 河口湖觀測所）：</strong><br>
                    天氣：<strong>萬里無雲（降水量 0.0 mm，日照時數 9.6 小時）</strong><br>
                    氣溫：最低 <strong>4.5°C</strong> ｜ 最高 <strong>15.1°C</strong> ｜ 依晨間即時雲層能見度啟動雙軌策略
                </div>
                <div class="route-stat">
                    <span>📏 里程：<strong>好天氣 54.9 km ｜ 天氣差 22.2 km</strong></span>
                    <span>⛰️ 爬升/下降：<strong>+775m / -408m ｜ +532m / -173m</strong></span>
                    <span>⏱️ 預估騎乘時間：<strong>好天氣 ~3.5hr ｜ 天氣差 ~1.5hr</strong></span>
                    <span>🏨 推薦住宿：<strong>Orange Cabin Inn far from station</strong>（河口湖北岸，步行 3 分鐘至紅葉迴廊）</span>
                </div>
                <p><strong>🚲 晴雨雙軌騎行決策機制：</strong></p>
                <div style="background: rgba(16, 185, 129, 0.08); border: 1px solid #10B981; border-radius: 8px; padding: 12px 16px; margin-bottom: 12px; font-size: 14px; line-height: 1.6;">
                    <strong style="color: #10B981;">☀️ 方案 A（晴天能見度高・大推薦）：</strong><br>
                    由加利旅館出發 ➔ 經桂川生活農路直攻 <strong>忍野八海</strong>（神之湧泉） ➔ 前進海拔 1,000m <strong>山中湖旭日丘紅葉祭</strong> ➔ 經富士吉田金鳥居與新倉山滑降至河口湖 ➔ 傍晚入住 <strong>Orange Cabin Inn</strong>（里程 54.9km，爬升 +775m）。
                </div>
                <div style="background: rgba(59, 130, 246, 0.08); border: 1px solid #3B82F6; border-radius: 8px; padding: 12px 16px; font-size: 14px; line-height: 1.6;">
                    <strong style="color: #3B82F6;">☁️ 方案 B（陰天/雲層厚/體力調節）：</strong><br>
                    由加利旅館出發 ➔ 避開海拔一千米高原，沿生活農路直達 <strong>新倉山淺間公園（五重塔＋富士山絕景）</strong> ➔ 輕鬆滑向河口湖大橋 ➔ 下午 14:00 提早入住 <strong>Orange Cabin Inn</strong> 休整，晚上散步賞夜楓點燈（里程僅 22.2km，爬升 +532m）。
                </div>
            </div>
        </div>\n\n        '''
    html = re.sub(day3_card_old, day3_card_new, html)

    # Update Day 4 Card details
    day4_card_old = r'<div class="day-card" id="day-4">[\s\S]*?(?=<div class="day-card" id="day-5">)'
    day4_card_new = '''<div class="day-card" id="day-4">
            <div class="day-header">
                <span class="day-num">Day 4</span> 11/16（一）清晨獨享紅葉迴廊 ➔ 富士五湖深度慢遊 ➔ 【住宿機動決定日】
            </div>
            <div class="day-body">
                <div class="foliage-box">
                    <strong>🍂 歷史紅葉情報（河口湖紅葉迴廊）：</strong> <strong>見頃最高峰！</strong> 晨光穿透深紅隧道，此行最高潮。
                </div>
                <div class="weather-box">
                    <strong>☀️ 去年實測天氣（2025/11/16 JMA 河口湖觀測所）：</strong><br>
                    天氣：<strong>全日大晴（降水量 0.0 mm，日照時數 9.1 小時）</strong><br>
                    氣溫：最低 <strong>3.2°C</strong> ｜ 最高 <strong>14.6°C</strong> ｜ 晨間清冷但乾燥無風
                </div>
                <div class="route-stat">
                    <span>📏 里程：<strong>25.0 ~ 50.0 km</strong> (彈性調節)</span>
                    <span>⛰️ 爬升/下降：<strong>+250m ~ +500m</strong></span>
                    <span>⏱️ 預估騎乘時間：<strong>2.0 ~ 3.5 小時</strong></span>
                    <span>🏨 住宿策略：<strong>當日視天候、體力與心情機動決定</strong>（可連住 Orange Cabin 或機動向西推進）</span>
                </div>
                <p><strong>🚲 當日活動與住宿機動策略：</strong></p>
                <ol style="margin-left: 20px; color: #475569; font-size: 14.5px;">
                    <li><strong>06:30-08:00 清晨必訪無人紅葉迴廊：</strong> 住宿就在旁邊的絕對優勢！在觀光團湧入前，獨享晨光中無人的深紅隧道。</li>
                    <li><strong>白天彈性慢遊選項：</strong>
                        <br>・若 Day 3 已走完山中湖：今日悠閒騎行大石公園、河口淺間神社（天空鳥居）、久保田一竹美術館、西湖療癒之里根場。
                        <br>・若 Day 3 走五重塔備案：今日可輕裝補完忍野八海與山中湖。
                    </li>
                    <li><strong>住宿機動性：</strong> 若想徹底放鬆可選擇連住 Orange Cabin Inn（免打包行李）；若想提前推進可當天下午彈性預訂西湖/本棲湖/富士宮周邊住宿，享受旅行最極致的自由！</li>
                </ol>
            </div>
        </div>\n\n        '''
    html = re.sub(day4_card_old, day4_card_new, html)

    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)

print("Successfully updated itinerary with Day 3 dual-track & Day 4 flexible lodging strategy!")
