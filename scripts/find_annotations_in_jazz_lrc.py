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

for folder in sorted(SRC_DIR.iterdir()):
    if not folder.is_dir() or folder.name.startswith(("_", ".")) or folder.name in ["slow mood", "播放器", "網頁版"]:
        continue
    lrc_file = folder / "lyrics.lrc"
    if not lrc_file.exists():
        continue
    lines = lrc_file.read_text(encoding="utf-8", errors="replace").splitlines()
    bad_lines = []
    for l in lines:
        t = re.sub(r'\[\d+:\d+(?:\.\d+)?\]', '', l).strip()
        # Check if line is a prompt instruction (English bracket, solo, sound effect, etc.)
        if re.search(r'^\(.*(?:chord|resonat|silence|guitar|fade|solo|effect|chime|sound|cheering).*\)$', t, re.I):
            bad_lines.append(l)
        elif re.search(r'^\[.*(?:Intro|Verse|Chorus|Solo|Bridge|Outro|Male|Female|Instrumental).*\]$', t, re.I):
            bad_lines.append(l)
    if bad_lines:
        print(f"[{folder.name}] ({len(bad_lines)} annotations found):")
        for b in bad_lines[:3]:
            print("   ", b)
