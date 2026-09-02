#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Clean up legacy un-suffixed duplicate folders and files in stems/, music/, and covers/.
Keeps only the standardized, clean 'Take1', 'Take2', 'Take3', 'Take4' multi-take files.
"""

import os
import sys
import shutil
from pathlib import Path

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
        sys.stderr.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass

WORKSPACE_ROOT = Path(__file__).resolve().parent
MUSIC_DIR = WORKSPACE_ROOT / "music"
COVERS_DIR = WORKSPACE_ROOT / "covers"
STEMS_DIR = WORKSPACE_ROOT / "stems"

# 1. Clean Stems Folders: remove legacy folders that don't have "_Take" in their name
print("[INFO] Cleaning up legacy duplicate folders in stems/ ...")
cleaned_stems = 0
for folder in STEMS_DIR.iterdir():
    if folder.is_dir():
        if "_Take" not in folder.name and not folder.name.startswith("Day7"):
            # Check if there is already a Take version for this day
            day_prefix = folder.name.split("_")[0]
            has_take_version = any("_Take" in f.name and f.name.startswith(day_prefix) for f in STEMS_DIR.iterdir() if f.is_dir())
            if has_take_version:
                print(f"Removing legacy duplicate stem folder: {folder.name}")
                shutil.rmtree(folder)
                cleaned_stems += 1

# 2. Clean Music MP3 / LRC: remove legacy files that don't have "_Take" in their name
print("\n[INFO] Cleaning up legacy duplicate files in music/ ...")
cleaned_music = 0
for f in MUSIC_DIR.iterdir():
    if f.is_file() and "_Take" not in f.name and not f.name.startswith("Day7"):
        day_prefix = f.name.split("_")[0]
        has_take_version = any("_Take" in x.name and x.name.startswith(day_prefix) and x.suffix == f.suffix for x in MUSIC_DIR.iterdir())
        if has_take_version:
            print(f"Removing legacy duplicate file: {f.name}")
            f.unlink()
            cleaned_music += 1

# 3. Clean Covers: remove legacy covers that don't have "_Take" in their name
print("\n[INFO] Cleaning up legacy duplicate covers in covers/ ...")
cleaned_covers = 0
for f in COVERS_DIR.iterdir():
    if f.is_file() and "_Take" not in f.name and not f.name.startswith("Day7"):
        day_prefix = f.name.split("_")[0]
        has_take_version = any("_Take" in x.name and x.name.startswith(day_prefix) for x in COVERS_DIR.iterdir())
        if has_take_version:
            print(f"Removing legacy duplicate cover: {f.name}")
            f.unlink()
            cleaned_covers += 1

print(f"\n[SUCCESS] Cleanup complete:")
print(f"• Removed {cleaned_stems} legacy stem folders")
print(f"• Removed {cleaned_music} legacy music/lrc files")
print(f"• Removed {cleaned_covers} legacy cover images")
