import sys, re

files_itinerary = [
    'C:/Users/ymero/Downloads/tokyo_fuji_cycling_itinerary_19days_v2.html',
    'd:/2026東京單車騎旅/tokyo_fuji_cycling_itinerary_19days_v2.html'
]

# CSS style additions for badge-booked and map-link
css_addon = '''
        .badge-booked {
            background: #059669;
            color: #FFFFFF;
            padding: 2px 7px;
            border-radius: 4px;
            font-size: 11px;
            font-weight: 700;
            display: inline-block;
            margin-top: 3px;
            letter-spacing: 0.3px;
            box-shadow: 0 1px 3px rgba(5, 150, 105, 0.2);
        }
        .map-link {
            color: #0284C7;
            text-decoration: none;
            font-weight: 600;
            display: inline-flex;
            align-items: center;
            gap: 2px;
        }
        .map-link:hover {
            text-decoration: underline;
            color: #0369A1;
        }
'''

# New Table HTML with Booked Badges and Google Maps links
table_html = '''        <!-- 19天實測數據總表 -->
        <h2 class="section-title">📊 19日每日里程、爬升、去年實測天氣與紅葉見頃總覽</h2>
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
                        <td><strong>78.0 km</strong></td>
                        <td>+228m / -46m</td>
                        <td><strong>Mt. Takao Base Camp</strong><br><a href="https://www.google.com/maps/search/?api=1&query=%E6%9D%B1%E4%BA%AC%E9%83%BD%E5%85%AB%E7%8E%8B%E5%AD%90%E5%B8%82%E9%AB%98%E5%B0%BE%E7%94%BA1799-3+Mt.Takao+Base+Camp" target="_blank" class="map-link">📍 東京都八王子市高尾町1799-3 ↗</a></td>
                        <td>☀️ 晴 ｜ 11.8°C ~ 19.6°C<br>降水 0.0mm ｜ 日照 9.4h</td>
                        <td>多摩水岸秋芒 ｜ 雙專用道全程零紅綠燈直達高尾山腳</td>
                    </tr>
                    <tr>
                        <td><strong>11/14（六）<br><span style="color:#B91C1C;">Day 2</span></strong><br><span class="badge-booked">✅ 🏨 已訂房</span></td>
                        <td>Mt. Takao Base Camp ➔ 大垂水峠 ➔ 相模湖 ➔ 縣道35秋山街道 ➔ 都留市</td>
                        <td><strong>54.0 km</strong></td>
                        <td>+850m / -556m</td>
                        <td><strong>ビジネス旅館 由加利</strong><br><a href="https://www.google.com/maps/search/?api=1&query=%E5%B1%B1%E6%A2%A8%E7%9C%8C%E9%83%BD%E7%95%99%E5%B8%82%E4%B8%8A%E8%B0%B71%E4%B8%81%E7%9B%AE3-4+%E7%94%B1%E5%8A%A0%E5%88%A9%E6%97%85%E9%A4%A8" target="_blank" class="map-link">📍 山梨縣都留市上谷1丁目3-4 ↗</a></td>
                        <td>☀️ 快晴 ｜ 7.8°C ~ 17.2°C<br>降水 0.0mm ｜ 日照 8.9h</td>
                        <td>秋山溪谷初紅 ｜ 清晨避開大車，秋山街道35km零貨車幽靜溪谷</td>
                    </tr>
                    <tr>
                        <td><strong>11/15（日）<br><span style="color:#B91C1C;">Day 3</span></strong><br><span class="badge-booked">✅ 🏨 已訂房</span></td>
                        <td>由加利旅館 ➔ <strong>【晴】衝山中湖+忍野 / 【陰】走新倉山五重塔</strong> ➔ 河口湖</td>
                        <td><strong>22.2 ~ 54.9 km</strong></td>
                        <td>+532m ~ +775m</td>
                        <td><strong>Orange Cabin Inn</strong><br><a href="https://www.google.com/maps/search/?api=1&query=%E5%B1%B1%E6%A2%A8%E7%9C%8C%E5%8D%97%E9%83%BD%E7%95%99%E9%83%A1%E5%84%82%E5%A3%AB%E6%B2%B3%E5%8F%A3%E6%B9%96%E7%94%BA%E6%B2%B3%E5%8F%A31916-3+Orange+Cabin+Inn" target="_blank" class="map-link">📍 山梨縣富士河口湖町河口1916-3 ↗</a></td>
                        <td>☀️ 快晴 ｜ 4.5°C ~ 15.1°C<br>降水 0.0mm ｜ 日照 9.6h</td>
                        <td>🔥 <strong>雙湖見頃最盛期</strong> ｜ 晴雨雙軌決策，晚上賞紅葉迴廊點燈</td>
                    </tr>
                    <tr>
                        <td><strong>11/16（一）<br><span style="color:#B91C1C;">Day 4</span></strong></td>
                        <td>清晨獨享紅葉迴廊 ➔ 富士五湖深度探索 ➔ <strong>【當日機動決定】</strong></td>
                        <td><strong>25.0 ~ 52.7 km</strong></td>
                        <td>+250m ~ +629m</td>
                        <td><strong>當日視天候體力機動決定</strong><br><small style="color:#64748B;">連住木屋 / 浩庵 / kagelow</small></td>
                        <td>☀️ 快晴 ｜ 3.2°C ~ 14.6°C<br>降水 0.0mm ｜ 日照 9.1h</td>
                        <td>🔥 <strong>紅葉迴廊見頃最高峰</strong> ｜ 清晨06:30獨享無人晨光深紅隧道</td>
                    </tr>
                    <tr>
                        <td><strong>11/17（二）<br><span style="color:#B91C1C;">Day 5</span></strong></td>
                        <td><strong>【五湖天候核心緩衝日】</strong> 西湖療癒之里 ➔ 青木原樹海 ➔ 溫泉休整</td>
                        <td><strong>15.0 ~ 30.0 km</strong></td>
                        <td>+150m ~ +280m</td>
                        <td><strong>本棲湖浩庵 / 河口湖 / 富士吉田</strong></td>
                        <td>☀️ 晴朗 ｜ 5.8°C ~ 16.4°C<br>降水 0.0mm ｜ 日照 8.8h</td>
                        <td>🔥 <strong>西湖/本棲湖深秋紅葉</strong> ｜ 高原天候定海神針，防雨防初雪防低溫</td>
                    </tr>
                    <tr>
                        <td><strong>11/18（三）<br><span style="color:#B91C1C;">Day 6</span></strong></td>
                        <td>本棲湖浩庵（千圓逆富士） ➔ 朝霧高原牧場 ➔ 白糸之瀑 ➔ 富士宮市</td>
                        <td><strong>39.6 km</strong></td>
                        <td>+151m / -933m</td>
                        <td><strong>富士宮市區飯店</strong><br><small style="color:#64748B;">淺間大社總本社旁</small></td>
                        <td>☀️ 萬里晴空 ｜ 4.2°C ~ 15.8°C<br>降水 0.0mm ｜ 日照 9.0h</td>
                        <td>朝霧高原黃金芒草 ｜ 自海拔900m一路近千米大長下坡滑降富士宮</td>
                    </tr>
                    <tr>
                        <td><strong>11/19（四）<br><span style="color:#B91C1C;">Day 7</span></strong></td>
                        <td>富士宮 ➔ 潤井川CR ➔ 田子の浦港 ➔ 駿河灣千本松原海堤 ➔ 沼津 ➔ 三島</td>
                        <td><strong>41.3 km</strong></td>
                        <td>+32m / -118m</td>
                        <td><strong>三島市區飯店</strong><br><small style="color:#64748B;">三嶋大社周邊</small></td>
                        <td>☀️ 快晴 ｜ 2.2°C ~ 13.9°C<br>降水 0.0mm ｜ 日照 8.3h</td>
                        <td>田子之浦富士絕景 ｜ 全平緩海堤專用道（+32m/-118m），零紅綠燈狂飆沼津</td>
                    </tr>
                    <tr>
                        <td><strong>11/20（五）<br><span style="color:#B91C1C;">Day 8</span></strong><br><span class="badge-booked">✅ 🏨 已訂房</span></td>
                        <td>三島 ➔ 狩野川自行車道 ➔ 修善寺溫泉（竹林小徑 / 桂橋）</td>
                        <td><strong>20.9 km</strong></td>
                        <td>+262m / -188m</td>
                        <td><strong>Onsen Yado Mizuguchi</strong><br><a href="https://www.google.com/maps/search/?api=1&query=%E9%9D%99%E5%B2%A1%E7%9C%8C%E4%BC%8A%E8%B1%86%E5%B8%82%E4%BF%AE%E5%96%84%E5%AF%BA3463-17+%E6%B8%A9%E6%B3%89%E5%AE%BF%E6%B0%B4%E5%8F%A3" target="_blank" class="map-link">📍 靜岡縣伊豆市修善寺3463-17 ↗</a></td>
                        <td>☀️ 快晴 ｜ 6.9°C ~ 18.6°C<br>降水 0.0mm ｜ 日照 9.6h</td>
                        <td>🔥 <strong>修善寺・虹之鄉見頃</strong> ｜ 避開三連休人潮提早進駐名湯放鬆</td>
                    </tr>
                    <tr>
                        <td><strong>11/21（六）<br><span style="color:#B91C1C;">Day 9</span></strong><br><span class="badge badge-mod" style="font-size:10px;">三連休首日</span><br><span class="badge-booked">✅ 🏨 已訂房</span></td>
                        <td>修善寺 ➔ 避開天城峠（走冷川峠/一碧湖） ➔ 城崎海岸門脇吊橋 ➔ 伊東川奈</td>
                        <td><strong>47.9 km</strong></td>
                        <td>+888m / -824m</td>
                        <td><strong>kawana seaview standard</strong><br><a href="https://www.google.com/maps/search/?api=1&query=%E9%9D%99%E5%B2%A1%E7%9C%8C%E4%BC%8A%E6%9D%B1%E5%B8%82%E6%96%B0%E4%BA%95484-30+KAWANA" target="_blank" class="map-link">📍 靜岡縣伊東市新井484-30 KAWANA ↗</a></td>
                        <td>☀️ 快晴 ｜ 5.9°C ~ 19.3°C<br>降水 0.0mm ｜ 日照 9.3h</td>
                        <td>🔥 <strong>一碧湖伊豆之瞳見頃</strong> ｜ 門脇吊橋懸崖白浪與相模灣海景第一排住宿</td>
                    </tr>
                    <tr>
                        <td><strong>11/22（日）<br><span style="color:#B91C1C;">Day 10</span></strong><br><span class="badge badge-mod" style="font-size:10px;">三連休中日</span><br><span class="badge-booked">✅ 🏨 已訂房</span></td>
                        <td>伊東 ➔ 宇佐美 ➔ 避開危險隧道（走網代舊街） ➔ 南熱海・下多賀</td>
                        <td><strong>15.1 km</strong></td>
                        <td>+330m / -326m</td>
                        <td><strong>Apt南熱海-網代</strong><br><a href="https://www.google.com/maps/search/?api=1&query=%E9%9D%99%E5%B2%A1%E7%9C%8C%E7%86%B1%E6%B5%B7%E5%B8%82%E4%B8%8B%E5%A4%9A%E8%B2%BA440+Apt%E5%8D%97%E7%86%B1%E6%B5%B7" target="_blank" class="map-link">📍 靜岡縣熱海市下多賀440 ↗</a></td>
                        <td>☀️ 快晴 ｜ 7.6°C ~ 19.2°C<br>降水 0.0mm ｜ 日照 9.3h</td>
                        <td>🔥 <strong>網代灣長浜海景第一排</strong> ｜ 避開三連休熱海塞車潮，悠閒入住海景公寓</td>
                    </tr>
                    <tr>
                        <td><strong>11/23（一）<br><span style="color:#B91C1C;">Day 11</span></strong><br><span class="badge badge-mod" style="font-size:10px;">勤勞感謝日</span><br><span class="badge-booked">✅ 🏨 已訂房</span></td>
                        <td>南熱海換宿 ➔ 熱海梅園紅葉祭 ➔ <strong>晚上 20:20 熱海海上花火大會</strong></td>
                        <td><strong>17.7 km</strong></td>
                        <td>+340m / -336m</td>
                        <td><strong>Izu Kansya</strong><br><a href="https://www.google.com/maps/search/?api=1&query=%E9%9D%99%E5%B2%A1%E7%9C%8C%E7%86%B1%E6%B5%B7%E5%B8%82%E4%B8%8B%E5%A4%9A%E8%B2%BA1473-11+Izu+Kansya" target="_blank" class="map-link">📍 靜岡縣熱海市下多賀1473-11 ↗</a></td>
                        <td>☀️ 快晴 ｜ 10.4°C ~ 19.7°C<br>降水 0.0mm ｜ 日照 9.7h</td>
                        <td>🎆 <strong>熱海海上煙火祭特設日</strong> ｜ 白天賞日本最晚紅葉，晚上直擊震撼高空煙火</td>
                    </tr>
                    <tr>
                        <td><strong>11/24（二）<br><span style="color:#B91C1C;">Day 12</span></strong></td>
                        <td>南熱海 ➔ 縣道740號柑橘道 ➔ 小田原城 ➔ 湘南海岸防風林 ➔ 江之島</td>
                        <td><strong>68.4 km</strong></td>
                        <td>+302m / -303m</td>
                        <td><strong>江之島 / 藤澤市區飯店</strong></td>
                        <td>☀️ 快晴 ｜ 8.9°C ~ 18.0°C<br>降水 0.0mm ｜ 日照 9.4h</td>
                        <td>灌籃高手湘南海岸 ｜ 小田原後一馬平川相模灣平路，順暢直達江之島</td>
                    </tr>
                    <tr>
                        <td><strong>11/25（三）<br><span style="color:#B91C1C;">Day 13</span></strong></td>
                        <td>江之島 ➔ 鎌倉高校前平交道 ➔ 長谷寺 ➔ 柏尾川水岸綠道 ➔ 橫濱港未來</td>
                        <td><strong>33.5 km</strong></td>
                        <td>+215m / -214m</td>
                        <td><strong>橫濱港未來飯店</strong></td>
                        <td>⛅ 陰/晴 ｜ 9.3°C ~ 12.4°C<br>降水 0.0mm ｜ 日照 0.0h</td>
                        <td>🔥 <strong>鎌倉長谷寺古寺紅葉</strong> ｜ 柏尾川水岸平整綠道直達橫濱</td>
                    </tr>
                    <tr>
                        <td><strong>11/26（四）<br><span style="color:#B91C1C;">Day 14</span></strong></td>
                        <td>橫濱 ➔ 第一京濱/羽田 ➔ 築地 ➔ 豐洲大橋自行車道 ➔ 台場海濱公園</td>
                        <td><strong>34.0 km</strong></td>
                        <td>+40m / -40m</td>
                        <td><strong>台場 / 有明飯店</strong></td>
                        <td>☀️ 快晴 ｜ 6.2°C ~ 18.6°C<br>降水 0.0mm ｜ 日照 9.0h</td>
                        <td>橫濱山下公園黃金銀杏 ➔ 豐洲大橋眺望東京灣與獨角獸鋼彈</td>
                    </tr>
                    <tr>
                        <td><strong>11/27（五）<br><span style="color:#B91C1C;">Day 15</span></strong></td>
                        <td>台場 ➔ 葛西臨海公園 ➔ 荒川自行車道（右岸全柏油） ➔ 赤羽岩淵赤水門</td>
                        <td><strong>38.0 km</strong></td>
                        <td>+27m / -26m</td>
                        <td><strong>赤羽 / 王子飯店</strong></td>
                        <td>☀️ 晴/多雲 ｜ 7.3°C ~ 16.2°C<br>降水 0.0mm ｜ 日照 3.7h</td>
                        <td>荒川河畔金黃芒草 ｜ 金八老師河堤與百年岩淵赤水門</td>
                    </tr>
                    <tr>
                        <td><strong>11/28（六）<br><span style="color:#B91C1C;">Day 16</span></strong></td>
                        <td>赤羽 ➔ 荒川CR ➔ 入間川CR ➔ 小江戶川越喜多院（藏造老街）</td>
                        <td><strong>56.5 km</strong></td>
                        <td>+36m / -41m</td>
                        <td><strong>川越市區飯店</strong></td>
                        <td>☀️ 快晴 ｜ 8.4°C ~ 19.8°C<br>降水 0.0mm ｜ 日照 9.1h</td>
                        <td>🔥 <strong>川越喜多院古寺紅葉</strong> ｜ 時之鐘與藏造黑瓦老街風貌</td>
                    </tr>
                    <tr>
                        <td><strong>11/29（日）<br><span style="color:#B91C1C;">Day 17</span></strong></td>
                        <td>川越 ➔ 荒川CR ➔ 葛飾水元公園（萬棵水杉黃金森林） ➔ 柴又帝釋天 ➔ 淺草</td>
                        <td><strong>36.4 km</strong></td>
                        <td>+37m / -19m</td>
                        <td><strong>淺草 / 上野飯店</strong></td>
                        <td>☀️ 晴/多雲 ｜ 9.0°C ~ 15.3°C<br>降水 0.0mm ｜ 日照 5.2h</td>
                        <td>🔥 <strong>葛飾水元公園萬棵水杉見頃</strong> ｜ 寅次郎柴又老街與雷門</td>
                    </tr>
                    <tr>
                        <td><strong>11/30（一）<br><span style="color:#B91C1C;">Day 18</span></strong></td>
                        <td>淺草 ➔ 東京大學本鄉（赤門/大銀杏地毯） ➔ 皇居 ➔ 明治神宮外苑銀杏見頃 ➔ 秋葉原</td>
                        <td><strong>22.0 km</strong></td>
                        <td>+73m / -87m</td>
                        <td><strong>秋葉原 / 上野飯店</strong></td>
                        <td>☀️ 快晴 ｜ 7.1°C ~ 16.3°C<br>降水 0.0mm ｜ 日照 8.9h</td>
                        <td>🔥 <strong>神宮外苑與東大黃金雨最盛期</strong> ｜ 莉香名場面巡禮</td>
                    </tr>
                    <tr>
                        <td><strong>12/01（二）<br><span style="color:#B91C1C;">Day 19</span></strong></td>
                        <td>秋葉原還車（CycleTrip Base） ➔ 神田明神 ➔ 日暮里搭京成Skyliner ➔ 成田機場</td>
                        <td><strong>8.0 km</strong></td>
                        <td>+10m / -10m</td>
                        <td><strong>返台溫暖的家</strong></td>
                        <td>☀️ 快晴 ｜ 6.4°C ~ 20.0°C<br>降水 0.0mm ｜ 日照 7.1h</td>
                        <td>神田明神平安祈福 ｜ 745km世界線圓滿閉環</td>
                    </tr>
                </tbody>
            </table>
        </div>'''

