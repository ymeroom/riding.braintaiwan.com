import json
import sys
import re

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
        sys.stderr.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass

with open("workspace_clips_raw.json", "r", encoding="utf-8") as f:
    clips = json.load(f)

print(f"Total clips in workspace_clips_raw.json: {len(clips)}")

# Expected 19 days titles:
EXPECTED_DAYS = {
    1: ["世界線的起跑線", "World Line Departure"],
    2: ["峠道狂詩曲", "Toge Rhapsody"],
    3: ["水鏡神域", "Mirrored Sacred Realm"],
    4: ["千圓紙幣的晨光", "Morning Glow on the 1000-Yen Bill"],
    5: ["山獸神之森", "Sanctuary of the Ancient Woods"],
    6: ["破風降臨千米疾走", "Thousand-Meter Wind Descent"],
    7: ["駿河灣的蔚藍防潮堤", "Suruga Blue Sea Wall"],
    8: ["修善寺竹林幽夢", "Bamboo Dream of Shuzenji"],
    9: ["熔岩懸崖與伊豆之瞳", "Lava Cliffs and Eye of Izu"],
    10: ["網代夕照的避風港", "Ajiro Golden Haven"],
    11: ["海灣夜空的最後花火", "Fireworks Over the Caldera Bay"],
    12: ["早雲柑橘道與湘南風", "Mandarin Groves and Shonan Breeze"],
    13: ["高校前的命運路口", "Destiny Crossing at Kamakura High"],
    14: ["獨角獸與彩虹之橋", "Unicorn on the Rainbow Bridge"],
    15: ["葛飾下町的昭和人情", "Shitamachi Memories of Katsushika"],
    16: ["江戶川無重力巡航", "Zero-Gravity Cruise on Edogawa"],
    17: ["萬棵水杉的黃金童話", "Golden Fairy Tale of Metasequoia"],
    18: ["神宮外苑的黃金雨", "Golden Rain at Jingu Gaien"],
    19: ["776公里的世界線閉環", "Closing the 776km World Line"]
}

# Group all clips
found_days = {}
stem_days = {}

for c in clips:
    title = c.get("title", "")
    is_stem = any(f"({stem})" in title for stem in [
        "Vocals", "Instrumental", "Drums", "Bass", "Guitar", "Keyboard",
        "Percussion", "Strings", "Synth", "FX", "Brass", "Woodwinds", "Backing Vocals"
    ])
    
    matched_day = None
    for d_num, keywords in EXPECTED_DAYS.items():
        if any(k in title for k in keywords):
            matched_day = d_num
            break
            
    if matched_day:
        if is_stem:
            stem_days.setdefault(matched_day, []).append(c)
        else:
            found_days.setdefault(matched_day, []).append(c)

print("\n=== AUDIT RESULTS FOR 19 DAYS ===")
for d in range(1, 20):
    songs = found_days.get(d, [])
    stems = stem_days.get(d, [])
    status = f"✅ Found {len(songs)} main songs, {len(stems)} stems" if songs else (f"⚠️ Only {len(stems)} stems (Main song missing)" if stems else "❌ MISSING completely")
    print(f"Day {d:02d}: {EXPECTED_DAYS[d][0]} -> {status}")
    for s in songs:
        dur = s.get("metadata", {}).get("duration", 0)
        print(f"   • [{s.get('id')}] {s.get('title')} ({dur:.1f}s) | created: {s.get('created_at', '')[:19]}")

missing_days = [d for d in range(1, 20) if not found_days.get(d)]
print(f"\nMissing Main Song Days: {missing_days}")
