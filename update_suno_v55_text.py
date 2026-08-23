import sys
sys.stdout.reconfigure(encoding='utf-8')

with open("d:/2026東京單車騎旅/generate_suno_v55.py", "r", encoding="utf-8") as f:
    text = f.read()

# Update Day 1 Outro
old_d1_outro = '''[Outro: Soft Vocal Ad-lib & Guitar Outro]
[Voice: Female Vocal - Japanese] 調布の街に、茜色の夕焼け
[Voice: Male Vocal - Mandarin] 第一天，我們順利抵達
[Voice: Duet / Harmony]
Day One, Complete...'''

new_d1_outro = '''[Outro: Soft Vocal Ad-lib & Guitar Outro]
[Voice: Female Vocal - Japanese] 高尾山の麓、Base Camp の灯り
[Voice: Male Vocal - Mandarin] 泡進極樂湯溫泉 第一天七十八公里順利抵達
[Voice: Duet / Harmony]
Day One Complete, Mt. Takao Base Camp...'''

text = text.replace(old_d1_outro, new_d1_outro)

# Update Day 2 Outro
old_d2_outro = '''[Outro: Shamisen Outro Phrase & Fade]
[Voice: Male Vocal - Mandarin] 暮色降臨都留 聽見棘輪清脆的歌唱
[Voice: Female Vocal - Japanese] 山を越えた静かな歓喜、都留の夜へ
[Voice: Duet / Harmony]
(Shamisen outro phrase trailing into night wind)'''

new_d2_outro = '''[Outro: Shamisen Outro Phrase & Fade]
[Voice: Male Vocal - Mandarin] 翻越大垂水與秋山 抵達由加利旅館的溫暖
[Voice: Female Vocal - Japanese] 都留の町、由加利旅館で乾杯！
[Voice: Duet / Harmony]
(Shamisen outro phrase trailing into peaceful night wind)'''

text = text.replace(old_d2_outro, new_d2_outro)

with open("d:/2026東京單車騎旅/generate_suno_v55.py", "w", encoding="utf-8") as f:
    f.write(text)

print("Updated generate_suno_v55.py!")