# Update Day 8 & Day 9 Card details
day8_card_new = '''<div class="day-card" id="day-8">
            <div class="day-header">
                <span class="day-num">Day 8</span> 11/20（五）三島 ➔ 狩野川自行車道 ➔ 修善寺溫泉（宿 Onsen Yado Mizuguchi） <span class="badge-booked">✅ 🏨 已訂房</span>
            </div>
            <div class="day-body">
                <div class="foliage-box">
                    <strong>🍂 歷史紅葉情報（修善寺溫泉街 / 虹之鄉）：</strong> <strong>見頃最盛期！</strong> 竹林小徑桂橋楓紅，古湯石疊溫泉街。
                </div>
                <div class="weather-box">
                    <strong>☀️ 去年實測天氣（2025/11/20 JMA 修善寺觀測所）：</strong><br>
                    天氣：<strong>快晴（降水量 0.0 mm，日照時數 9.6 小時）</strong><br>
                    氣溫：最低 <strong>6.9°C</strong> ｜ 最高 <strong>18.6°C</strong> ｜ 溫泉谷地微風宜人
                </div>
                <div class="route-stat">
                    <span>📏 里程：<strong>20.9 km</strong> (超輕鬆短程名湯休整)</span>
                    <span>⛰️ 爬升/下降：<strong>+262m / -188m</strong> (海拔 24m ➔ 101m)</span>
                    <span>⏱️ 預估騎乘時間：<strong>1.5 ~ 2.0 小時</strong></span>
                    <span>🏨 鎖定住宿：<strong>Onsen Yado Mizuguchi（温泉宿 水口）</strong> <a href="https://www.google.com/maps/search/?api=1&query=%E9%9D%99%E5%B2%A1%E7%9C%8C%E4%BC%8A%E8%B1%86%E5%B8%82%E4%BF%AE%E5%96%84%E5%AF%BA3463-17+%E6%B8%A9%E6%B3%89%E5%AE%BF%E6%B0%B4%E5%8F%A3" target="_blank" class="map-link">📍 靜岡縣伊豆市修善寺3463-17 ↗</a></span>
                </div>
                <p><strong>🚲 名湯休整騎行導引：</strong></p>
                <ol style="margin-left: 20px; color: #475569; font-size: 14.5px;">
                    <li><strong>狩野川自行車道漫騎：</strong> 由三島出發，沿著清澈平緩的狩野川專用道逆流而上，一路欣賞伊豆鄉村風光與遠方山景。</li>
                    <li><strong>提早入住修善寺名湯：</strong> 中午過後抵達修善寺，入住「温泉宿 水口（修善寺3463-17）」，換上浴衣漫步竹林小徑、獨鈷之湯與修禪寺。</li>
                    <li><strong>虹之鄉紅葉點燈：</strong> 傍晚探訪虹之鄉賞夜楓，回旅館享受正宗伊豆溫泉暖湯與會席料理，身心徹底回血！</li>
                </ol>
            </div>
        </div>\n\n        '''

