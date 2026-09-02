import json
import sys
import re
from pathlib import Path

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
        sys.stderr.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass

MANIFEST = Path(r"d:\2026東京單車騎旅\songs_manifest.json")
SRC_DIR = Path(r"D:\Suno jazz version")

with open(MANIFEST, "r", encoding="utf-8") as f:
    tracks = json.load(f)["tracks"]

# Map folders in SRC_DIR to clip IDs
jazz_lrc_by_id = {}
jazz_lrc_by_name = {}

for folder in SRC_DIR.iterdir():
    if not folder.is_dir() or folder.name.startswith(("_", ".")) or folder.name in ["slow mood", "播放器", "網頁版"]:
        continue
    lrc_file = folder / "lyrics.lrc"
    if not lrc_file.exists():
        continue
    text = lrc_file.read_text(encoding="utf-8", errors="replace")
    
    # ID
    id_files = [f for f in folder.iterdir() if f.name.startswith(".id-")]
    if id_files:
        cid = id_files[0].name.replace(".id-", "")
        jazz_lrc_by_id[cid] = text
        
    clean_name = folder.name.replace("《", "").replace("》", "").replace(" v2", "").strip()
    jazz_lrc_by_name[clean_name] = text

print(f"Jazz LRC by ID: {len(jazz_lrc_by_id)}")
print(f"Jazz LRC by Name: {len(jazz_lrc_by_name)}")

matched_by_id = 0
matched_by_name = 0
no_lrc = 0

for t in tracks:
    cid = t.get("id")
    clean_title = t.get("title", "").replace("《", "").replace("》", "").split(" (")[0].strip()
    if cid in jazz_lrc_by_id:
        matched_by_id += 1
    elif clean_title in jazz_lrc_by_name:
        matched_by_name += 1
    else:
        no_lrc += 1
        print(f"No Jazz LRC for: Day {t.get('day', 99)} {t.get('version')} ({t.get('take_str')}): {clean_title}")

print(f"\nTotal: {len(tracks)} | Matched by ID: {matched_by_id} | Matched by Name: {matched_by_name} | Others: {no_lrc}")
