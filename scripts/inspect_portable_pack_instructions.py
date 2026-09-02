import os
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

all_lines = []
for lrc_file in PACK_DIR.glob("*.lrc"):
    text = lrc_file.read_text(encoding="utf-8", errors="replace")
    for line in text.splitlines():
        clean = re.sub(r'\[\d+:\d+(?:\.\d+)?\]', '', line).strip()
        if clean and not clean.startswith("[ti:") and not clean.startswith("[ar:") and not clean.startswith("[al:") and not clean.startswith("[by:") and not clean.startswith("[length:"):
            all_lines.append((lrc_file.name, clean))

print(f"Total lines in portable pack LRCs: {len(all_lines)}")

# Find lines with prompt instructions / brackets
sample_instr = set()
for fname, line in all_lines:
    if re.search(r'\[.*?(?:Verse|Chorus|Solo|Intro|Outro|Bridge|Male|Female|Instrumental|Fade|Drop|Guitar|Drum|Piano|Brass).*?\]', line, re.I):
        sample_instr.add(line)
    elif re.search(r'\(.*?(?:guitar|solo|fade|silence|synth|drums|beat|tempo|acoustic|sound|shred|pulse|chord).*?\)', line, re.I):
        sample_instr.add(line)

print(f"Found {len(sample_instr)} instruction variations in portable pack LRCs. Samples:")
for s in sorted(list(sample_instr))[:30]:
    print("  •", s)
