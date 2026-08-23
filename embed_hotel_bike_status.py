import sys, re

files_itinerary = [
    'C:/Users/ymero/Downloads/tokyo_fuji_cycling_itinerary_19days_v2.html',
    'd:/2026東京單車騎旅/tokyo_fuji_cycling_itinerary_19days_v2.html'
]

# Section for Hotel Bike Verification Checklist
hotel_bike_section = '''        <!-- 住宿飯店單車擺放友善度實測清單 -->
        <div style="background: #F8FAFC; border: 1px solid #CBD5E1; border-left: 5px solid #059669; border-radius: 10px; padding: 18px 22px; margin-bottom: 24px;">
            <h3 style="font-size: 16px; color: #065F46; margin-top: 0; margin-bottom: 12px; display: flex; align-items: center; gap: 8px;">
                🚲 19日已訂住宿「單車停放/進房友善度」實測核實狀態
            </h3>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 12px; font-size: 13px;">
                <div style="background: #ECFDF5; border: 1px solid #A7F3D0; padding: 10px 14px; border-radius: 6px;">
                    <strong style="color: #047857;">✅ 官方明確確認可放單車：</strong>
                    <ul style="margin-left: 16px; margin-top: 4px; color: #065F46; line-height: 1.6;">
                        <li><strong>11/14 由加利旅館 (Yukari)</strong>：都留市，明確可放單車</li>
                        <li><strong>11/21 KAWANA Seaview Standard</strong>：伊東川奈，明確可放單車</li>
                        <li><strong>11/22 Apt南熱海-網代</strong>：南熱海長浜，明確可放單車</li>
                        <li><strong>11/27-29 花庵旅舍 (Hostel Hana An)</strong>：葛飾金町，明確可放單車</li>
                    </ul>
                </div>
                <div style="background: #F0FDF4; border: 1px solid #BBF7D0; padding: 10px 14px; border-radius: 6px;">
                    <strong style="color: #15803D;">👍 戶外基地/獨棟木屋（空間充裕可放）：</strong>
                    <ul style="margin-left: 16px; margin-top: 4px; color: #166534; line-height: 1.6;">
                        <li><strong>11/13 Mt.Takao Base Camp</strong>：高尾山戶外基地，設單車專用車架</li>
                        <li><strong>11/15 Orange Cabin Inn</strong>：河口湖獨立木屋，玄關前廊寬敞</li>
                        <li><strong>11/20 温泉宿 水口 (Mizuguchi)</strong>：修善寺傳統名湯，玄關內側/遮雨處</li>
                        <li><strong>11/23 Izu Kansya (伊豆観舎)</strong>：南熱海獨棟度假屋，專屬私密空間</li>
                    </ul>
                </div>
                <div style="background: #FEF2F2; border: 1px solid #FECACA; padding: 10px 14px; border-radius: 6px; grid-column: 1 / -1;">
                    <strong style="color: #B91C1C;">⛔ 確定無法停放單車（避坑黑名單）：</strong>
                    <span style="color: #991B1B; margin-left: 8px;"><strong>GRAND HOSTEL LDK TOKYO Nishikasai (西葛西)</strong> —— 官方確認無單車停放空間且禁止攜帶進房，已果斷剔除避坑！</span>
                </div>
            </div>
        </div>'''

for path in files_itinerary:
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()

    # Insert right before 19-day table
    if '19日已訂住宿「單車停放/進房友善度」' not in html:
        html = html.replace('<!-- 19天實測數據總表 -->', hotel_bike_section + '\n\n        <!-- 19天實測數據總表 -->')

    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)

print("Successfully updated hotel bicycle storage status in itinerary HTML!")
