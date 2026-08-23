import re

files_suno = [
    'C:/Users/ymero/Downloads/suno_cycling_soundtrack_19days.html',
    'd:/2026東京單車騎旅/suno_cycling_soundtrack_19days.html'
]

for path in files_suno:
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()

    # Update Track 11 lyrics
    html = re.sub(
        r'Izu Kansya',
        'guest house MARUYA（熱海銀座）',
        html
    )
    html = re.sub(
        r'下多賀1473-11',
        '熱海銀座町7-8',
        html
    )

    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)

print("Updated Suno soundtrack HTML for Track 11!")
