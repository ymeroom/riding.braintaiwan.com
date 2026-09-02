import json
import sys
import re
from pathlib import Path

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
        sys.stderr.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass

with open("workspace_clips_raw.json", "r", encoding="utf-8") as f:
    clips = json.load(f)

STEMS_DIR = Path("stems")

EXPECTED_DAYS = [
    (1, "世界線的起跑線 (World Line Departure)"),
    (2, "峠道狂詩曲 (Toge Rhapsody)"),
    (3, "水鏡神域 (Mirrored Sacred Realm)"),
    (4, "千圓紙幣的晨光 (Morning Glow on the 1000-Yen Bill)"),
    (5, "山獸神之森的休止符 (Sanctuary of the Ancient Woods)"),
    (6, "破風降臨千米疾走 (Thousand-Meter Wind Descent)"),
    (7, "駿河灣的蔚藍防潮堤 (Suruga Blue Sea Wall)"),
    (8, "修善寺竹林幽夢 (Bamboo Dream of Shuzenji)"),
    (9, "熔岩懸崖與伊豆之瞳 (Lava Cliffs and Eye of Izu)"),
    (10, "網代夕照的避風港 (Ajiro Golden Haven)"),
    (11, "海灣夜空的最後花火 (Fireworks Over the Caldera Bay)"),
    (12, "早雲柑橘道與湘南風 (Mandarin Groves and Shonan Breeze)"),
    (13, "高校前的命運路口 (Destiny Crossing at Kamakura High)"),
    (14, "獨角獸與彩虹之橋 (Unicorn on the Rainbow Bridge)"),
    (15, "葛飾下町的昭和人情 (Shitamachi Memories of Katsushika)"),
    (16, "江戶川無重力巡航 (Zero-Gravity Cruise on Edogawa)"),
    (17, "萬棵水杉的黃金童話 (Golden Fairy Tale of Metasequoia)"),
    (18, "神宮外苑的黃金雨 (Golden Rain at Jingu Gaien)"),
    (19, "776公里的世界線閉環 (Closing the 776km World Line)")
]

print("=" * 100)
print("     2026 東京單車騎旅 19 天逐天（Day 01 ~ Day 19）Suno 原始生成與 Stems 逐一檢核")
print("=" * 100)

for day_num, title in EXPECTED_DAYS:
    day_str = f"Day{day_num:02d}"
    kw = title.split("(")[0].strip()
    
    # Matching raw clips
    matched = [c for c in clips if kw in c.get("title", "") or kw in c.get("metadata", {}).get("prompt", "")]
    main_songs = []
    for c in matched:
        t = c.get("title", "")
        is_stem = any(f"({s})" in t for s in [
            "Vocals", "Instrumental", "Drums", "Bass", "Guitar", "Keyboard",
            "Percussion", "Strings", "Synth", "FX", "Brass", "Woodwinds", "Backing Vocals"
        ])
        if not is_stem:
            main_songs.append(c)
            
    # Check local stems folders
    local_stem_folders = [d for d in STEMS_DIR.glob(f"{day_str}*") if d.is_dir()]
    
    print(f"\n【Day {day_num:02d}】《{title}》")
    print(f"  • Suno 上生成之主歌數: {len(main_songs)} 首")
    
    a_takes = []
    b_takes = []
    for s in main_songs:
        t = s.get("title", "")
        tags = s.get("metadata", {}).get("tags", "")
        dur = s.get("metadata", {}).get("duration", 0)
        cid = s.get("id")
        is_b = bool(re.search(r'Bossa|Folk|Acoustic|Mellow|Gentle|105 BPM|115 BPM|120 BPM|慢活|民謠', tags + " " + t, re.I))
        if is_b:
            b_takes.append((cid, dur, tags[:50]))
        else:
            a_takes.append((cid, dur, tags[:50]))
            
    print(f"    - ⚡ A版 (熱血搖滾): {len(a_takes)} 首 ({', '.join([f'ID: {x[0][:8]}.. ({x[1]:.0f}s)' for x in a_takes]) if a_takes else '尚未生成'})")
    print(f"    - 🍃 B版 (慢活民謠): {len(b_takes)} 首 ({', '.join([f'ID: {x[0][:8]}.. ({x[1]:.0f}s)' for x in b_takes]) if b_takes else '尚未生成'})")
    
    print(f"  • 本地 Stems 分軌資料夾 (共 {len(local_stem_folders)} 組，每組 12 軌):")
    for sf in local_stem_folders:
        files = list(sf.glob("*.mp3")) + list(sf.glob("*.wav"))
        print(f"    📁 {sf.name} ({len(files)} 軌音訊)")
