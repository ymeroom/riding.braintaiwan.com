import sys
sys.stdout.reconfigure(encoding='utf-8')

# Read generate_suno_v55.py
with open("d:/2026東京單車騎旅/generate_suno_v55.py", "r", encoding="utf-8") as f:
    text = f.read()

# Update Day 5 & Day 6 definitions
old_d5_block = '''        "day": 5,
        "date": "11/17 (二)",
        "stage": "stage1",
        "stage_name": "第一階段：多摩川出城 ➔ 富士五湖賞楓",
        "title": "千円札の蒼い鏡：青木ヶ原の風 (千圓紙幣上的逆富士)",
        "title_en": "The Thousand-Yen Mirror: Aoki Forest Wind",'''

new_d5_block = '''        "day": 5,
        "date": "11/17 (二)",
        "stage": "stage1",
        "stage_name": "第一階段：多摩川出城 ➔ 富士五湖賞楓",
        "title": "湖畔の休息：青木ヶ原と癒しの里 (湖畔休整・樹海與療癒之里)",
        "title_en": "Lakeside Rest: Aoki Forest & Healing Village",'''

text = text.replace(old_d5_block, new_d5_block)

old_d6_block = '''        "day": 6,
        "date": "11/18 (三)",
        "stage": "stage1",
        "stage_name": "第一階段：多摩川出城 ➔ 富士五湖賞楓",
        "title": "新倉山絵葉書：五重塔と富士の休日 (新倉山明信片・富士休整日)",
        "title_en": "Arakurayama Postcard: The Pagoda and Rest Day",'''

new_d6_block = '''        "day": 6,
        "date": "11/18 (三)",
        "stage": "stage1",
        "stage_name": "第一階段：多摩川出城 ➔ 富士五湖賞楓",
        "title": "千円札の蒼い鏡：朝霧高原ダウンヒル (千圓逆富士・朝霧高原俯衝之章)",
        "title_en": "Thousand-Yen Mirror: Asagiri Plateau Downhill",'''

text = text.replace(old_d6_block, new_d6_block)

with open("d:/2026東京單車騎旅/generate_suno_v55.py", "w", encoding="utf-8") as f:
    f.write(text)

print("Updated generate_suno_v55.py for Day 5 & 6 swap!")
