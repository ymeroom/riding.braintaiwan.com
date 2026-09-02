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

SRC_DIR = Path(r"D:\Suno jazz version")

all_lines = []
for lrc_file in SRC_DIR.rglob("lyrics.lrc"):
    text = lrc_file.read_text(encoding="utf-8", errors="replace")
    for line in text.splitlines():
        # Strip timestamp
        clean = re.sub(r'\[\d+:\d+(?:\.\d+)?\]', '', line).strip()
        if clean:
            all_lines.append((lrc_file.parent.name, clean))

print(f"Total lines across all LRCs: {len(all_lines)}")

# Find lines with prompt instructions / brackets / purely English
print("\n--- Detected Instruction / Bracket / English Lines ---")
sample_instr = set()
for folder, line in all_lines:
    if re.search(r'\[.*?(?:Verse|Chorus|Solo|Intro|Outro|Bridge|Male|Female|Instrumental).*?\]', line, re.I):
        sample_instr.add(line)
    elif re.search(r'\(.*?(?:guitar|solo|fade|silence|synth|drums|beat|tempo|acoustic|sound).*?\)', line, re.I):
        sample_instr.add(line)
    elif line.startswith("(") and line.endswith(")") and any(w in line.lower() for w in ["power", "chord", "resonat", "shred", "fades", "tempo", "vibe"]):
        sample_instr.add(line)

for s in sorted(list(sample_instr))[:30]:
    print("  •", s)
