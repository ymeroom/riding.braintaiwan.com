import json
import sys
import re
from collections import defaultdict

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
        sys.stderr.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass

with open("workspace_clips_raw.json", "r", encoding="utf-8") as f:
    clips = json.load(f)

print(f"Total raw clips loaded: {len(clips)}")

# Check Day 19 specifically first
print("\n" + "=" * 80)
print("             DAY 19: 《776公里的世界線閉環》 全量 Raw Clips 深度分析")
print("=" * 80)

day19_clips = []
for c in clips:
    title = c.get("title", "")
    prompt = c.get("metadata", {}).get("prompt", "")
    if "776" in title or "世界線閉環" in title or "Closing the 776km" in title or "776" in prompt or "世界線閉環" in prompt or "Day 19" in title or "Day19" in title:
        day19_clips.append(c)

print(f"Found {len(day19_clips)} clips matching Day 19:")
for idx, c in enumerate(day19_clips, 1):
    dur = c.get("metadata", {}).get("duration", 0)
    tags = c.get("metadata", {}).get("tags", "")
    cid = c.get("id")
    title = c.get("title")
    created = c.get("created_at", "")[:19]
    print(f"{idx:02d}. [{cid}] {title} ({dur:.1f}s, {created})")
    print(f"    Tags: {tags}")

# Now inspect every day 1..19 in detail
print("\n" + "=" * 80)
print("             19 天每一天在 Suno 帳號中的原始生成狀況檢核")
print("=" * 80)

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

for d in range(1, 20):
    kws = EXPECTED_DAYS[d]
    matched = [c for c in clips if any(k in c.get("title", "") or k in c.get("metadata", {}).get("prompt", "") for k in kws)]
    
    main_songs = []
    stems = []
    for c in matched:
        t = c.get("title", "")
        is_stem = any(f"({s})" in t for s in [
            "Vocals", "Instrumental", "Drums", "Bass", "Guitar", "Keyboard",
            "Percussion", "Strings", "Synth", "FX", "Brass", "Woodwinds", "Backing Vocals"
        ])
        if is_stem:
            stems.append(c)
        else:
            main_songs.append(c)
            
    print(f"\n[Day {d:02d}: {kws[0]}] 總計 {len(matched)} 個 Clip (主歌: {len(main_songs)} 首, 分軌: {len(stems)} 軌)")
    for s in main_songs:
        t = s.get("title", "")
        tags = s.get("metadata", {}).get("tags", "")
        is_b = bool(re.search(r'Bossa|Folk|Acoustic|Mellow|Gentle|105 BPM|115 BPM|120 BPM|慢活|民謠', tags + " " + t, re.I))
        v_type = "🍃 B版慢活" if is_b else "⚡ A版熱血"
        print(f"   • 主歌 [{s.get('id')}]: {t} -> 判定: {v_type}")
        print(f"     風格 Tags: {tags[:70]}...")
