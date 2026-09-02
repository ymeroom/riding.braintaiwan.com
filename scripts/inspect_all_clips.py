import json
import sys

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
        sys.stderr.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass

# Combine all clips
with open("workspace_clips_raw.json", "r", encoding="utf-8") as f:
    c1 = json.load(f)

with open("all_user_clips.json", "r", encoding="utf-8") as f:
    c2 = json.load(f)

all_clips_dict = {}
for c in c1 + c2:
    cid = c.get("id")
    if cid:
        all_clips_dict[cid] = c

print(f"Total unique clips found: {len(all_clips_dict)}")

# Group by parent songs and stems
main_songs = []
stems = []

for cid, c in all_clips_dict.items():
    title = c.get("title", "")
    is_stem = any(f"({stem})" in title for stem in [
        "Vocals", "Instrumental", "Drums", "Bass", "Guitar", "Keyboard",
        "Percussion", "Strings", "Synth", "FX", "Brass", "Woodwinds", "Backing Vocals"
    ])
    if is_stem:
        stems.append(c)
    else:
        main_songs.append(c)

print(f"Main songs count: {len(main_songs)}")
print(f"Stems count: {len(stems)}")

print("\n=== All Main Songs ===")
for i, s in enumerate(main_songs, 1):
    t = s.get("title", "")
    dur = s.get("metadata", {}).get("duration", 0)
    created = s.get("created_at", "")[:10]
    tags = s.get("metadata", {}).get("tags", "")[:40]
    print(f"{i:02d}. [{s.get('id')}] {t} ({dur:.1f}s, {created}) | {tags}")
