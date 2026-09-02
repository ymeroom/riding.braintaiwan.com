import re

# 1. Upgrade Itinerary Portal (tokyo_fuji_cycling_itinerary_19days_v2.html & index.html)
def upgrade_itinerary(fp):
    with open(fp, 'r', encoding='utf-8') as f:
        content = f.read()

    # Meta viewport
    content = content.replace(
        '<meta name="viewport" content="width=device-width, initial-scale=1.0">',
        '<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no, viewport-fit=cover">'
    )

    # Add sticky day column and mobile styling for summary table and floating bottom bar
    mobile_itinerary_css = """
        /* === Samsung Galaxy S23 Ultra & Mobile OLED Visual Optimizations === */
        @media (max-width: 768px) {
            body {
                padding-bottom: 80px; /* Space for floating bottom bar */
                font-size: 14.5px;
                -webkit-font-smoothing: antialiased;
            }
            .container {
                border-radius: 0;
                box-shadow: none;
            }
            .hero {
                padding: 24px 16px;
                border-radius: 0;
            }
            .hero h1 {
                font-size: 20px;
                line-height: 1.35;
            }
            .hero p {
                font-size: 12.5px;
            }
            .hero-meta {
                gap: 6px;
            }
            .meta-tag {
                font-size: 11.5px;
                padding: 5px 10px;
            }
            .content {
                padding: 16px 12px;
            }
            /* Stats Grid: 2 columns on mobile */
            .stats-grid {
                grid-template-columns: repeat(2, 1fr);
                gap: 8px;
                margin-bottom: 18px;
            }
            .stat-card {
                padding: 12px 10px;
                border-radius: 10px;
            }
            .stat-card .val {
                font-size: 19px;
            }
            .stat-card .label {
                font-size: 11px;
            }
            
            /* Table Horizontal Scroll with Sticky First Column */
            .summary-table-container {
                overflow-x: auto;
                -webkit-overflow-scrolling: touch;
                border-radius: 10px;
                border: 1px solid #CBD5E1;
                margin-bottom: 24px;
                position: relative;
            }
            .summary-table {
                min-width: 680px;
                font-size: 12.5px;
            }
            .summary-table th, .summary-table td {
                padding: 10px 8px;
            }
            .summary-table td:first-child, .summary-table th:first-child {
                position: sticky;
                left: 0;
                background: #F8FAFC;
                z-index: 2;
                font-weight: 800;
                box-shadow: 2px 0 5px rgba(0,0,0,0.05);
            }
            .summary-table tr:hover td:first-child {
                background: #EEF2FF;
            }

            /* Day Cards */
            .day-card {
                padding: 16px 14px;
                border-radius: 12px;
                margin-bottom: 18px;
            }
            .day-title {
                font-size: 16px;
                line-height: 1.4;
            }
            .day-stats {
                font-size: 12.5px;
                margin-bottom: 12px;
            }
            .route-step {
                font-size: 13px;
                line-height: 1.6;
            }
            .hotel-box {
                padding: 12px 14px;
                font-size: 13px;
                border-radius: 10px;
            }
            .hotel-link {
                min-height: 44px;
                display: inline-flex;
                align-items: center;
                justify-content: center;
                padding: 8px 14px;
                font-size: 13px;
                margin-top: 6px;
            }
            
            /* Floating Bottom Bar */
            .mobile-bottom-bar {
                display: flex !important;
            }
        }

        .table-swipe-hint {
            display: none;
            background: #EFF6FF;
            border: 1px solid #BFDBFE;
            color: #1D4ED8;
            padding: 7px 12px;
            font-size: 11.5px;
            font-weight: 700;
            border-radius: 6px;
            margin-bottom: 8px;
            text-align: center;
        }
        @media (max-width: 768px) {
            .table-swipe-hint {
                display: block;
            }
        }

        .mobile-bottom-bar {
            display: none;
            position: fixed;
            bottom: 0;
            left: 0;
            right: 0;
            background: rgba(15, 23, 42, 0.96);
            backdrop-filter: blur(12px);
            -webkit-backdrop-filter: blur(12px);
            border-top: 1px solid rgba(255, 255, 255, 0.15);
            padding: 8px 10px calc(8px + env(safe-area-inset-bottom));
            z-index: 9999;
            justify-content: space-around;
            gap: 6px;
        }

        .mobile-bar-btn {
            flex: 1;
            background: #1E293B;
            border: 1px solid #334155;
            color: #F8FAFC;
            padding: 9px 4px;
            border-radius: 8px;
            text-align: center;
            font-size: 11.5px;
            font-weight: 700;
            text-decoration: none;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 4px;
            min-height: 44px;
        }
        .mobile-bar-btn.primary {
            background: #2563EB;
            border-color: #3B82F6;
            color: #FFFFFF;
        }
        .mobile-bar-btn.accent {
            background: #D97724;
            border-color: #F59E0B;
            color: #FFFFFF;
        }
    """

    content = content.replace('</style>', f'{mobile_itinerary_css}\n    </style>')

    # Add table swipe hint before summary table if not already present
    if "table-swipe-hint" not in content:
        content = content.replace(
            '<div class="summary-table-container">',
            '<div class="table-swipe-hint">👈 左右滑動查看完整 19 日數據 ｜ 點擊任一日可直接平滑跳轉 👉</div>\n        <div class="summary-table-container">'
        )

    # Inject floating bottom bar before </body>
    floating_bar_html = """
    <!-- Mobile S23 Ultra Quick Bottom Action Bar -->
    <div class="mobile-bottom-bar">
        <a href="#summary-table-section" class="mobile-bar-btn">📋 總表跳轉</a>
        <a href="tokyo_cycling_19days_map_demo.html" class="mobile-bar-btn primary">🗺️ 全線地圖</a>
        <a href="suno_cycling_soundtrack_19days.html" class="mobile-bar-btn accent">🎵 音樂詞庫</a>
        <a href="javascript:window.scrollTo({top:0, behavior:'smooth'});" class="mobile-bar-btn">⬆️ 置頂</a>
    </div>
    """
    if "mobile-bottom-bar" not in content:
        content = content.replace('</body>', f'{floating_bar_html}\n</body>')

    with open(fp, 'w', encoding='utf-8') as f:
        f.write(content)

