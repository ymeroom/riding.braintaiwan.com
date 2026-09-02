import re, json

# 1. Update all_19days_route_data.json Day 2 timeline & tips
with open('d:/2026東京單車騎旅/all_19days_route_data.json', 'r', encoding='utf-8') as f:
    all_data = json.load(f)

for item in all_data:
    if item['day'] == 2:
        item['timeline'] = [
            {
                "name": "起點：Mt. Takao Base Camp (高尾山口 190m)",
                "km": 0.0,
                "type": "start",
                "coord": [139.2708, 35.6315],
                "desc": "08:30 退房出發，直接踏上國道 20 號（甲州街道），展開今日唯一一段主要爬升。"
            },
            {
                "name": "唯一主要峠道：大垂水峠 (標高 392m)",
                "km": 4.3,
                "type": "pivot",
                "coord": [139.2390, 35.6170],
                "desc": "《頭文字D》經典山道！平均坡度 5.3%，由高尾山口踩踏 4.3 公里（爬升 200m）即輕鬆攻頂，跨越東京都與神奈川縣界。"
            },
            {
                "name": "甲州街道順降：千木良 (Chigira 240m)",
                "km": 10.8,
                "type": "waypoint",
                "coord": [139.2130, 35.6120],
                "desc": "沿國道 20 號一路順暢滑降，穿過千木良集落，直抵相模湖畔。"
            },
            {
                "name": "🌊 湖光山色絕景：神奈川縣立相模湖公園 (175m)",
                "km": 14.1,
                "type": "scenic",
                "coord": [139.1880, 35.6135],
                "desc": "🚨 必停打卡點！左轉下切湖畔木棧道，遠眺對岸嵐山楓紅與平靜湖面倒影，在湖畔露天座喝杯熱咖啡。"
            },
            {
                "name": "桂川河谷順騎：藤野 ➔ 上野原 (205m)",
                "km": 24.5,
                "type": "waypoint",
                "coord": [139.1080, 35.6280],
                "desc": "告別陡坡，沿著桂川河谷平緩順騎（坡度僅 0.5%~1%），兩側秋山峽谷夾道。"
            },
            {
                "name": "🍁 國寶名勝／午餐：日本三奇橋「甲斐猿橋」大黑屋",
                "km": 42.0,
                "type": "rest",
                "coord": [138.9800, 35.6150],
                "desc": "🍁 絕景午餐！於橋頭老舖【大黑屋】俯瞰 30 米深谷懸空木橋與楓紅，享用手打蕎麥麵／忠治烏龍麵（備案：大月站前 濱野屋）。"
            },
            {
                "name": "關鍵轉折：大月站前 ➔ 切入國道 139 號 (358m)",
                "km": 48.2,
                "type": "pivot",
                "coord": [138.9400, 35.6100],
                "desc": "抵達大月市區，告別國道 20 號，左轉切入【國道 139 號（富士道）】，沿清澈的桂川逆流平緩漫騎 12 公里。"
            },
            {
                "name": "終點：ビジネス旅館 由加利 (都留市 475m)",
                "km": 60.4,
                "type": "end",
                "coord": [138.9065, 35.5525],
                "desc": "抵達富士急行線都留文科大學前站旁，入住昭和日式和風旅館，單車安全停妥，大浴場泡熱水澡徹底放鬆！"
            }
        ]
        item['expert_tip'] = "💡 <strong>在地車友實戰解析：</strong> 徹底放棄爬升破千米的秋山深山隧道，改走經典【國道20號河谷直達線 ➔ 相模湖公園水岸 ➔ 日本三奇橋猿橋 ➔ 大月 ➔ 國道139 ➔ 都留】！除了出發後 4 公里爬大垂水峠（+200m）外，後續 50 公里沿著桂川河谷緩緩平騎（坡度 < 1%），輕鬆暢遊猿橋紅葉絕景！<div style='margin-top:8px; padding-top:8px; border-top:1px dashed rgba(59,130,246,0.3); font-size:11.5px; color:#DDD6FE;'><strong style='color:#C084FC;'>🎬 聖地巡禮：</strong> 《頭文字D》（甲州街道大垂水峠飆車傳說）；《歌川廣重》（浮世繪名勝・甲陽猿橋之圖）；俳聖松尾芭蕉隱居名所（都留市芭蕉館）</div>"

with open('d:/2026東京單車騎旅/all_19days_route_data.json', 'w', encoding='utf-8') as f:
    json.dump(all_data, f, ensure_ascii=False)

