import json, sys

with open("d:/2026東京單車騎旅/all_19days_route_data.json", "r", encoding="utf-8") as f:
    days_data = json.load(f)

# Update bike storage notes for relevant days
bike_notes = {
    1: "🚲 戶外活動基地，設有單車專用停放架",
    2: "🚲 官方確認：可安全停放單車",
    3: "🚲 獨棟鄉村木屋，前廊/玄關空間充裕",
    8: "🚲 傳統溫泉名湯，設有玄關室內/遮雨停放處",
    9: "🚲 官方確認：海景民宿可安全停放單車",
    10: "🚲 官方確認：海景公寓可安全停放單車",
    11: "🚲 獨棟度假屋，專屬私密空間好停放",
    15: "🚲 官方確認：下町青年旅舍可安全停放單車",
    16: "🚲 官方確認：連住免移車，安全安心"
}

for d in days_data:
    d_num = d["day"]
    if d_num in bike_notes:
        d["bike_status"] = bike_notes[d_num]
    else:
        d["bike_status"] = "🚲 市區商旅/機動（建議牽進房或向櫃台確認）"

json_data_str = json.dumps(days_data, ensure_ascii=False)

# Rebuild map app script
with open("d:/2026東京單車騎旅/build_19days_map_app.py", "r", encoding="utf-8") as f:
    app_py = f.read()

# Replace hotelCard render logic in script
old_render = '''hotelCard.innerHTML = `
            <div class="hotel-name">${d.hotel} ${d.booked ? '<span class="badge-booked">✅ 已訂房</span>' : ''}</div>
            <div class="hotel-addr">📍 ${d.hotel_addr}</div>
            <a href="${d.hotel_url}" target="_blank" class="hotel-link">在 Google Maps 中查看位置 ↗</a>
        `;'''

new_render = '''hotelCard.innerHTML = `
            <div class="hotel-name">${d.hotel} ${d.booked ? '<span class="badge-booked">✅ 已訂房</span>' : ''}</div>
            <div class="hotel-addr">📍 ${d.hotel_addr}</div>
            <div style="font-size: 11.5px; color: #10B981; font-weight: 600; margin-bottom: 6px;">${d.bike_status}</div>
            <a href="${d.hotel_url}" target="_blank" class="hotel-link">在 Google Maps 中查看位置 ↗</a>
        `;'''

app_py = app_py.replace(old_render, new_render)

with open("d:/2026東京單車騎旅/build_19days_map_app.py", "w", encoding="utf-8") as f:
    f.write(app_py)

print("Updated build_19days_map_app.py with bike status!")
