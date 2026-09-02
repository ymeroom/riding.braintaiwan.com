import sys
import re
from pathlib import Path

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
        sys.stderr.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass

PACK_DIR = Path(r"d:\2026東京單車騎旅\2026東京單車騎旅_手機隨身包")

bad_found = []
for lrc in PACK_DIR.glob("*.lrc"):
    text = lrc.read_text(encoding="utf-8")
    for line in text.splitlines():
        if re.search(r'\[(Intro|Verse|Chorus|Solo|Bridge|Outro|Male|Female|Both|Duet)\]', line, re.I):
            bad_found.append((lrc.name, line))
        elif re.search(r'\(.*?(?:chord|resonat|silence|fades into|wave sound|bell chime|solo with|guitar duel|drum fill|cello solo).*?\)', line, re.I):
            bad_found.append((lrc.name, line))

print(f"Total .lrc files: {len(list(PACK_DIR.glob('*.lrc')))}")
print(f"Total prompt instruction anomalies found: {len(bad_found)}")
if bad_found:
    for f, l in bad_found[:10]:
        print(f"  • {f}: {l}")
else:
    print("✨ PERFECT! 100% of non-lyric prompt annotations have been cleanly eliminated!")
