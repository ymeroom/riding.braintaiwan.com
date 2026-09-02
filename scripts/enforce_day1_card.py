import re

# Complete perfect Day 1 Card
day1_card_html = """        <!-- 第一階段 -->
        <div class="stage-header">
            <span>第一階段：多摩川水岸出城 ➔ 桂川河谷 ➔ 富士五湖賞楓最盛期</span>
            <span>Day 1 – Day 6</span>
        </div>

        <!-- Day 1 -->
        <div class="day-card" id="day-1">
            <div class="day-header">
                <div>
                    <div class="day-title"><span class="day-num">Day 1</span> 11/13（五）秋葉原取車 ➔ 國道15號 ➔ 六鄉橋 ➔ 多摩川CR ➔ 府中四谷橋 ➔ 淺川CR ➔ 南淺川橋 ➔ 高尾山口</div>
                    <div style="margin-top: 6px;">
                        <a href="day1_route_map_demo.html" target="_blank" style="display: inline-flex; align-items: center; gap: 4px; background: #2563EB; color: #FFFFFF; padding: 4px 12px; border-radius: 6px; font-size: 12.5px; font-weight: 700; text-decoration: none; box-shadow: 0 2px 6px rgba(37,99,235,0.3);">🗺️ 開啟 Day 1 具體地圖 Demo (NAVITIME/Leaflet/GPX) ➔</a>
                    </div>
                    <div class="day-stats" style="margin-top: 8px;">
                        81.5 km ｜ <span class="elev-pill">+245 m / -55 m</span> ｜ 海拔 3~193m（多摩川＋淺川水岸純平路）
                        <span class="weather-pill">☀️ 11.8~19.6°C ｜ 0mm</span>
                        <span class="koyo-pill">🍁 郊區初染紅</span>
                    </div>
                </div>
            </div>

            <div class="route-step"><span class="step-label">路線：</span>
                <ul style="margin: 8px 0 0 16px; padding: 0; line-height: 1.75; font-size: 13.5px;">
                    <li><strong>起點：秋葉原 CycleTrip Base（0 km）</strong><br>
                    09:30 取車、配件檢查、安裝手機導航架與馬鞍包、胎壓確認、加購免責保險 (CDW)。</li>
                    <li><strong>市區順暢出城段：國道15號 (第一京濱)（5.2 km）</strong><br>
                    經銀座、品川，國道 15 號路肩寬達 1.5~2 米、柏油平整，順暢往南出城。</li>
                    <li><strong>午餐名店推薦：蒲田 とんかつ 檍 (Aoki)（19.5 km）</strong><br>
                    🥩 平日限定「上等里肌豬排定食」（170g 林SPF特選黑豚，肉質粉嫩多汁配大碗熱豚汁！單車停大田區公設蒲田東口駐輪場，前 2 小時免費）。（<a href="https://www.google.com/maps/search/?api=1&query=とんかつ檍+蒲田本店" target="_blank" style="color: #15803D; font-weight: 700; text-decoration: underline;">📍 Google Maps 導航 ↗</a>）</li>
                    <li><strong>關鍵轉折點：六鄉橋 ➔ 多摩川自行車專用道（22 km）</strong><br>
                    🚨 離開國道 15 號，直接下引道切入【多摩川自行車專用道（左岸堤防）】，正式告別紅綠燈與汽車！</li>
                    <li><strong>水岸專用道：二子玉川・兵庫島公園（31.6 km）</strong><br>
                    沿多摩川左岸堤頂專用道暢騎，眺望秋芒金黃搖曳，享受全封閉無車流巡航。</li>
                    <li><strong>專用道無縫切換：府中四谷橋 ➔ 淺川自行車道（54.5 km）</strong><br>
                    🚨 橫跨府中四谷橋，無縫銜接【淺川自行車專用道 (浅川ゆったりロード)】，沿清澈溪水逆流緩上。</li>
                    <li><strong>合流點轉折：鶴巻橋 ➔ 南淺川自行車道（71 km）</strong><br>
                    🚨 於八王子市役所旁鶴巻橋，順勢切入【南淺川自行車專用道 (南浅川遊歩道)】，直指高尾山麓！</li>
                    <li><strong>秋色水岸：陵南公園・南淺川橋（76.5 km）</strong><br>
                    南淺川兩側林木染紅，水質清冽見底，平坦專用道一路通往高尾車站周邊。</li>
                    <li><strong>終點：Mt. Takao Base Camp (高尾山腳)（81.5 km）</strong><br>
                    抵達高尾山腳（海拔 190m），入住專業戶外單車基地，步行 3 分鐘泡京王高尾山極樂湯露天溫泉！</li>
                </ul>
            </div>

            <!-- 晚餐雙軌推薦 -->
            <div style="background: #FFFBEB; border: 1px solid #FCD34D; border-left: 4px solid #D97706; border-radius: 8px; padding: 12px 14px; margin-bottom: 14px; font-size: 13px; color: #92400E;">
                <strong style="color: #B45309; font-size: 13.5px;">♨️ 晚餐雙軌決策（抵達高尾山口後）：</strong>
                <ul style="margin: 6px 0 0 16px; padding: 0; line-height: 1.6;">
                    <li><strong>方案 A（早到首選・16:30 前抵達）：【高橋家】180年老舖 山藥泥蕎麥麵 ＋ 舞菇天婦羅</strong>（17:30 閉店前壓線享用名物，步行 3 分鐘）。（<a href="https://www.google.com/maps/search/?api=1&query=高橋家+高尾山口" target="_blank" style="color: #B45309; font-weight: 700; text-decoration: underline;">📍 Google Maps 導航 ↗</a>）</li>
                    <li><strong>方案 B（最強保底・17:00 後抵達）：【京王高尾山溫泉 極樂湯 食堂】</strong>（營業至 22:00，L.O. 21:30），穿浴衣悠閒享用高尾山藥泥蕎麥麵定食與冰生啤！（<a href="https://www.google.com/maps/search/?api=1&query=京王高尾山温泉+極楽湯" target="_blank" style="color: #B45309; font-weight: 700; text-decoration: underline;">📍 Google Maps 導航 ↗</a>）</li>
                    <li><strong>方案 C（夜間小酌）：【Mt. Takao Base Camp 一樓 Cafe & Bar】</strong>（週五營業至 20:30），多摩在地精釀生啤酒 ✕ 特製手打牛肉漢堡。</li>
                </ul>
            </div>

            <div class="hotel-box">
                <div class="hotel-name">🏨 住宿：Mt. Takao Base Camp（高尾山腳）</div>
                <div class="hotel-address">地址：東京都八王子市高尾町1799-3（京王高尾山口站步行 3 分鐘）</div>
                <div class="booking-status status-booked">✅ 已完成訂房 ｜ 專業戶外單車基地、步行 3 分鐘泡極樂湯露天溫泉</div>
                <div class="bike-store-info">🚲 戶外活動大本營，門口與室內設專用單車停放架，單車安全無虞</div>
                <a href="https://www.google.com/maps/search/?api=1&query=東京都八王子市高尾町1799-3+Mt.Takao+Base+Camp" target="_blank" class="hotel-link">📍 在 Google Maps 查看旅館位置 ↗</a>
            </div>

            <div class="weather-box">
                <span class="weather-icon">☀️</span> 去年實測：晴朗乾燥 ｜ 氣溫 11.8°C ~ 19.6°C ｜ 降水 0.0mm ｜ 日照 9.4h ｜ 體感涼爽舒適，非常適合出城熱身。
            </div>

            <div class="foliage-box">
                <span class="foliage-icon">🍁</span> 紅葉預測：多摩川水岸秋芒盛開 ｜ 淺川水岸林木初染紅 ｜ 高尾山麓秋色初顯
            </div>

            <div class="highlight-badge">
                💡 <strong>在地避坑實戰：</strong> 放棄穿越世田谷區綠道（暗渠步道多處禁騎且路擋密集），改採「第一京濱 ＋ 多摩川/淺川/南淺川三段自行車專用道」，整整 58 公里全封閉、零紅綠燈直達高尾山腳！
                <div style="margin-top: 8px; padding-top: 8px; border-top: 1px dashed rgba(43,76,89,0.3); font-size: 12.5px; color: var(--secondary);">
                    🎬 <strong>聖地巡禮：</strong> 《命運石之門 Steins;Gate》（秋葉原電器街、廣播會館）、《飆速宅男》（多摩川水岸特訓） ｜ 《正宗哥吉拉 Shin Godzilla》（多摩川防衛線、丸子橋作戰名場面）
                </div>
            </div>
            
            <div style="margin-top: 14px; display: flex; gap: 10px; flex-wrap: wrap;">
                <a href="day1_route_map_demo.html" class="hotel-link" style="background: #2563EB; color: #FFFFFF; font-weight: 700; text-decoration: none; display: inline-flex; align-items: center; gap: 6px;">🗺️ 查看 Day 1 獨立詳細地圖與標高 Demo ➔</a>
                <a href="day1_track.gpx" download="day1_track.gpx" class="hotel-link" style="background: #D97724; color: #FFFFFF; font-weight: 700; text-decoration: none; display: inline-flex; align-items: center; gap: 6px;">💾 下載 Day 1 GPX 軌跡檔</a>
            </div>
        </div>"""

files = [
    'd:/2026東京單車騎旅/tokyo_fuji_cycling_itinerary_19days_v2.html',
    'd:/2026東京單車騎旅/index.html',
    'C:/Users/ymero/Downloads/tokyo_fuji_cycling_itinerary_19days_v2.html',
    'C:/Users/ymero/Downloads/index.html'
]

for fp in files:
    with open(fp, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace stage header and Day 1 card
    content = re.sub(
        r'<!-- 第一階段 -->.*?<!-- Day 2 -->',
        day1_card_html + '\n\n        <!-- Day 2 -->',
        content,
        flags=re.DOTALL
    )

    with open(fp, 'w', encoding='utf-8') as f:
        f.write(content)

print("Enforced accurate Day 1 Card across all portal files!")