upgrade_itinerary('d:/2026東京單車騎旅/tokyo_fuji_cycling_itinerary_19days_v2.html')
upgrade_itinerary('d:/2026東京單車騎旅/index.html')
upgrade_itinerary('C:/Users/ymero/Downloads/tokyo_fuji_cycling_itinerary_19days_v2.html')
upgrade_itinerary('C:/Users/ymero/Downloads/index.html')
print("Upgraded itinerary portal for S23 Ultra mobile view!")

# 2. Upgrade tokyo_cycling_19days_map_demo.html
def upgrade_master_map(fp):
    with open(fp, 'r', encoding='utf-8') as f:
        content = f.read()

    content = content.replace(
        '<meta name="viewport" content="width=device-width, initial-scale=1.0">',
        '<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no, viewport-fit=cover">'
    )

    mobile_map_css = """
        /* === Samsung S23 Ultra Mobile Optimizations for Master Map === */
        @media (max-width: 768px) {
            body {
                padding: 10px 10px 80px 10px;
                font-size: 14px;
            }
            header {
                padding: 14px;
                border-radius: 12px;
                margin-bottom: 10px;
            }
            .header-top {
                flex-direction: column;
                align-items: flex-start;
                gap: 10px;
            }
            .header-title h1 {
                font-size: 18px;
            }
            .header-nav {
                width: 100%;
                display: grid;
                grid-template-columns: 1fr 1fr;
                gap: 8px;
            }
            .nav-btn {
                justify-content: center;
                min-height: 44px;
            }
            .days-nav-wrapper {
                padding: 8px 10px;
                border-radius: 10px;
                margin-bottom: 10px;
            }
            .day-tab {
                padding: 7px 10px;
                min-width: 58px;
                font-size: 12px;
            }
            .stats-bar {
                grid-template-columns: repeat(2, 1fr);
                gap: 8px;
                margin-bottom: 10px;
            }
            .stat-box {
                padding: 10px 8px;
                border-radius: 8px;
            }
            .stat-box .val {
                font-size: 16px;
            }
            .main-layout {
                grid-template-columns: 1fr;
                gap: 10px;
                margin-bottom: 10px;
            }
            #map {
                height: 380px;
                border-radius: 10px;
            }
            .sidebar {
                max-height: 320px;
                padding: 12px;
                border-radius: 10px;
            }
            .chart-card {
                padding: 12px;
                border-radius: 10px;
                margin-bottom: 10px;
            }
            .chart-container {
                height: 180px;
            }
            .mobile-bottom-bar {
                display: flex !important;
            }
        }

        .mobile-bottom-bar {
            display: none;
            position: fixed;
            bottom: 0;
            left: 0;
            right: 0;
            background: rgba(15, 23, 42, 0.96);
            backdrop-filter: blur(12px);
            -webkit-backdrop-filter: blur(12px);
            border-top: 1px solid rgba(255, 255, 255, 0.15);
            padding: 8px 10px calc(8px + env(safe-area-inset-bottom));
            z-index: 9999;
            justify-content: space-around;
            gap: 6px;
        }
        .mobile-bar-btn {
            flex: 1;
            background: #1E293B;
            border: 1px solid #334155;
            color: #F8FAFC;
            padding: 9px 4px;
            border-radius: 8px;
            text-align: center;
            font-size: 12px;
            font-weight: 700;
            text-decoration: none;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 4px;
            min-height: 44px;
        }
        .mobile-bar-btn.primary {
            background: #2563EB;
            border-color: #3B82F6;
            color: #FFFFFF;
        }
        .mobile-bar-btn.accent {
            background: #D97724;
            border-color: #F59E0B;
            color: #FFFFFF;
        }
    """

    content = content.replace('</style>', f'{mobile_map_css}\n    </style>')

    floating_bar_html = """
    <!-- Mobile S23 Ultra Quick Bottom Action Bar -->
    <div class="mobile-bottom-bar">
        <a href="tokyo_fuji_cycling_itinerary_19days_v2.html" class="mobile-bar-btn">📋 總行程表</a>
        <a href="suno_cycling_soundtrack_19days.html" class="mobile-bar-btn accent">🎵 音樂詞庫</a>
        <a id="mobile-gpx-btn" href="day1_track.gpx" download="track.gpx" class="mobile-bar-btn primary">💾 下載GPX</a>
    </div>
    """
    if "mobile-bottom-bar" not in content:
        content = content.replace('</body>', f'{floating_bar_html}\n</body>')

    with open(fp, 'w', encoding='utf-8') as f:
        f.write(content)

