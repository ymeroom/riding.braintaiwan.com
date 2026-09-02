import json
import sys
from pathlib import Path

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
        sys.stderr.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass

SRC_DIR = Path(r"D:\Suno jazz version")
MANIFEST = Path(r"d:\2026東京單車騎旅\songs_manifest.json")

with open(MANIFEST, "r", encoding="utf-8") as f:
    tracks = json.load(f)["tracks"]

tracks_by_id = {t["id"]: t for t in tracks if "id" in t}

print(f"Total tracks in manifest: {len(tracks)}")

# Check each folder in Suno jazz version
found_in_manifest = 0
not_found = []

for folder in sorted(SRC_DIR.iterdir()):
    if not folder.is_dir() or folder.name.startswith(("_", ".")) or folder.name in ["slow mood", "播放器", "網頁版"]:
        continue
    id_files = [f for f in folder.iterdir() if f.name.startswith(".id-")]
    if id_files:
        cid = id_files[0].name.replace(".id-", "")
        if cid in tracks_by_id:
            t = tracks_by_id[cid]
            day_str = f"Day{t.get('day', 99):02d}"
            ver = t.get("version", "A")
            take = t.get("take_str", "Take1")
            print(f"Folder: {folder.name:<55} -> {day_str} {ver} ({take}): {t.get('title')[:30]}")
            found_in_manifest += 1
        else:
            not_found.append((folder.name, cid))
    else:
        not_found.append((folder.name, "No .id- file"))

print(f"\nMatched {found_in_manifest} folders to manifest.")
if not_found:
    print(f"Unmatched: {len(not_found)}")
    for n, i in not_found:
        print("  ", n, i)
