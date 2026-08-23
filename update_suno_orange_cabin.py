import sys
sys.stdout.reconfigure(encoding='utf-8')

with open("d:/2026東京單車騎旅/generate_suno_v55.py", "r", encoding="utf-8") as f:
    text = f.read()

# Update Day 3 Outro
old_d3_outro = '''[Outro: Soft Piano Trailing into Wind]
[Voice: Female Vocal - Japanese] 静かな湖畔、満天の星空
[Voice: Male Vocal - Mandarin] 今夜，山中湖在星光下睡去
[Voice: Duet / Harmony]
Good night, Mt. Fuji...'''

new_d3_outro = '''[Outro: Soft Piano Trailing into Wind]
[Voice: Female Vocal - Japanese] 河口湖北岸、Orange Cabin の温もり
[Voice: Male Vocal - Mandarin] 紅葉迴廊旁的木屋 今夜在富士山下安眠
[Voice: Duet / Harmony]
Good night, Orange Cabin and Mt. Fuji...'''

text = text.replace(old_d3_outro, new_d3_outro)

# Update Day 4 Outro
old_d4_outro = '''[Outro: Violin and Piano Duet Softly Fading]
[Voice: Female Vocal - Japanese] 夜の回廊に、灯る赤い光
[Voice: Male Vocal - Mandarin] 河口湖的紅葉，晚安
[Voice: Duet / Harmony]
(Violin trails off into gentle silence)'''

new_d4_outro = '''[Outro: Violin and Piano Duet Softly Fading]
[Voice: Female Vocal - Japanese] 夜の回廊に灯る赤い光、Orange Cabin 連泊の贅沢
[Voice: Male Vocal - Mandarin] 免收行李的第二晚，河口湖紅葉迴廊，晚安
[Voice: Duet / Harmony]
(Violin and piano trailing off into serene lake silence)'''

text = text.replace(old_d4_outro, new_d4_outro)

with open("d:/2026東京單車騎旅/generate_suno_v55.py", "w", encoding="utf-8") as f:
    f.write(text)

print("Updated generate_suno_v55.py with Orange Cabin text!")
