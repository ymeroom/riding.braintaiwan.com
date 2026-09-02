#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Merge downloaded local Suno MP3s and 19-Day Master Dual-Style Soundtrack into songs_manifest.json
"""

import json
import sys
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
MANIFEST_FILE = WORKSPACE_ROOT / "songs_manifest.json"

import build_suno_dual_vocals

# Find all downloaded MP3s in music/
downloaded_mp3s = list(MUSIC_DIR.glob("*.mp3"))
print(f"[INFO] Found {len(downloaded_mp3s)} downloaded MP3 files in music/")

manifest_tracks = []

for item in build_suno_dual_vocals.tracks:
    day_num = item["track"]
    day_str = f"Day{day_num:02d}"
    clean_day = item["day"]
    base_title = item["title"]
    theme = item.get("theme", "")
    lyrics = item["lyrics"]

    # -------------------------------------------------------------
    # Version A: 熱血搖滾 (Anime Rock / J-Rock)
    # -------------------------------------------------------------
    mp3_a_candidates = list(MUSIC_DIR.glob(f"{day_str}_A_*.mp3"))
    lrc_a_candidates = list(MUSIC_DIR.glob(f"{day_str}_A_*.lrc"))
    cover_a_candidates = list(COVERS_DIR.glob(f"{day_str}_A_*.jpg"))
    stems_a_candidates = list(STEMS_DIR.glob(f"{day_str}_A_*"))

    mp3_a_path = f"music/{mp3_a_candidates[0].name}" if mp3_a_candidates else f"music/{day_str}_A_熱血搖滾_{base_title}.mp3"
    lrc_a_path = f"music/{lrc_a_candidates[0].name}" if lrc_a_candidates else f"music/{day_str}_A_熱血搖滾_{base_title}.lrc"
    cover_a_path = f"covers/{cover_a_candidates[0].name}" if cover_a_candidates else "assets/default_cover.jpg"
    stems_a_path = f"stems/{stems_a_candidates[0].name}" if stems_a_candidates else None

    manifest_tracks.append({
        "id": f"suno_{day_str.lower()}_a",
        "day": day_num,
        "day_str": day_str,
        "day_label": clean_day,
        "version": "A",
        "version_name": "⚡ A版 熱血搖滾",
        "style_desc": "熱血搖滾",
        "title": base_title,
        "display_name": f"{day_str} A版: {base_title} (熱血搖滾)",
        "theme": theme,
        "style_prompt": item.get("style", ""),
        "duration": 215.0,
        "has_local_mp3": bool(mp3_a_candidates),
        "mp3_file": mp3_a_path,
        "lrc_file": lrc_a_path,
        "cover_file": cover_a_path,
        "stems_dir": stems_a_path,
        "prompt_lyrics": lyrics
    })

    # -------------------------------------------------------------
    # Version B: 慢活民謠 (Acoustic Folk / Bossa / City Pop)
    # -------------------------------------------------------------
    mp3_b_candidates = list(MUSIC_DIR.glob(f"{day_str}_B_*.mp3"))
    lrc_b_candidates = list(MUSIC_DIR.glob(f"{day_str}_B_*.lrc"))
    cover_b_candidates = list(COVERS_DIR.glob(f"{day_str}_B_*.jpg"))
    stems_b_candidates = list(STEMS_DIR.glob(f"{day_str}_B_*"))

    mp3_b_path = f"music/{mp3_b_candidates[0].name}" if mp3_b_candidates else f"music/{day_str}_B_慢活民謠_{base_title}.mp3"
    lrc_b_path = f"music/{lrc_b_candidates[0].name}" if lrc_b_candidates else f"music/{day_str}_B_慢活民謠_{base_title}.lrc"
    cover_b_path = f"covers/{cover_b_candidates[0].name}" if cover_b_candidates else "assets/default_cover.jpg"
    stems_b_path = f"stems/{stems_b_candidates[0].name}" if stems_b_candidates else None

    manifest_tracks.append({
        "id": f"suno_{day_str.lower()}_b",
        "day": day_num,
        "day_str": day_str,
        "day_label": clean_day,
        "version": "B",
        "version_name": "🍃 B版 慢活民謠",
        "style_desc": "慢活民謠",
        "title": f"{base_title} (慢活漫遊)",
        "display_name": f"{day_str} B版: {base_title} (慢活民謠)",
        "theme": theme,
        "style_prompt": "Acoustic folk, fingerstyle acoustic guitar, warm upright bass, gentle brush drums, melodic piano, relaxing Japanese city pop, cozy cafe vibe, dual male-female mellow harmonies, 115 BPM",
        "duration": 195.0,
        "has_local_mp3": bool(mp3_b_candidates),
        "mp3_file": mp3_b_path,
        "lrc_file": lrc_b_path,
        "cover_file": cover_b_path,
        "stems_dir": stems_b_path,
        "prompt_lyrics": lyrics
    })

# Save manifest
manifest_data = {
    "album": "2026 東京單車騎旅 19日主題曲全集 (38首雙主唱雙風格)",
    "artist": "2026 東京單車騎旅",
    "description": "東京・富士五湖・伊豆・東京灣 19日單車騎旅 Suno AI 官方雙版本音樂全集",
    "total_tracks": len(manifest_tracks),
    "days_count": 19,
    "local_mp3_count": len(downloaded_mp3s),
    "tracks": manifest_tracks
}

with open(MANIFEST_FILE, "w", encoding="utf-8") as f:
    json.dump(manifest_data, f, ensure_ascii=False, indent=2)

print(f"[SUCCESS] Merged manifest created with {len(manifest_tracks)} tracks ({len(downloaded_mp3s)} local MP3s linked) in {MANIFEST_FILE}")
