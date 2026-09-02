import sys
sys.stdout.reconfigure(encoding='utf-8')

with open("d:/2026東京單車騎旅/generate_suno_v55.py", "r", encoding="utf-8") as f:
    text = f.read()

# Update Day 11 Song title and outro for Atami fireworks
old_d11_def = '''        "day": 11,
        "date": "11/23 (一)",
        "stage": "stage2",
        "stage_name": "第二階段：朝霧駿河灣海堤 ➔ 伊豆名湯紅葉祭",
        "title": "蜜柑色の坂道：難攻不落の小田原城 (柑橘坡道・小田原開城之章)",
        "title_en": "Mandarin Orange Slopes: Impregnable Odawara",'''

new_d11_def = '''        "day": 11,
        "date": "11/23 (一)",
        "stage": "stage2",
        "stage_name": "第二階段：朝霧駿河灣海堤 ➔ 伊豆名湯紅葉祭",
        "title": "熱海海上花火：相模湾の夜空に咲く大輪 (熱海海上花火・夜空璀璨之章)",
        "title_en": "Atami Sea Fireworks: Blossoms in Sagami Night Sky",'''

text = text.replace(old_d11_def, new_d11_def)

# Update Day 10 Outro
old_d10_outro = '''[Outro: Muted Trumpet Trailing Over Ocean Moonroad]
[Voice: Female Vocal - Japanese] 熱海湾に浮かぶ、月の道
[Voice: Male Vocal - Mandarin] 熱海月夜，晚安
[Voice: Duet / Harmony]
(Trumpet solo fading out softly)'''

new_d10_outro = '''[Outro: Muted Trumpet Trailing Over Ocean Moonroad]
[Voice: Female Vocal - Japanese] 南熱海の長浜海岸、波の音が優しい
[Voice: Male Vocal - Mandarin] Apt南熱海的海景公寓，今夜安眠
[Voice: Duet / Harmony]
(Trumpet solo fading out softly over quiet waves)'''

text = text.replace(old_d10_outro, new_d10_outro)

# Update Day 11 Outro
old_d11_outro = '''[Outro: Triumphant Brass Coda]
[Voice: Female Vocal - Japanese] 小田原城の天守に、翻る秋風
[Voice: Male Vocal - Mandarin] 伊豆征程，圓滿收官！
[Voice: Duet / Harmony]
(Triumphant brass coda, big cymbal crash)'''

new_d11_outro = '''[Outro: Triumphant Brass Coda]
[Voice: Female Vocal - Japanese] 熱海湾の大花火、胸に響く轟音
[Voice: Male Vocal - Mandarin] 下多賀 Izu Kansya 的夜空，花火祭圓滿落幕！
[Voice: Duet / Harmony]
(Triumphant fireworks booming and brass coda)'''

text = text.replace(old_d11_outro, new_d11_outro)

with open("d:/2026東京單車騎旅/generate_suno_v55.py", "w", encoding="utf-8") as f:
    f.write(text)

print("Updated generate_suno_v55.py for Day 10 and Day 11 Atami stay!")
