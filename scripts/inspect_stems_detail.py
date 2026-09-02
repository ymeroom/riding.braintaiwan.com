import os
import sys
import json
from pathlib import Path
from collections import defaultdict

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
        sys.stderr.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass

STEMS_DIR = Path("stems")

stems_by_day = defaultdict(list)

for folder in STEMS_DIR.iterdir():
    if folder.is_dir():
        files = list(folder.glob("*.mp3")) + list(folder.glob("*.wav"))
        name = folder.name
        # Match day
        day_match = name.split("_")[0]
        stems_by_day[day_match].append((name, len(files), [f.stem for f in files]))

print("=" * 80)
print(f"{'天數/分類':<10} | {'資料夾數 (首歌)':<15} | {'詳細資料夾名稱與軌數'}")
print("-" * 80)

for day in sorted(stems_by_day.keys()):
    folders = stems_by_day[day]
    print(f"\n[{day}] 共 {len(folders)} 首有分軌:")
    for fname, count, tracks in folders:
        print(f"  📁 {fname} ({count} 軌: {', '.join(tracks[:6])}...)")

print("=" * 80)
