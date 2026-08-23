import re

with open('d:/2026東京單車騎旅/tokyo_fuji_cycling_itinerary_19days_v2.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Add smooth scroll CSS and day-card scroll-margin
css_to_add = """
        html {
            scroll-behavior: smooth;
        }

        .day-card {
            scroll-margin-top: 40px;
        }

        .summary-row-clickable {
            cursor: pointer;
            transition: all 0.15s ease;
        }

        .summary-row-clickable:hover {
            background-color: #F0F9FF !important;
        }

        .day-jump-link {
            display: inline-block;
            color: inherit;
            text-decoration: none;
            width: 100%;
        }

        .day-jump-badge {
            display: inline-flex;
            align-items: center;
            gap: 4px;
            background: #EFF6FF;
            color: #1D4ED8;
            border: 1px solid #BFDBFE;
            padding: 3px 8px;
            border-radius: 6px;
            font-size: 11.5px;
            font-weight: 700;
            margin-top: 4px;
            transition: all 0.15s ease;
        }

        .summary-row-clickable:hover .day-jump-badge {
            background: #2563EB;
            color: #FFFFFF;
            border-color: #1D4ED8;
            transform: translateX(2px);
        }
"""

if 'summary-row-clickable' not in html:
    html = html.replace('/* 日程卡片 */', css_to_add + '\n        /* 日程卡片 */')

# 2. Add id="day-X" to all 19 day cards
for d in range(1, 20):
    old_card_pattern = f'<!-- Day {d} -->\\s*<div class="day-card"'
    # We want to replace `<div class="day-card"` with `<div class="day-card" id="day-{d}">`
    # Check if id="day-{d}" is already present
    if f'id="day-{d}"' not in html:
        # Match <!-- Day d --> \s* <div class="day-card"
        html = re.sub(
            rf'(<!-- Day {d} -->\s*<div class="day-card)("|\s)',
            rf'\1" id="day-{d}"\2',
            html
        )

# 3. Update the summary table rows to be clickable and link to #day-X
# In the summary table:
# Match <tr> \s* <td><strong>(11/\d+.*?Day (\d+).*?)</td>
# We can make each row have onclick="location.hash='#day-{d}'" and add .summary-row-clickable
def replace_table_row(match):
    day_num = match.group(1)
    return f'<tr class="summary-row-clickable" onclick="document.getElementById(\'day-{day_num}\').scrollIntoView({{behavior: \'smooth\'}})" title="點擊直達 Day {day_num} 詳細騎行日程">'

# Let's see the structure of rows in the summary table
# Rows have: <td><strong>11/13（五）<br><span style="color:#B91C1C;">Day 1</span></strong>
for d in range(1, 20):
    # Pattern: <td><strong>(11/\d+.*?)Day {d}</span></strong>
    # Let's replace the <tr> preceding Day d
    pattern = rf'<tr>(\s*<td><strong>\d+/\d+[^<]*?<br><span style="color:#B91C1C;">Day {d}</span></strong>)'
    replacement = rf'<tr class="summary-row-clickable" onclick="document.getElementById(\'day-{d}\').scrollIntoView({{behavior: \'smooth\'}})" title="點擊直達 Day {d} 詳細騎行日程">\1<br><span class="day-jump-badge">👇 詳細日程 ➔</span>'
    html = re.sub(pattern, replacement, html)

# Also update table header note to tell the user they can click any row to jump
html = html.replace(
    '📊 19日每日里程、爬升、去年實測天氣與紅葉見頃總覽 (日本國土地理院 GSI 1m DEM 實測核實版)',
    '📊 19日每日里程、爬升、去年實測天氣與紅葉見頃總覽 ｜ 💡 點擊任一日程即可直達下方詳細規劃'
)

# Save to all locations
with open('d:/2026東京單車騎旅/tokyo_fuji_cycling_itinerary_19days_v2.html', 'w', encoding='utf-8') as f:
    f.write(html)

with open('d:/2026東京單車騎旅/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

with open('C:/Users/ymero/Downloads/tokyo_fuji_cycling_itinerary_19days_v2.html', 'w', encoding='utf-8') as f:
    f.write(html)

with open('C:/Users/ymero/Downloads/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Successfully patched table jump links to all 19 day cards!")
