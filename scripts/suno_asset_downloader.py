#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Suno AI Asset Downloader & Processor for 2026 Tokyo Cycling Tour
Downloads MP3, Cover Art, LRC Synced Lyrics, Lossless WAV, and Stem Separated Tracks (WAV).
Tags MP3 files with complete ID3 metadata and generates songs_manifest.json for the Web PWA Player.
"""

import os
import sys
import json
import time
import re
import argparse
import requests
from pathlib import Path
from typing import List, Dict, Any, Optional
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
    print("[WARN] mutagen library not found. ID3 tagging will be skipped. Run 'pip install mutagen' to enable.")

# Base directories
WORKSPACE_ROOT = Path(__file__).resolve().parent
MUSIC_DIR = WORKSPACE_ROOT / "music"
WAV_DIR = WORKSPACE_ROOT / "wav"
STEMS_DIR = WORKSPACE_ROOT / "stems"
COVERS_DIR = WORKSPACE_ROOT / "covers"
MANIFEST_FILE = WORKSPACE_ROOT / "songs_manifest.json"

DEFAULT_WORKSPACE_ID = "9e6e1488-d6d1-47ef-8ee4-b2ebe788f58b"
SUNO_API_BASE = "https://studio-api.prod.suno.com"

def ensure_directories():
    """Ensure all target asset directories exist."""
    MUSIC_DIR.mkdir(parents=True, exist_ok=True)
    WAV_DIR.mkdir(parents=True, exist_ok=True)
    STEMS_DIR.mkdir(parents=True, exist_ok=True)
    COVERS_DIR.mkdir(parents=True, exist_ok=True)

def sanitize_filename(name: str) -> str:
    """Sanitize string to be safe for Windows/Unix filenames."""
    # Replace illegal characters
    cleaned = re.sub(r'[\\/*?:"<>|]', '_', name)
    cleaned = re.sub(r'\s+', '_', cleaned).strip(' ._')
    return cleaned

def format_lrc_timestamp(seconds: float) -> str:
    """Format seconds into [mm:ss.xx] standard LRC timestamp."""
    minutes = int(seconds // 60)
    remaining_secs = seconds % 60
    return f"[{minutes:02d}:{remaining_secs:05.2f}]"

def convert_suno_timed_lyrics_to_lrc(clip_data: Dict[str, Any], raw_lyrics: str = "") -> str:
    """
    Convert Suno word/line timestamps to standard synchronized LRC format.
    Handles aligned_words, timed_lyrics, or raw prompt parsing.
    """
    lrc_lines = []
    
    # Metadata tags
    title = clip_data.get("title", "Tokyo Cycling Soundtrack")
    lrc_lines.append(f"[ti:{title}]")
    lrc_lines.append(f"[ar:2026 東京單車騎旅]")
    lrc_lines.append(f"[al:2026 東京單車騎旅 19日主題曲]")
    lrc_lines.append(f"[by:Suno AI]")
    lrc_lines.append("")

    timed_lyrics = clip_data.get("timed_lyrics") or clip_data.get("aligned_words")
    
    if timed_lyrics and isinstance(timed_lyrics, list):
        # Timed lyrics format 1: list of lines with start/end or word timings
        for item in timed_lyrics:
            if isinstance(item, dict):
                start = item.get("start") or item.get("start_time") or item.get("time") or 0.0
                text = item.get("text") or item.get("word") or item.get("line") or ""
                # Clean prompt tags like [Verse], [Chorus]
                if text.strip():
                    lrc_lines.append(f"{format_lrc_timestamp(float(start))}{text.strip()}")
            elif isinstance(item, str):
                lrc_lines.append(item)
    else:
        # Fallback: parse raw prompt/lyrics text
        lyrics_text = raw_lyrics or clip_data.get("metadata", {}).get("prompt", "") or clip_data.get("prompt", "")
        if lyrics_text:
            lines = [line.strip() for line in lyrics_text.splitlines() if line.strip()]
            duration = clip_data.get("metadata", {}).get("duration", 180.0) or 180.0
            
            # Filter out structural markers like [Verse 1], [Chorus] or keep them as timestamps
            parsed_entries = []
            for line in lines:
                parsed_entries.append(line)
            
            if parsed_entries:
                step = (duration - 10.0) / max(len(parsed_entries), 1)
                curr = 5.0
                for line in parsed_entries:
                    lrc_lines.append(f"{format_lrc_timestamp(curr)}{line}")
                    curr += step

    return "\n".join(lrc_lines)

class SunoClient:
    def __init__(self, token: Optional[str] = None):
        self.session = requests.Session()
        self.token = token.strip() if token else ""
        if self.token.startswith("Bearer "):
            self.token = self.token[7:].strip()
            
        self.session.headers.update({
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
            "Accept": "application/json",
            "Referer": "https://suno.com/",
            "Origin": "https://suno.com"
        })
        if self.token:
            self.session.headers["Authorization"] = f"Bearer {self.token}"

    def get_workspace_clips(self, workspace_id: str) -> List[Dict[str, Any]]:
        """Fetch all clips belonging to the workspace / project."""
        all_clips = []
        
        # Method 1: Project clips API
        endpoints_to_try = [
            f"{SUNO_API_BASE}/api/project/{workspace_id}/clips",
            f"{SUNO_API_BASE}/api/project/{workspace_id}",
            f"{SUNO_API_BASE}/api/feed/v2?project_id={workspace_id}",
            f"{SUNO_API_BASE}/api/feed/?project_id={workspace_id}",
            f"{SUNO_API_BASE}/api/playlist/{workspace_id}/"
        ]
        
        print(f"[INFO] Fetching tracks for Workspace ID: {workspace_id} ...")
        
        for endpoint in endpoints_to_try:
            try:
                page = 1
                while True:
                    url = f"{endpoint}?page={page}" if "?" not in endpoint else f"{endpoint}&page={page}"
                    resp = self.session.get(url, timeout=20)
                    if resp.status_code == 200:
                        data = resp.json()
                        clips = []
                        if isinstance(data, list):
                            clips = data
                        elif isinstance(data, dict):
                            clips = data.get("clips") or data.get("items") or data.get("playlist_clips") or data.get("data") or []
                            if not clips and "id" in data:
                                clips = [data]
                        
                        if clips:
                            all_clips.extend(clips)
                            print(f"[INFO] Loaded {len(clips)} clips from page {page} via {endpoint}")
                            # Check pagination
                            if len(clips) < 20 or not data.get("has_more", False) if isinstance(data, dict) else True:
                                break
                            page += 1
                        else:
                            break
                    elif resp.status_code == 401:
                        print("[ERROR] 401 Unauthorized. Your Suno Bearer Token may be expired or invalid.")
                        break
                    else:
                        break
                if all_clips:
                    break
            except Exception as e:
                print(f"[DEBUG] Endpoint {endpoint} failed: {e}")
                continue
                
        # Deduplicate clips by ID
        unique_clips = {}
        for c in all_clips:
            cid = c.get("id") or c.get("clip_id")
            if cid and cid not in unique_clips:
                unique_clips[cid] = c
                
        return list(unique_clips.values())

    def fetch_clip_timed_lyrics(self, clip_id: str) -> Optional[Dict[str, Any]]:
        """Fetch detailed synchronized lyrics timestamps for a clip."""
        endpoints = [
            f"{SUNO_API_BASE}/api/clip/{clip_id}/timed_lyrics",
            f"{SUNO_API_BASE}/api/gen/{clip_id}/aligned_lyrics/",
            f"{SUNO_API_BASE}/api/clip/{clip_id}"
        ]
        for url in endpoints:
            try:
                resp = self.session.get(url, timeout=15)
                if resp.status_code == 200:
                    data = resp.json()
                    if isinstance(data, dict) and ("timed_lyrics" in data or "aligned_words" in data or "timings" in data):
                        return data
            except Exception:
                continue
        return None

    def request_wav_url(self, clip_id: str) -> Optional[str]:
        """Request lossless WAV master download link (requires Pro/Premier)."""
        endpoints = [
            f"{SUNO_API_BASE}/api/gen/{clip_id}/download_wav/",
            f"{SUNO_API_BASE}/api/gen/wav/{clip_id}/",
            f"{SUNO_API_BASE}/api/clip/{clip_id}/download_wav"
        ]
        for url in endpoints:
            try:
                resp = self.session.post(url, timeout=20)
                if resp.status_code in [200, 201]:
                    data = resp.json()
                    return data.get("wav_url") or data.get("url") or data.get("audio_url")
                elif resp.status_code == 200 and resp.headers.get("content-type", "").startswith("audio/"):
                    return url
            except Exception:
                continue
        return None

    def request_stems(self, clip_id: str) -> Optional[List[Dict[str, Any]]]:
        """Request stem separation (Vocals + Instrumental WAV) for a clip."""
        # 1. Check if stems already generated
        try:
            resp = self.session.get(f"{SUNO_API_BASE}/api/clip/{clip_id}", timeout=15)
            if resp.status_code == 200:
                data = resp.json()
                if data.get("stem_clips"):
                    return data.get("stem_clips")
        except Exception:
            pass

        # 2. Trigger separation
        print(f"[INFO] Triggering Stem separation for clip {clip_id}...")
        try:
            resp = self.session.post(
                f"{SUNO_API_BASE}/api/gen/stems/",
                json={"clip_id": clip_id},
                timeout=20
            )
            if resp.status_code not in [200, 201]:
                resp = self.session.post(
                    f"{SUNO_API_BASE}/api/gen/{clip_id}/stems/",
                    timeout=20
                )
        except Exception as e:
            print(f"[WARN] Failed to trigger stems: {e}")
            return None

        # 3. Poll for completion (up to 60s)
        for _ in range(12):
            time.sleep(5)
            try:
                check = self.session.get(f"{SUNO_API_BASE}/api/clip/{clip_id}", timeout=15)
                if check.status_code == 200:
                    data = check.json()
                    stems = data.get("stem_clips")
                    if stems and len(stems) >= 2:
                        return stems
            except Exception:
                continue
        return None

def download_file(url: str, dest_path: Path, desc: str = "") -> bool:
    """Download a file with progress bar and retry mechanism."""
    if not url:
        return False
    
    if dest_path.exists() and dest_path.stat().st_size > 1024:
        # File already downloaded
        return True

    dest_path.parent.mkdir(parents=True, exist_ok=True)
    temp_path = dest_path.with_suffix(dest_path.suffix + ".tmp")

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"
    }

    for attempt in range(3):
        try:
            resp = requests.get(url, headers=headers, stream=True, timeout=60)
            if resp.status_code == 200:
                total_size = int(resp.headers.get("content-length", 0))
                with open(temp_path, "wb") as f, tqdm(
                    total=total_size,
                    unit="B",
                    unit_scale=True,
                    desc=desc or dest_path.name[:30],
                    leave=False
                ) as bar:
                    for chunk in resp.iter_content(chunk_size=65536):
                        if chunk:
                            f.write(chunk)
                            bar.update(len(chunk))
                temp_path.replace(dest_path)
                return True
            elif resp.status_code == 404:
                print(f"[WARN] 404 Not Found: {url}")
                return False
            time.sleep(2)
        except Exception as e:
            if attempt == 2:
                print(f"[ERROR] Failed to download {url}: {e}")
            time.sleep(2)
            
    if temp_path.exists():
        temp_path.unlink()
    return False

def embed_id3_tags(mp3_path: Path, metadata: Dict[str, Any], cover_path: Optional[Path] = None):
    """Write standard ID3v2.3 tags and embed cover art into MP3 file."""
    if not MUTAGEN_AVAILABLE or not mp3_path.exists():
        return

    try:
        audio = MP3(str(mp3_path), ID3=ID3)
        try:
            audio.add_tags()
        except Exception:
            pass # Tags already exist

        # UTF-8 encoded ID3 tags (encoding=3)
        title = metadata.get("title", mp3_path.stem)
        artist = metadata.get("artist", "2026 東京單車騎旅")
        album = metadata.get("album", "2026 東京單車騎旅 19日主題曲")
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

        # Embed Cover Art
        if cover_path and cover_path.exists():
            with open(cover_path, "rb") as img_f:
                img_data = img_f.read()
                mime = "image/jpeg" if cover_path.suffix.lower() in [".jpg", ".jpeg"] else "image/png"
                audio.tags["APIC"] = APIC(
                    encoding=3,
                    mime=mime,
                    type=3, # Cover (front)
                    desc="Cover",
                    data=img_data
                )

        audio.save(v2_version=3)
    except Exception as e:
        print(f"[WARN] Failed to write ID3 tags for {mp3_path.name}: {e}")

def organize_and_process_clips(clips: List[Dict[str, Any]], client: SunoClient, download_wav: bool = True, download_stems: bool = True):
    """
    Map clips to Day 01~19 A/B versions, download all assets, write ID3 tags, and output manifest.
    """
    ensure_directories()
    manifest_tracks = []
    
    print(f"\n=======================================================")
    print(f"  Processing {len(clips)} Suno Clips for 19-Day Cycling Tour")
    print(f"=======================================================\n")

    # Sort and categorize clips
    # Strategy: Match day and A/B style from title/tags or prompt
    for idx, clip in enumerate(clips, start=1):
        clip_id = clip.get("id") or clip.get("clip_id")
        raw_title = clip.get("title", f"Track_{idx}").strip()
        tags = clip.get("metadata", {}).get("tags", "") or clip.get("tags", "")
        prompt = clip.get("metadata", {}).get("prompt", "") or clip.get("prompt", "")
        audio_url = clip.get("audio_url", "")
        image_url = clip.get("image_large_url") or clip.get("image_url", "")
        duration = clip.get("metadata", {}).get("duration", 0) or clip.get("duration", 0)

        # Determine Day and Version A/B
        # Search patterns: Day 01, Day1, D01, D1, 第1天, etc.
        day_match = re.search(r'(?:Day|D|第)\s*([0-9]{1,2})', raw_title, re.IGNORECASE)
        if not day_match:
            day_match = re.search(r'(?:Day|D|第)\s*([0-9]{1,2})', prompt, re.IGNORECASE)

        day_num = int(day_match.group(1)) if day_match else ((idx - 1) // 2 + 1)
        day_str = f"Day{day_num:02d}"

        # Determine Version A (Rock/Energetic/Style 1) vs B (Folk/Acoustic/Style 2)
        version = "A"
        style_desc = "熱血搖滾"
        if re.search(r'[ _\-\[\(]B[ \]\-\)]|民謠|放鬆|Jazz|Acoustic|Folk|慢活|療癒', raw_title + " " + tags, re.IGNORECASE):
            version = "B"
            style_desc = "慢活民謠"
        elif re.search(r'[ _\-\[\(]A[ \]\-\)]|搖滾|熱血|Rock|Fast|Energetic|Power', raw_title + " " + tags, re.IGNORECASE):
            version = "A"
            style_desc = "熱血搖滾"
        else:
            # Fallback based on even/odd index
            version = "A" if (idx % 2 == 1) else "B"
            style_desc = "熱血搖滾" if version == "A" else "慢活民謠"

        clean_title = re.sub(r'^(?:Day|D|第)?\s*[0-9]{1,2}\s*[-_ ]*\s*(?:[AB][-_ ]*)?', '', raw_title, flags=re.IGNORECASE).strip()
        if not clean_title:
            clean_title = f"單車主題曲_{day_str}_{version}"

        base_name = f"{day_str}_{version}_{style_desc}_{sanitize_filename(clean_title)}"
        print(f"[{idx}/{len(clips)}] Processing: {base_name} (ID: {clip_id})")

        # 1. Download Cover Art
        cover_path = COVERS_DIR / f"{day_str}_{version}_cover.jpg"
        if image_url:
            download_file(image_url, cover_path, desc=f"Cover {day_str}_{version}")

        # 2. Download MP3
        mp3_path = MUSIC_DIR / f"{base_name}.mp3"
        if audio_url:
            download_file(audio_url, mp3_path, desc=f"MP3 {base_name[:20]}")

        # 3. Generate LRC Timed Lyrics
        lrc_path = MUSIC_DIR / f"{base_name}.lrc"
        # Try fetching real time alignment from API if available
        timed_data = client.fetch_clip_timed_lyrics(clip_id) if client.token else None
        merged_clip_data = {**clip, **(timed_data or {})}
        lrc_content = convert_suno_timed_lyrics_to_lrc(merged_clip_data, raw_lyrics=prompt)
        with open(lrc_path, "w", encoding="utf-8") as f_lrc:
            f_lrc.write(lrc_content)

        # 4. Embed ID3 Tags into MP3
        embed_id3_tags(
            mp3_path,
            metadata={
                "title": f"{day_str} {version}版 - {clean_title} ({style_desc})",
                "artist": "2026 東京單車騎旅",
                "album": "2026 東京單車騎旅 19日主題曲",
                "year": 2026,
                "track_number": idx,
                "genre": f"Cycling / {style_desc}",
                "lyrics": prompt or lrc_content
            },
            cover_path=cover_path
        )

        # 5. Lossless WAV Download (Optional)
        wav_path = WAV_DIR / f"{base_name}.wav"
        if download_wav and client.token:
            wav_url = clip.get("audio_wav_url") or clip.get("wav_url") or client.request_wav_url(clip_id)
            if wav_url:
                download_file(wav_url, wav_path, desc=f"WAV {base_name[:20]}")

        # 6. Stems Download (Optional)
        if download_stems and client.token:
            stems_folder = STEMS_DIR / base_name
            stem_clips = client.request_stems(clip_id)
            if stem_clips:
                stems_folder.mkdir(parents=True, exist_ok=True)
                for s_clip in stem_clips:
                    s_title = s_clip.get("title", "").lower()
                    s_type = "vocals" if "vocal" in s_title else "instrumental"
                    s_audio = s_clip.get("audio_wav_url") or s_clip.get("audio_url")
                    if s_audio:
                        download_file(s_audio, stems_folder / f"{s_type}.wav", desc=f"Stem {s_type}")

        # 7. Record to Manifest Entry
        manifest_tracks.append({
            "id": clip_id,
            "day": day_num,
            "day_str": day_str,
            "version": version,
            "style_desc": style_desc,
            "title": clean_title,
            "display_name": f"{day_str} {version}版: {clean_title} ({style_desc})",
            "tags": tags,
            "duration": duration,
            "mp3_file": f"music/{mp3_path.name}",
            "lrc_file": f"music/{lrc_path.name}",
            "wav_file": f"wav/{wav_path.name}" if wav_path.exists() else None,
            "cover_file": f"covers/{cover_path.name}" if cover_path.exists() else (image_url or "assets/default_cover.jpg"),
            "prompt_lyrics": prompt
        })

    # Sort manifest by Day and Version (A then B)
    manifest_tracks.sort(key=lambda x: (x["day"], x["version"]))

    # Save songs_manifest.json
    with open(MANIFEST_FILE, "w", encoding="utf-8") as mf:
        json.dump({
            "album": "2026 東京單車騎旅 19日主題曲全集 (38首雙版本)",
            "updated_at": time.strftime("%Y-%m-%d %H:%M:%S"),
            "total_tracks": len(manifest_tracks),
            "tracks": manifest_tracks
        }, mf, ensure_ascii=False, indent=2)

    print(f"\n[SUCCESS] All assets processed! Manifest saved to: {MANIFEST_FILE}")
    print(f"• Total MP3 & LRC: {len(manifest_tracks)}")
    print(f"• Music Folder: {MUSIC_DIR}")
    print(f"• WAV Folder: {WAV_DIR}")
    print(f"• Stems Folder: {STEMS_DIR}")

def main():
    parser = argparse.ArgumentParser(description="Suno AI Complete Asset Downloader & Processor")
    parser.add_argument("--token", "-t", help="Suno Bearer Token / Session Token (JWT)")
    parser.add_argument("--wid", "-w", default=DEFAULT_WORKSPACE_ID, help="Suno Workspace / Project ID")
    parser.add_argument("--input-json", "-i", help="Load clips from a local JSON file instead of API")
    parser.add_argument("--no-wav", action="store_true", help="Skip WAV master download")
    parser.add_argument("--no-stems", action="store_true", help="Skip stems separation & download")
    args = parser.parse_args()

    token = args.token or os.environ.get("SUNO_TOKEN")
    
    # If no token and no input JSON, prompt user
    if not token and not args.input_json:
        print("\n=======================================================")
        print("   Suno AI 38首主題曲 全資產自動化下載器 (2026東京騎旅)   ")
        print("=======================================================")
        print("\n請提供 Suno Bearer Token 以取得最高音質 WAV 與 Stems 分軌下載權限。")
        print("【如何獲取 Token】")
        print(" 1. 打開 Chrome / Edge 瀏覽器進入 suno.com 並登入")
        print(" 2. 按 F12 打開開發者人員工具 (DevTools) -> 切換到 'Network' (網路) 分頁")
        print(" 3. 在上方篩選欄輸入 'studio-api' 或 'client'")
        print(" 4. 點擊任一請求 -> 查看 'Headers' -> 複製 'authorization: Bearer eyJ...' 中的 Token")
        print(" (如果直接按 Enter 略過，腳本將嘗試使用公開 CDN 下載 MP3/封面/LRC)\n")
        
        user_input = input("請貼上 Suno Token (或直接按 Enter 僅下載公開資產): ").strip()
        if user_input:
            token = user_input

    client = SunoClient(token)
    clips = []

    if args.input_json and Path(args.input_json).exists():
        print(f"[INFO] Loading clips from local JSON: {args.input_json}")
        with open(args.input_json, "r", encoding="utf-8") as f:
            data = json.load(f)
            clips = data.get("clips") or data if isinstance(data, list) else [data]
    else:
        clips = client.get_workspace_clips(args.wid)

    if not clips:
        print("[WARN] No clips retrieved from Suno API directly.")
        print("[INFO] Fallback: If you have exported the workspace HAR or JSON, run:")
        print(f"       python suno_asset_downloader.py --input-json your_clips.json")
        return

    organize_and_process_clips(
        clips=clips,
        client=client,
        download_wav=not args.no_wav,
        download_stems=not args.no_stems
    )

if __name__ == "__main__":
    main()
