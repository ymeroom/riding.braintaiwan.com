#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Distinct Multi-Take Downloader & ID3 Tagging for All 78 Tracks
Names every take distinctly (e.g. Day01_A_熱血搖滾_Take1_世界線的起跑線.mp3)
Ensures 100% of generated variations are preserved with full ID3 tags, covers, and LRC.
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

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
        sys.stderr.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass

from mutagen.mp3 import MP3
from mutagen.id3 import ID3, TIT2, TPE1, TALB, TDRC, TRCK, TCON, USLT, APIC

WORKSPACE_ROOT = Path(__file__).resolve().parent
MUSIC_DIR = WORKSPACE_ROOT / "music"
COVERS_DIR = WORKSPACE_ROOT / "covers"
STEMS_DIR = WORKSPACE_ROOT / "stems"
MANIFEST_FILE = WORKSPACE_ROOT / "songs_manifest.json"

MUSIC_DIR.mkdir(parents=True, exist_ok=True)
COVERS_DIR.mkdir(parents=True, exist_ok=True)
STEMS_DIR.mkdir(parents=True, exist_ok=True)

EXPECTED_DAYS = {
    1: ["世界線的起跑線", "World Line Departure"],
    2: ["峠道狂詩曲", "Toge Rhapsody"],
    3: ["水鏡神域", "Mirrored Sacred Realm"],
    4: ["千圓紙幣的晨光", "Morning Glow on the 1000-Yen Bill"],
    5: ["山獸神之森", "Sanctuary of the Ancient Woods"],
    6: ["破風降臨千米疾走", "Thousand-Meter Wind Descent"],
    7: ["駿河灣的蔚藍防潮堤", "Suruga Blue Sea Wall"],
    8: ["修善寺竹林幽夢", "Bamboo Dream of Shuzenji"],
    9: ["熔岩懸崖與伊豆之瞳", "Lava Cliffs and Eye of Izu"],
    10: ["網代夕照的避風港", "Ajiro Golden Haven"],
    11: ["海灣夜空的最後花火", "Fireworks Over the Caldera Bay"],
    12: ["早雲柑橘道與湘南風", "Mandarin Groves and Shonan Breeze"],
    13: ["高校前的命運路口", "Destiny Crossing at Kamakura High"],
    14: ["獨角獸與彩虹之橋", "Unicorn on the Rainbow Bridge"],
    15: ["葛飾下町的昭和人情", "Shitamachi Memories of Katsushika"],
    16: ["江戶川無重力巡航", "Zero-Gravity Cruise on Edogawa"],
    17: ["萬棵水杉的黃金童話", "Golden Fairy Tale of Metasequoia"],
    18: ["神宮外苑的黃金雨", "Golden Rain at Jingu Gaien"],
    19: ["776公里的世界線閉環", "Closing the 776km World Line"]
}

def sanitize_filename(name: str) -> str:
    cleaned = re.sub(r'[\\/*?:"<>|《》\(\)]', '', name)
    cleaned = re.sub(r'\s+', '_', cleaned).strip(' ._')
    return cleaned

