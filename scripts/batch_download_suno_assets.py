#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Master Suno Asset Batch Downloader & Processor
Downloads MP3s, Cover Art, LRC lyrics, and Stems (WAV/MP3) for all clips in the workspace.
Embeds ID3 tags (cover, lyrics, album, artist, day) and updates songs_manifest.json.
"""

import os
import sys
import json
import re
import time
import requests
from pathlib import Path
from typing import Dict, Any, List, Optional
from tqdm import tqdm

# Force UTF-8 on Windows stdout
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
        sys.stderr.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass

# Mutagen for ID3 tagging
try:
    from mutagen.mp3 import MP3
    from mutagen.id3 import ID3, TIT2, TPE1, TALB, TDRC, TRCK, TCON, USLT, APIC
    MUTAGEN_AVAILABLE = True
except ImportError:
    MUTAGEN_AVAILABLE = False
    print("[WARN] mutagen library not found. ID3 tagging will be skipped.")

WORKSPACE_ROOT = Path(__file__).resolve().parent
MUSIC_DIR = WORKSPACE_ROOT / "music"
WAV_DIR = WORKSPACE_ROOT / "wav"
STEMS_DIR = WORKSPACE_ROOT / "stems"
COVERS_DIR = WORKSPACE_ROOT / "covers"
MANIFEST_FILE = WORKSPACE_ROOT / "songs_manifest.json"

MUSIC_DIR.mkdir(parents=True, exist_ok=True)
WAV_DIR.mkdir(parents=True, exist_ok=True)
STEMS_DIR.mkdir(parents=True, exist_ok=True)
COVERS_DIR.mkdir(parents=True, exist_ok=True)

# Map song title substrings to Day numbers
DAY_MAPPING = {
    "世界線的起跑線": 1,
    "World Line Departure": 1,
    "峠道狂詩曲": 2,
    "Toge Rhapsody": 2,
    "水鏡神域": 3,
    "Mirrored Sacred Realm": 3,
    "千圓紙幣的晨光": 4,
    "Morning Glow on the 1000-Yen Bill": 4,
    "山獸神之森": 5,
    "Sanctuary of the Ancient Woods": 5,
    "破風降臨千米疾走": 6,
    "Thousand-Meter Wind Descent": 6,
    "駿河灣的蔚藍防潮堤": 7,
    "Suruga Blue Sea Wall": 7,
    "修善寺竹林幽夢": 8,
    "Bamboo Dream of Shuzenji": 8,
    "熔岩懸崖與伊豆之瞳": 9,
    "Lava Cliffs and Eye of Izu": 9,
    "網代夕照的避風港": 10,
    "Ajiro Golden Haven": 10,
    "海灣夜空的最後花火": 11,
    "Fireworks Over the Caldera Bay": 11,
    "早雲柑橘道與湘南風": 12,
    "Mandarin Groves and Shonan Breeze": 12,
    "高校前的命運路口": 13,
    "Destiny Crossing at Kamakura High": 13,
    "獨角獸與彩虹之橋": 14,
    "Unicorn on the Rainbow Bridge": 14,
    "葛飾下町的昭和人情": 15,
    "Shitamachi Memories of Katsushika": 15,
    "江戶川無重力巡航": 16,
    "Zero-Gravity Cruise on Edogawa": 16,
    "萬棵水杉的黃金童話": 17,
    "Golden Fairy Tale of Metasequoia": 17,
    "神宮外苑的黃金雨": 18,
    "Golden Rain at Jingu Gaien": 18,
    "776公里的世界線閉環": 19,
    "Closing the 776km World Line": 19
}

def sanitize_filename(name: str) -> str:
    cleaned = re.sub(r'[\\/*?:"<>|《》\(\)]', '', name)
    cleaned = re.sub(r'\s+', '_', cleaned).strip(' ._')
    return cleaned

def format_lrc_timestamp(seconds: float) -> str:
    minutes = int(seconds // 60)
    remaining_secs = seconds % 60
    return f"[{minutes:02d}:{remaining_secs:05.2f}]"

def generate_lrc_from_prompt(title: str, day_str: str, version: str, style_name: str, lyrics_text: str, duration: float = 200.0) -> str:
    lines = [
        f"[ti:{title}]",
        f"[ar:2026 東京單車騎旅 ({version}版 - {style_name})]",
        f"[al:2026 東京單車騎旅 19日主題曲全集]",
        f"[by:Suno AI]",
        f"[length:{int(duration//60):02d}:{int(duration%60):02d}]",
        ""
    ]
    raw_lines = [l.strip() for l in lyrics_text.splitlines() if l.strip()]
    if raw_lines:
        step = max(2.5, (duration - 15.0) / max(len(raw_lines), 1))
        curr = 4.0
        for line in raw_lines:
            lines.append(f"{format_lrc_timestamp(curr)}{line}")
            curr += step
    return "\n".join(lines)

def download_file(url: str, dest_path: Path, desc: str = "") -> bool:
    if not url:
        return False
    if dest_path.exists() and dest_path.stat().st_size > 1024:
        return True

    dest_path.parent.mkdir(parents=True, exist_ok=True)
    temp_path = dest_path.with_suffix(dest_path.suffix + ".tmp")
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"
    }

    for attempt in range(3):
        try:
            r = requests.get(url, headers=headers, stream=True, timeout=60)
            if r.status_code == 200:
                total_size = int(r.headers.get("content-length", 0))
                with open(temp_path, "wb") as f, tqdm(
                    total=total_size,
                    unit="B",
                    unit_scale=True,
                    desc=desc or dest_path.name[:25],
                    leave=False
                ) as bar:
                    for chunk in r.iter_content(chunk_size=65536):
                        if chunk:
                            f.write(chunk)
                            bar.update(len(chunk))
                temp_path.replace(dest_path)
                return True
            elif r.status_code == 404:
                return False
            time.sleep(1)
        except Exception as e:
            time.sleep(2)

    if temp_path.exists():
        temp_path.unlink()
    return False

def embed_id3_tags(mp3_path: Path, metadata: Dict[str, Any], cover_path: Optional[Path] = None):
    if not MUTAGEN_AVAILABLE or not mp3_path.exists():
        return
    try:
        audio = MP3(str(mp3_path), ID3=ID3)
        try:
            audio.add_tags()
        except Exception:
            pass

        title = metadata.get("title", mp3_path.stem)
        artist = metadata.get("artist", "2026 東京單車騎旅")
        album = metadata.get("album", "2026 東京單車騎旅 19日主題曲全集")
        year = str(metadata.get("year", "2026"))
        track_no = str(metadata.get("track_number", "1"))
        genre = metadata.get("genre", "Cycling Soundtrack / J-Pop / Rock / Folk")
        lyrics = metadata.get("lyrics", "")

        audio.tags["TIT2"] = TIT2(encoding=3, text=title)
        audio.tags["TPE1"] = TPE1(encoding=3, text=artist)
        audio.tags["TALB"] = TALB(encoding=3, text=album)
        audio.tags["TDRC"] = TDRC(encoding=3, text=year)
        audio.tags["TRCK"] = TRCK(encoding=3, text=track_no)
        audio.tags["TCON"] = TCON(encoding=3, text=genre)

        if lyrics:
            audio.tags["USLT"] = USLT(encoding=3, lang="eng", desc="Lyrics", text=lyrics)

        if cover_path and cover_path.exists():
            with open(cover_path, "rb") as img_f:
                img_data = img_f.read()
                mime = "image/jpeg" if cover_path.suffix.lower() in [".jpg", ".jpeg"] else "image/png"
                audio.tags["APIC"] = APIC(
                    encoding=3,
                    mime=mime,
                    type=3,
                    desc="Cover",
                    data=img_data
                )
        audio.save(v2_version=3)
    except Exception as e:
        print(f"[WARN] ID3 error for {mp3_path.name}: {e}")

def main():
    print("\n=======================================================")
    print("   2026 東京單車騎旅 Suno 全資產批次下載與標籤寫入器   ")
    print("=======================================================\n")

    raw_file = WORKSPACE_ROOT / "workspace_clips_raw.json"
    if not raw_file.exists():
        print(f"[ERROR] {raw_file} not found. Please run fetch_all_clips.py first.")
        return

    with open(raw_file, "r", encoding="utf-8") as f:
        clips = json.load(f)

    print(f"[INFO] Loaded {len(clips)} total clips from Suno.")

    # Classify clips into main songs and stems
    main_songs = []
    stems_by_parent = {}

    for c in clips:
        title = c.get("title", "")
        is_stem = any(f"({stem})" in title for stem in [
            "Vocals", "Instrumental", "Drums", "Bass", "Guitar", "Keyboard",
            "Percussion", "Strings", "Synth", "FX", "Brass", "Woodwinds", "Backing Vocals"
        ])
        
        if is_stem:
            # Extract parent title
            parent_match = re.match(r'^(.*?)\s*\((Vocals|Instrumental|Drums|Bass|Guitar|Keyboard|Percussion|Strings|Synth|FX|Brass|Woodwinds|Backing Vocals)\)', title)
            if parent_match:
                parent_title = parent_match.group(1).strip()
                stem_type = parent_match.group(2).strip()
                stems_by_parent.setdefault(parent_title, []).append((stem_type, c))
        else:
            main_songs.append(c)

    print(f"[INFO] Identified {len(main_songs)} main songs and {sum(len(v) for v in stems_by_parent.values())} stem tracks.\n")

    # Group songs by day and version
    downloaded_tracks = []
    
    for idx, song in enumerate(main_songs, 1):
        cid = song.get("id")
        raw_title = song.get("title", "")
        audio_url = song.get("audio_url", "")
        image_url = song.get("image_large_url") or song.get("image_url", "")
        prompt = song.get("metadata", {}).get("prompt", "")
        tags = song.get("metadata", {}).get("tags", "")
        dur = song.get("metadata", {}).get("duration", 200.0)

        # Match day number
        matched_day = None
        for key, d_num in DAY_MAPPING.items():
            if key in raw_title or key in prompt:
                matched_day = d_num
                break
        if not matched_day:
            matched_day = idx

        day_str = f"Day{matched_day:02d}"

        # Match Version A vs B
        # A: Anime Rock, High Energy, J-Rock, 175 BPM
        # B: Acoustic Folk, Mellow, Bossa, Jazz, 105/120 BPM
        is_b = bool(re.search(r'Bossa|Folk|Acoustic|Mellow|Gentle|105 BPM|115 BPM|120 BPM|慢活|民謠', tags + " " + raw_title, re.I))
        version = "B" if is_b else "A"
        style_desc = "慢活民謠" if is_b else "熱血搖滾"

        clean_title = re.sub(r'^[《\(]?\s*(?:Day\s*\d+\s*[-_ ]*)?', '', raw_title).strip(' 》\)')
        base_name = f"{day_str}_{version}_{style_desc}_{sanitize_filename(clean_title)}"

        print(f"[{idx:02d}/{len(main_songs):02d}] 🚀 Processing: {base_name}")

        # 1. Download Cover Image
        cover_path = COVERS_DIR / f"{day_str}_{version}_cover.jpg"
        if image_url:
            download_file(image_url, cover_path, desc=f"Cover {day_str}_{version}")

        # 2. Download MP3
        mp3_path = MUSIC_DIR / f"{base_name}.mp3"
        if audio_url:
            download_file(audio_url, mp3_path, desc=f"MP3 {base_name[:20]}")

        # 3. Generate LRC
        lrc_path = MUSIC_DIR / f"{base_name}.lrc"
        lrc_text = generate_lrc_from_prompt(
            title=f"{day_str} {version}版 - {clean_title} ({style_desc})",
            day_str=day_str,
            version=version,
            style_name=style_desc,
            lyrics_text=prompt,
            duration=dur
        )
        with open(lrc_path, "w", encoding="utf-8") as lf:
            lf.write(lrc_text)

        # 4. Embed ID3 Tags
        if mp3_path.exists():
            embed_id3_tags(
                mp3_path,
                metadata={
                    "title": f"{day_str} {version}版 - {clean_title} ({style_desc})",
                    "artist": "2026 東京單車騎旅",
                    "album": "2026 東京單車騎旅 19日主題曲全集",
                    "year": 2026,
                    "track_number": idx,
                    "genre": f"Cycling / {style_desc}",
                    "lyrics": prompt
                },
                cover_path=cover_path
            )

        # 5. Download Stems for this song
        # Match stems by parent title
        stems_folder = STEMS_DIR / base_name
        stems_for_song = stems_by_parent.get(raw_title, [])
        if stems_for_song:
            stems_folder.mkdir(parents=True, exist_ok=True)
            for s_type, s_clip in stems_for_song:
                s_url = s_clip.get("audio_url")
                if s_url:
                    s_file = stems_folder / f"{s_type.lower()}.mp3"
                    download_file(s_url, s_file, desc=f"Stem {s_type}")

        downloaded_tracks.append({
            "id": cid,
            "day": matched_day,
            "day_str": day_str,
            "version": version,
            "style_desc": style_desc,
            "title": clean_title,
            "display_name": f"{day_str} {version}版: {clean_title} ({style_desc})",
            "tags": tags,
            "duration": dur,
            "mp3_file": f"music/{mp3_path.name}",
            "lrc_file": f"music/{lrc_path.name}",
            "cover_file": f"covers/{cover_path.name}" if cover_path.exists() else image_url,
            "stems_dir": f"stems/{base_name}" if stems_folder.exists() else None,
            "prompt_lyrics": prompt
        })

    # Update Manifest
    with open(MANIFEST_FILE, "w", encoding="utf-8") as mf:
        json.dump({
            "album": "2026 東京單車騎旅 19日主題曲全集 (Suno AI 官方雙版本)",
            "updated_at": time.strftime("%Y-%m-%d %H:%M:%S"),
            "total_tracks": len(downloaded_tracks),
            "tracks": sorted(downloaded_tracks, key=lambda x: (x["day"], x["version"]))
        }, mf, ensure_ascii=False, indent=2)

    print(f"\n=======================================================")
    print(f"🎉 全部音訊資產下載與標籤寫入完成！")
    print(f"• 成功下載 MP3 歌曲數: {len(downloaded_tracks)} 首")
    print(f"• 音訊資料夾: {MUSIC_DIR}")
    print(f"• 分軌資料夾: {STEMS_DIR}")
    print(f"• 封面資料夾: {COVERS_DIR}")
    print(f"• 播放器清單更新: {MANIFEST_FILE}")
    print(f"=======================================================\n")

if __name__ == "__main__":
    main()
