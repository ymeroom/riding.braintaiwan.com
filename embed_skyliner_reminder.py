import sys, re

files_itinerary = [
    'C:/Users/ymero/Downloads/tokyo_fuji_cycling_itinerary_19days_v2.html',
    'd:/2026東京單車騎旅/tokyo_fuji_cycling_itinerary_19days_v2.html'
]

# Checklist HTML snippet
checklist_box = '''        <!-- 出發前關鍵購票與待辦時程 -->
        <div style="background: #F0FDF4; border: 1px solid #86EFAC; border-left: 5px solid #16A34A; border-radius: 8px; padding: 18px 22px; margin-bottom: 24px; color: #166534;">
            <h3 style="font-size: 16px; margin-bottom: 12px; display: flex; align-items: center; gap: 8px; color: #15803D;">
                ⏰ 出發前關鍵購票與待辦提醒（已列入行事曆）
            </h3>
            <ul style="margin-left: 20px; font-size: 14px; line-height: 1.7;">
                <li>
                    <strong>📅 10/20（二）重要購票提醒：購買「外國人特惠 Skyliner e-ticket」（全包式 ¥2,310）</strong>
                    <br>・<strong>票券內容</strong>：已同時包含「基本乘車券」＋「特急指定席券」全部費用（<span style="color:#B91C1C; font-weight:700;">完全不需要 Suica！</span>）。
                    <br>・<strong>100% 零排隊刷臉進站【Face Check in Go】</strong>：在京成官網購買 e-ticket 後，在手機上傳自拍照完成臉部註冊。下飛機到成田機場改札口時，直接走「人臉辨識專用通道」，刷臉 1 秒開門直接進站，閘門自動吐出座位小票，完全免排隊！
                </li>
                <li>
                    <strong>📅 11/01（日）前裝備複檢</strong>：防風保暖長指手套、超輕量折疊風衣、高流明前後車燈（400~800 lumens）、Apple Wallet / Suica 儲值。
                </li>
            </ul>
        </div>'''

for path in files_itinerary:
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()

    if '出發前關鍵購票與待辦提醒' not in html:
        # Insert right before the warning callout box
        html = html.replace('<!-- 重點預警 -->', checklist_box + '\n\n        <!-- 重點預警 -->')

    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)

print("Successfully embedded 10/20 Skyliner reminder checklist into itinerary HTML!")
