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
        print(f"Missing LRC: {folder.name}")
        continue
    lines = lrc_file.read_text(encoding="utf-8", errors="replace").splitlines()
    # Count valid timestamped lines
    timed_lines = [l for l in lines if re.match(r'\[\d+:\d+(?:\.\d+)?\]', l)]
    first_time = timed_lines[0][:10] if timed_lines else "None"
    last_time = timed_lines[-1][:10] if timed_lines else "None"
    print(f"{folder.name[:45]:<46} | {len(timed_lines):2d} lines | {first_time} ~ {last_time}")
