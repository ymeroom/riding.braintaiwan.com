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

# Find all main song clips (exclude stems)
main_clips = []
for c in clips:
    title = c.get("title", "")
    is_stem = any(f"({stem})" in title for stem in [
        "Vocals", "Instrumental", "Drums", "Bass", "Guitar", "Keyboard",
        "Percussion", "Strings", "Synth", "FX", "Brass", "Woodwinds", "Backing Vocals"
    ])
    if not is_stem and c.get("audio_url"):
        main_clips.append(c)

print(f"Total main song clips across account: {len(main_clips)}")

# Group by Day, Style (A vs B)
grouped = {d: {"A": [], "B": []} for d in range(1, 20)}
other_songs = []

for c in main_clips:
    t = c.get("title", "")
    prompt = c.get("metadata", {}).get("prompt", "")
    tags = c.get("metadata", {}).get("tags", "")
    
    matched_day = None
    for d_num, kws in EXPECTED_DAYS.items():
        if any(k in t or k in prompt for k in kws):
            matched_day = d_num
            break
            
    if matched_day:
        # Determine A vs B
        is_b = bool(re.search(r'Bossa|Folk|Acoustic|Mellow|Gentle|105 BPM|115 BPM|120 BPM|慢活|民謠', tags + " " + t, re.I))
        style_key = "B" if is_b else "A"
        grouped[matched_day][style_key].append(c)
    else:
        other_songs.append(c)

print("\n" + "="*80)
print(f"{'天數':<7} | {'A版 Take數':<12} | {'B版 Take數':<12} | {'總首數':<8} | {'歌曲主題'}")
print("-" * 80)

total_day_tracks = 0
for d in range(1, 20):
    a_takes = len(grouped[d]["A"])
    b_takes = len(grouped[d]["B"])
    subtotal = a_takes + b_takes
    total_day_tracks += subtotal
    print(f"Day {d:02d}  | {a_takes} 首 (Take 1..{a_takes}) | {b_takes} 首 (Take 1..{b_takes}) | {subtotal} 首    | {EXPECTED_DAYS[d][0]}")

print("-" * 80)
print(f"19天主題曲總曲數: {total_day_tracks} 首")
print(f"額外其他單曲數: {len(other_songs)} 首")
print(f"全曲庫總計: {total_day_tracks + len(other_songs)} 首")
print("="*80)
