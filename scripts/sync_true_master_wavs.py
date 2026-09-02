#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sync True Master Lossless WAV files from 'D:\Suno jazz version' into 'D:\2026東京單車騎旅\wav\'.
Matches each true WAV file by Suno clip ID and duration, renaming to standard:
'01_Day01_A_熱血搖滾_Take1_世界線的起跑線 World Line Departure.wav'
"""

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
DEST_WAV_DIR = Path(r"D:\2026東京單車騎旅\wav")
MANIFEST_FILE = Path(r"D:\2026東京單車騎旅\songs_manifest.json")

DEST_WAV_DIR.mkdir(parents=True, exist_ok=True)

with open(MANIFEST_FILE, "r", encoding="utf-8") as f:
    manifest_data = json.load(f)

tracks = manifest_data.get("tracks", [])

# Build map from clip ID and duration to track info
tracks_by_id = {t["id"]: t for t in tracks if "id" in t}

print(f"[INFO] Scanning {SRC_DIR} for True Master WAV files...")

matched_count = 0
unmatched = []

# Scan all folders in SRC_DIR
for folder in SRC_DIR.iterdir():
    if not folder.is_dir() or folder.name.startswith(("_", ".")):
        continue
        
    wav_file = folder / "song.wav"
    if not wav_file.exists():
        continue
        
    # Find clip ID file (.id-xxxx)
    id_files = [f for f in folder.iterdir() if f.name.startswith(".id-")]
    clip_id = id_files[0].name.replace(".id-", "") if id_files else None
    
    # Get duration using ffprobe
    res = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(wav_file)],
        capture_output=True, text=True
    )
    try:
        dur = float(res.stdout.strip())
    except Exception:
        dur = 0.0

    target_track = None
    if clip_id and clip_id in tracks_by_id:
        target_track = tracks_by_id[clip_id]
    else:
        # Fallback match by folder title keyword & duration
        clean_folder = folder.name.replace("《", "").replace("》", "").replace(" v2", "").strip()
        candidates = [t for t in tracks if clean_folder in t.get("title", "") or clean_folder in t.get("display_name", "")]
        if candidates:
            # Match closest duration
            candidates.sort(key=lambda x: abs(x.get("duration", 0) - dur))
            target_track = candidates[0]

    if target_track:
        day = target_track.get("day", 99)
        day_str = target_track.get("day_str", "Day99")
        ver = target_track.get("version", "A")
        style_desc = target_track.get("style_desc", "熱血搖滾")
        take_str = target_track.get("take_str", "Take1")
        title = target_track.get("title", "").replace(f" ({take_str})", "").replace("《", "").replace("》", "").strip()

        if day != 99:
            dest_filename = f"{day:02d}_{day_str}_{ver}_{style_desc}_{take_str}_{title}.wav"
        else:
            dest_filename = f"99_Bonus_{ver}_{style_desc}_{take_str}_{title}.wav"

        dest_path = DEST_WAV_DIR / dest_filename
        size_mb = wav_file.stat().st_size / (1024 * 1024)
        print(f"✅ Syncing True Master WAV ({size_mb:.1f}MB): {folder.name} -> {dest_filename}")
        shutil.copy2(wav_file, dest_path)
        matched_count += 1
    else:
        unmatched.append((folder.name, wav_file, dur))

print("\n" + "=" * 80)
print(f"🎉 成功同步 {matched_count} 首 True Master 原生無損 WAV 檔！")
print(f"📁 目標目錄: {DEST_WAV_DIR}")
if unmatched:
    print(f"⚠️ 未匹配資料夾 ({len(unmatched)} 個):")
    for name, path, d in unmatched:
        print(f"   - {name} (dur: {d:.1f}s)")
print("=" * 80)
