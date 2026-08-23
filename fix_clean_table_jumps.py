import re

with open('d:/2026東京單車騎旅/tokyo_fuji_cycling_itinerary_19days_v2.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Let's clean up any double quotes or leftover tags in Day cards
for d in range(1, 20):
    content = re.sub(rf'<!-- Day {d} -->\s*<div class="day-card[^>]*>', f'<!-- Day {d} -->\n        <div class="day-card" id="day-{d}">', content)

# Now let's cleanly format each table row in the summary table
# For day 1 to 19:
for d in range(1, 20):
    # Match the row containing Day {d}
    # Pattern: <tr[^>]*>(\s*<td><strong>\d+/\d+[^<]*?<br><span style="color:#B91C1C;">Day {d}</span></strong>)
    pattern = rf'<tr[^>]*>(\s*<td><strong>\d+/\d+[^<]*?<br><span style="color:#B91C1C;">Day {d}</span></strong>)(?:<br><br>|<br>)?'
    replacement = rf'<tr class="summary-row-clickable" onclick="scrollToDay({d})" title="點擊直達 Day {d} 詳細騎行日程">\1<br><a href="#day-{d}" class="day-jump-badge" onclick="event.stopPropagation(); scrollToDay({d}); return false;">👇 詳細日程 ➔</a><br>'
    content = re.sub(pattern, replacement, content)

# Save to all target files
files = [
    'd:/2026東京單車騎旅/tokyo_fuji_cycling_itinerary_19days_v2.html',
    'd:/2026東京單車騎旅/index.html',
    'C:/Users/ymero/Downloads/tokyo_fuji_cycling_itinerary_19days_v2.html',
    'C:/Users/ymero/Downloads/index.html'
]

for fp in files:
    with open(fp, 'w', encoding='utf-8') as f:
        f.write(content)

print("Cleanly injected onclick and IDs for all 19 days!")
