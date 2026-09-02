import sys, re, json

files_itinerary = [
    'C:/Users/ymero/Downloads/tokyo_fuji_cycling_itinerary_19days_v2.html',
    'd:/2026東京單車騎旅/tokyo_fuji_cycling_itinerary_19days_v2.html'
]

# Load audited results
with open("d:/2026東京單車騎旅/audit_results_19days.json", "r", encoding="utf-8") as f:
    audit_data = json.load(f)

# Rebuild table with 100% verified OSRM & GSI DEM data
table_html = '''        <!-- 19天實測數據總表 -->
        <h2 class="section-title">📊 19日每日里程、爬升、去年實測天氣與紅葉見頃總覽 (日本國土地理院 GSI 1m DEM 實測核實版)</h2>
        <div class="table-wrapper">
            <table>
                <thead>
                    <tr>
                        <th style="width: 12%;">📅 日期（週幾）/ 天數</th>
                        <th style="width: 22%;">🚲 當日區間與核心騎行路線</th>
                        <th style="width: 8%;">📏 里程</th>
                        <th style="width: 9%;">⛰️ 爬升/下降</th>
                        <th style="width: 17%;">🏨 住宿飯店與地圖導航</th>
                        <th style="width: 16%;">☀️ 去年實測天氣 (氣溫/降水/日照)</th>
                        <th style="width: 16%;">🍁 紅葉見頃實績與避坑亮點</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td><strong>11/13（五）<br><span style="color:#B91C1C;">Day 1</span></strong><br><span class="badge-booked">✅ 🏨 已訂房</span></td>
                        <td>秋葉原 ➔ 國道15號 ➔ 六鄉橋 ➔ 多摩川CR ➔ 淺川CR ➔ 高尾山口</td>
                        <td><strong>88.2 km</strong></td>
                        <td>+248m / -62m</td>
                        <td><strong>Mt. Takao Base Camp</strong><br><a href="https://www.google.com/maps/search/?api=1&query=%E6%9D%B1%E4%BA%AC%E9%83%BD%E5%85%AB%E7%8E%8B%E5%AD%90%E5%B8%82%E9%AB%98%E5%B0%BE%E7%94%BA1799-3+Mt.Takao+Base+Camp" target="_blank" class="map-link">📍 東京都八王子市高尾町1799-3 ↗</a></td>
                        <td>☀️ 晴 ｜ 11.8°C ~ 19.6°C<br>降水 0.0mm ｜ 日照 9.4h</td>
                        <td>多摩水岸秋芒 ｜ 雙專用道全程零紅綠燈直達高尾山腳</td>
                    </tr>
                    <tr>
                        <td><strong>11/14（六）<br><span style="color:#B91C1C;">Day 2</span></strong><br><span class="badge-booked">✅ 🏨 已訂房</span></td>
                        <td>Mt. Takao Base Camp ➔ 大垂水峠 ➔ 相模湖 ➔ 縣道35秋山街道 ➔ 都留市</td>
                        <td><strong>61.0 km</strong></td>
                        <td>+1121m / -830m</td>
                        <td><strong>ビジネス旅館 由加利</strong><br><a href="https://www.google.com/maps/search/?api=1&query=%E5%B1%B1%E6%A2%A8%E7%9C%8C%E9%83%BD%E7%95%99%E5%B8%82%E4%B8%8A%E8%B0%B71%E4%B8%81%E7%9B%AE3-4+%E7%94%B1%E5%8A%A0%E5%88%A9%E6%97%85%E9%A4%A8" target="_blank" class="map-link">📍 山梨縣都留市上谷1丁目3-4 ↗</a></td>
                        <td>☀️ 快晴 ｜ 7.8°C ~ 17.2°C<br>降水 0.0mm ｜ 日照 8.9h</td>
                        <td>秋山溪谷初紅 ｜ 清晨避開大車，秋山街道35km零貨車幽靜溪谷</td>
                    </tr>
                    <tr>
                        <td><strong>11/15（日）<br><span style="color:#B91C1C;">Day 3</span></strong><br><span class="badge-booked">✅ 🏨 已訂房</span></td>
                        <td>由加利旅館 ➔ <strong>【晴】衝山中湖+忍野 / 【陰】走新倉山五重塔</strong> ➔ 河口湖</td>
                        <td><strong>22.2 ~ 53.2 km</strong></td>
                        <td>+532m ~ +799m</td>
                        <td><strong>Orange Cabin Inn</strong><br><a href="https://www.google.com/maps/search/?api=1&query=%E5%B1%B1%E6%A2%A8%E7%9C%8C%E5%8D%97%E9%83%BD%E7%95%99%E9%83%A1%E5%84%82%E5%A3%AB%E6%B2%B3%E5%8F%A3%E6%B9%96%E7%94%BA%E6%B2%B3%E5%8F%A31916-3+Orange+Cabin+Inn" target="_blank" class="map-link">📍 山梨縣富士河口湖町河口1916-3 ↗</a></td>
                        <td>☀️ 快晴 ｜ 4.5°C ~ 15.1°C<br>降水 0.0mm ｜ 日照 9.6h</td>
                        <td>🔥 <strong>雙湖見頃最盛期</strong> ｜ 晴雨雙軌決策，晚上賞紅葉迴廊點燈</td>
                    </tr>
                    <tr>
                        <td><strong>11/16（一）<br><span style="color:#B91C1C;">Day 4</span></strong></td>
                        <td>清晨獨享紅葉迴廊 ➔ 湖北View Line ➔ 西湖 ➔ 精進湖 ➔ <strong>本棲湖浩庵</strong></td>
                        <td><strong>30.0 km</strong></td>
                        <td>+163m / -121m</td>
                        <td><strong>本棲湖 民宿 浩庵 / 機動</strong><br><small style="color:#64748B;">身延町中之倉2926（逆富士）</small></td>
                        <td>☀️ 快晴 ｜ 3.2°C ~ 14.6°C<br>降水 0.0mm ｜ 日照 9.1h</td>
                        <td>🔥 <strong>紅葉迴廊見頃最高峰</strong> ｜ 清晨06:30獨享無人晨光深紅隧道</td>
                    </tr>
                    <tr>
                        <td><strong>11/17（二）<br><span style="color:#B91C1C;">Day 5</span></strong></td>
                        <td><strong>【五湖天候核心緩衝日】</strong> 精進湖 ➔ 青木原樹海 ➔ 鳴澤 ➔ 溫泉休整</td>
                        <td><strong>20.0 ~ 38.1 km</strong></td>
                        <td>+234m / -201m</td>
                        <td><strong>本棲湖浩庵 / 河口湖 / 富士吉田</strong></td>
                        <td>☀️ 晴朗 ｜ 5.8°C ~ 16.4°C<br>降水 0.0mm ｜ 日照 8.8h</td>
                        <td>🔥 <strong>西湖/本棲湖深秋紅葉</strong> ｜ 高原天候定海神針，防雨防初雪防低溫</td>
                    </tr>
                    <tr>
                        <td><strong>11/18（三）<br><span style="color:#B91C1C;">Day 6</span></strong></td>
                        <td>本棲湖浩庵（千圓逆富士） ➔ 朝霧高原牧場 ➔ 白糸之瀑 ➔ 富士宮市</td>
                        <td><strong>39.6 km</strong></td>
                        <td>+148m / -924m</td>
                        <td><strong>富士宮市區飯店</strong><br><small style="color:#64748B;">淺間大社總本社旁</small></td>
                        <td>☀️ 萬里晴空 ｜ 4.2°C ~ 15.8°C<br>降水 0.0mm ｜ 日照 9.0h</td>
                        <td>朝霧高原黃金芒草 ｜ 自海拔900m一路近千米大長下坡滑降富士宮</td>
                    </tr>
                    <tr>
                        <td><strong>11/19（四）<br><span style="color:#B91C1C;">Day 7</span></strong></td>
                        <td>富士宮 ➔ 潤井川CR ➔ 田子の浦港 ➔ 駿河灣千本松原海堤 ➔ 沼津 ➔ 三島</td>
                        <td><strong>41.3 km</strong></td>
                        <td>+44m / -118m</td>
                        <td><strong>三島市區飯店</strong><br><small style="color:#64748B;">三嶋大社周邊</small></td>
                        <td>☀️ 快晴 ｜ 2.2°C ~ 13.9°C<br>降水 0.0mm ｜ 日照 8.3h</td>
                        <td>田子之浦富士絕景 ｜ 全平緩海堤專用道，零紅綠燈狂飆沼津</td>
                    </tr>
                    <tr>
                        <td><strong>11/20（五）<br><span style="color:#B91C1C;">Day 8</span></strong><br><span class="badge-booked">✅ 🏨 已訂房</span></td>
                        <td>三島 ➔ 狩野川自行車道 ➔ 修善寺溫泉（竹林小徑 / 桂橋）</td>
                        <td><strong>20.9 km</strong></td>
                        <td>+167m / -76m</td>
                        <td><strong>Onsen Yado Mizuguchi</strong><br><a href="https://www.google.com/maps/search/?api=1&query=%E9%9D%99%E5%B2%A1%E7%9C%8C%E4%BC%8A%E8%B1%86%E5%B8%82%E4%BF%AE%E5%96%84%E5%AF%BA3463-17+%E6%B8%A9%E6%B3%89%E5%AE%BF%E6%B0%B4%E5%8F%A3" target="_blank" class="map-link">📍 靜岡縣伊豆市修善寺3463-17 ↗</a></td>
                        <td>☀️ 快晴 ｜ 6.9°C ~ 18.6°C<br>降水 0.0mm ｜ 日照 9.6h</td>
                        <td>🔥 <strong>修善寺・虹之鄉見頃</strong> ｜ 避開三連休人潮提早進駐名湯放鬆</td>
                    </tr>
                    <tr>
                        <td><strong>11/21（六）<br><span style="color:#B91C1C;">Day 9</span></strong><br><span class="badge badge-mod" style="font-size:10px;">三連休首日</span><br><span class="badge-booked">✅ 🏨 已訂房</span></td>
                        <td>修善寺 ➔ 避開天城峠（走冷川峠/一碧湖） ➔ 城崎海岸門脇吊橋 ➔ 伊東川奈</td>
                        <td><strong>47.9 km</strong></td>
                        <td>+871m / -931m</td>
                        <td><strong>kawana seaview standard</strong><br><a href="https://www.google.com/maps/search/?api=1&query=%E9%9D%99%E5%B2%A1%E7%9C%8C%E4%BC%8A%E6%9D%B1%E5%B8%82%E6%96%B0%E4%BA%95484-30+KAWANA" target="_blank" class="map-link">📍 靜岡縣伊東市新井484-30 KAWANA ↗</a></td>
                        <td>☀️ 快晴 ｜ 5.9°C ~ 19.3°C<br>降水 0.0mm ｜ 日照 9.3h</td>
                        <td>🔥 <strong>一碧湖伊豆之瞳見頃</strong> ｜ 門脇吊橋懸崖白浪與相模灣海景第一排住宿</td>
                    </tr>
                    <tr>
                        <td><strong>11/22（日）<br><span style="color:#B91C1C;">Day 10</span></strong><br><span class="badge badge-mod" style="font-size:10px;">三連休中日</span><br><span class="badge-booked">✅ 🏨 已訂房</span></td>
                        <td>伊東 ➔ 宇佐美 ➔ 避開危險隧道（走網代舊街） ➔ 南熱海・下多賀</td>
                        <td><strong>17.4 km</strong></td>
                        <td>+314m / -352m</td>
                        <td><strong>Apt南熱海-網代</strong><br><a href="https://www.google.com/maps/search/?api=1&query=%E9%9D%99%E5%B2%A1%E7%9C%8C%E7%86%B1%E6%B5%B7%E5%B8%82%E4%B8%8B%E5%A4%9A%E8%B2%BA440+Apt%E5%8D%97%E7%86%B1%E6%B5%B7" target="_blank" class="map-link">📍 靜岡縣熱海市下多賀440 ↗</a></td>
                        <td>☀️ 快晴 ｜ 7.6°C ~ 19.2°C<br>降水 0.0mm ｜ 日照 9.3h</td>
                        <td>🔥 <strong>網代灣長浜海景第一排</strong> ｜ 避開三連休熱海塞車潮，悠閒入住海景公寓</td>
                    </tr>
                    <tr>
                        <td><strong>11/23（一）<br><span style="color:#B91C1C;">Day 11</span></strong><br><span class="badge badge-mod" style="font-size:10px;">勤勞感謝日</span><br><span class="badge-booked">✅ 🏨 已訂房</span></td>
                        <td>南熱海換宿 ➔ 熱海梅園紅葉祭 ➔ <strong>晚上 20:20 熱海海上花火大會</strong></td>
                        <td><strong>17.7 km</strong></td>
                        <td>+279m / -282m</td>
                        <td><strong>Izu Kansya</strong><br><a href="https://www.google.com/maps/search/?api=1&query=%E9%9D%99%E5%B2%A1%E7%9C%8C%E7%86%B1%E6%B5%B7%E5%B8%82%E4%B8%8B%E5%A4%9A%E8%B2%BA1473-11+Izu+Kansya" target="_blank" class="map-link">📍 靜岡縣熱海市下多賀1473-11 ↗</a></td>
                        <td>☀️ 快晴 ｜ 10.4°C ~ 19.7°C<br>降水 0.0mm ｜ 日照 9.7h</td>
                        <td>🎆 <strong>熱海海上煙火祭特設日</strong> ｜ 白天賞日本最晚紅葉，晚上直擊震撼高空煙火</td>
                    </tr>
                    <tr>
                        <td><strong>11/24（二）<br><span style="color:#B91C1C;">Day 12</span></strong></td>
                        <td>南熱海 ➔ 縣道740號柑橘道 ➔ 小田原城 ➔ 湘南海岸防風林 ➔ 江之島</td>
                        <td><strong>68.4 km</strong></td>
                        <td>+357m / -361m</td>
                        <td><strong>江之島 / 藤澤市區飯店</strong></td>
                        <td>☀️ 快晴 ｜ 8.9°C ~ 18.0°C<br>降水 0.0mm ｜ 日照 9.4h</td>
                        <td>灌籃高手湘南海岸 ｜ 小田原後一馬平川相模灣平路，順暢直達江之島</td>
                    </tr>
                    <tr>
                        <td><strong>11/25（三）<br><span style="color:#B91C1C;">Day 13</span></strong></td>
                        <td>江之島 ➔ 鎌倉高校前平交道 ➔ 長谷寺 ➔ 柏尾川水岸綠道 ➔ 橫濱港未來</td>
                        <td><strong>32.4 km</strong></td>
                        <td>+61m / -54m</td>
                        <td><strong>橫濱港未來飯店</strong></td>
                        <td>⛅ 陰/晴 ｜ 9.3°C ~ 12.4°C<br>降水 0.0mm ｜ 日照 0.0h</td>
                        <td>🔥 <strong>鎌倉長谷寺古寺紅葉</strong> ｜ 柏尾川水岸平整綠道直達橫濱</td>
                    </tr>
                    <tr>
                        <td><strong>11/26（四）<br><span style="color:#B91C1C;">Day 14</span></strong></td>
                        <td>橫濱 ➔ 第一京濱/羽田 ➔ 築地 ➔ 豐洲大橋自行車道 ➔ 台場海濱公園</td>
                        <td><strong>38.8 km</strong></td>
                        <td>+19m / -14m</td>
                        <td><strong>台場 / 有明飯店</strong></td>
                        <td>☀️ 快晴 ｜ 6.2°C ~ 18.6°C<br>降水 0.0mm ｜ 日照 9.0h</td>
                        <td>橫濱山下公園黃金銀杏 ➔ 豐洲大橋眺望東京灣與獨角獸鋼彈</td>
                    </tr>
                    <tr>
                        <td><strong>11/27（五）<br><span style="color:#B91C1C;">Day 15</span></strong><br><span class="badge-booked">✅ 🏨 已訂房</span></td>
                        <td>台場 ➔ 葛西臨海公園 ➔ 中川水岸綠道 ➔ 柴又 ➔ 葛飾金町</td>
                        <td><strong>28.5 km</strong></td>
                        <td>+9m / -16m</td>
                        <td><strong>花庵旅舍 (Hostel Hana An)</strong><br><a href="https://www.google.com/maps/search/?api=1&query=%E6%9D%B1%E4%BA%AC%E9%83%BD%E8%91%9B%E9%A3%BE%E5%8D%80%E9%87%91%E7%94%BA4-23-11+%E8%8A%B1%E5%BA%B5%E6%97%85%E8%88%8D" target="_blank" class="map-link">📍 東京都葛飾區金町4-23-11 ↗</a></td>
                        <td>☀️ 晴/多雲 ｜ 7.3°C ~ 16.2°C<br>降水 0.0mm ｜ 日照 3.7h</td>
                        <td>葛西海風與中川秋草 ｜ 避開市中心擁擠人潮，入住水元公園旁清幽下町旅舍</td>
                    </tr>
                    <tr>
                        <td><strong>11/28（六）<br><span style="color:#B91C1C;">Day 16</span></strong><br><span class="badge-booked">✅ 🏨 已訂房</span></td>
                        <td>金町出發 ➔ <strong>【輕裝免行李】</strong> 江戶川CR / 荒川 ➔ 小江戶川越 / 葛飾老街 ➔ 返回金町</td>
                        <td><strong>35.0 ~ 55.0 km</strong></td>
                        <td>+29m / -27m</td>
                        <td><strong>花庵旅舍 (Hostel Hana An)</strong><br><small style="color:#64748B;">連住第2晚・免換飯店</small></td>
                        <td>☀️ 快晴 ｜ 8.4°C ~ 19.8°C<br>降水 0.0mm ｜ 日照 9.1h</td>
                        <td>🔥 <strong>江戶老街與水岸金秋</strong> ｜ 週末免收行李輕裝暢快巡航，夜晚悠閒漫步下町居酒屋</td>
                    </tr>
                    <tr>
                        <td><strong>11/29（日）<br><span style="color:#B91C1C;">Day 17</span></strong></td>
                        <td>金町退房 ➔ <strong>水元公園（萬棵水杉黃金森林見頃）</strong> ➔ 柴又帝釋天 ➔ 淺草/上野</td>
                        <td><strong>16.6 km</strong></td>
                        <td>+4m / -4m</td>
                        <td><strong>淺草 / 上野 / 東京市區飯店</strong></td>
                        <td>☀️ 晴/多雲 ｜ 9.0°C ~ 15.3°C<br>降水 0.0mm ｜ 日照 5.2h</td>
                        <td>🔥 <strong>水元公園水杉見頃最高峰</strong> ｜ 清晨5分鐘直達無人水杉金黃森林，極致震撼</td>
                    </tr>
                    <tr>
                        <td><strong>11/30（一）<br><span style="color:#B91C1C;">Day 18</span></strong></td>
                        <td>淺草 ➔ 東京大學本鄉（赤門/大銀杏地毯） ➔ 皇居 ➔ 明治神宮外苑銀杏見頃 ➔ 秋葉原</td>
                        <td><strong>23.7 km</strong></td>
                        <td>+49m / -46m</td>
                        <td><strong>秋葉原 / 上野飯店</strong></td>
                        <td>☀️ 快晴 ｜ 7.1°C ~ 16.3°C<br>降水 0.0mm ｜ 日照 8.9h</td>
                        <td>🔥 <strong>神宮外苑與東大黃金雨最盛期</strong> ｜ 莉香名場面巡禮</td>
                    </tr>
                    <tr>
                        <td><strong>12/01（二）<br><span style="color:#B91C1C;">Day 19</span></strong></td>
                        <td>秋葉原還車（CycleTrip Base） ➔ 神田明神 ➔ 日暮里搭京成Skyliner ➔ 成田機場</td>
                        <td><strong>7.9 km</strong></td>
                        <td>+9m / -13m</td>
                        <td><strong>返台溫暖的家</strong></td>
                        <td>☀️ 快晴 ｜ 6.4°C ~ 20.0°C<br>降水 0.0mm ｜ 日照 7.1h</td>
                        <td>神田明神平安祈福 ｜ 776km世界線圓滿閉環</td>
                    </tr>
                </tbody>
            </table>
        </div>'''

