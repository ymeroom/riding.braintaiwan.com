import json
import sys
from pathlib import Path

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
        sys.stderr.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass

MANIFEST = Path(r"d:\2026東京單車騎旅\songs_manifest.json")
with open(MANIFEST, "r", encoding="utf-8") as f:
    tracks = json.load(f)["tracks"]

print(f"Total tracks: {len(tracks)}")
by_day_ver = {}
for t in tracks:
    key = f"Day{t.get('day', 99):02d}_{t.get('version', 'A')}"
    by_day_ver.setdefault(key, []).append(t)

print(f"Unique Day+Version combinations: {len(by_day_ver)}")
for k, v in sorted(by_day_ver.items()):
    takes = [t.get("take_str", "Take1") for t in v]
    durs = [f"{t.get('duration', 0):.1f}s" for t in v]
    print(f"  • {k:<10}: {len(v)} tracks ({', '.join(takes)}) | durs: {', '.join(durs)} | {v[0].get('title')[:25]}")
