#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Builds songs_manifest.json and 38 standard .lrc files in music/
from the 19 days rich master dataset.
"""

import os
import sys
import json
import re
from pathlib import Path

# Force UTF-8 on Windows stdout
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
        sys.stderr.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass

WORKSPACE_ROOT = Path(__file__).resolve().parent
MUSIC_DIR = WORKSPACE_ROOT / "music"
COVERS_DIR = WORKSPACE_ROOT / "covers"
MANIFEST_FILE = WORKSPACE_ROOT / "songs_manifest.json"

MUSIC_DIR.mkdir(parents=True, exist_ok=True)
COVERS_DIR.mkdir(parents=True, exist_ok=True)

# Import tracks from build_suno_dual_vocals
import build_suno_dual_vocals

def format_lrc_timestamp(seconds: float) -> str:
    minutes = int(seconds // 60)
    remaining_secs = seconds % 60
    return f"[{minutes:02d}:{remaining_secs:05.2f}]"

def generate_lrc_content(title: str, day_str: str, version: str, style_name: str, lyrics_text: str, duration: float = 210.0) -> str:
    lines = [
        f"[ti:{title}]",
        f"[ar:2026 東京單車騎旅 ({version}版 - {style_name})]",
        f"[al:2026 東京單車騎旅 19日主題曲全集]",
        f"[by:Suno AI]",
        f"[length:{int(duration//60):02d}:{int(duration%60):02d}]",
        ""
    ]
    
    # Parse lyric lines
    raw_lines = [l.strip() for l in lyrics_text.splitlines() if l.strip()]
    
    # Filter out empty and parse structural markers
    parsed = []
    for line in raw_lines:
        parsed.append(line)
        
    if parsed:
        step = (duration - 15.0) / max(len(parsed), 1)
        curr = 4.0
        for line in parsed:
            lines.append(f"{format_lrc_timestamp(curr)}{line}")
            curr += step
            
    return "\n".join(lines)

def main():
    manifest_tracks = []
    raw_tracks = build_suno_dual_vocals.tracks
    
    print(f"[INFO] Processing {len(raw_tracks)} day tracks into 38 dual-style tracks (A/B)...")
    
    for item in raw_tracks:
        day_num = item["track"]
        day_str = f"Day{day_num:02d}"
        clean_day = item["day"]
        base_title = item["title"]
        theme = item.get("theme", "")
        lyrics = item["lyrics"]
        
        # -------------------------------------------------------------
        # Version A: 熱血雙主唱搖滾 (High Energy Anime Rock / J-Rock)
        # -------------------------------------------------------------
        title_a = f"{base_title}"
        style_a_desc = "熱血搖滾"
        filename_a = f"{day_str}_A_{style_a_desc}_{re.sub(r'[^a-zA-Z0-9_\u4e00-\u9fa5]', '_', base_title)}"
        lrc_path_a = MUSIC_DIR / f"{filename_a}.lrc"
        mp3_path_a = MUSIC_DIR / f"{filename_a}.mp3"
        
        lrc_text_a = generate_lrc_content(
            title=f"{day_str} A版 - {base_title} ({style_a_desc})",
            day_str=day_str,
            version="A",
            style_name=style_a_desc,
            lyrics_text=lyrics,
            duration=215.0
        )
        with open(lrc_path_a, "w", encoding="utf-8") as f:
            f.write(lrc_text_a)
            
        manifest_tracks.append({
            "id": f"suno_{day_str.lower()}_a",
            "day": day_num,
            "day_str": day_str,
            "day_label": clean_day,
            "version": "A",
            "version_name": "⚡ A版 熱血搖滾",
            "style_desc": style_a_desc,
            "title": base_title,
            "display_name": f"{day_str} A版: {base_title} ({style_a_desc})",
            "theme": theme,
            "style_prompt": item.get("style", ""),
            "duration": 215.0,
            "mp3_file": f"music/{filename_a}.mp3",
            "lrc_file": f"music/{filename_a}.lrc",
            "wav_file": f"wav/{filename_a}.wav",
            "stems_dir": f"stems/{filename_a}",
            "cover_file": f"covers/{day_str}_A_cover.jpg",
            "lyrics_preview": lyrics[:300] + "..."
        })

        # -------------------------------------------------------------
        # Version B: 放鬆慢活民謠爵士 (Acoustic Folk / Bossa / City Pop)
        # -------------------------------------------------------------
        title_b = f"{base_title} (慢活漫遊)"
        style_b_desc = "慢活民謠"
        filename_b = f"{day_str}_B_{style_b_desc}_{re.sub(r'[^a-zA-Z0-9_\u4e00-\u9fa5]', '_', base_title)}"
        lrc_path_b = MUSIC_DIR / f"{filename_b}.lrc"
        mp3_path_b = MUSIC_DIR / f"{filename_b}.mp3"
        
        # Soft romantic lyrics variant
        style_b_prompt = "Acoustic folk, fingerstyle acoustic guitar, warm upright bass, gentle brush drums, melodic piano, relaxing Japanese city pop, cozy cafe vibe, dual male-female mellow harmonies, 115 BPM"
        lrc_text_b = generate_lrc_content(
            title=f"{day_str} B版 - {base_title} ({style_b_desc})",
            day_str=day_str,
            version="B",
            style_name=style_b_desc,
            lyrics_text=lyrics,
            duration=195.0
        )
        with open(lrc_path_b, "w", encoding="utf-8") as f:
            f.write(lrc_text_b)
            
        manifest_tracks.append({
            "id": f"suno_{day_str.lower()}_b",
            "day": day_num,
            "day_str": day_str,
            "day_label": clean_day,
            "version": "B",
            "version_name": "🍃 B版 慢活民謠",
            "style_desc": style_b_desc,
            "title": f"{base_title} (慢活漫遊)",
            "display_name": f"{day_str} B版: {base_title} ({style_b_desc})",
            "theme": theme,
            "style_prompt": style_b_prompt,
            "duration": 195.0,
            "mp3_file": f"music/{filename_b}.mp3",
            "lrc_file": f"music/{filename_b}.lrc",
            "wav_file": f"wav/{filename_b}.wav",
            "stems_dir": f"stems/{filename_b}",
            "cover_file": f"covers/{day_str}_B_cover.jpg",
            "lyrics_preview": lyrics[:300] + "..."
        })

    # Sort tracks
    manifest_tracks.sort(key=lambda x: (x["day"], x["version"]))
    
    manifest_data = {
        "album": "2026 東京單車騎旅 19日主題曲全集 (38首雙主唱雙風格)",
        "artist": "2026 東京單車騎旅",
        "description": "東京・富士五湖・伊豆・東京灣 19日單車騎旅 Suno AI 官方雙版本音樂全集",
        "total_tracks": len(manifest_tracks),
        "days_count": 19,
        "tracks": manifest_tracks
    }
    
    with open(MANIFEST_FILE, "w", encoding="utf-8") as mf:
        json.dump(manifest_data, mf, ensure_ascii=False, indent=2)
        
    print(f"[SUCCESS] Generated {len(manifest_tracks)} tracks manifest in {MANIFEST_FILE}")
    print(f"[SUCCESS] Generated {len(manifest_tracks)} .lrc lyrics files in {MUSIC_DIR}")

if __name__ == "__main__":
    main()