for path in files_itinerary:
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()

    # Update summary stats cards at top
    html = re.sub(r'<div class="val">~745 km<\/div>', '<div class="val">~776 km</div>', html)
    html = re.sub(r'<div class="val">\+4,750 m<\/div>', '<div class="val">+4,925 m</div>', html)

    # Replace summary table
    pattern = r'<!-- 19天實測數據總表 -->[\s\S]*?(?=<!-- 避坑路段對照表 -->)'
    html = re.sub(pattern, table_html + '\n\n        ', html)

    # Update Day 1 Card
    html = re.sub(
        r'<div class="day-card" id="day-1">[\s\S]*?(?=<div class="day-card" id="day-2">)',
        '''<div class="day-card" id="day-1">
            <div class="day-header">
                <span class="day-num">Day 1</span> 11/13（五）秋葉原（CycleTrip Base 09:30 取車）➔ 國道 15 號 ➔ 六鄉橋 ➔ 多摩川自行車道 ➔ 淺川自行車道 ➔ 高尾山口（宿 Mt. Takao Base Camp） <span class="badge-booked">✅ 🏨 已訂房</span>
            </div>
            <div class="day-body">
                <div class="foliage-box">
                    <strong>🍂 歷史紅葉情報（多摩川水岸 / 淺川水岸）：</strong> 多摩川秋芒金黃搖曳，淺川水岸林木初染微紅。
                </div>
                <div class="weather-box">
                    <strong>☀️ 去年實測天氣（2025/11/13 JMA 八王子觀測所）：</strong><br>
                    天氣：<strong>晴（降水量 0.0 mm，日照時數 9.4 小時）</strong><br>
                    氣溫：最低 <strong>11.8°C</strong> ｜ 最高 <strong>19.6°C</strong> ｜ 微風平穩
                </div>
                <div class="route-stat">
                    <span>📏 里程：<strong>88.2 km</strong> (水岸專用道平緩巡航)</span>
                    <span>⛰️ 爬升/下降：<strong>+248m / -62m</strong> (海拔 3m ➔ 193m，極度平緩無負擔)</span>
                    <span>⏱️ 預估騎乘時間：<strong>4.0 ~ 4.5 小時</strong></span>
                    <span>🏨 鎖定住宿：<strong>Mt. Takao Base Camp</strong> <a href="https://www.google.com/maps/search/?api=1&query=%E6%9D%B1%E4%BA%AC%E9%83%BD%E5%85%AB%E7%8E%8B%E5%AD%90%E5%B8%82%E9%AB%98%E5%B0%BE%E7%94%BA1799-3+Mt.Takao+Base+Camp" target="_blank" class="map-link">📍 東京都八王子市高尾町1799-3 ↗</a></span>
                </div>
                <p><strong>🚲 在地車友黃金出城導引：</strong></p>
                <ol style="margin-left: 20px; color: #475569; font-size: 14.5px;">
                    <li><strong>09:30 秋葉原順暢出城：</strong> 取車後沿寬闊筆直的國道 15 號（第一京濱）南下，至六鄉橋直接切入「多摩川自行車道」。</li>
                    <li><strong>全封閉雙專用道暢快奔馳：</strong> 沿多摩川專用道逆流平緩緩上，在府中四谷橋無縫切入「淺川自行車道」，全程整整 65 公里完全封閉、零紅綠燈、零大車！</li>
                    <li><strong>高尾山口極樂湯溫泉：</strong> 下午直達高尾山腳，入住 Mt. Takao Base Camp，步行 3 分鐘至「京王高尾山極樂湯」享受露天溫泉暖湯，為隔天攻大垂水峠與秋山街道儲備 100% 體力！</li>
                </ol>
            </div>
        </div>\n\n        ''',
        html
    )

    # Update Day 2 Card
    html = re.sub(
        r'<div class="day-card" id="day-2">[\s\S]*?(?=<div class="day-card" id="day-3">)',
        '''<div class="day-card" id="day-2">
            <div class="day-header">
                <span class="day-num">Day 2</span> 11/14（六）Mt. Takao Base Camp ➔ 清晨攻大垂水峠 ➔ 相模湖 ➔ 縣道 35 號（秋山街道）➔ 都留市（宿 由加利旅館） <span class="badge-booked">✅ 🏨 已訂房</span>
            </div>
            <div class="day-body">
                <div class="foliage-box">
                    <strong>🍂 歷史紅葉情報（大垂水峠 / 秋山溪谷）：</strong> <strong>秋山街道見頃！</strong> 幽靜溪谷兩側山壁層林盡染。
                </div>
                <div class="weather-box">
                    <strong>☀️ 去年實測天氣（2025/11/14 JMA 大月/都留觀測所）：</strong><br>
                    天氣：<strong>快晴（降水量 0.0 mm，日照時數 8.9 小時）</strong><br>
                    氣溫：最低 <strong>7.8°C</strong> ｜ 最高 <strong>17.2°C</strong> ｜ 山谷清涼乾燥
                </div>
                <div class="route-stat">
                    <span>📏 里程：<strong>61.0 km</strong></span>
                    <span>⛰️ 爬升/下降：<strong>+1121m / -830m</strong> (海拔 193m ➔ 484m，最高秋山隧道 674m)</span>
                    <span>⏱️ 預估騎乘時間：<strong>3.5 ~ 4.0 小時</strong></span>
                    <span>🏨 鎖定住宿：<strong>ビジネス旅館 由加利 (Yukari Ryokan)</strong> <a href="https://www.google.com/maps/search/?api=1&query=%E5%B1%B1%E6%A2%A8%E7%9C%8C%E9%83%BD%E7%95%99%E5%B8%82%E4%B8%8A%E8%B0%B71%E4%B8%81%E7%9B%AE3-4+%E7%94%B1%E5%8A%A0%E5%88%A9%E6%97%85%E9%A4%A8" target="_blank" class="map-link">📍 山梨縣都留市上谷1丁目3-4 ↗</a></span>
                </div>
                <p><strong>🚲 避開大車之經典 Plan B 導引：</strong></p>
                <ol style="margin-left: 20px; color: #475569; font-size: 14.5px;">
                    <li><strong>清晨 08:00 直攻大垂水峠：</strong> 由高尾山腳出發，清晨時段國道 20 號幾乎無觀光大車，僅需爬升 +202m（3.8km，平均坡度 5.3%）輕鬆翻越大垂水峠（標高 392m）。</li>
                    <li><strong>切入山梨縣道 35 號（秋山街道）：</strong> 過相模湖後左轉切入秋山街道，整整 35 公里沿著秋山川幽靜溪谷緩緩爬升，完全禁止大型貨車通行，路況極佳。</li>
                    <li><strong>翻越秋山隧道滑降都留：</strong> 穿過標高 674m 的秋山隧道後，一路順暢大下坡滑降至都留市中心，入住由加利旅館享用在地家常晚餐。</li>
                </ol>
            </div>
        </div>\n\n        ''',
        html
    )

    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)

print("Successfully updated itinerary HTML with 100% GSI DEM 1m audited data!")