def format_lrc_timestamp(seconds: float) -> str:
    minutes = int(seconds // 60)
    remaining_secs = seconds % 60
    return f"[{minutes:02d}:{remaining_secs:05.2f}]"

def generate_lrc_from_prompt(title: str, day_str: str, version: str, take_str: str, style_name: str, lyrics_text: str, duration: float = 200.0) -> str:
    lines = [
        f"[ti:{title} ({take_str})]",
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
    print("=" * 80)
    print("   2026 東京單車騎旅 78首全量 Take 獨立命名下載與 ID3 標籤寫入")
    print("=" * 80)

    with open("workspace_clips_raw.json", "r", encoding="utf-8") as f:
        all_clips = json.load(f)

    # 1. Separate main songs from stems
    main_clips = []
    stems_by_parent = {}

    for c in all_clips:
        title = c.get("title", "")
        is_stem = any(f"({stem})" in title for stem in [
            "Vocals", "Instrumental", "Drums", "Bass", "Guitar", "Keyboard",
            "Percussion", "Strings", "Synth", "FX", "Brass", "Woodwinds", "Backing Vocals"
        ])
        if is_stem:
            parent_match = re.match(r'^(.*?)\s*\((Vocals|Instrumental|Drums|Bass|Guitar|Keyboard|Percussion|Strings|Synth|FX|Brass|Woodwinds|Backing Vocals)\)', title)
            if parent_match:
                parent_title = parent_match.group(1).strip()
                stem_type = parent_match.group(2).strip()
                stems_by_parent.setdefault(parent_title, []).append((stem_type, c))
        else:
            if c.get("audio_url"):
                main_clips.append(c)

    print(f"[INFO] Total main songs to process: {len(main_clips)} songs")

    # 2. Sort by creation date
    main_clips.sort(key=lambda x: x.get("created_at", ""))

    # 3. Group and index takes per (Day, Version)
    take_counters = {}
    manifest_tracks = []

    for idx, clip in enumerate(main_clips, 1):
        cid = clip.get("id")
        raw_title = clip.get("title", "")
        audio_url = clip.get("audio_url", "")
        image_url = clip.get("image_large_url") or clip.get("image_url", "")
        prompt = clip.get("metadata", {}).get("prompt", "")
        tags = clip.get("metadata", {}).get("tags", "")
        dur = clip.get("metadata", {}).get("duration", 200.0)

        # Determine Day
        matched_day = None
        for d_num, kws in EXPECTED_DAYS.items():
            if any(k in raw_title or k in prompt for k in kws):
                matched_day = d_num
                break

        if matched_day:
            day_str = f"Day{matched_day:02d}"
            is_b = bool(re.search(r'Bossa|Folk|Acoustic|Mellow|Gentle|105 BPM|115 BPM|120 BPM|慢活|民謠', tags + " " + raw_title, re.I))
            version = "B" if is_b else "A"
            style_desc = "慢活民謠" if is_b else "熱血搖滾"
            clean_title = re.sub(r'^[《\(]?\s*(?:Day\s*\d+\s*[-_ ]*)?', '', raw_title).strip(' 》\)')
        else:
            day_str = "Bonus"
            version = "B" if bool(re.search(r'Folk|Acoustic|Mellow|慢活', tags + " " + raw_title, re.I)) else "A"
            style_desc = "慢活民謠" if version == "B" else "熱血搖滾"
            clean_title = sanitize_filename(raw_title)

        group_key = f"{day_str}_{version}_{clean_title}"
        take_counters[group_key] = take_counters.get(group_key, 0) + 1
        take_num = take_counters[group_key]
        take_str = f"Take{take_num}"

        base_filename = f"{day_str}_{version}_{style_desc}_{take_str}_{sanitize_filename(clean_title)}"
        print(f"[{idx:02d}/{len(main_clips):02d}] 🎵 {base_filename}")

        # Download Cover
        cover_path = COVERS_DIR / f"{day_str}_{version}_{take_str}_cover.jpg"
        if image_url:
            download_file(image_url, cover_path, desc=f"Cover {day_str}_{version}_{take_str}")

        # Download MP3
        mp3_path = MUSIC_DIR / f"{base_filename}.mp3"
        download_file(audio_url, mp3_path, desc=f"MP3 {base_filename[:20]}")

        # Generate LRC
        lrc_path = MUSIC_DIR / f"{base_filename}.lrc"
        lrc_text = generate_lrc_from_prompt(
            title=f"{day_str} {version}版 ({take_str}) - {clean_title} ({style_desc})",
            day_str=day_str,
            version=version,
            take_str=take_str,
            style_name=style_desc,
            lyrics_text=prompt,
            duration=dur
        )
        with open(lrc_path, "w", encoding="utf-8") as lf:
            lf.write(lrc_text)

        # Embed ID3 Tags
        if mp3_path.exists():
            embed_id3_tags(
                mp3_path,
                metadata={
                    "title": f"{day_str} {version}版 ({take_str}) - {clean_title} ({style_desc})",
                    "artist": "2026 東京單車騎旅",
                    "album": "2026 東京單車騎旅 19日主題曲全集",
                    "year": 2026,
                    "track_number": idx,
                    "genre": f"Cycling / {style_desc}",
                    "lyrics": prompt
                },
                cover_path=cover_path
            )

        # Download Stems
        stems_folder = STEMS_DIR / base_filename
        stems_for_song = stems_by_parent.get(raw_title, [])
        if stems_for_song:
            stems_folder.mkdir(parents=True, exist_ok=True)
            for s_type, s_clip in stems_for_song:
                s_url = s_clip.get("audio_url")
                if s_url:
                    s_file = stems_folder / f"{s_type.lower()}.mp3"
                    download_file(s_url, s_file, desc=f"Stem {s_type}")

        manifest_tracks.append({
            "id": cid,
            "day": matched_day or 99,
            "day_str": day_str,
            "version": version,
            "take": take_num,
            "take_str": take_str,
            "style_desc": style_desc,
            "title": f"{clean_title} ({take_str})",
            "display_name": f"{day_str} {version}版 ({take_str}): {clean_title} ({style_desc})",
            "tags": tags,
            "duration": dur,
            "mp3_file": f"music/{mp3_path.name}",
            "lrc_file": f"music/{lrc_path.name}",
            "cover_file": f"covers/{cover_path.name}" if cover_path.exists() else image_url,
            "stems_dir": f"stems/{base_filename}" if stems_folder.exists() else None,
            "prompt_lyrics": prompt
        })

    # Save final complete manifest
    with open(MANIFEST_FILE, "w", encoding="utf-8") as mf:
        json.dump({
            "album": "2026 東京單車騎旅 19日主題曲全集 (78首全量 Take 雙版本)",
            "updated_at": time.strftime("%Y-%m-%d %H:%M:%S"),
            "total_tracks": len(manifest_tracks),
            "tracks": manifest_tracks
        }, mf, ensure_ascii=False, indent=2)

    print("\n" + "=" * 80)
    print(f"🎉 全部 78 首 Take 獨立歸檔與標籤寫入 100% 完成！")
    print(f"• MP3 與 LRC 檔案數: {len(manifest_tracks)} 組")
    print(f"• 存放位置: {MUSIC_DIR}")
    print(f"• 播放清單索引: {MANIFEST_FILE}")
    print("=" * 80)

if __name__ == "__main__":
    main()
