import sys, re

# 1. Update itinerary HTML
files_itinerary = [
    'C:/Users/ymero/Downloads/tokyo_fuji_cycling_itinerary_19days_v2.html',
    'd:/2026東京單車騎旅/tokyo_fuji_cycling_itinerary_19days_v2.html'
]

# Let's inspect and rewrite the itinerary HTML with the updated Day 1 and Day 2 details
for path in files_itinerary:
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()

    # Update Day 1 Card & Summary table
    # Replace Day 1 lodging and description
    html = re.sub(
        r'<tr[^>]*>\s*<td[^>]*><strong>Day 1<\/strong><\/td>\s*<td>11/13（五）<\/td>\s*<td>秋葉原 ➔ 府中／調布<\/td>[\s\S]*?<\/tr>',
        '''<tr>
            <td><strong>Day 1</strong></td>
            <td>11/13（五）</td>
            <td>秋葉原 ➔ 國道15號 ➔ 六鄉橋 ➔ 多摩川CR ➔ 淺川CR ➔ <strong>高尾山口</strong></td>
            <td><strong>78.0 km</strong></td>
            <td>+228m / -46m</td>
            <td><span class="badge badge-easy">平緩水岸</span></td>
            <td><strong>Mt. Takao Base Camp</strong>（高尾山極樂湯）</td>
            <td>晴朗乾燥 0.0mm (11.8~19.6°C)</td>
            <td>沿多摩川與淺川雙專用道逆流緩上，全程零紅綠燈直達高尾山腳</td>
        </tr>''',
        html
    )

    # Update Day 2 in summary table
    html = re.sub(
        r'<tr[^>]*>\s*<td[^>]*><strong>Day 2<\/strong><\/td>\s*<td>11/14（六）<\/td>\s*<td>府中 ➔ 都留市<\/td>[\s\S]*?<\/tr>',
        '''<tr>
            <td><strong>Day 2</strong></td>
            <td>11/14（六）</td>
            <td>Mt. Takao Base Camp ➔ 大垂水峠 ➔ 相模湖 ➔ <strong>縣道35秋山街道</strong> ➔ <strong>都留市</strong></td>
            <td><strong>54.0 km</strong></td>
            <td>+850m / -556m</td>
            <td><span class="badge badge-mod">幽靜山道</span></td>
            <td><strong>ビジネス旅館 由加利</strong>（都留市中心）</td>
            <td>晴朗乾燥 0.0mm (7.8~17.2°C)</td>
            <td>清晨翻大垂水峠避開大車，相模湖直切縣道35號秋山溪谷，下午輕鬆抵達由加利旅館</td>
        </tr>''',
        html
    )

    # Update Day 3 in summary table
    html = re.sub(
        r'<tr[^>]*>\s*<td[^>]*><strong>Day 3<\/strong><\/td>\s*<td>11/15（日）<\/td>\s*<td>都留市 ➔ 山中湖<\/td>[\s\S]*?<\/tr>',
        '''<tr>
            <td><strong>Day 3</strong></td>
            <td>11/15（日）</td>
            <td>由加利旅館 ➔ 富士急行線生活農路（縣道713號） ➔ 富士吉田金鳥居 ➔ <strong>山中湖</strong></td>
            <td><strong>38.0 km</strong></td>
            <td>+520m / -60m</td>
            <td><span class="badge badge-mod">高原緩升</span></td>
            <td>山中湖畔溫泉旅館（富士山景第一排）</td>
            <td>晴朗乾燥 0.0mm (4.5~15.1°C)</td>
            <td>由加利旅館出發，沿桂川西側幽靜生活農路平緩登上海拔一千米山中湖</td>
        </tr>''',
        html
    )

    # Update Day 1 Card details
    day1_card_old = r'<div class="day-card" id="day-1">[\s\S]*?(?=<div class="day-card" id="day-2">)'
    day1_card_new = '''<div class="day-card" id="day-1">
            <div class="day-header">
                <span class="day-num">Day 1</span> 11/13（五）秋葉原取車 ➔ 國道15號平坦出城 ➔ 六鄉橋 ➔ 多摩川CR ➔ 淺川CR ➔ 高尾山口（宿 Mt. Takao Base Camp）
                <div style="margin-top: 6px;"><a href="day1_route_map_demo.html" target="_blank" style="display: inline-flex; align-items: center; gap: 4px; background: #2563EB; color: #FFFFFF; padding: 3px 10px; border-radius: 6px; font-size: 12px; font-weight: 700; text-decoration: none;">🗺️ 開啟 Day 1 具體地圖 Demo (NAVITIME/Leaflet/GPX) ➔</a></div>
            </div>
            <div class="day-body">
                <div class="foliage-box">
                    <strong>🍂 歷史紅葉情報（東京都心 / 多摩水岸）：</strong> 都心綠葉轉黃初階（見頃預計 11/28～12/03），多摩川高灘地芒草盛開，秋風和煦。
                </div>
                <div class="weather-box">
                    <strong>☀️ 去年實測天氣（2025/11/13 JMA 東京觀測所）：</strong><br>
                    天氣：<strong>全日晴朗無雨（降水量 0.0 mm，日照時數 9.4 小時）</strong><br>
                    氣溫：最低 <strong>11.8°C</strong> ｜ 最高 <strong>19.6°C</strong> ｜ 風速：微風 2.1 m/s（體感極度舒適）
                </div>
                <div class="route-stat">
                    <span>📏 里程：<strong>78.0 km</strong></span>
                    <span>⛰️ 爬升/下降：<strong>+228m / -46m</strong> (海拔 3m ➔ 190m)</span>
                    <span>⏱️ 預估騎乘時間：<strong>4.0 ~ 4.5 小時</strong></span>
                    <span>🏨 推薦住宿：<strong>Mt. Takao Base Camp</strong>（步行 3 分鐘至高尾山極樂湯溫泉）</span>
                </div>
                <p><strong>🚲 騎行路線導引：</strong></p>
                <ol style="margin-left: 20px; color: #475569; font-size: 14.5px;">
                    <li><strong>09:30 秋葉原取車：</strong> 在 CycleTrip Base 完成取車手續，調校胎壓與坐墊，穿過銀座、新橋寬敞車道進入國道 15 號（第一京濱）。</li>
                    <li><strong>六鄉橋無縫切入水岸：</strong> 於六鄉橋直接切入「多摩川自行車道（左岸）」，整整 32 公里無紅綠燈、無汽車干擾。</li>
                    <li><strong>府中・日野匯流轉接淺川：</strong> 於多摩川與淺川匯流處切入「淺川自行車專用道（Asakawa CR）」，沿著平整平緩的柏油路直抵高尾山腳。</li>
                    <li><strong>傍晚抵達高尾山 Base Camp：</strong> 入住單車友善的 Mt. Takao Base Camp，晚上前往隔壁「極樂湯」享受露天溫泉與山麓美食，為隔天的秋山街道儲備充沛體力！</li>
                </ol>
            </div>
        </div>\n\n        '''
    html = re.sub(day1_card_old, day1_card_new, html)

    # Update Day 2 Card details
    day2_card_old = r'<div class="day-card" id="day-2">[\s\S]*?(?=<div class="day-card" id="day-3">)'
    day2_card_new = '''<div class="day-card" id="day-2">
            <div class="day-header">
                <span class="day-num">Day 2</span> 11/14（六）Mt. Takao Base Camp ➔ 清晨大垂水峠 ➔ 相模湖 ➔ 山梨縣道35號秋山街道 ➔ 都留市（宿 ビジネス旅館 由加利）
                <div style="margin-top: 6px;"><a href="day2_route_map_demo.html" target="_blank" style="display: inline-flex; align-items: center; gap: 4px; background: #D97724; color: #FFFFFF; padding: 3px 10px; border-radius: 6px; font-size: 12px; font-weight: 700; text-decoration: none;">🗺️ 開啟 Day 2 具體地圖 Demo (NAVITIME/Leaflet/GPX) ➔</a></div>
            </div>
            <div class="day-body">
                <div class="foliage-box">
                    <strong>🍂 歷史紅葉情報（相模湖 / 秋山溪谷 / 都留）：</strong> 淺色初紅（30-40% 轉色），山林間黃綠紅交錯，溪谷景致極美。
                </div>
                <div class="weather-box">
                    <strong>☀️ 去年實測天氣（2025/11/14 JMA 八王子/相模原觀測所）：</strong><br>
                    天氣：<strong>晴（降水量 0.0 mm，日照時數 8.9 小時）</strong><br>
                    氣溫：最低 <strong>7.8°C</strong> ｜ 最高 <strong>17.2°C</strong> ｜ 清晨出發微涼需薄風衣
                </div>
                <div class="route-stat">
                    <span>📏 里程：<strong>54.0 km</strong> (黃金折衷精簡版)</span>
                    <span>⛰️ 爬升/下降：<strong>+850m / -556m</strong> (海拔 190m ➔ 560m ➔ 484m)</span>
                    <span>⏱️ 預估騎乘時間：<strong>3.5 ~ 4.0 小時</strong></span>
                    <span>🏨 推薦住宿：<strong>ビジネス旅館 由加利</strong>（山梨縣都留市上谷1丁目3-4）</span>
                </div>
                <p><strong>🚲 騎行路線導引（方案 B 黃金折衷走法）：</strong></p>
                <ol style="margin-left: 20px; color: #475569; font-size: 14.5px;">
                    <li><strong>08:00 清晨直攻大垂水峠：</strong> 由 Mt. Takao Base Camp 出門即攻大垂水峠（4.2km，爬升 202m，均坡 4.8%），清晨車流極少，體力最充沛時順暢登頂！</li>
                    <li><strong>相模湖畔俯衝：</strong> 順暢下坡 3.5km 抵達相模湖底（海拔 205m），欣賞晨霧湖光。</li>
                    <li><strong>關鍵避坑轉折：</strong> 在相模湖畔名倉果斷左轉切入<strong>「山梨縣道 35 號（秋山街道）」</strong>，徹底脫離國道 20 號大車威脅！</li>
                    <li><strong>幽靜秋山溪谷漫遊：</strong> 沿秋山川緩坡慢騎 30 公里，兩側深秋楓紅、溪水潺潺，最高點秋山隧道（560m）後滑降至都留市。</li>
                    <li><strong>下午 13:30 輕鬆抵達由加利旅館：</strong> 位於都留市核心商圈，周邊超商居酒屋齊全，並緊鄰富士急行線車站，從容休整。</li>
                </ol>
            </div>
        </div>\n\n        '''
    html = re.sub(day2_card_old, day2_card_new, html)

    # Update Day 3 Card details
    day3_card_old = r'<div class="day-card" id="day-3">[\s\S]*?(?=<div class="day-card" id="day-4">)'
    day3_card_new = '''<div class="day-card" id="day-3">
            <div class="day-header">
                <span class="day-num">Day 3</span> 11/15（日）由加利旅館 ➔ 富士急行線西側生活農路（縣道713號） ➔ 富士吉田金鳥居 ➔ 山中湖（夕陽與紅葉祭）
            </div>
            <div class="day-body">
                <div class="foliage-box">
                    <strong>🍂 歷史紅葉情報（山中湖 旭日丘湖畔綠地公園）：</strong> <strong>見頃最盛期（11/05～11/18）！</strong> 夕陽與楓葉交相輝映。
                </div>
                <div class="weather-box">
                    <strong>☀️ 去年實測天氣（2025/11/15 JMA 山中湖觀測所）：</strong><br>
                    天氣：<strong>萬里無雲（降水量 0.0 mm，日照時數 9.6 小時）</strong><br>
                    氣溫：最低 <strong>4.5°C</strong> ｜ 最高 <strong>15.1°C</strong> ｜ 高原傍晚降溫迅速需禦寒保暖
                </div>
                <div class="route-stat">
                    <span>📏 里程：<strong>38.0 km</strong></span>
                    <span>⛰️ 爬升/下降：<strong>+520m / -60m</strong> (海拔 484m ➔ 1,000m)</span>
                    <span>⏱️ 預估騎乘時間：<strong>2.5 ~ 3.0 小時</strong></span>
                    <span>🏨 推薦住宿：<strong>山中湖畔溫泉旅館</strong>（富士山景第一排）</span>
                </div>
                <p><strong>🚲 騎行路線導引：</strong></p>
                <ol style="margin-left: 20px; color: #475569; font-size: 14.5px;">
                    <li><strong>由加利旅館愜意出發：</strong> 享用早餐後 09:00 出發，沿富士急行線鐵路西側的縣道 713 號（大野夏狩線）生活農路前進，完全避開大貨車。</li>
                    <li><strong>穿過富士吉田金鳥居：</strong> 仰望雄偉的金鳥居與巍峨富士山，感受江戶富士講信仰的歷史氛圍。</li>
                    <li><strong>抵達海拔一千米山中湖：</strong> 沿湖畔專用自行車道巡航，下午在「旭日丘湖畔綠地公園」欣賞見頃最盛期的夕陽紅葉祭！</li>
                </ol>
            </div>
        </div>\n\n        '''
    html = re.sub(day3_card_old, day3_card_new, html)

    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Successfully updated {path}")
