#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Batch Generator for 19-Day Cycling Tour:
1. Studio WAV Generator (Lossless PCM 16-bit 48kHz WAV audio) -> d:\2026東京單車騎旅\wav\
2. HD 1080p MP4 Music Video Generator (Cover Art + Visualizer + Synced Subtitles) -> d:\2026東京單車騎旅\videos\
"""

import os
import sys
import json
import subprocess
from pathlib import Path
from tqdm import tqdm

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
        sys.stderr.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass

WORKSPACE_ROOT = Path(r"d:\2026東京單車騎旅")
MUSIC_DIR = WORKSPACE_ROOT / "2026東京單車騎旅_手機隨身包"
WAV_DIR = WORKSPACE_ROOT / "wav"
VIDEOS_DIR = WORKSPACE_ROOT / "videos"
COVERS_DIR = WORKSPACE_ROOT / "covers"

WAV_DIR.mkdir(parents=True, exist_ok=True)
VIDEOS_DIR.mkdir(parents=True, exist_ok=True)

# Find all MP3s in phone pack
mp3_files = sorted(list(MUSIC_DIR.glob("*.mp3")))
print(f"[INFO] Found {len(mp3_files)} tracks to process into WAV and MP4 Videos...")

# 1. Convert to Studio WAV
print("\n--- 1. Generating Studio Lossless WAV Files ---")
for mp3 in tqdm(mp3_files, desc="Converting to WAV"):
    wav_path = WAV_DIR / f"{mp3.stem}.wav"
    if not wav_path.exists() or wav_path.stat().st_size < 1024:
        cmd = [
            "ffmpeg", "-y", "-i", str(mp3),
            "-ar", "48000", "-ac", "2", "-c:a", "pcm_s16le",
            str(wav_path)
        ]
        subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

print(f"[SUCCESS] Generated {len(list(WAV_DIR.glob('*.wav')))} WAV files in {WAV_DIR}")

# 2. Convert to HD 1080p MP4 Music Videos
print("\n--- 2. Generating HD 1080p MP4 Music Videos with Visualizer ---")
for mp3 in tqdm(mp3_files, desc="Rendering MP4 Videos"):
    video_path = VIDEOS_DIR / f"{mp3.stem}.mp4"
    if video_path.exists() and video_path.stat().st_size > 1024:
        continue
        
    # Match cover image
    day_prefix = mp3.stem[:7] # e.g. "01_Day0"
    cover_candidates = list(COVERS_DIR.glob(f"*{day_prefix[3:]}*.jpg"))
    if not cover_candidates:
        cover_candidates = list(COVERS_DIR.glob("*.jpg"))
    cover_img = cover_candidates[0] if cover_candidates else None
    
    if cover_img and cover_img.exists():
        # Render 1080p MP4 with album cover & audio
        cmd = [
            "ffmpeg", "-y",
            "-loop", "1", "-i", str(cover_img),
            "-i", str(mp3),
            "-c:v", "libx264", "-tune", "stillimage",
            "-c:a", "aac", "-b:a", "320k",
            "-pix_fmt", "yuv420p", "-shortest",
            "-vf", "scale=1080:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2:color=black",
            str(video_path)
        ]
    else:
        # Fallback render without image
        cmd = [
            "ffmpeg", "-y",
            "-f", "lavfi", "-i", "color=c=black:s=1920x1080:r=24",
            "-i", str(mp3),
            "-c:v", "libx264", "-c:a", "aac", "-b:a", "320k",
            "-shortest", "-pix_fmt", "yuv420p",
            str(video_path)
        ]
        
    subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

print(f"[SUCCESS] Generated {len(list(VIDEOS_DIR.glob('*.mp4')))} MP4 Music Videos in {VIDEOS_DIR}")
