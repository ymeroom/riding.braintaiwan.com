import os, re

# Complete CSS for Sticky Top 5-Theme Switcher
sticky_theme_css = """
        /* ==========================================================================
           🎨 5 大主題風格置頂切換列 (Sticky Top 5-Themes Switcher Bar)
           ========================================================================== */
        .top-theme-sticky-nav {
            position: sticky;
            top: 0;
            left: 0;
            right: 0;
            width: 100%;
            z-index: 99999;
            background: rgba(15, 23, 42, 0.95);
            backdrop-filter: blur(16px);
            -webkit-backdrop-filter: blur(16px);
            border-bottom: 2px solid rgba(59, 130, 246, 0.4);
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
            padding: 8px 12px;
            margin-bottom: 12px;
        }

        .theme-nav-inner {
            max-width: 1200px;
            margin: 0 auto;
            display: flex;
            align-items: center;
            justify-content: space-between;
            flex-wrap: wrap;
            gap: 8px;
        }

        .theme-nav-title {
            color: #FFFFFF;
            font-size: 13.5px;
            font-weight: 800;
            display: flex;
            align-items: center;
            gap: 6px;
            white-space: nowrap;
        }

        .theme-btn-group {
            display: flex;
            gap: 6px;
            flex-wrap: wrap;
            align-items: center;
        }

        .theme-pill-btn {
            background: #1E293B;
            border: 1px solid #475569;
            color: #E2E8F0;
            padding: 7px 12px;
            border-radius: 20px;
            font-size: 12px;
            font-weight: 700;
            cursor: pointer;
            transition: all 0.15s ease;
            display: inline-flex;
            align-items: center;
            gap: 4px;
            user-select: none;
        }

        .theme-pill-btn:hover {
            transform: translateY(-1px);
            color: #FFFFFF;
            border-color: #94A3B8;
            background: #334155;
        }

        .theme-pill-btn.active {
            background: #2563EB !important;
            color: #FFFFFF !important;
            border-color: #60A5FA !important;
            box-shadow: 0 0 12px rgba(37, 99, 235, 0.6) !important;
        }

        @media (max-width: 768px) {
            .top-theme-sticky-nav {
                padding: 6px 8px;
            }
            .theme-nav-inner {
                flex-direction: column;
                align-items: flex-start;
                gap: 6px;
            }
            .theme-btn-group {
                width: 100%;
                display: grid;
                grid-template-columns: repeat(3, 1fr);
                gap: 5px;
            }
            .theme-pill-btn {
                justify-content: center;
                padding: 8px 4px;
                font-size: 11px;
                border-radius: 6px;
            }
            .theme-pill-btn:nth-child(4), .theme-pill-btn:nth-child(5) {
                grid-column: span 1.5;
            }
        }
"""

sticky_theme_html = """
<!-- 🎨 5 大主題風格置頂即時切換列 (Sticky Top) -->
<div class="top-theme-sticky-nav">
    <div class="theme-nav-inner">
        <div class="theme-nav-title">
            <span>🎨 5 大風格切換：</span>
            <span id="current-theme-name" style="color: #38BDF8; font-weight: 800;">🚴 4. 單車風格</span>
        </div>
        <div class="theme-btn-group">
            <button type="button" class="theme-pill-btn" onclick="setTheme('indie')">🌿 1. 文藝青年</button>
            <button type="button" class="theme-pill-btn" onclick="setTheme('sport')">⚡ 2. 運動風格</button>
            <button type="button" class="theme-pill-btn" onclick="setTheme('japan')">🎌 3. 哈日風格</button>
            <button type="button" class="theme-pill-btn active" onclick="setTheme('cycling')">🚴 4. 單車風格</button>
            <button type="button" class="theme-pill-btn" onclick="setTheme('outdoor')">⛺ 5. 休閒風格</button>
        </div>
    </div>
</div>
"""

