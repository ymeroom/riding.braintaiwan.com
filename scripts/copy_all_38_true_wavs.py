import os
import sys
import shutil
import subprocess
from pathlib import Path

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
        sys.stderr.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass

SRC_DIR = Path(r"D:\Suno jazz version")
DEST_DIR = Path(r"D:\2026東京單車騎旅\wav")

# Mapping of folder names in 'D:\Suno jazz version' to our standardized 19-day WAV filenames
DAYS_MAP = {
    "《世界線的起跑線 (World Line Departure)》": "01_Day01_A_熱血搖滾_Take1_世界線的起跑線 World Line Departure.wav",
    "《世界線的起跑線 (World Line Departure)》 v2": "01_Day01_A_熱血搖滾_Take2_世界線的起跑線 World Line Departure.wav",
    "《峠道狂詩曲 (Toge Rhapsody)》": "02_Day02_A_熱血搖滾_Take1_峠道狂詩曲 Toge Rhapsody.wav",
    "《峠道狂詩曲 (Toge Rhapsody)》 v2": "02_Day02_A_熱血搖滾_Take2_峠道狂詩曲 Toge Rhapsody.wav",
    "《水鏡神域 (Mirrored Sacred Realm)》": "03_Day03_A_熱血搖滾_Take1_水鏡神域 Mirrored Sacred Realm.wav",
    "《水鏡神域 (Mirrored Sacred Realm)》 v2": "03_Day03_A_熱血搖滾_Take2_水鏡神域 Mirrored Sacred Realm.wav",
    "《千圓紙幣的晨光 (Morning Glow on the 1000-Yen Bill)》": "04_Day04_B_慢活民謠_Take1_千圓紙幣的晨光 Morning Glow on the 1000-Yen Bill.wav",
    "《千圓紙幣的晨光 (Morning Glow on the 1000-Yen Bill)》 v2": "04_Day04_B_慢活民謠_Take2_千圓紙幣的晨光 Morning Glow on the 1000-Yen Bill.wav",
    "《山獸神之森的休止符 (Sanctuary of the Ancient Woods)》": "05_Day05_A_熱血搖滾_Take1_山獸神之森的休止符 Sanctuary of the Ancient Woods.wav",
    "《山獸神之森的休止符 (Sanctuary of the Ancient Woods)》 v2": "05_Day05_A_熱血搖滾_Take2_山獸神之森的休止符 Sanctuary of the Ancient Woods.wav",
    "《破風降臨千米疾走 (Thousand-Meter Wind Descent)》": "06_Day06_A_熱血搖滾_Take1_破風降臨千米疾走 Thousand-Meter Wind Descent.wav",
    "《破風降臨千米疾走 (Thousand-Meter Wind Descent)》 v2": "06_Day06_A_熱血搖滾_Take2_破風降臨千米疾走 Thousand-Meter Wind Descent.wav",
    "《駿河灣的蔚藍防潮堤 (Suruga Blue Sea Wall)》": "07_Day07_A_熱血搖滾_Take1_駿河灣的蔚藍防潮堤 Suruga Blue Sea Wall.wav",
    "《駿河灣的蔚藍防潮堤 (Suruga Blue Sea Wall)》 v2": "07_Day07_A_熱血搖滾_Take2_駿河灣的蔚藍防潮堤 Suruga Blue Sea Wall.wav",
    "《修善寺竹林幽夢 (Bamboo Dream of Shuzenji)》": "08_Day08_B_慢活民謠_Take1_修善寺竹林幽夢 Bamboo Dream of Shuzenji.wav",
    "《修善寺竹林幽夢 (Bamboo Dream of Shuzenji)》 v2": "08_Day08_B_慢活民謠_Take2_修善寺竹林幽夢 Bamboo Dream of Shuzenji.wav",
    "《熔岩懸崖與伊豆之瞳 (Lava Cliffs and Eye of Izu)》": "09_Day09_A_熱血搖滾_Take1_熔岩懸崖與伊豆之瞳 Lava Cliffs and Eye of Izu.wav",
    "《熔岩懸崖與伊豆之瞳 (Lava Cliffs and Eye of Izu)》 v2": "09_Day09_A_熱血搖滾_Take2_熔岩懸崖與伊豆之瞳 Lava Cliffs and Eye of Izu.wav",
    "《網代夕照的避風港 (Ajiro Golden Haven)》": "10_Day10_A_熱血搖滾_Take1_網代夕照的避風港 Ajiro Golden Haven.wav",
    "《網代夕照的避風港 (Ajiro Golden Haven)》 v2": "10_Day10_A_熱血搖滾_Take2_網代夕照的避風港 Ajiro Golden Haven.wav",
    "《海灣夜空的最後花火 (Fireworks Over the Caldera Bay)》": "11_Day11_A_熱血搖滾_Take1_海灣夜空的最後花火 Fireworks Over the Caldera Bay.wav",
    "《海灣夜空的最後花火 (Fireworks Over the Caldera Bay)》 v2": "11_Day11_A_熱血搖滾_Take2_海灣夜空的最後花火 Fireworks Over the Caldera Bay.wav",
    "《早雲柑橘道與湘南風 (Mandarin Groves and Shonan Breeze)》": "12_Day12_B_慢活民謠_Take1_早雲柑橘道與湘南風 Mandarin Groves and Shonan Breeze.wav",
    "《早雲柑橘道與湘南風 (Mandarin Groves and Shonan Breeze)》 v2": "12_Day12_B_慢活民謠_Take2_早雲柑橘道與湘南風 Mandarin Groves and Shonan Breeze.wav",
    "《高校前的命運路口 (Destiny Crossing at Kamakura High)》": "13_Day13_B_慢活民謠_Take1_高校前的命運路口 Destiny Crossing at Kamakura High.wav",
    "《高校前的命運路口 (Destiny Crossing at Kamakura High)》 v2": "13_Day13_B_慢活民謠_Take2_高校前的命運路口 Destiny Crossing at Kamakura High.wav",
    "《獨角獸與彩虹之橋 (Unicorn on the Rainbow Bridge)》": "14_Day14_A_熱血搖滾_Take1_獨角獸與彩虹之橋 Unicorn on the Rainbow Bridge.wav",
    "《獨角獸與彩虹之橋 (Unicorn on the Rainbow Bridge)》 v2": "14_Day14_B_慢活民謠_Take1_獨角獸與彩虹之橋 Unicorn on the Rainbow Bridge.wav",
    "《葛飾下町的昭和人情 (Shitamachi Memories of Katsushika)》": "15_Day15_A_熱血搖滾_Take1_葛飾下町的昭和人情 Shitamachi Memories of Katsushika.wav",
    "《葛飾下町的昭和人情 (Shitamachi Memories of Katsushika)》 v2": "15_Day15_A_熱血搖滾_Take2_葛飾下町的昭和人情 Shitamachi Memories of Katsushika.wav",
    "《江戶川無重力巡航 (Zero-Gravity Cruise on Edogawa)》": "16_Day16_B_慢活民謠_Take1_江戶川無重力巡航 Zero-Gravity Cruise on Edogawa.wav",
    "《江戶川無重力巡航 (Zero-Gravity Cruise on Edogawa)》 v2": "16_Day16_B_慢活民謠_Take2_江戶川無重力巡航 Zero-Gravity Cruise on Edogawa.wav",
    "《萬棵水杉的黃金童話 (Golden Fairy Tale of Metasequoia)》": "17_Day17_B_慢活民謠_Take1_萬棵水杉的黃金童話 Golden Fairy Tale of Metasequoia.wav",
    "《萬棵水杉的黃金童話 (Golden Fairy Tale of Metasequoia)》 v2": "17_Day17_B_慢活民謠_Take2_萬棵水杉的黃金童話 Golden Fairy Tale of Metasequoia.wav",
    "《神宮外苑的黃金雨 (Golden Rain at Jingu Gaien)》": "18_Day18_A_熱血搖滾_Take1_神宮外苑的黃金雨 Golden Rain at Jingu Gaien.wav",
    "《神宮外苑的黃金雨 (Golden Rain at Jingu Gaien)》 v2": "18_Day18_A_熱血搖滾_Take2_神宮外苑的黃金雨 Golden Rain at Jingu Gaien.wav",
    "《776公里的世界線閉環 (Closing the 776km World Line)》": "19_Day19_A_熱血搖滾_Take1_776公里的世界線閉環 Closing the 776km World Line.wav",
    "《776公里的世界線閉環 (Closing the 776km World Line)》 v2": "19_Day19_A_熱血搖滾_Take2_776公里的世界線閉環 Closing the 776km World Line.wav",
}