# 2. Enrich Day 2 card in tokyo_fuji_cycling_itinerary_19days_v2.html & index.html
with open('d:/2026東京單車騎旅/tokyo_fuji_cycling_itinerary_19days_v2.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Build comprehensive Day 2 Card content
day2_card_replacement = """        <!-- Day 2 -->
        <div class="day-card" id="day-2">
            <div class="day-header">
                <div>
                    <div class="day-title"><span class="day-num">Day 2</span> 11/14（六）高尾山口 ➔ 甲州街道(國道20) ➔ 大垂水峠(392m) ➔ 相模湖 ➔ 日本三奇橋(猿橋) ➔ 大月 ➔ 國道139 ➔ 都留</div>
                    <div class="day-stats">
                        60.4 km ｜ <span class="elev-pill">+1049 m / -762 m</span> ｜ 海拔 175~475m（低爬升桂川河谷直達線）
                    </div>
                </div>
            </div>

            <div class="route-step"><span class="step-label">路線：</span>Mt. Takao Base Camp (08:30 出發) ➔ 國道 20 號（甲州街道） ➔ 攻頂【大垂水峠（標高392m）】 ➔ 順暢滑降經【千木良】 ➔ 🌊 <strong>【相模湖公園】水岸木棧道（遠眺嵐山紅葉倒影、湖畔熱咖啡）</strong> ➔ 藤野 ➔ 上野原 ➔ 桂川河谷緩平騎行 ➔ 🍁 <strong>國寶名勝【日本三奇橋・甲斐猿橋】</strong> ➔ 大月站前切入【國道 139 號】 ➔ 沿桂川水岸逆流緩騎 12km ➔ 都留市 ビジネス旅館 由加利</div>

            <!-- 午餐與景觀推薦 -->
            <div style="background: #F0FDF4; border: 1px solid #86EFAC; border-left: 4px solid #16A34A; border-radius: 8px; padding: 12px 14px; margin-bottom: 12px; font-size: 13px; color: #166534;">
                <strong style="color: #15803D; font-size: 13.5px;">🍴 中午絕景推薦（第 42 km 處）：</strong><br>
                ・<strong>【大黑屋】甲斐猿橋畔 絕景手打蕎麥麵／忠治烏龍麵</strong>：坐在正對 30 公尺深峽谷懸空木橋的和風座席，一邊吃熱騰騰蕎麥麵、一邊賞滿山楓紅絕景！（<a href="https://www.google.com/maps/search/?api=1&query=大黒屋+山梨県大月市猿橋町" target="_blank" style="color: #15803D; font-weight: 700; text-decoration: underline;">📍 Google Maps 導航 ↗</a>）<br>
                ・<em>備案</em>：【大月站前 濱野屋】大月名物「おつけだんご」手作蔬菜小麥糰子湯定食。
            </div>

            <!-- 晚餐自由選擇專區 -->
            <div style="background: #FFFBEB; border: 1px solid #FCD34D; border-left: 4px solid #D97706; border-radius: 8px; padding: 12px 14px; margin-bottom: 14px; font-size: 13px; color: #92400E;">
                <strong style="color: #B45309; font-size: 13.5px;">🍻 晚餐自由選擇（由加利旅館大浴場泡完澡後，步行 2～4 分鐘即達）：</strong>
                <ul style="margin: 6px 0 0 16px; padding: 0; line-height: 1.6;">
                    <li><strong>🍢 方案一（炭火串燒居酒屋）：【炭火串焼 居酒屋 どんぐり】</strong>（步行 2 分鐘）<br>
                    職人炭火現烤串燒拼盤 ✕ 甲斐名物烤香魚 ✕ 冰鎮生啤酒／山梨在地清酒七賢，放鬆暢飲首選！（<a href="https://www.google.com/maps/search/?api=1&query=居酒屋+どんぐり+都留市" target="_blank" style="color: #B45309; font-weight: 700; text-decoration: underline;">📍 Google Maps 導航 ↗</a>）</li>
                    <li><strong>🍜 方案二（山梨靈魂手打麵）：【富士山名水手打 吉田烏龍麵】</strong>（步行 3 分鐘）<br>
                    極具勁道嚼勁的粗麵條 ✕ 燉肉片 ✕ 鮮甜高麗菜，搭配獨門香辣醬「すりだね」，碳水爆發！</li>
                    <li><strong>🍱 方案三（和風海鮮老舖定食）：【江戸八 (Edohachi)】</strong>（步行 4 分鐘）<br>
                    刺身天婦羅御膳 ✕ 特選厚切炸豬排，搭配富士山名水炊煮的香甜白米飯，份量十足。（<a href="https://www.google.com/maps/search/?api=1&query=江戸八+都留市" target="_blank" style="color: #B45309; font-weight: 700; text-decoration: underline;">📍 Google Maps 導航 ↗</a>）</li>
                </ul>
            </div>

            <div class="hotel-box">
                <div class="hotel-name">🏨 住宿：ビジネス旅館 由加利（都留市）</div>
                <div class="hotel-address">地址：山梨縣都留市上谷1丁目3-4（富士急行線「都留文科大學前」站正前方，步行 1 分鐘）</div>
                <div class="booking-status status-booked">✅ 已完成訂房 ｜ 榻榻米和室、大浴場泡湯放鬆雙腿</div>
                <div class="bike-store-info">🚲 傳統日式和風商務旅館，單車可安心停放於館內玄關或指定安全區域</div>
                <a href="https://www.google.com/maps/search/?api=1&query=山梨県都留市上谷1丁目3-4+ビジネス旅館+由加利" target="_blank" class="hotel-link">📍 在 Google Maps 查看旅館位置 ↗</a>
            </div>

            <div class="weather-box">
                <span class="weather-icon">☀️</span> 去年實測：快晴（萬里無雲） ｜ 氣溫 7.8°C ~ 17.2°C ｜ 降水 0.0mm ｜ 日照 8.9h ｜ 風速 1.8m/s
            </div>

            <div class="foliage-box">
                <span class="foliage-icon">🍁</span> 紅葉預測：相模湖畔與桂川峽谷紅葉見頃 ｜ 甲斐猿橋兩側楓紅絕景 ｜ 都留市山景染紅
            </div>

            <div class="highlight-badge">
                💡 <strong>在地車友避坑實戰解析：</strong> 徹底放棄爬升破千米的秋山深山隧道，改走經典【國道20號河谷直達線 ➔ 相模湖公園水岸 ➔ 日本三奇橋猿橋 ➔ 大月 ➔ 國道139 ➔ 都留】！除了出發後 4 公里爬大垂水峠（+200m）外，後續 50 公里沿著桂川河谷緩緩平騎（坡度 < 1%），輕鬆暢遊猿橋紅葉絕景！
                <div style="margin-top: 8px; padding-top: 8px; border-top: 1px dashed rgba(43,76,89,0.3); font-size: 12.5px; color: var(--secondary);">
                    🎬 <strong>聖地巡禮：</strong> 《頭文字D》（甲州街道大垂水峠飆車傳說）；《歌川廣重》（浮世繪名勝・甲陽猿橋之圖）；俳聖松尾芭蕉隱居名所（都留市芭蕉館）
                </div>
            </div>
            
            <div style="margin-top: 14px; display: flex; gap: 10px; flex-wrap: wrap;">
                <a href="day2_route_map_demo.html" class="hotel-link" style="background: #2563EB; color: #FFFFFF; font-weight: 700; text-decoration: none; display: inline-flex; align-items: center; gap: 6px;">🗺️ 查看 Day 2 獨立詳細地圖與標高 Demo ➔</a>
                <a href="day2_track.gpx" download="day2_track.gpx" class="hotel-link" style="background: #D97724; color: #FFFFFF; font-weight: 700; text-decoration: none; display: inline-flex; align-items: center; gap: 6px;">💾 下載 Day 2 GPX 軌跡檔</a>
            </div>
        </div>"""

# Replace existing Day 2 Card
html = re.sub(
    r'<!-- Day 2 -->\s*<div class="day-card" id="day-2">.*?</div>\s*<!-- Day 3 -->',
    day2_card_replacement + '\n\n        <!-- Day 3 -->',
    html,
    flags=re.DOTALL
)

files = [
    'd:/2026東京單車騎旅/tokyo_fuji_cycling_itinerary_19days_v2.html',
    'd:/2026東京單車騎旅/index.html',
    'C:/Users/ymero/Downloads/tokyo_fuji_cycling_itinerary_19days_v2.html',
    'C:/Users/ymero/Downloads/index.html'
]

for fp in files:
    with open(fp, 'w', encoding='utf-8') as f:
        f.write(html)

print("Enriched Day 2 itinerary with Sagami Lake view, Saruhashi lunch, and 3 dinner options!")
