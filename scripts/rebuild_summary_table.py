import sys, re

files_itinerary = [
    'C:/Users/ymero/Downloads/tokyo_fuji_cycling_itinerary_19days_v2.html',
    'd:/2026東京單車騎旅/tokyo_fuji_cycling_itinerary_19days_v2.html'
]

# Clean, unified, 7-column table definition
table_html = '''        <!-- 19天實測數據總表 -->
        <h2 class="section-title">📊 19日每日里程、爬升、去年實測天氣與紅葉見頃總覽</h2>
        <div class="table-wrapper">
            <table>
                <thead>
                    <tr>
                        <th style="width: 11%;">📅 日期（週幾）/ 天數</th>
                        <th style="width: 22%;">🚲 當日區間與核心騎行路線</th>
                        <th style="width: 8%;">📏 里程</th>
                        <th style="width: 9%;">⛰️ 爬升/下降</th>
                        <th style="width: 16%;">🏨 推薦住宿地點</th>
                        <th style="width: 17%;">☀️ 去年實測天氣 (氣溫/降水/日照)</th>
                        <th style="width: 17%;">🍁 紅葉見頃實績與避坑亮點</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td><strong>11/13（五）<br><span style="color:#B91C1C;">Day 1</span></strong></td>
                        <td>秋葉原 ➔ 國道15號 ➔ 六鄉橋 ➔ 多摩川CR ➔ 淺川CR ➔ 高尾山口</td>
                        <td><strong>78.0 km</strong></td>
                        <td>+228m / -46m</td>
                        <td><strong>Mt. Takao Base Camp</strong><br><small style="color:#64748B;">步行3分至高尾山極樂湯</small></td>
                        <td>☀️ 晴 ｜ 11.8°C ~ 19.6°C<br>降水 0.0mm ｜ 日照 9.4h</td>
                        <td>多摩水岸秋芒 ｜ 雙專用道全程零紅綠燈直達高尾山腳</td>
                    </tr>
                    <tr>
                        <td><strong>11/14（六）<br><span style="color:#B91C1C;">Day 2</span></strong></td>
                        <td>Mt. Takao Base Camp ➔ 大垂水峠 ➔ 相模湖 ➔ 縣道35秋山街道 ➔ 都留市</td>
                        <td><strong>54.0 km</strong></td>
                        <td>+850m / -556m</td>
                        <td><strong>ビジネス旅館 由加利</strong><br><small style="color:#64748B;">都留市中心生活圈</small></td>
                        <td>☀️ 快晴 ｜ 7.8°C ~ 17.2°C<br>降水 0.0mm ｜ 日照 8.9h</td>
                        <td>秋山溪谷初紅 ｜ 清晨避開大車，秋山街道35km零貨車幽靜溪谷</td>
                    </tr>
                    <tr>
                        <td><strong>11/15（日）<br><span style="color:#B91C1C;">Day 3</span></strong></td>
                        <td>由加利旅館 ➔ <strong>【晴】衝山中湖+忍野 / 【陰】走新倉山五重塔</strong> ➔ 河口湖</td>
                        <td><strong>22.2 ~ 54.9 km</strong></td>
                        <td>+532m ~ +775m</td>
                        <td><strong>Orange Cabin Inn</strong><br><small style="color:#64748B;">連住第1晚・紅葉迴廊旁</small></td>
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
                        <td><strong>48.0 km</strong></td>
                        <td>+180m / -890m</td>
                        <td><strong>富士宮市區飯店</strong><br><small style="color:#64748B;">淺間大社總本社旁</small></td>
                        <td>☀️ 萬里晴空 ｜ 4.2°C ~ 15.8°C<br>降水 0.0mm ｜ 日照 9.0h</td>
                        <td>朝霧高原黃金芒草 ｜ 自海拔900m一路千米大長下坡滑降富士宮</td>
                    </tr>
                    <tr>
                        <td><strong>11/19（四）<br><span style="color:#B91C1C;">Day 7</span></strong></td>
                        <td>富士宮 ➔ 潤井川CR ➔ 田子の浦港 ➔ 駿河灣千本松原海堤 ➔ 沼津 ➔ 三島</td>
                        <td><strong>72.0 km</strong></td>
                        <td>+110m / -980m</td>
                        <td><strong>三島市區飯店</strong><br><small style="color:#64748B;">三嶋大社周邊</small></td>
                        <td>☀️ 快晴 ｜ 2.2°C ~ 13.9°C<br>降水 0.0mm ｜ 日照 8.3h</td>
                        <td>田子之浦富士絕景 ｜ 全封閉海岸堤防專用道，零紅綠燈狂飆沼津</td>
                    </tr>
                    <tr>
                        <td><strong>11/20（五）<br><span style="color:#B91C1C;">Day 8</span></strong></td>
                        <td>三島 ➔ 狩野川自行車道 ➔ 修善寺溫泉（竹林小徑 / 桂橋）</td>
                        <td><strong>21.9 km</strong></td>
                        <td>+100m / -42m</td>
                        <td><strong>修善寺名湯溫泉旅館</strong><br><small style="color:#64748B;">古湯石疊溫泉街</small></td>
                        <td>☀️ 快晴 ｜ 6.9°C ~ 18.6°C<br>降水 0.0mm ｜ 日照 9.6h</td>
                        <td>🔥 <strong>修善寺・虹之鄉見頃</strong> ｜ 避開三連休人潮提早進駐名湯放鬆</td>
                    </tr>
                    <tr>
                        <td><strong>11/21（六）<br><span style="color:#B91C1C;">Day 9</span></strong><br><span class="badge badge-mod" style="font-size:10px;">三連休首日</span></td>
                        <td>修善寺 ➔ 避開天城峠（走冷川峠/一碧湖） ➔ 城崎海岸門脇吊橋 ➔ 伊東</td>
                        <td><strong>42.2 km</strong></td>
                        <td>+510m / -600m</td>
                        <td><strong>伊東溫泉海濱飯店</strong></td>
                        <td>☀️ 快晴 ｜ 5.9°C ~ 19.3°C<br>降水 0.0mm ｜ 日照 9.3h</td>
                        <td>🔥 <strong>一碧湖伊豆之瞳見頃</strong> ｜ 門脇吊橋懸崖白浪與4000年熔岩海岸</td>
                    </tr>
                    <tr>
                        <td><strong>11/22（日）<br><span style="color:#B91C1C;">Day 10</span></strong><br><span class="badge badge-mod" style="font-size:10px;">三連休中日</span></td>
                        <td>伊東 ➔ 避開宇佐美網代隧道（走網代舊街） ➔ 熱海梅園最晚紅葉祭</td>
                        <td><strong>31.5 km</strong></td>
                        <td>+460m / -465m</td>
                        <td><strong>熱海海濱溫泉飯店</strong></td>
                        <td>☀️ 快晴 ｜ 7.6°C ~ 19.2°C<br>降水 0.0mm ｜ 日照 9.3h</td>
                        <td>🔥 <strong>熱海梅園日本最晚紅葉</strong> ｜ 昭和復古夜景與月光之道</td>
                    </tr>
                    <tr>
                        <td><strong>11/23（一）<br><span style="color:#B91C1C;">Day 11</span></strong><br><span class="badge badge-mod" style="font-size:10px;">勤勞感謝日</span></td>
                        <td>熱海 ➔ 避開江之浦隧道（切入縣道740號柑橘景觀道） ➔ 小田原城</td>
                        <td><strong>23.5 km</strong></td>
                        <td>+286m / -279m</td>
                        <td><strong>小田原市區飯店</strong><br><small style="color:#64748B;">小田原城下町</small></td>
                        <td>☀️ 快晴 ｜ 10.4°C ~ 19.7°C<br>降水 0.0mm ｜ 日照 9.7h</td>
                        <td>小田原城護城河楓紅 ｜ 縣道740俯瞰相模灣海景與蜜柑山坡</td>
                    </tr>
                    <tr>
                        <td><strong>11/24（二）<br><span style="color:#B91C1C;">Day 12</span></strong></td>
                        <td>小田原 ➔ 國道1號 ➔ 茅崎烏帽子岩 ➔ 湘南海岸防風林 ➔ 江之島</td>
                        <td><strong>38.7 km</strong></td>
                        <td>+65m / -71m</td>
                        <td><strong>江之島 / 藤澤飯店</strong></td>
                        <td>☀️ 快晴 ｜ 8.9°C ~ 18.0°C<br>降水 0.0mm ｜ 日照 9.4h</td>
                        <td>灌籃高手湘南海岸 ｜ 遠眺富士冠頂與相模灣深邃海景</td>
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

for path in files_itinerary:
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()

    # Match and replace the entire summary table section
    pattern = r'<!-- 19天實測數據總表 -->[\s\S]*?(?=<!-- 避坑路段對照表 -->)'
    html = re.sub(pattern, table_html + '\n\n        ', html)

    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)

print("Successfully updated master summary table columns and all 19 rows aligned!")
