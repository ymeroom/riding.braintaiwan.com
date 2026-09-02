import os
import sys
import json
import shutil
import subprocess
from pathlib import Path

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
        sys.stderr.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass

SRC_DIR = Path(r"D:\Suno jazz version")
DEST_DIR = Path(r"D:\2026東京單車騎旅\wav")
MANIFEST = Path(r"D:\2026東京單車騎旅\songs_manifest.json")

DEST_DIR.mkdir(parents=True, exist_ok=True)

with open(MANIFEST, "r", encoding="utf-8") as f:
    tracks = json.load(f)["tracks"]

tracks_by_id = {t["id"]: t for t in tracks if "id" in t}

print(f"[INFO] Copying all True Master WAVs from {SRC_DIR} to {DEST_DIR}...")

copied = 0
for folder in sorted(SRC_DIR.iterdir()):
    if not folder.is_dir() or folder.name.startswith(("_", ".")):
        continue
    wav_file = folder / "song.wav"
    if not wav_file.exists():
        continue
    
    # Clip ID
    id_files = [f for f in folder.iterdir() if f.name.startswith(".id-")]
    clip_id = id_files[0].name.replace(".id-", "") if id_files else None

    # Get duration
    dur = 0.0
    try:
        r = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(wav_file)], capture_output=True, text=True)
        dur = float(r.stdout.strip())
    except Exception:
        pass

    target = None
    if clip_id and clip_id in tracks_by_id:
        target = tracks_by_id[clip_id]
    else:
        clean_name = folder.name.replace("《", "").replace("》", "").replace(" v2", "").strip()
        cands = [t for t in tracks if clean_name in t.get("title", "") or clean_name in t.get("display_name", "")]
        if cands:
            cands.sort(key=lambda x: abs(x.get("duration", 0) - dur))
            target = cands[0]

    if target:
        day = target.get("day", 99)
        day_str = target.get("day_str", "Day99")
        ver = target.get("version", "A")
        style_desc = target.get("style_desc", "熱血搖滾")
        take_str = target.get("take_str", "Take1")
        title = target.get("title", "").replace(f" ({take_str})", "").replace("《", "").replace("》", "").strip()

        dest_name = f"{day:02d}_{day_str}_{ver}_{style_desc}_{take_str}_{title}.wav" if day != 99 else f"99_Bonus_{ver}_{style_desc}_{take_str}_{title}.wav"
        dest_path = DEST_DIR / dest_name
        
        shutil.copy2(wav_file, dest_path)
        size_mb = dest_path.stat().st_size / (1024 * 1024)
        print(f"✅ Overwritten with True WAV ({size_mb:.1f}MB): {dest_name}")
        copied += 1

# Check inbox WAV for Day 1
inbox_wav = SRC_DIR / "_inbox" / "《世界線的起跑線 (World Line Departure)》.wav"
if inbox_wav.exists():
    d1_target = DEST_DIR / "01_Day01_B_慢活民謠_Take1_世界線的起跑線 World Line Departure.wav"
    shutil.copy2(inbox_wav, d1_target)
    print(f"✅ Overwritten Day 01 Take 1 with inbox True WAV ({d1_target.stat().st_size / (1024*1024):.1f}MB)")

print(f"\n[DONE] Successfully copied {copied} True Master WAV files into {DEST_DIR}!")
