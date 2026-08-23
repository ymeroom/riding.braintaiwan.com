import json, sys

# Load culture data into all_19days_route_data.json
with open("d:/2026東京單車騎旅/all_19days_route_data.json", "r", encoding="utf-8") as f:
    days_data = json.load(f)

# Import culture dict from inject script
from inject_culture_to_itinerary import culture_data

for d in days_data:
    day_num = d["day"]
    if day_num in culture_data:
        d["culture"] = culture_data[day_num]
        # Append culture highlight to expert tip if helpful
        c = culture_data[day_num]
        culture_tip = f"<div style='margin-top:8px; padding-top:8px; border-top:1px dashed rgba(59,130,246,0.3); font-size:11.5px; color:#DDD6FE;'><strong style='color:#C084FC;'>🎬 聖地巡禮：</strong> {c['anime']} ｜ {c['movie']}</div>"
        if "🎬 聖地巡禮" not in d["expert_tip"]:
            d["expert_tip"] += culture_tip

with open("d:/2026東京單車騎旅/all_19days_route_data.json", "w", encoding="utf-8") as f:
    json.dump(days_data, f, ensure_ascii=False)

# Rebuild map app with culture data
with open("d:/2026東京單車騎旅/rebuild_master_map_demo.py", "r", encoding="utf-8") as f:
    app_py = f.read()

# Execute rebuild
exec(app_py)

print("Updated Map Demo App with full Anime, J-Drama, Movie, and Cultural History notes!")