print(f"[INFO] Copying all {len(DAYS_MAP)} True Master WAV files...")
count = 0
for folder_name, dest_name in DAYS_MAP.items():
    src_wav = SRC_DIR / folder_name / "song.wav"
    dest_path = DEST_DIR / dest_name
    if src_wav.exists():
        shutil.copyfile(src_wav, dest_path)
        size_mb = dest_path.stat().st_size / (1024 * 1024)
        print(f"✅ [{count+1:02d}/{len(DAYS_MAP)}] {dest_name} ({size_mb:.1f} MB)")
        count += 1
    else:
        print(f"❌ Missing src: {src_wav}")

# Handle Day 1 inbox
inbox_wav = SRC_DIR / "_inbox" / "《世界線的起跑線 (World Line Departure)》.wav"
if inbox_wav.exists():
    d1_dest = DEST_DIR / "01_Day01_B_慢活民謠_Take1_世界線的起跑線 World Line Departure.wav"
    shutil.copyfile(inbox_wav, d1_dest)
    print(f"✅ [Inbox] 01_Day01_B_慢活民謠_Take1 ({d1_dest.stat().st_size / (1024*1024):.1f} MB)")

print(f"\n[SUCCESS] All True Master Lossless WAVs successfully copied to {DEST_DIR}!")
