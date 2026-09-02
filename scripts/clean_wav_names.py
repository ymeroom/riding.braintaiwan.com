import os
import sys
import re
from pathlib import Path

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
        sys.stderr.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass

WAV_DIR = Path(r"d:\2026東京單車騎旅\wav")

cleaned = 0
for f in list(WAV_DIR.glob("*.wav")):
    # Remove files with unmatched parenthesis
    if "(" in f.name and ")" not in f.name:
        f.unlink()
        cleaned += 1

print(f"Cleaned {cleaned} unstandardized files in {WAV_DIR}")
print(f"Remaining clean True Master WAVs: {len(list(WAV_DIR.glob('*.wav')))}")
