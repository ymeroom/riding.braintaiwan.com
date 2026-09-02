import json
import sys
from pathlib import Path

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
        sys.stderr.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass

WORKSPACE = Path(r"d:\2026東京單車騎旅")
PACK_DIR = WORKSPACE / "2026東京單車騎旅_手機隨身包"
MANIFEST_PATH = WORKSPACE / "songs_manifest.json"

with open(MANIFEST_PATH, "r", encoding="utf-8") as f:
    data = json.load(f)

tracks = data.get("tracks", [])

# Read all .lrc from PACK_DIR
lrc_files = {f.stem: f.read_text(encoding="utf-8") for f in PACK_DIR.glob("*.lrc")}

updated_count = 0
for t in tracks:
    day = t.get("day", 99)
    day_str = t.get("day_str", f"Day{day:02d}")
    ver = t.get("version", "A")
    style_desc = t.get("style_desc", "熱血搖滾")
    take_str = t.get("take_str", "Take1")
    title = t.get("title", "").replace(f" ({take_str})", "").replace("《", "").replace("》", "").strip()

    # Look for matching lrc
    found_lrc = None
    for stem, content in lrc_files.items():
        if f"{day:02d}_{day_str}_{ver}_{style_desc}_{take_str}" in stem:
            found_lrc = content
            break
        elif title.split()[0] in stem and str(day) in stem and ver in stem:
            found_lrc = content
            break

    if found_lrc:
        t["lyrics_lrc"] = found_lrc
        t["lyrics"] = "\n".join([line.split("]")[-1] for line in found_lrc.splitlines() if "]" in line])
        updated_count += 1

with open(MANIFEST_PATH, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"[SUCCESS] Updated {updated_count} / {len(tracks)} tracks in {MANIFEST_PATH}")
