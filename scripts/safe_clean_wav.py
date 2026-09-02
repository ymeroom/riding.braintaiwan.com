import os
import sys
from pathlib import Path

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
        sys.stderr.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass

WAV_DIR = Path(r"d:\2026東京單車騎旅\wav")

for f in list(WAV_DIR.glob("*.wav")):
    if "(" in f.name and ")" not in f.name:
        try:
            f.unlink()
            print(f"Removed: {f.name}")
        except Exception as e:
            print(f"Error {f.name}: {e}")

print(f"Total True Master WAVs in {WAV_DIR}: {len(list(WAV_DIR.glob('*.wav')))}")
