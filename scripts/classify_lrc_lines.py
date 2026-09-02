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

english_lines = []
for folder in sorted(SRC_DIR.iterdir()):
    if not folder.is_dir() or folder.name.startswith(("_", ".")) or folder.name in ["slow mood", "播放器", "網頁版"]:
        continue
    lrc_file = folder / "lyrics.lrc"
    if not lrc_file.exists():
        continue
    for line in lrc_file.read_text(encoding="utf-8", errors="replace").splitlines():
        t = re.sub(r'\[\d+:\d+(?:\.\d+)?\]', '', line).strip()
        # Check if contains ASCII / English or brackets
        if re.search(r'[a-zA-Z\(\)\[\]]', t):
            english_lines.append((folder.name, t))

print(f"Total lines with English or brackets: {len(english_lines)}")
unique_patterns = set(l[1] for l in english_lines)

print("\n--- ALL Unique English / Bracket Patterns Found in Suno LRCs ---")
for p in sorted(list(unique_patterns)):
    # Classify as REAL LYRIC or PROMPT ANNOTATION
    is_noise = False
    if re.search(r'(chord|resonat|silence|fades into|wave sound|bell chime|synth|guitar|orchestral|effect)', p, re.I):
        is_noise = True
    elif re.search(r'\[(Intro|Verse|Chorus|Pre-Chorus|Bridge|Outro|Solo|Instrumental)\]', p, re.I):
        is_noise = True
    status = "❌ NOISE (To Delete)" if is_noise else "✅ REAL LYRICS (Keep)"
    print(f"{status:<26} | {p}")
