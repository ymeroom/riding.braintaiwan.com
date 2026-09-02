import sys
import time

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
        sys.stderr.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass

from faster_whisper import WhisperModel

print("Loading faster_whisper model (tiny/base)...")
t0 = time.time()
model = WhisperModel("tiny", device="cpu", compute_type="int8")
print(f"Model loaded in {time.time() - t0:.2f}s")

sample_audio = r"d:\2026東京單車騎旅\music\Day01_A_熱血搖滾_Take1_世界線的起跑線_World_Line_Departure.mp3"
segments, info = model.transcribe(sample_audio, beam_size=1)
print(f"Detected language: {info.language} ({info.language_probability:.2f})")

for i, s in enumerate(segments):
    if i < 5:
        print(f"[{s.start:.2f} -> {s.end:.2f}] {s.text}")
