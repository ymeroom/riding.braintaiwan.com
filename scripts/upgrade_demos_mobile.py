import re, os

# 1. Optimize day1_route_map_demo.html & day2_route_map_demo.html for S23 Ultra
def upgrade_single_day_demo(fp):
    with open(fp, 'r', encoding='utf-8') as f:
        content = f.read()

    # Meta viewport update
    content = content.replace(
        '<meta name="viewport" content="width=device-width, initial-scale=1.0">',
        '<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no, viewport-fit=cover">'
    )

    # Mobile CSS injection
    mobile_css = """
        /* === Samsung S23 Ultra & Mobile OLED Visual Optimizations === */
        @media (max-width: 768px) {
            body {
                padding: 10px 10px 80px 10px; /* Safe padding for bottom action bar */
                font-size: 14px;
            }
            header {
                padding: 16px 14px;
                border-radius: 12px;
                margin-bottom: 12px;
            }
            .header-title h1 {
                font-size: 17px;
                line-height: 1.35;
            }
            .header-title p {
                font-size: 12px;
            }
            .btn-group {
                width: 100%;
                display: grid;
                grid-template-columns: 1fr 1fr;
                gap: 8px;
            }
            .action-btn {
                justify-content: center;
                padding: 11px 12px;
                font-size: 12px;
                border-radius: 8px;
                min-height: 44px;
            }
            .action-btn.gpx {
                grid-column: 1 / -1;
            }
            .stats-bar {
                grid-template-columns: repeat(2, 1fr);
                gap: 8px;
                margin-bottom: 12px;
            }
            .stat-box {
                padding: 12px 10px;
                border-radius: 10px;
            }
            .stat-box .val {
                font-size: 17px;
            }
            .stat-box .lbl {
                font-size: 11px;
            }
            .main-layout {
                grid-template-columns: 1fr;
                gap: 12px;
                margin-bottom: 12px;
            }
            #map {
                height: 380px;
                border-radius: 10px;
            }
            .sidebar {
                max-height: 320px;
                padding: 14px;
                border-radius: 10px;
            }
            .waypoint-card {
                padding: 10px 12px;
                min-height: 48px;
            }
            .chart-card {
                padding: 14px;
                border-radius: 10px;
                margin-bottom: 12px;
            }
            .chart-container {
                height: 190px;
            }
            .tip-callout {
                padding: 14px;
                font-size: 12.5px;
                border-radius: 10px;
            }
            /* Floating Bottom Bar for S23 Ultra one-hand riding use */
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
            background: rgba(15, 23, 42, 0.95);
            backdrop-filter: blur(12px);
            -webkit-backdrop-filter: blur(12px);
            border-top: 1px solid rgba(255, 255, 255, 0.15);
            padding: 8px 12px calc(8px + env(safe-area-inset-bottom));
            z-index: 9999;
            justify-content: space-around;
            gap: 8px;
        }

        .mobile-bar-btn {
            flex: 1;
            background: #1E293B;
            border: 1px solid #334155;
            color: #F8FAFC;
            padding: 10px 8px;
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

    content = content.replace('</style>', f'{mobile_css}\n    </style>')

    # Inject floating bottom bar before </body>
    floating_bar_html = """
    <!-- Mobile S23 Ultra Quick Bottom Action Bar -->
    <div class="mobile-bottom-bar">
        <a href="tokyo_fuji_cycling_itinerary_19days_v2.html" class="mobile-bar-btn">📋 總行程表</a>
        <a href="tokyo_cycling_19days_map_demo.html" class="mobile-bar-btn primary">🗺️ 19日總地圖</a>
        <a href="suno_cycling_soundtrack_19days.html" class="mobile-bar-btn">🎵 音樂詞庫</a>
    </div>
    """
    if "mobile-bottom-bar" not in content:
        content = content.replace('</body>', f'{floating_bar_html}\n</body>')

    with open(fp, 'w', encoding='utf-8') as f:
        f.write(content)

upgrade_single_day_demo('d:/2026東京單車騎旅/day1_route_map_demo.html')
upgrade_single_day_demo('d:/2026東京單車騎旅/day2_route_map_demo.html')
upgrade_single_day_demo('C:/Users/ymero/Downloads/day1_route_map_demo.html')
upgrade_single_day_demo('C:/Users/ymero/Downloads/day2_route_map_demo.html')
print("Upgraded day1 and day2 demos for S23 Ultra mobile view!")
