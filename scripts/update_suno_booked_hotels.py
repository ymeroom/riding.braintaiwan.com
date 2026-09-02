import sys
sys.stdout.reconfigure(encoding='utf-8')

with open("d:/2026東京單車騎旅/generate_suno_v55.py", "r", encoding="utf-8") as f:
    text = f.read()

# Update Day 8 Outro
old_d8_outro = '''[Outro: Shamisen Trailing with Onsen Water Sound]
[Voice: Female Vocal - Japanese] 竹林の小径、静かに響く湯の音
[Voice: Male Vocal - Mandarin] 今夜，在修善寺的古湯裡放鬆
[Voice: Duet / Harmony]
Good night, Shuzenji Onsen...'''

new_d8_outro = '''[Outro: Shamisen Trailing with Onsen Water Sound]
[Voice: Female Vocal - Japanese] 竹林の小径、温泉宿水口の温もり
[Voice: Male Vocal - Mandarin] 今夜在修善寺的古湯裡徹底放鬆，晚安
[Voice: Duet / Harmony]
Good night, Onsen Yado Mizuguchi...'''

text = text.replace(old_d8_outro, new_d8_outro)

# Update Day 9 Outro
old_d9_outro = '''[Outro: Electric Guitar Fading into Ocean Waves]
[Voice: Female Vocal - Japanese] 城ヶ崎の海、星が落ちる水平線
[Voice: Male Vocal - Mandarin] 東伊豆海岸，海風晚安
[Voice: Duet / Harmony]
(Surf sounds wash out the last guitar note)'''

new_d9_outro = '''[Outro: Electric Guitar Fading into Ocean Waves]
[Voice: Female Vocal - Japanese] 川奈の海風、kawana seaview の窓辺に星が降る
[Voice: Male Vocal - Mandarin] 東伊豆海岸第一排，海浪聲中晚安
[Voice: Duet / Harmony]
(Surf sounds wash out the last guitar note)'''

text = text.replace(old_d9_outro, new_d9_outro)

with open("d:/2026東京單車騎旅/generate_suno_v55.py", "w", encoding="utf-8") as f:
    f.write(text)

print("Updated generate_suno_v55.py for Day 8 and Day 9 booked hotels!")
