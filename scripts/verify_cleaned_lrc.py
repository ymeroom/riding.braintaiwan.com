import sys
from pathlib import Path

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
        sys.stderr.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass

PACK_DIR = Path(r"d:\2026東京單車騎旅\2026東京單車騎旅_手機隨身包")

test_files = [
    "01_Day01_A_熱血搖滾_Take1_世界線的起跑線 World Line Departure.lrc",
    "01_Day01_B_慢活民謠_Take1_世界線的起跑線 World Line Departure.lrc",
    "08_Day08_B_慢活民謠_Take1_修善寺竹林幽夢 Bamboo Dream of Shuzenji.lrc",
    "14_Day14_A_熱血搖滾_Take1_獨角獸與彩虹之橋 Unicorn on the Rainbow Bridge.lrc",
    "18_Day18_A_熱血搖滾_Take1_神宮外苑的黃金雨 Golden Rain at Jingu Gaien.lrc",
    "19_Day19_A_熱血搖滾_Take1_776公里的世界線閉環 Closing the 776km World Line.lrc"
]

for tf in test_files:
    p = PACK_DIR / tf
    if p.exists():
        lines = p.read_text(encoding="utf-8").splitlines()
        print(f"\n==================== {tf} ({len(lines)} lines) ====================")
        for l in lines[:10]:
            print("  ", l)
        print("   ...")
        for l in lines[-3:]:
            print("  ", l)
