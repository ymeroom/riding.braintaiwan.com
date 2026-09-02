import json
import sys

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
        sys.stderr.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass

with open("workspace_clips_raw.json", "r", encoding="utf-8") as f:
    clips = json.load(f)

for day in [2, 3]:
    print(f"\n--- Checking Day {day} ---")
    for c in clips:
        t = c.get("title", "")
        if "峠道" in t or "Toge" in t or "水鏡" in t or "Sacred" in t or "Day 2" in t or "Day 3" in t:
            is_stem = any(f"({stem})" in t for stem in [
                "Vocals", "Instrumental", "Drums", "Bass", "Guitar", "Keyboard",
                "Percussion", "Strings", "Synth", "FX", "Brass", "Woodwinds", "Backing Vocals"
            ])
            if not is_stem:
                print(f"Main: [{c.get('id')}] {t} | dur: {c.get('metadata', {}).get('duration')}")