upgrade_master_map('d:/2026東京單車騎旅/tokyo_cycling_19days_map_demo.html')
upgrade_master_map('C:/Users/ymero/Downloads/tokyo_cycling_19days_map_demo.html')
print("Upgraded master map for S23 Ultra mobile view!")

# 3. Upgrade suno_cycling_soundtrack_19days.html
def upgrade_soundtrack(fp):
    with open(fp, 'r', encoding='utf-8') as f:
        content = f.read()

    content = content.replace(
        '<meta name="viewport" content="width=device-width, initial-scale=1.0">',
        '<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no, viewport-fit=cover">'
    )

    mobile_suno_css = """
        /* === Samsung S23 Ultra Mobile Optimizations for Soundtrack === */
        @media (max-width: 768px) {
            body {
                padding-bottom: 80px;
                font-size: 14px;
            }
            .header-banner {
                padding: 24px 16px;
                border-radius: 0;
            }
            .header-banner h1 {
                font-size: 20px;
                line-height: 1.35;
            }
            .header-banner p {
                font-size: 12.5px;
            }
            .style-toggle-container {
                padding: 12px 14px;
                border-radius: 12px;
                margin-bottom: 16px;
            }
            .style-btn-group {
                display: grid;
                grid-template-columns: 1fr 1fr;
                gap: 8px;
            }
            .style-btn {
                padding: 12px 10px;
                font-size: 13px;
                min-height: 48px;
                justify-content: center;
            }
            .song-card {
                padding: 16px 14px;
                border-radius: 12px;
                margin-bottom: 16px;
            }
            .song-title {
                font-size: 16px;
            }
            .copy-btn {
                width: 100%;
                min-height: 48px;
                font-size: 13.5px;
                justify-content: center;
                margin-top: 8px;
            }
            .mobile-bottom-bar {
                display: flex !important;
            }
        }

        .mobile-bottom-bar {
            display: none;
            position: fixed;
            bottom: 0;
            left: 0;
            right: 0;
            background: rgba(15, 23, 42, 0.96);
            backdrop-filter: blur(12px);
            -webkit-backdrop-filter: blur(12px);
            border-top: 1px solid rgba(255, 255, 255, 0.15);
            padding: 8px 10px calc(8px + env(safe-area-inset-bottom));
            z-index: 9999;
            justify-content: space-around;
            gap: 6px;
        }
        .mobile-bar-btn {
            flex: 1;
            background: #1E293B;
            border: 1px solid #334155;
            color: #F8FAFC;
            padding: 9px 4px;
            border-radius: 8px;
            text-align: center;
            font-size: 12px;
            font-weight: 700;
            text-decoration: none;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 4px;
            min-height: 44px;
        }
        .mobile-bar-btn.primary {
            background: #2563EB;
            border-color: #3B82F6;
            color: #FFFFFF;
        }
        .mobile-bar-btn.accent {
            background: #D97724;
            border-color: #F59E0B;
            color: #FFFFFF;
        }
    """

    content = content.replace('</style>', f'{mobile_suno_css}\n    </style>')

    floating_bar_html = """
    <!-- Mobile S23 Ultra Quick Bottom Action Bar -->
    <div class="mobile-bottom-bar">
        <a href="tokyo_fuji_cycling_itinerary_19days_v2.html" class="mobile-bar-btn">📋 總行程表</a>
        <a href="tokyo_cycling_19days_map_demo.html" class="mobile-bar-btn primary">🗺️ 全線地圖</a>
        <a href="javascript:window.scrollTo({top:0, behavior:'smooth'});" class="mobile-bar-btn">⬆️ 置頂</a>
    </div>
    """
    if "mobile-bottom-bar" not in content:
        content = content.replace('</body>', f'{floating_bar_html}\n</body>')

    with open(fp, 'w', encoding='utf-8') as f:
        f.write(content)

upgrade_soundtrack('d:/2026東京單車騎旅/suno_cycling_soundtrack_19days.html')
upgrade_soundtrack('C:/Users/ymero/Downloads/suno_cycling_soundtrack_19days.html')
print("Upgraded soundtrack for S23 Ultra mobile view!")
