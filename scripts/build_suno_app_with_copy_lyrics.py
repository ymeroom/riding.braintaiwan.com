import json, sys

with open("d:/2026東京單車騎旅/generate_suno_19tracks_masterpiece.py", "r", encoding="utf-8") as f:
    # Let's import tracks_bilingual from update_suno_bilingual_balanced data or generate cleanly
    pass

from update_suno_bilingual_balanced import tracks_bilingual

html_content = f'''<!DOCTYPE html>
<html lang="zh-TW">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>東京・富士五湖・伊豆・東京灣 19日單車騎旅 ｜ 19首 Suno AI 官方台日雙語全量音樂詞庫 (50:50 中日平衡版・一鍵複製)</title>
    <style>
        :root {{
            --bg-dark: #0B0F19;
            --card-bg: #131D2F;
            --card-hover: #1E293B;
            --border: #233554;
            --text-light: #F8FAFC;
            --text-muted: #94A3B8;
            --primary: #2563EB;
            --accent: #F59E0B;
            --purple: #A855F7;
            --success: #10B981;
        }}

        * {{
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }}

        body {{
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
            background-color: var(--bg-dark);
            color: var(--text-light);
            line-height: 1.6;
            padding: 16px;
        }}

        .container {{
            max-width: 1280px;
            margin: 0 auto;
        }}

        header {{
            background: linear-gradient(135deg, #1E1B4B 0%, #31102E 50%, #451A03 100%);
            border: 1px solid var(--border);
            border-radius: 16px;
            padding: 24px 28px;
            margin-bottom: 24px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            flex-wrap: wrap;
            gap: 16px;
            box-shadow: 0 8px 24px rgba(0,0,0,0.3);
        }}

        .header-title h1 {{
            font-size: 24px;
            font-weight: 800;
            color: #FFFFFF;
            margin-bottom: 6px;
        }}

        .header-title p {{
            font-size: 14px;
            color: #CBD5E1;
        }}

        .nav-links {{
            display: flex;
            gap: 10px;
            flex-wrap: wrap;
        }}

        .nav-btn {{
            background: rgba(255, 255, 255, 0.12);
            color: #FFFFFF;
            padding: 9px 16px;
            border-radius: 8px;
            text-decoration: none;
            font-size: 13px;
            font-weight: 700;
            display: inline-flex;
            align-items: center;
            gap: 6px;
            border: 1px solid rgba(255, 255, 255, 0.2);
            transition: all 0.15s ease;
        }}

        .nav-btn:hover {{
            background: rgba(255, 255, 255, 0.25);
            transform: translateY(-1px);
        }}

        .nav-btn.primary {{
            background: var(--primary);
            border-color: #3B82F6;
        }}

        .quick-nav-bar {{
            background: var(--card-bg);
            border: 1px solid var(--border);
            border-radius: 12px;
            padding: 12px 16px;
            margin-bottom: 24px;
            display: flex;
            gap: 8px;
            overflow-x: auto;
            white-space: nowrap;
            scrollbar-width: thin;
        }}

        .track-nav-btn {{
            background: #1E293B;
            border: 1px solid #334155;
            color: #94A3B8;
            padding: 6px 12px;
            border-radius: 6px;
            font-size: 12px;
            font-weight: 700;
            text-decoration: none;
            transition: all 0.15s ease;
        }}

        .track-nav-btn:hover {{
            background: #2563EB;
            color: #FFFFFF;
            border-color: #60A5FA;
        }}

        .track-card {{
            background: var(--card-bg);
            border: 1px solid var(--border);
            border-radius: 16px;
            padding: 22px;
            margin-bottom: 24px;
            transition: all 0.2s ease;
        }}

        .track-card:hover {{
            border-color: #3B82F6;
            box-shadow: 0 8px 24px rgba(37, 99, 235, 0.15);
        }}

        .track-header {{
            display: flex;
            justify-content: space-between;
            align-items: flex-start;
            flex-wrap: wrap;
            gap: 12px;
            border-bottom: 1px solid var(--border);
            padding-bottom: 14px;
            margin-bottom: 16px;
        }}

        .track-title-box h2 {{
            font-size: 19px;
            font-weight: 800;
            color: #F8FAFC;
            display: flex;
            align-items: center;
            gap: 8px;
        }}

        .track-badge {{
            background: #2563EB;
            color: #FFFFFF;
            padding: 3px 8px;
            border-radius: 6px;
            font-size: 12px;
            font-weight: 800;
        }}

        .track-day {{
            font-size: 13px;
            color: var(--accent);
            font-weight: 700;
            margin-top: 4px;
        }}

        .track-theme {{
            background: rgba(168, 85, 247, 0.1);
            border: 1px solid rgba(168, 85, 247, 0.3);
            color: #D8B4FE;
            padding: 8px 12px;
            border-radius: 8px;
            font-size: 12.5px;
            margin-bottom: 14px;
        }}

        .prompt-box {{
            background: #0F172A;
            border: 1px solid #334155;
            border-left: 4px solid var(--accent);
            border-radius: 8px;
            padding: 12px 14px;
            margin-bottom: 16px;
            position: relative;
        }}

        .prompt-header {{
            font-size: 12px;
            font-weight: 700;
            color: var(--accent);
            margin-bottom: 6px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }}

        .prompt-text {{
            font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
            font-size: 12px;
            color: #E2E8F0;
            word-break: break-all;
        }}

        .copy-btn {{
            background: #334155;
            color: #F8FAFC;
            border: 1px solid #475569;
            padding: 5px 12px;
            border-radius: 6px;
            font-size: 11.5px;
            font-weight: 700;
            cursor: pointer;
            transition: all 0.15s ease;
            display: inline-flex;
            align-items: center;
            gap: 4px;
        }}

        .copy-btn:hover {{
            background: #2563EB;
            border-color: #3B82F6;
            transform: translateY(-1px);
        }}

        .copy-lyrics-btn {{
            background: #0284C7;
            border-color: #38BDF8;
            color: #FFFFFF;
        }}

        .copy-lyrics-btn:hover {{
            background: #0369A1;
            border-color: #7DD3FC;
        }}

        .lyrics-section {{
            margin-top: 14px;
        }}

        .lyrics-header {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 8px;
        }}

        .lyrics-header-title {{
            font-size: 13px;
            font-weight: 700;
            color: #38BDF8;
            display: flex;
            align-items: center;
            gap: 6px;
        }}

        .lyrics-box {{
            background: #090D16;
            border: 1px solid #1E293B;
            border-radius: 10px;
            padding: 18px;
            font-family: inherit;
            font-size: 13.5px;
            color: #CBD5E1;
            line-height: 1.7;
            white-space: pre-line;
        }}

        .toast {{
            position: fixed;
            bottom: 24px;
            right: 24px;
            background: #10B981;
            color: #FFFFFF;
            padding: 12px 20px;
            border-radius: 8px;
            font-size: 14px;
            font-weight: 700;
            box-shadow: 0 8px 24px rgba(0,0,0,0.4);
            display: none;
            z-index: 9999;
        }}
    </style>
</head>
<body>

<div class="container">
    <header>
        <div class="header-title">
            <h1>東京・富士五湖・伊豆・東京灣 19日秋季單車騎旅</h1>
            <p>🎵 19首 Suno AI 官方雙語音樂詞庫 ｜ 50:50 中日平衡版 ✕ 一鍵複製提示詞與全曲歌詞 ✕ J-POP ✕ Anime Rock</p>
        </div>
        <div class="nav-links">
            <a href="tokyo_fuji_cycling_itinerary_19days_v2.html" class="nav-btn primary">📋 返回 19日總行程表 ➔</a>
            <a href="tokyo_cycling_19days_map_demo.html" target="_blank" class="nav-btn">🗺️ 19日互動地圖 Demo ↗</a>
        </div>
    </header>

    <!-- 快速曲目跳轉列 -->
    <div class="quick-nav-bar">
'''

