import json
import sys
from collections import defaultdict

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
        sys.stderr.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass

with open("workspace_clips_raw.json", "r", encoding="utf-8") as f:
    clips = json.load(f)

print(f"Total raw clips: {len(clips)}")

# Separate main songs from stems
main_songs = []
stems_map = defaultdict(list)

for c in clips:
    title = c.get("title", "")
    is_stem = bool(c.get("is_stem") or "stem" in c.get("metadata", {}) or any(x in title for x in [
        "(Vocals)", "(Instrumental)", "(Drums)", "(Bass)", "(Guitar)", "(Keyboard)", 
        "(Percussion)", "(Strings)", "(Synth)", "(FX)", "(Brass)", "(Woodwinds)", "(Backing Vocals)"
    ]))
    
    if is_stem:
        # Group to parent song if parent_clip_id exists
        parent_id = c.get("parent_clip_id") or c.get("metadata", {}).get("parent_clip_id")
        base_title = title.split("》")[0] + "》" if "》" in title else title.split("(")[0].strip()
        key = parent_id or base_title
        stems_map[key].append(c)
    else:
        main_songs.append(c)

print(f"Main songs count: {len(main_songs)}")
print(f"Stems groupings count: {len(stems_map)}")

print("\n--- Main Songs List ---")
for i, s in enumerate(main_songs, 1):
    audio_url = s.get("audio_url")
    wav_url = s.get("audio_wav_url") or s.get("wav_url")
    title = s.get("title")
    duration = s.get("metadata", {}).get("duration")
    print(f"{i:02d}. [{s.get('id')}] {title} | dur: {duration}s | mp3: {'YES' if audio_url else 'NO'} | wav: {'YES' if wav_url else 'NO'}")
