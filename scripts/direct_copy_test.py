import os
import sys
import shutil
from pathlib import Path

SRC = Path(r"D:\Suno jazz version")
DEST = Path(r"D:\2026東京單車騎旅\wav")

print("Copying inbox True WAV...")
inbox_wav = SRC / "_inbox" / "《世界線的起跑線 (World Line Departure)》.wav"
dest_wav = DEST / "01_Day01_B_慢活民謠_Take1_世界線的起跑線 World Line Departure.wav"

if inbox_wav.exists():
    shutil.copyfile(inbox_wav, dest_wav)
    print(f"Copied! Inbox size: {inbox_wav.stat().st_size}, Dest size: {dest_wav.stat().st_size}")
else:
    print("Inbox file not found!")
