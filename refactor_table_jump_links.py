import re

# Read original base or current file
with open('d:/2026東京單車騎旅/tokyo_fuji_cycling_itinerary_19days_v2.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Clean up any malformed id="day-X""
content = re.sub(r'id="day-(\d+)"+\s*', '', content)
content = re.sub(r'class="summary-row-clickable"[^>]*', '', content)
content = re.sub(r'<span class="day-jump-badge">.*?</span>', '', content)
content = re.sub(r'\\\'', "'", content)

# 1. Add CSS
enhanced_css = """
        html {
            scroll-behavior: smooth;
        }

        .day-card {
            scroll-margin-top: 24px;
            transition: transform 0.15s ease, box-shadow 0.25s ease, border-color 0.25s ease;
        }

        .summary-row-clickable {
            cursor: pointer;
            transition: background-color 0.15s ease;
        }

        .summary-row-clickable:hover {
            background-color: #F0F9FF !important;
        }

        .day-jump-badge {
            display: inline-flex;
            align-items: center;
            gap: 4px;
            background: #EFF6FF;
            color: #1D4ED8;
            border: 1px solid #BFDBFE;
            padding: 2px 7px;
            border-radius: 6px;
            font-size: 11px;
            font-weight: 700;
            margin-top: 4px;
            transition: all 0.15s ease;
            text-decoration: none;
        }

        .summary-row-clickable:hover .day-jump-badge {
            background: #2563EB;
            color: #FFFFFF;
            border-color: #1D4ED8;
            transform: translateX(2px);
        }
"""

if 'summary-row-clickable' not in content:
    content = content.replace('/* 日程卡片 */', enhanced_css + '\n        /* 日程卡片 */')

# 2. Add id="day-X" to all 19 Day cards cleanly
for d in range(1, 20):
    content = re.sub(
        rf'(<!-- Day {d} -->\s*<div class="day-card)',
        rf'\1" id="day-{d}',
        content
    )

# 3. Enhance table rows with onclick="scrollToDay(d)" and jump badges
for d in range(1, 20):
    # Pattern matching <tr> preceding Day d in table
    # <td><strong>11/13（五）<br><span style="color:#B91C1C;">Day 1</span></strong>
    pattern = rf'<tr>(\s*<td><strong>\d+/\d+[^<]*?<br><span style="color:#B91C1C;">Day {d}</span></strong>)'
    replacement = rf'<tr class="summary-row-clickable" onclick="scrollToDay({d})" title="點擊直達 Day {d} 詳細騎行日程">\1<br><a href="#day-{d}" class="day-jump-badge" onclick="event.stopPropagation(); scrollToDay({d}); return false;">👇 詳細日程 ➔</a>'
    content = re.sub(pattern, replacement, content)

# 4. Add scrollToDay JS function before </body>
js_code = """
<script>
function scrollToDay(dayNum) {
    const el = document.getElementById('day-' + dayNum);
    if (el) {
        el.scrollIntoView({ behavior: 'smooth' });
        el.style.borderColor = '#2563EB';
        el.style.boxShadow = '0 0 0 3px rgba(37, 99, 235, 0.35)';
        setTimeout(() => {
            el.style.borderColor = '';
            el.style.boxShadow = '';
        }, 1800);
    }
}
</script>
"""

if 'function scrollToDay' not in content:
    content = content.replace('</body>', js_code + '\n</body>')

# 5. Save all copies
files_to_update = [
    'd:/2026東京單車騎旅/tokyo_fuji_cycling_itinerary_19days_v2.html',
    'd:/2026東京單車騎旅/index.html',
    'C:/Users/ymero/Downloads/tokyo_fuji_cycling_itinerary_19days_v2.html',
    'C:/Users/ymero/Downloads/index.html'
]

for fp in files_to_update:
    with open(fp, 'w', encoding='utf-8') as f:
        f.write(content)

print("Applied smooth scroll and highlight pulse on all 19 Day cards!")