for t in tracks_bilingual:
    track_no = t["track"]
    html_content += f'        <a href="#track-{track_no}" class="track-nav-btn">T{track_no:02d}: Day {track_no}</a>\n'

html_content += '''    </div>

    <!-- 19 首曲目詳細卡片 (含風格提示詞與歌詞一鍵複製) -->
'''

for t in tracks_bilingual:
    track_no = t["track"]
    title = t["title"]
    day = t["day"]
    theme = t["theme"]
    style = t["style"]
    lyrics = t["lyrics"]

    html_content += f'''    <div class="track-card" id="track-{track_no}">
        <div class="track-header">
            <div class="track-title-box">
                <h2><span class="track-badge">Track {track_no:02d}</span> 《{title}》</h2>
                <div class="track-day">📅 {day}</div>
            </div>
        </div>

        <div class="track-theme">
            🎬 <strong>影視動漫與歷史意象：</strong> {theme}
        </div>

        <div class="prompt-box">
            <div class="prompt-header">
                <span>🎛️ Suno AI Style of Music (風格提示詞)</span>
                <button class="copy-btn" onclick="copyText('prompt-{track_no}', this)">📋 複製風格提示詞</button>
            </div>
            <div class="prompt-text" id="prompt-{track_no}">{style}</div>
        </div>

        <div class="lyrics-section">
            <div class="lyrics-header">
                <span class="lyrics-header-title">📜 Suno AI 雙語結構化歌詞 (Lyrics - 可直接貼上創作)</span>
                <button class="copy-btn copy-lyrics-btn" onclick="copyText('lyrics-{track_no}', this)">📋 複製全曲歌詞</button>
            </div>
            <div class="lyrics-box" id="lyrics-{track_no}">{lyrics}</div>
        </div>
    </div>
'''

html_content += '''</div>

<div id="toast" class="toast"></div>

<script>
function copyText(elementId, btnElement) {
    const text = document.getElementById(elementId).innerText;
    navigator.clipboard.writeText(text).then(() => {
        const originalText = btnElement.innerText;
        btnElement.innerText = "✅ 已複製！";
        btnElement.style.background = "#10B981";
        btnElement.style.borderColor = "#34D399";
        
        showToast(elementId.startsWith('prompt') ? "🎵 已成功複製風格提示詞 (Style Prompt)！" : "📜 已成功複製全曲雙語歌詞 (Lyrics)！");

        setTimeout(() => {
            btnElement.innerText = originalText;
            btnElement.style.background = "";
            btnElement.style.borderColor = "";
        }, 2000);
    });
}

function showToast(msg) {
    const toast = document.getElementById('toast');
    toast.innerText = msg;
    toast.style.display = 'block';
    setTimeout(() => {
        toast.style.display = 'none';
    }, 2500);
}
</script>

</body>
</html>'''

with open("C:/Users/ymero/Downloads/suno_cycling_soundtrack_19days.html", "w", encoding="utf-8") as f:
    f.write(html_content)

with open("d:/2026東京單車騎旅/suno_cycling_soundtrack_19days.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("Master 19-Track Suno Soundtrack rebuilt successfully with 1-click COPY for BOTH style prompt and lyrics!")
