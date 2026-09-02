import sys
sys.stdout.reconfigure(encoding='utf-8')

for filepath in ['C:/Users/ymero/Downloads/tokyo_fuji_cycling_itinerary_19days_v2.html', 'd:/2026東京單車騎旅/tokyo_fuji_cycling_itinerary_19days_v2.html']:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    target = '<span class="meta-tag">🍁 紅葉：富士五湖(最盛期) ➔ 伊豆溫泉 ➔ 鎌倉 ➔ 都心黃金銀杏</span>'
    replacement = target + '\n            <a href="suno_cycling_soundtrack_19days.html" target="_blank" class="meta-tag" style="background: #F59E0B; color: #1E293B; font-weight: 700; text-decoration: none;">🎵 19日 Suno AI 音樂詞庫 (一鍵複製) ➔</a>'
    
    if target in content and 'suno_cycling_soundtrack_19days.html' not in content:
        content = content.replace(target, replacement)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print("Updated", filepath)
