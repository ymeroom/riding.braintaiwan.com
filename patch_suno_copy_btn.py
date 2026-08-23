import sys, re

# Update update_suno_bilingual_balanced.py to add one-click copy button for lyrics as well
with open("d:/2026東京單車騎旅/update_suno_bilingual_balanced.py", "r", encoding="utf-8") as f:
    code = f.read()

# Replace lyrics section template to include copy button and modern feedback
old_lyrics_card = '''        <div class="lyrics-box" id="lyrics-{t['track']}">{t['lyrics']}</div>'''

new_lyrics_card = '''        <div class="lyrics-section">
            <div class="lyrics-header">
                <span class="lyrics-header-title">📜 Suno AI 雙語結構化歌詞 (Lyrics - 可直接貼上創作)</span>
                <button class="copy-btn copy-lyrics-btn" onclick="copyText('lyrics-{t[\'track\']}', this)">📋 複製全曲歌詞</button>
            </div>
            <div class="lyrics-box" id="lyrics-{t['track']}">{t['lyrics']}</div>
        </div>'''

code = code.replace(old_lyrics_card, new_lyrics_card)

# Update CSS and JS in the template
old_style_block = '''.copy-btn {
            background: #334155;
            color: #F8FAFC;
            border: none;
            padding: 4px 10px;
            border-radius: 4px;
            font-size: 11px;
            font-weight: 700;
            cursor: pointer;
            transition: all 0.15s ease;
        }

        .copy-btn:hover {
            background: #2563EB;
        }'''

new_style_block = '''.copy-btn {
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
        }

        .copy-btn:hover {
            background: #2563EB;
            border-color: #3B82F6;
            transform: translateY(-1px);
        }

        .copy-lyrics-btn {
            background: #0284C7;
            border-color: #38BDF8;
            color: #FFFFFF;
        }

        .copy-lyrics-btn:hover {
            background: #0369A1;
            border-color: #7DD3FC;
        }

        .lyrics-section {
            margin-top: 14px;
        }

        .lyrics-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 8px;
        }

        .lyrics-header-title {
            font-size: 13px;
            font-weight: 700;
            color: #38BDF8;
            display: flex;
            align-items: center;
            gap: 6px;
        }

        /* 複製成功提示 Toast */
        .toast {
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
            animation: fadeInOut 2.5s ease forwards;
        }

        @keyframes fadeInOut {
            0% { opacity: 0; transform: translateY(20px); }
            15% { opacity: 1; transform: translateY(0); }
            85% { opacity: 1; transform: translateY(0); }
            100% { opacity: 0; transform: translateY(20px); }
        }'''

code = code.replace(old_style_block, new_style_block)

# Update copy script
old_copy_script = '''function copyPrompt(id) {
    const text = document.getElementById(id).innerText;
    navigator.clipboard.writeText(text).then(() => {
        alert("已成功複製 Suno AI 風格提示詞！可直接貼上至 Suno 創作欄。");
    });
}'''

new_copy_script = '''function copyText(elementId, btnElement) {
    const text = document.getElementById(elementId).innerText;
    navigator.clipboard.writeText(text).then(() => {
        const originalText = btnElement.innerText;
        btnElement.innerText = "✅ 已複製到剪貼簿！";
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
    let toast = document.getElementById('toast');
    if (!toast) {
        toast = document.createElement('div');
        toast.id = 'toast';
        toast.className = 'toast';
        document.body.appendChild(toast);
    }
    toast.innerText = msg;
    toast.style.display = 'block';
    setTimeout(() => {
        toast.style.display = 'none';
    }, 2500);
}'''

code = code.replace(old_copy_script, new_copy_script)

# Also update the prompt copy call
code = code.replace("onclick=\"copyPrompt('prompt-{t['track']}')\"", "onclick=\"copyText('prompt-{t[\\'track\\']}', this)\"")

with open("d:/2026東京單車騎旅/update_suno_bilingual_balanced.py", "w", encoding="utf-8") as f:
    f.write(code)

print("Updated script to add one-click copy for lyrics and prompt!")
