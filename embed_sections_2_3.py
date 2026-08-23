import sys, re

files_itinerary = [
    'C:/Users/ymero/Downloads/tokyo_fuji_cycling_itinerary_19days_v2.html',
    'd:/2026東京單車騎旅/tokyo_fuji_cycling_itinerary_19days_v2.html'
]

# Comprehensive Pre-Trip Reminders HTML Section
reminders_section_html = '''        <!-- 出發前關鍵購票、裝備與穿搭提醒專區 -->
        <div style="background: #F8FAFC; border: 1px solid #CBD5E1; border-radius: 12px; padding: 22px; margin-bottom: 28px; box-shadow: 0 4px 12px rgba(0,0,0,0.03);">
            <h2 style="font-size: 18px; color: #1E293B; margin-top: 0; margin-bottom: 16px; display: flex; align-items: center; gap: 8px; border-bottom: 2px solid #E2E8F0; padding-bottom: 10px;">
                📋 出發前關鍵待辦、取車裝備與洋蔥穿搭提醒事項
            </h2>

            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 16px;">
                
                <!-- 區塊一：10/20 購票提醒 -->
                <div style="background: #F0FDF4; border: 1px solid #86EFAC; border-left: 5px solid #16A34A; border-radius: 8px; padding: 16px;">
                    <h3 style="font-size: 15px; color: #15803D; margin-top: 0; margin-bottom: 10px; display: flex; align-items: center; gap: 6px;">
                        ⏰ 一、 機場交通與 10/20 購票提醒
                    </h3>
                    <ul style="margin-left: 18px; font-size: 13.5px; line-height: 1.65; color: #166534; padding-left: 0;">
                        <li><strong>📅 10/20（二）重要購票（出發前24天）：</strong> 購買「外國人特惠 Skyliner e-ticket」（全包式 ¥2,310）。
                            <br>・<strong>票券內容</strong>：已包含「乘車券」＋「特急指定席券」（<span style="color:#B91C1C; font-weight:700;">完全不需要 Suica！</span>）。
                        </li>
                        <li><strong>零排隊刷臉進站【Face Check in Go】：</strong> 官網買完後上傳自拍照註冊臉部。下機抵達成田機場改札口走「人臉辨識專用通道」，刷臉 1 秒開門進站，閘門自動吐出座位小票，100% 免排隊！</li>
                        <li><strong>日暮里站轉乘神技：</strong> 坐到日暮里站內專用轉乘口，站內直接轉 JR 山手線/京濱東北線 2 站（4分鐘）直達秋葉原。</li>
                    </ul>
                </div>

                <!-- 區塊二：CycleTrip 取車與裝備避坑 -->
                <div style="background: #EFF6FF; border: 1px solid #93C5FD; border-left: 5px solid #2563EB; border-radius: 8px; padding: 16px;">
                    <h3 style="font-size: 15px; color: #1D4ED8; margin-top: 0; margin-bottom: 10px; display: flex; align-items: center; gap: 6px;">
                        🚲 二、 CycleTrip Base 取車與配件確認
                    </h3>
                    <ul style="margin-left: 18px; font-size: 13.5px; line-height: 1.65; color: #1E40AF; padding-left: 0;">
                        <li><strong>車輛配件確認（出發前/現場逐項檢查）：</strong>
                            <br>・💡 <strong>高流明前燈（重要）</strong>：11 月中旬日本約 16:30 即日落，建議前燈流明數在 <strong>400～800 lumens</strong> 以上。
                            <br>・💡 <strong>後警示燈（紅色高亮）</strong>：騎行秋山街道（Day 2）與伊豆海岸隧道時必備。
                            <br>・💡 <strong>簡易維修組</strong>：確認隨車附有隨身打氣筒、挖胎棒、備用內胎（確認同規格氣嘴長度）。
                        </li>
                        <li><strong>單車保險（CDW）：</strong> 取車時建議加購店家提供的<strong>「免責補償保險（事故自負額減免）」</strong>，騎行更安心無憂。</li>
                    </ul>
                </div>

                <!-- 區塊三：洋蔥式穿搭法則 -->
                <div style="background: #FFFBEB; border: 1px solid #FCD34D; border-left: 5px solid #D97706; border-radius: 8px; padding: 16px; grid-column: 1 / -1;">
                    <h3 style="font-size: 15px; color: #B45309; margin-top: 0; margin-bottom: 10px; display: flex; align-items: center; gap: 6px;">
                        🧥 三、 11 月中下旬「洋蔥式分層穿搭法則」（應對 15°C 巨大溫差）
                    </h3>
                    <p style="font-size: 13.5px; color: #92400E; margin-top: 0; margin-bottom: 10px;">
                        這趟騎旅跨越了<strong>「海拔近 1,000m 的富士五湖高原（3°C～15°C）」</strong>與<strong>「溫暖的伊豆相模灣海岸（10°C～20°C）」</strong>，溫差高達 15 度：
                    </p>
                    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 12px; font-size: 13px; color: #78350F;">
                        <div style="background: rgba(255,255,255,0.7); padding: 10px; border-radius: 6px;">
                            <strong>👕 底層（排汗）：</strong><br>長袖透氣排汗排濕底衫（避免流汗後在高原吹風受寒）。
                        </div>
                        <div style="background: rgba(255,255,255,0.7); padding: 10px; border-radius: 6px;">
                            <strong>🧥 中層（保暖）：</strong><br>輕量單車刷毛中層或排汗保暖車衣。
                        </div>
                        <div style="background: rgba(255,255,255,0.7); padding: 10px; border-radius: 6px;">
                            <strong>🌬️ 外層（防風・必備）：</strong><br>超輕量防風防潑水風衣，可摺疊收進後背口袋。在「Day 6 朝霧高原千米長下坡」與「清晨河口湖」時穿上禦寒。
                        </div>
                        <div style="background: rgba(255,255,255,0.7); padding: 10px; border-radius: 6px;">
                            <strong>🧤 配件（關鍵細節）：</strong><br>
                            ・<strong>防風長指手套</strong>（下坡與清晨防凍手）。<br>
                            ・<strong>魔術頭巾 / 護頸</strong>（防冷風灌入領口）。<br>
                            ・<strong>太陽眼鏡 / 變色鏡片</strong>（秋冬日照角度低，傍晚陽光斜射刺眼）。
                        </div>
                    </div>
                </div>

            </div>
        </div>'''

for path in files_itinerary:
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()

    # Replace existing single reminder box or insert before warning box
    pattern = r'<!-- 出發前關鍵購票與待辦時程 -->[\s\S]*?(?=<!-- 重點預警 -->)'
    if re.search(pattern, html):
        html = re.sub(pattern, reminders_section_html + '\n\n        ', html)
    else:
        html = html.replace('<!-- 重點預警 -->', reminders_section_html + '\n\n        <!-- 重點預警 -->')

    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)

print("Successfully embedded Section 2 (CycleTrip) and Section 3 (Layering) into itinerary HTML!")
