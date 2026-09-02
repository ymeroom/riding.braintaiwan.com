import json
import sys
import re

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
        sys.stderr.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass

with open("workspace_clips_raw.json", "r", encoding="utf-8") as f:
    clips = json.load(f)

print(f"Total clips in raw feed: {len(clips)}")

# Filter clips that are songs (exclude individual stem isolated tracks unless needed)
full_songs = []
for c in clips:
    title = c.get("title", "")
    # Check if it's a full song or stem
    is_instrument_stem = any(f"({stem})" in title for stem in [
        "Vocals", "Instrumental", "Drums", "Bass", "Guitar", "Keyboard",
        "Percussion", "Strings", "Synth", "FX", "Brass", "Woodwinds", "Backing Vocals"
    ])
    if not is_instrument_stem and c.get("audio_url"):
        full_songs.append(c)

print(f"Full songs count: {len(full_songs)}")
for idx, s in enumerate(full_songs, 1):
    title = s.get("title", "")
    tags = s.get("metadata", {}).get("tags", "")
    dur = s.get("metadata", {}).get("duration", 0)
    cid = s.get("id")
    print(f"{idx:02d}. [{cid}] {title} | {dur:.1f}s | Tags: {tags[:60]}...")