day9_card_new = '''<div class="day-card" id="day-9">
            <div class="day-header">
                <span class="day-num">Day 9</span> 11/21（六・三連休首日）修善寺 ➔ 冷川峠 ➔ 一碧湖 ➔ 城崎海岸 ➔ 伊東川奈（宿 kawana seaview standard） <span class="badge-booked">✅ 🏨 已訂房</span>
            </div>
            <div class="day-body">
                <div class="foliage-box">
                    <strong>🍂 歷史紅葉情報（一碧湖 / 伊豆高原）：</strong> <strong>見頃最盛期！</strong> 一碧湖倒映滿山楓紅，被譽為「伊豆之瞳」。
                </div>
                <div class="weather-box">
                    <strong>☀️ 去年實測天氣（2025/11/21 JMA 伊東/一碧湖觀測所）：</strong><br>
                    天氣：<strong>快晴（降水量 0.0 mm，日照時數 9.3 小時）</strong><br>
                    氣溫：最低 <strong>5.9°C</strong> ｜ 最高 <strong>19.3°C</strong> ｜ 東伊豆海岸陽光燦爛
                </div>
                <div class="route-stat">
                    <span>📏 里程：<strong>47.9 km</strong></span>
                    <span>⛰️ 爬升/下降：<strong>+888m / -824m</strong></span>
                    <span>⏱️ 預估騎乘時間：<strong>3.0 ~ 3.5 小時</strong></span>
                    <span>🏨 鎖定住宿：<strong>kawana seaview standard (KAWANA)</strong> <a href="https://www.google.com/maps/search/?api=1&query=%E9%9D%99%E5%B2%A1%E7%9C%8C%E4%BC%8A%E6%9D%B1%E5%B8%82%E6%96%B0%E4%BA%95484-30+KAWANA" target="_blank" class="map-link">📍 靜岡縣伊東市新井484-30 KAWANA ↗</a></span>
                </div>
                <p><strong>🚲 在地車友避坑與絕景走法導引：</strong></p>
                <ol style="margin-left: 20px; color: #475569; font-size: 14.5px;">
                    <li><strong>果斷放棄天城峠，走冷川峠舊道：</strong> 徹底避開三連休天城峠大塞車與觀光大巴，走幽靜無車的縣道 12 號（冷川峠）平緩翻越中伊豆。</li>
                    <li><strong>探訪一碧湖與城崎海岸：</strong> 漫步一碧湖紅葉步道，隨後抵達城崎海岸門脇吊橋，俯瞰 4000 年大室山熔岩注入太平洋的壯闊海蝕崖。</li>
                    <li><strong>入住川奈海景標準房：</strong> 傍晚抵達「kawana seaview standard（伊東市新井484-30）」，在房間窗前欣賞相模灣海平線日落與滿天星斗！</li>
                </ol>
            </div>
        </div>\n\n        '''

for path in files_itinerary:
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()

    # Add CSS styles if not present
    if '.badge-booked' not in html:
        html = html.replace('/* 避坑速查表格 */', css_addon + '\n        /* 避坑速查表格 */')

    # Replace summary table
    pattern = r'<!-- 19天實測數據總表 -->[\s\S]*?(?=<!-- 避坑路段對照表 -->)'
    html = re.sub(pattern, table_html + '\n\n        ', html)

    # Replace Day 8 & Day 9 cards
    html = re.sub(r'<div class="day-card" id="day-8">[\s\S]*?(?=<div class="day-card" id="day-9">)', day8_card_new, html)
    html = re.sub(r'<div class="day-card" id="day-9">[\s\S]*?(?=<div class="day-card" id="day-10">)', day9_card_new, html)

    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)

print("Successfully updated itinerary HTML with badges and Google Maps links for all booked hotels!")
