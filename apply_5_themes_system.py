import re

# Theme System CSS and JS for tokyo_fuji_cycling_itinerary_19days_v2.html & index.html
theme_css = """
        /* ==========================================================================
           🎨 5 大主題風格系統 (5 Visual Themes Engine)
           1. 文藝青年風格 (Indie / Muji / Warm Minimalist)
           2. 運動風格 (Athletic / High-Energy Strava / Neon)
           3. 哈日風格 (J-Pop / 和風朱赤 / 日本動漫)
           4. 單車風格 (Pro Cycling / Rapha Asphalt & Hi-Vis Pink)
           5. 休閒風格 (Outdoor Camping / Nature Chill)
           ========================================================================== */

        /* 預設主題：4. 單車風格 (Cycling) 或 可自由切換 */
        :root, [data-theme="cycling"] {
            --bg-body: #12141A;
            --bg-container: #181B22;
            --card-bg: #212631;
            --card-border: #333B4D;
            --text-main: #F3F4F6;
            --text-sub: #9CA3AF;
            --text-muted: #6B7280;
            --brand-primary: #FB7185; /* Rapha Hi-Vis Pink */
            --brand-secondary: #FBBF24; /* Tour de France Yellow */
            --brand-accent: #38BDF8;
            --hero-bg: linear-gradient(135deg, #181B22 0%, #2A1728 50%, #0F172A 100%);
            --hero-text: #FFFFFF;
            --stat-val: #FB7185;
            --table-header-bg: #262D3D;
            --table-header-text: #F3F4F6;
            --table-stripe: #1C212B;
            --day-title-color: #FB7185;
            --day-num-bg: #FB7185;
            --day-num-text: #FFFFFF;
            --elev-pill-bg: #881337;
            --elev-pill-text: #FECDD3;
            --theme-tag: "🚴 單車專業風 (Rapha Racing)";
        }

        /* 1. 文藝青年風格 (Indie / Muji / Kraft) */
        [data-theme="indie"] {
            --bg-body: #F4EFEA;
            --bg-container: #FAF7F2;
            --card-bg: #FFFFFF;
            --card-border: #E5DDD3;
            --text-main: #3E3832;
            --text-sub: #786C60;
            --text-muted: #9E9184;
            --brand-primary: #8C6239; /* Morandi Cedar */
            --brand-secondary: #607274; /* Earth Grey-Green */
            --brand-accent: #B06161;
            --hero-bg: linear-gradient(135deg, #5C4B40 0%, #8C6239 50%, #4A3E37 100%);
            --hero-text: #FFFDF9;
            --stat-val: #8C6239;
            --table-header-bg: #EDE5DC;
            --table-header-text: #3E3832;
            --table-stripe: #F9F6F1;
            --day-title-color: #5C4B40;
            --day-num-bg: #8C6239;
            --day-num-text: #FFFFFF;
            --elev-pill-bg: #EDE5DC;
            --elev-pill-text: #5C4B40;
            --theme-tag: "🌿 文藝青年風 (Muji Minimal)";
        }

        /* 2. 運動風格 (Athletic / Strava / Neon) */
        [data-theme="sport"] {
            --bg-body: #080B11;
            --bg-container: #0F172A;
            --card-bg: #1E293B;
            --card-border: #334155;
            --text-main: #F8FAFC;
            --text-sub: #94A3B8;
            --text-muted: #64748B;
            --brand-primary: #FC4C02; /* Strava Energy Orange */
            --brand-secondary: #10B981; /* High-Volt Emerald */
            --brand-accent: #06B6D4; /* Electric Cyan */
            --hero-bg: linear-gradient(135deg, #0F172A 0%, #7C2D12 50%, #1E1B4B 100%);
            --hero-text: #FFFFFF;
            --stat-val: #FC4C02;
            --table-header-bg: #1E293B;
            --table-header-text: #F8FAFC;
            --table-stripe: #131D31;
            --day-title-color: #FC4C02;
            --day-num-bg: #FC4C02;
            --day-num-text: #FFFFFF;
            --elev-pill-bg: #431407;
            --elev-pill-text: #FFEDD5;
            --theme-tag: "⚡ 運動極限風 (Strava Pro)";
        }

        /* 3. 哈日風格 (J-Pop / 和風朱赤 / 傳統與動漫) */
        [data-theme="japan"] {
            --bg-body: #FDF8F5;
            --bg-container: #FFFFFF;
            --card-bg: #FFFFFF;
            --card-border: #FBCFE8;
            --text-main: #1F2937;
            --text-sub: #4B5563;
            --text-muted: #9CA3AF;
            --brand-primary: #DC2626; /* 神社朱赤 */
            --brand-secondary: #DB2777; /* 櫻花粉紅 */
            --brand-accent: #2563EB; /* 藍染 Indigo */
            --hero-bg: linear-gradient(135deg, #881337 0%, #BE123C 50%, #991B1B 100%);
            --hero-text: #FFFFFF;
            --stat-val: #DC2626;
            --table-header-bg: #FFE4E6;
            --table-header-text: #9F1239;
            --table-stripe: #FFF1F2;
            --day-title-color: #BE123C;
            --day-num-bg: #DC2626;
            --day-num-text: #FFFFFF;
            --elev-pill-bg: #FFE4E6;
            --elev-pill-text: #9F1239;
            --theme-tag: "🎌 哈日和風 (J-Pop / 朱赤)";
        }

        /* 5. 休閒風格 (Outdoor Camping / Nature Chill) */
        [data-theme="outdoor"] {
            --bg-body: #F0FDF4;
            --bg-container: #F7FEE7;
            --card-bg: #FFFFFF;
            --card-border: #BBF7D0;
            --text-main: #14532D;
            --text-sub: #374151;
            --text-muted: #6B7280;
            --brand-primary: #059669; /* Forest Pine */
            --brand-secondary: #D97706; /* Campfire Ochre */
            --brand-accent: #0284C7; /* Mountain Lake */
            --hero-bg: linear-gradient(135deg, #064E3B 0%, #047857 50%, #78350F 100%);
            --hero-text: #FFFFFF;
            --stat-val: #059669;
            --table-header-bg: #DCFCE7;
            --table-header-text: #14532D;
            --table-stripe: #F0FDF4;
            --day-title-color: #065F46;
            --day-num-bg: #059669;
            --day-num-text: #FFFFFF;
            --elev-pill-bg: #DCFCE7;
            --elev-pill-text: #14532D;
            --theme-tag: "⛺ 休閒野營風 (Snow Peak Nature)";
        }

        /* 主題切換控制列 (Theme Switcher Floating / Header Bar) */
        .theme-switcher-bar {
            background: rgba(15, 23, 42, 0.88);
            backdrop-filter: blur(12px);
            -webkit-backdrop-filter: blur(12px);
            border: 1px solid rgba(255, 255, 255, 0.15);
            border-radius: 16px;
            padding: 10px 14px;
            margin-bottom: 20px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            flex-wrap: wrap;
            gap: 10px;
            box-shadow: 0 8px 24px rgba(0,0,0,0.12);
        }

        .theme-switcher-title {
            color: #F8FAFC;
            font-size: 13.5px;
            font-weight: 800;
            display: flex;
            align-items: center;
            gap: 6px;
        }

        .theme-btn-group {
            display: flex;
            gap: 6px;
            flex-wrap: wrap;
        }

        .theme-pill-btn {
            background: #1E293B;
            border: 1px solid #334155;
            color: #CBD5E1;
            padding: 7px 13px;
            border-radius: 20px;
            font-size: 12.5px;
            font-weight: 700;
            cursor: pointer;
            transition: all 0.18s ease;
            display: inline-flex;
            align-items: center;
            gap: 5px;
            user-select: none;
        }

        .theme-pill-btn:hover {
            transform: translateY(-1px);
            color: #FFFFFF;
            border-color: #64748B;
        }

        .theme-pill-btn.active {
            background: #2563EB;
            color: #FFFFFF;
            border-color: #60A5FA;
            box-shadow: 0 0 12px rgba(37, 99, 235, 0.5);
        }

        /* 根據當前主題渲染對應主色 */
        body {
            background-color: var(--bg-body) !important;
            color: var(--text-main) !important;
            transition: background-color 0.25s ease, color 0.25s ease;
        }

        .container {
            background-color: var(--bg-container) !important;
            border-color: var(--card-border) !important;
        }

        .hero {
            background: var(--hero-bg) !important;
        }

        .hero h1, .hero p {
            color: var(--hero-text) !important;
        }

        .stat-card {
            background: var(--card-bg) !important;
            border-color: var(--card-border) !important;
        }

        .stat-card .val {
            color: var(--stat-val) !important;
        }

        .stat-card .label {
            color: var(--text-sub) !important;
        }

        .summary-table-container {
            border-color: var(--card-border) !important;
        }

        .summary-table th {
            background: var(--table-header-bg) !important;
            color: var(--table-header-text) !important;
        }

        .summary-table tr:nth-child(even) td {
            background: var(--table-stripe) !important;
        }

        .day-card {
            background: var(--card-bg) !important;
            border-color: var(--card-border) !important;
        }

        .day-title {
            color: var(--day-title-color) !important;
        }

        .day-num {
            background: var(--day-num-bg) !important;
            color: var(--day-num-text) !important;
        }

        .elev-pill {
            background: var(--elev-pill-bg) !important;
            color: var(--elev-pill-text) !important;
        }

        @media (max-width: 768px) {
            .theme-switcher-bar {
                padding: 10px 10px;
                border-radius: 12px;
                margin-bottom: 14px;
            }
            .theme-btn-group {
                width: 100%;
                display: grid;
                grid-template-columns: repeat(3, 1fr);
                gap: 6px;
            }
            .theme-pill-btn {
                justify-content: center;
                padding: 8px 6px;
                font-size: 11.5px;
                border-radius: 8px;
            }
            .theme-pill-btn:nth-child(4), .theme-pill-btn:nth-child(5) {
                grid-column: span 1.5;
            }
        }
"""

