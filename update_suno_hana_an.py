import sys
sys.stdout.reconfigure(encoding='utf-8')

with open("d:/2026東京單車騎旅/generate_suno_v55.py", "r", encoding="utf-8") as f:
    text = f.read()

# Update Day 15 Outro
old_d15_outro = '''[Outro: Nostalgic Whistle Trailing Over Riverbank]
[Voice: Female Vocal - Japanese] 赤水門の向こう、沈む夕日
[Voice: Male Vocal - Mandarin] 荒川金黃色的夕陽，晚安
[Voice: Duet / Harmony]
(Whistle melody softly trailing off into night silence)'''

new_d15_outro = '''[Outro: Nostalgic Whistle Trailing Over Riverbank]
[Voice: Female Vocal - Japanese] 葛飾金町、花庵旅舎の静かな灯り
[Voice: Male Vocal - Mandarin] 水元公園旁的下町，今夜安眠
[Voice: Duet / Harmony]
(Whistle melody softly trailing off into peaceful night)'''

text = text.replace(old_d15_outro, new_d15_outro)

# Update Day 16 Outro
old_d16_outro = '''[Outro: Shamisen and Accordion Festive Ending]
[Voice: Female Vocal - Japanese] 時の鐘が鳴る、小江戸の夕暮れ
[Voice: Male Vocal - Mandarin] 川越的黑瓦老街，明天見！
[Voice: Duet / Harmony]
(Festive shamisen and accordion chord finish)'''

new_d16_outro = '''[Outro: Shamisen and Accordion Festive Ending]
[Voice: Female Vocal - Japanese] 花庵旅舎連泊の夜、江戸川の風が心地いい
[Voice: Male Vocal - Mandarin] 週末免收行李的愜意，葛飾下町晚安！
[Voice: Duet / Harmony]
(Festive shamisen and accordion soft finish)'''

text = text.replace(old_d16_outro, new_d16_outro)

with open("d:/2026東京單車騎旅/generate_suno_v55.py", "w", encoding="utf-8") as f:
    f.write(text)

print("Updated generate_suno_v55.py for Day 15 and Day 16 Hostel Hana An!")
