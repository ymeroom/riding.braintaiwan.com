import os, re

theme_css_global = """
        /* ==========================================================================
           🎨 5 大主題風格系統 (5 Visual Themes Engine)
           ========================================================================== */
        :root, [data-theme="cycling"] {
            --bg-dark: #12141A;
            --card-bg: #1E232E;
            --border: #333B4D;
            --text-light: #F3F4F6;
            --text-muted: #9CA3AF;
            --primary: #FB7185;
            --accent: #FBBF24;
            --header-grad: linear-gradient(135deg, #181B22 0%, #2A1728 50%, #0F172A 100%);
            --theme-tag: "🚴 單車專業風";
        }
        [data-theme="indie"] {
            --bg-dark: #F4EFEA;
            --card-bg: #FFFFFF;
            --border: #E5DDD3;
            --text-light: #3E3832;
            --text-muted: #786C60;
            --primary: #8C6239;
            --accent: #607274;
            --header-grad: linear-gradient(135deg, #5C4B40 0%, #8C6239 50%, #4A3E37 100%);
            --theme-tag: "🌿 文藝青年風";
        }
        [data-theme="sport"] {
            --bg-dark: #080B11;
            --card-bg: #111827;
            --border: #1F2937;
            --text-light: #F8FAFC;
            --text-muted: #94A3B8;
            --primary: #FC4C02;
            --accent: #10B981;
            --header-grad: linear-gradient(135deg, #0F172A 0%, #7C2D12 50%, #1E1B4B 100%);
            --theme-tag: "⚡ 運動極限風";
        }
        [data-theme="japan"] {
            --bg-dark: #FDF8F5;
            --card-bg: #FFFFFF;
            --border: #FBCFE8;
            --text-light: #1F2937;
            --text-muted: #4B5563;
            --primary: #DC2626;
            --accent: #DB2777;
            --header-grad: linear-gradient(135deg, #881337 0%, #BE123C 50%, #991B1B 100%);
            --theme-tag: "🎌 哈日和風";
        }
        [data-theme="outdoor"] {
            --bg-dark: #F0FDF4;
            --card-bg: #FFFFFF;
            --border: #BBF7D0;
            --text-light: #14532D;
            --text-muted: #374151;
            --primary: #059669;
            --accent: #D97706;
            --header-grad: linear-gradient(135deg, #064E3B 0%, #047857 50%, #78350F 100%);
            --theme-tag: "⛺ 休閒野營風";
        }

        body {
            background-color: var(--bg-dark) !important;
            color: var(--text-light) !important;
            transition: background-color 0.25s ease, color 0.25s ease;
        }
        header {
            background: var(--header-grad) !important;
        }

        .theme-switcher-compact {
            background: rgba(15, 23, 42, 0.9);
            backdrop-filter: blur(12px);
            border: 1px solid rgba(255, 255, 255, 0.15);
            border-radius: 12px;
            padding: 8px 12px;
            margin-bottom: 12px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            flex-wrap: wrap;
            gap: 6px;
        }
        .theme-btn-group-compact {
            display: flex;
            gap: 4px;
            flex-wrap: wrap;
        }
        .theme-btn-mini {
            background: #1E293B;
            border: 1px solid #334155;
            color: #CBD5E1;
            padding: 5px 9px;
            border-radius: 6px;
            font-size: 11.5px;
            font-weight: 700;
            cursor: pointer;
            transition: all 0.15s ease;
        }
        .theme-btn-mini:hover {
            color: #FFFFFF;
            border-color: #64748B;
        }
        .theme-btn-mini.active {
            background: #2563EB;
            color: #FFFFFF;
            border-color: #60A5FA;
        }
"""

theme_bar_compact_html = """
    <!-- 🎨 5 大主題風格即時切換系統 -->
    <div class="theme-switcher-compact">
        <div style="font-size:12.5px; font-weight:800; color:#F8FAFC;">
            <span>🎨 主題風格：</span>
            <span id="current-theme-name" style="color:#38BDF8;">🚴 單車專業風</span>
        </div>
        <div class="theme-btn-group-compact">
            <button type="button" class="theme-btn-mini" onclick="setTheme('indie')">🌿 文藝青年</button>
            <button type="button" class="theme-btn-mini" onclick="setTheme('sport')">⚡ 運動極限</button>
            <button type="button" class="theme-btn-mini" onclick="setTheme('japan')">🎌 哈日和風</button>
            <button type="button" class="theme-btn-mini active" onclick="setTheme('cycling')">🚴 單車專業</button>
            <button type="button" class="theme-btn-mini" onclick="setTheme('outdoor')">⛺ 休閒野營</button>
        </div>
    </div>
"""

theme_js_global = """
<script>
const THEMES = {
    'indie': { name: '🌿 文藝青年風', color: '#8C6239' },
    'sport': { name: '⚡ 運動極限風', color: '#FC4C02' },
    'japan': { name: '🎌 哈日和風', color: '#DC2626' },
    'cycling': { name: '🚴 單車專業風', color: '#FB7185' },
    'outdoor': { name: '⛺ 休閒野營風', color: '#059669' }
};

function setTheme(themeKey) {
    if (!THEMES[themeKey]) themeKey = 'cycling';
    document.documentElement.setAttribute('data-theme', themeKey);
    localStorage.setItem('riding_preferred_theme', themeKey);

    document.querySelectorAll('.theme-btn-mini, .theme-pill-btn').forEach(btn => {
        btn.classList.remove('active');
        if (btn.getAttribute('onclick') && btn.getAttribute('onclick').includes(themeKey)) {
            btn.classList.add('active');
        }
    });

    const label = document.getElementById('current-theme-name');
    if (label) {
        label.textContent = THEMES[themeKey].name;
        label.style.color = THEMES[themeKey].color;
    }
}

document.addEventListener('DOMContentLoaded', () => {
    const savedTheme = localStorage.getItem('riding_preferred_theme') || 'cycling';
    setTheme(savedTheme);
});
</script>
"""

pages = [
    'd:/2026東京單車騎旅/tokyo_cycling_19days_map_demo.html',
    'd:/2026東京單車騎旅/day1_route_map_demo.html',
    'd:/2026東京單車騎旅/day2_route_map_demo.html',
    'd:/2026東京單車騎旅/suno_cycling_soundtrack_19days.html',
    'C:/Users/ymero/Downloads/tokyo_cycling_19days_map_demo.html',
    'C:/Users/ymero/Downloads/day1_route_map_demo.html',
    'C:/Users/ymero/Downloads/day2_route_map_demo.html',
    'C:/Users/ymero/Downloads/suno_cycling_soundtrack_19days.html'
]

for p in pages:
    if os.path.exists(p):
        with open(p, 'r', encoding='utf-8') as f:
            c = f.read()

        if "🎨 5 大主題風格系統" not in c:
            c = c.replace('</style>', f'{theme_css_global}\n    </style>')

        if "theme-switcher-compact" not in c and '<div class="container">' in c:
            c = c.replace('<div class="container">', f'<div class="container">\n{theme_bar_compact_html}')
        elif "theme-switcher-compact" not in c and '<div class="content">' in c:
            c = c.replace('<div class="content">', f'{theme_bar_compact_html}\n<div class="content">')

        if "setTheme" not in c:
            c = c.replace('</body>', f'{theme_js_global}\n</body>')

        with open(p, 'w', encoding='utf-8') as f:
            f.write(c)

print("Applied 5-Theme Engine across all pages!")