theme_bar_html = """
    <!-- 🎨 5 大主題風格即時切換系統 (Live 5-Themes Switcher) -->
    <div class="theme-switcher-bar">
        <div class="theme-switcher-title">
            <span>🎨 頁面視覺風格切換：</span>
            <span id="current-theme-name" style="color:#38BDF8; font-weight:700;">🚴 單車專業風</span>
        </div>
        <div class="theme-btn-group">
            <button type="button" class="theme-pill-btn" onclick="setTheme('indie')">🌿 文藝青年</button>
            <button type="button" class="theme-pill-btn" onclick="setTheme('sport')">⚡ 運動極限</button>
            <button type="button" class="theme-pill-btn" onclick="setTheme('japan')">🎌 哈日和風</button>
            <button type="button" class="theme-pill-btn active" onclick="setTheme('cycling')">🚴 單車專業</button>
            <button type="button" class="theme-pill-btn" onclick="setTheme('outdoor')">⛺ 休閒野營</button>
        </div>
    </div>
"""

theme_js = """
<script>
// Theme Switcher Logic
const THEMES = {
    'indie': { name: '🌿 文藝青年風 (Muji Minimal)', color: '#8C6239' },
    'sport': { name: '⚡ 運動極限風 (Strava Pro)', color: '#FC4C02' },
    'japan': { name: '🎌 哈日和風 (J-Pop / 朱赤)', color: '#DC2626' },
    'cycling': { name: '🚴 單車專業風 (Rapha Racing)', color: '#FB7185' },
    'outdoor': { name: '⛺ 休閒野營風 (Snow Peak Chill)', color: '#059669' }
};

function setTheme(themeKey) {
    if (!THEMES[themeKey]) themeKey = 'cycling';
    
    // Apply data-theme to root
    document.documentElement.setAttribute('data-theme', themeKey);
    localStorage.setItem('riding_preferred_theme', themeKey);

    // Update active button
    document.querySelectorAll('.theme-pill-btn').forEach(btn => {
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

// Auto load preferred theme from localStorage (default: cycling)
document.addEventListener('DOMContentLoaded', () => {
    const savedTheme = localStorage.getItem('riding_preferred_theme') || 'cycling';
    setTheme(savedTheme);
});
</script>
"""

def inject_themes_to_file(fp):
    with open(fp, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Inject CSS before </style>
    if "🎨 5 大主題風格系統" not in content:
        content = content.replace('</style>', f'{theme_css}\n    </style>')

    # 2. Inject Theme Switcher Bar inside container before content or after hero
    if "theme-switcher-bar" not in content:
        content = content.replace(
            '<div class="content">',
            f'{theme_bar_html}\n    <div class="content">'
        )

    # 3. Inject JS before </body>
    if "setTheme" not in content:
        content = content.replace('</body>', f'{theme_js}\n</body>')

    with open(fp, 'w', encoding='utf-8') as f:
        f.write(content)

inject_themes_to_file('d:/2026東京單車騎旅/tokyo_fuji_cycling_itinerary_19days_v2.html')
inject_themes_to_file('d:/2026東京單車騎旅/index.html')
inject_themes_to_file('C:/Users/ymero/Downloads/tokyo_fuji_cycling_itinerary_19days_v2.html')
inject_themes_to_file('C:/Users/ymero/Downloads/index.html')

print("Injected 5-Theme Switcher System into Portal files!")