sticky_theme_js = """
<script>
// 5 Themes Definition
const THEMES = {
    'indie': { name: '🌿 1. 文藝青年風格 (Muji Minimal)', color: '#8C6239' },
    'sport': { name: '⚡ 2. 運動風格 (Strava Athletic)', color: '#FC4C02' },
    'japan': { name: '🎌 3. 哈日風格 (J-Pop / 和風朱赤)', color: '#DC2626' },
    'cycling': { name: '🚴 4. 單車風格 (Rapha Racing)', color: '#FB7185' },
    'outdoor': { name: '⛺ 5. 休閒風格 (Snow Peak Chill)', color: '#059669' }
};

function setTheme(themeKey) {
    if (!THEMES[themeKey]) themeKey = 'cycling';
    
    // Apply data-theme to HTML root
    document.documentElement.setAttribute('data-theme', themeKey);
    localStorage.setItem('riding_preferred_theme', themeKey);

    // Update active button state
    document.querySelectorAll('.theme-pill-btn, .theme-btn-mini').forEach(btn => {
        btn.classList.remove('active');
        if (btn.getAttribute('onclick') && btn.getAttribute('onclick').includes(themeKey)) {
            btn.classList.add('active');
        }
    });

    // Update indicator text
    const label = document.getElementById('current-theme-name');
    if (label) {
        label.textContent = THEMES[themeKey].name;
        label.style.color = THEMES[themeKey].color;
    }
}

// Auto load preferred theme immediately
(function() {
    const savedTheme = localStorage.getItem('riding_preferred_theme') || 'cycling';
    document.documentElement.setAttribute('data-theme', savedTheme);
})();

document.addEventListener('DOMContentLoaded', () => {
    const savedTheme = localStorage.getItem('riding_preferred_theme') || 'cycling';
    setTheme(savedTheme);
});
</script>
"""

# Process all files
target_files = [
    'd:/2026東京單車騎旅/index.html',
    'd:/2026東京單車騎旅/tokyo_fuji_cycling_itinerary_19days_v2.html',
    'd:/2026東京單車騎旅/tokyo_cycling_19days_map_demo.html',
    'd:/2026東京單車騎旅/day1_route_map_demo.html',
    'd:/2026東京單車騎旅/day2_route_map_demo.html',
    'd:/2026東京單車騎旅/suno_cycling_soundtrack_19days.html',
    'C:/Users/ymero/Downloads/index.html',
    'C:/Users/ymero/Downloads/tokyo_fuji_cycling_itinerary_19days_v2.html',
    'C:/Users/ymero/Downloads/tokyo_cycling_19days_map_demo.html',
    'C:/Users/ymero/Downloads/day1_route_map_demo.html',
    'C:/Users/ymero/Downloads/day2_route_map_demo.html',
    'C:/Users/ymero/Downloads/suno_cycling_soundtrack_19days.html'
]

for fp in target_files:
    if not os.path.exists(fp):
        continue
    with open(fp, 'r', encoding='utf-8') as f:
        html = f.read()

    # Remove any old theme switcher bars
    html = re.sub(r'<!-- 🎨 5 大主題風格即時切換系統.*?</div>\s*</div>', '', html, flags=re.DOTALL)
    html = re.sub(r'<!-- 🎨 5 大主題風格置頂即時切換列.*?</div>\s*</div>', '', html, flags=re.DOTALL)
    html = re.sub(r'<div class="theme-switcher-compact">.*?</div>\s*</div>', '', html, flags=re.DOTALL)

    # 1. Inject CSS if not present
    if "top-theme-sticky-nav" not in html:
        html = html.replace('</style>', f'{sticky_theme_css}\n    </style>')

    # 2. Place Sticky Theme Bar right after <body>
    html = re.sub(r'<body[^>]*>', f'<body>\n{sticky_theme_html}', html, count=1)

    # 3. Inject JS before </body>
    if "THEMES" not in html or "setTheme" not in html:
        html = html.replace('</body>', f'{sticky_theme_js}\n</body>')

    with open(fp, 'w', encoding='utf-8') as f:
        f.write(html)

print("Placed Sticky Top 5-Theme Switcher at the very top of all pages!")
