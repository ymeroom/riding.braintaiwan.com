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
wav_files = sorted(list(WAV_DIR.glob("*.wav")))

print(f"Total WAV files in {WAV_DIR}: {len(wav_files)}")
print("\nSample 10 WAV files (size in MB):")
for f in wav_files[:15]:
    size_mb = f.stat().st_size / (1024 * 1024)
    print(f"  • {f.name} ({size_mb:.1f} MB)")
