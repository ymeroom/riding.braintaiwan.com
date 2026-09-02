#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Rebuilds '00_手機離線網頁播放器.html' with Samsung/Android file sandbox compatibility:
1. Direct Relative Loading (for PC / local web server)
2. One-tap '📂 點此授權載入本資料夾' Directory/File Picker (uses Blob URLs to bypass Android file sandbox)
3. Full Dynamic Synced LRC Scrolling + Tap to Seek
4. On-screen error diagnostic log and audio status bar
5. AudioContext unlock on first touch
"""

import sys
import json
from pathlib import Path

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
        sys.stderr.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass

PHONE_PACK_DIR = Path(r"d:\2026東京單車騎旅\2026東京單車騎旅_手機隨身包")
MANIFEST_FILE = Path(r"d:\2026東京單車騎旅\songs_manifest.json")

with open(MANIFEST_FILE, "r", encoding="utf-8") as f:
    manifest_data = json.load(f)

tracks = manifest_data.get("tracks", [])

# Rebuild mobile tracks manifest
mobile_manifest = []
for idx, t in enumerate(tracks, 1):
    day = t.get("day", 99)
    day_str = f"Day{day:02d}" if day != 99 else "Bonus"
    ver = t.get("version", "A")
    style_desc = t.get("style_desc", "熱血搖滾" if ver == "A" else "慢活民謠")
    take_str = t.get("take_str", "Take1")
    raw_title = t.get("title", "").replace(f" ({take_str})", "")
    clean_title = raw_title.replace("《", "").replace("》", "").strip()
    
    if day != 99:
        filename_base = f"{day:02d}_{day_str}_{ver}_{style_desc}_{take_str}_{clean_title}"
    else:
        filename_base = f"99_Bonus_{ver}_{style_desc}_{take_str}_{clean_title}"
        
    mp3_name = f"{filename_base}.mp3"
    lrc_name = f"{filename_base}.lrc"
    
    lrc_path = PHONE_PACK_DIR / lrc_name
    lrc_text = ""
    if lrc_path.exists():
        try:
            lrc_text = lrc_path.read_text(encoding="utf-8")
        except Exception:
            pass

    display_title = f"{day_str} {ver}版 ({take_str}): {clean_title}" if day != 99 else f"Bonus ({take_str}): {clean_title}"

    mobile_manifest.append({
        "index": idx,
        "day": day,
        "day_str": day_str,
        "version": ver,
        "style_desc": style_desc,
        "take_str": take_str,
        "title": clean_title,
        "display_title": display_title,
        "duration": t.get("duration", 200),
        "mp3_file": mp3_name,
        "lrc_file": lrc_name,
        "lrc_text": lrc_text
    })

html_content = """<!DOCTYPE html>
<html lang="zh-TW">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>2026 東京單車騎旅 手機離線隨身播放器</title>
    <style>
        :root {
            --bg-color: #0b1120;
            --card-bg: #1e293b;
            --primary: #38bdf8;
            --primary-accent: #f59e0b;
            --text-main: #f8fafc;
            --text-muted: #94a3b8;
            --highlight: #22d3ee;
            --border: #334155;
            --success: #10b981;
        }
        * { box-sizing: border-box; margin: 0; padding: 0; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Noto Sans TC", sans-serif; -webkit-tap-highlight-color: transparent; }
        body { background: var(--bg-color); color: var(--text-main); min-height: 100vh; display: flex; flex-direction: column; }
        
        /* Header */
        header { padding: 12px 16px; background: rgba(30, 41, 59, 0.95); backdrop-filter: blur(10px); border-bottom: 1px solid var(--border); display: flex; justify-content: space-between; align-items: center; position: sticky; top: 0; z-index: 50; }
        .header-title { font-size: 15px; font-weight: 700; color: var(--primary); display: flex; align-items: center; gap: 6px; }
        .badge { font-size: 11px; background: #0284c7; padding: 2px 8px; border-radius: 10px; color: #fff; }

        /* Android Permission / Folder Button Notice */
        .android-notice { background: #172554; border: 1px dashed #3b82f6; border-radius: 12px; margin: 10px 16px 0; padding: 12px; display: flex; flex-direction: column; gap: 8px; }
        .notice-text { font-size: 12px; color: #bfdbfe; line-height: 1.4; }
        .btn-grant-folder { background: linear-gradient(135deg, #2563eb, #38bdf8); color: #fff; border: none; padding: 10px 14px; border-radius: 8px; font-size: 13px; font-weight: 700; display: flex; align-items: center; justify-content: center; gap: 6px; cursor: pointer; }
        .btn-grant-folder:active { transform: scale(0.98); }

        /* Filter Tabs */
        .filter-bar { display: flex; gap: 8px; padding: 10px 16px; background: #0f172a; overflow-x: auto; border-bottom: 1px solid var(--border); scrollbar-width: none; }
        .filter-bar::-webkit-scrollbar { display: none; }
        .filter-btn { padding: 6px 14px; background: #1e293b; color: var(--text-muted); border: 1px solid var(--border); border-radius: 20px; font-size: 12px; font-weight: 600; white-space: nowrap; cursor: pointer; }
        .filter-btn.active { background: var(--primary); color: #0f172a; border-color: var(--primary); font-weight: 700; }

        /* Container */
        .container { flex: 1; display: flex; flex-direction: column; padding: 12px 16px 20px; gap: 14px; max-width: 600px; margin: 0 auto; width: 100%; }

        /* Player Card */
        .player-card { background: var(--card-bg); border: 1px solid var(--border); border-radius: 16px; padding: 16px; display: flex; flex-direction: column; gap: 12px; box-shadow: 0 8px 20px rgba(0,0,0,0.4); }
        .track-meta { display: flex; flex-direction: column; gap: 4px; }
        .track-tag { font-size: 11px; font-weight: 700; color: var(--primary-accent); letter-spacing: 0.5px; }
        .track-title { font-size: 18px; font-weight: 800; color: #fff; line-height: 1.3; }
        .track-sub { font-size: 12px; color: var(--text-muted); }

        /* Lyrics Screen */
        .lyrics-box { height: 160px; overflow-y: auto; background: #070b14; border-radius: 12px; padding: 12px; text-align: center; scroll-behavior: smooth; border: 1px solid #1e293b; }
        .lyric-line { font-size: 14px; color: #475569; margin: 8px 0; transition: all 0.2s ease; cursor: pointer; }
        .lyric-line.active { font-size: 16px; color: var(--highlight); font-weight: 800; transform: scale(1.04); text-shadow: 0 0 10px rgba(34, 211, 238, 0.4); }

        /* Progress */
        .progress-box { display: flex; flex-direction: column; gap: 6px; }
        .progress-bar-bg { width: 100%; height: 8px; background: #334155; border-radius: 4px; cursor: pointer; position: relative; }
        .progress-bar-fill { height: 100%; background: linear-gradient(90deg, #38bdf8, #818cf8); border-radius: 4px; width: 0%; transition: width 0.1s linear; }
        .time-row { display: flex; justify-content: space-between; font-size: 11px; color: var(--text-muted); font-variant-numeric: tabular-nums; }

        /* Controls */
        .controls-row { display: flex; justify-content: center; align-items: center; gap: 24px; margin-top: 4px; }
        .btn-ctrl { background: #334155; color: #fff; border: none; width: 46px; height: 46px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 18px; cursor: pointer; }
        .btn-ctrl:active { transform: scale(0.92); }
        .btn-play { width: 60px; height: 60px; background: linear-gradient(135deg, #0284c7, #38bdf8); color: #0f172a; font-size: 22px; box-shadow: 0 4px 15px rgba(56, 189, 248, 0.4); }

        /* Status & Error Toast */
        .status-box { font-size: 11px; padding: 6px 10px; border-radius: 6px; background: #0f172a; border: 1px solid var(--border); color: #94a3b8; text-align: center; }
        .status-box.error { background: #450a0a; border-color: #ef4444; color: #fca5a5; }
        .status-box.success { background: #064e3b; border-color: #10b981; color: #a7f3d0; }

        /* Playlist List */
        .playlist-card { background: var(--card-bg); border: 1px solid var(--border); border-radius: 16px; padding: 12px; display: flex; flex-direction: column; gap: 6px; max-height: 380px; overflow-y: auto; }
        .playlist-header { font-size: 13px; font-weight: 700; color: var(--text-muted); padding-bottom: 6px; border-bottom: 1px solid var(--border); }
        .track-item { display: flex; align-items: center; justify-content: space-between; padding: 10px; border-radius: 8px; background: #0f172a; cursor: pointer; transition: background 0.15s; }
        .track-item:active, .track-item.playing { background: #0369a1; }
        .track-item-left { display: flex; align-items: center; gap: 8px; overflow: hidden; }
        .track-num { font-size: 11px; color: var(--text-muted); font-weight: 700; min-width: 22px; }
        .track-item.playing .track-num { color: #38bdf8; }
        .track-item-name { font-size: 13px; font-weight: 600; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
        .track-item-tag { font-size: 10px; padding: 2px 6px; border-radius: 4px; background: #1e293b; color: #94a3b8; }
    </style>
</head>
<body>

    <header>
        <div class="header-title">
            <span>🚴 2026 東京單車騎旅</span>
        </div>
        <div class="badge" id="total-badge">78 首全曲</div>
    </header>

    <!-- Android Direct File Access Helper Button -->
    <div class="android-notice" id="android-notice">
        <div class="notice-text">
            📱 <b>手機本地安全限制說明</b>：部分三星/安卓瀏覽器開本地 HTML 時會阻擋讀取同層 MP3。若點擊播放沒聲音，請點擊下方按鈕選取此資料夾即可解除限制！
        </div>
        <button class="btn-grant-folder" onclick="triggerFilePicker()">
            <span>📂 點此授權讀取本資料夾 MP3 (一次選取即可)</span>
        </button>
        <input type="file" id="local-file-input" multiple accept="audio/mp3,audio/*,.mp3,.lrc" style="display:none;" onchange="handleLocalFilesSelected(event)">
    </div>

    <!-- Filter Tabs -->
    <div class="filter-bar">
        <button class="filter-btn active" onclick="setFilter('ALL')">全部 (78首)</button>
        <button class="filter-btn" onclick="setFilter('A')">⚡ A版 熱血搖滾</button>
        <button class="filter-btn" onclick="setFilter('B')">🍃 B版 慢活民謠</button>
        <button class="filter-btn" onclick="setFilter('BONUS')">🎁 旅程加贈曲</button>
    </div>

    <div class="container">
        <!-- Player -->
        <div class="player-card">
            <div class="track-meta">
                <span class="track-tag" id="track-badge">Day 01 A版 (Take 1)</span>
                <h2 class="track-title" id="player-title">世界線的起跑線</h2>
                <p class="track-sub" id="player-desc">熱血搖滾 / J-Rock / 175 BPM</p>
            </div>

            <!-- Dynamic Lyrics -->
            <div class="lyrics-box" id="lyrics-box">
                <div class="lyric-line">點擊下方播放開始同步歌詞</div>
            </div>

            <!-- Progress -->
            <div class="progress-box">
                <div class="progress-bar-bg" id="progress-bg" onclick="seekAudio(event)">
                    <div class="progress-bar-fill" id="progress-fill"></div>
                </div>
                <div class="time-row">
                    <span id="time-current">00:00</span>
                    <span id="time-total">00:00</span>
                </div>
            </div>

            <!-- Controls -->
            <div class="controls-row">
                <button class="btn-ctrl" onclick="playPrev()">⏮</button>
                <button class="btn-ctrl btn-play" id="btn-play" onclick="togglePlay()">▶</button>
                <button class="btn-ctrl" onclick="playNext()">⏭</button>
            </div>

            <!-- Diagnostic / Status Message -->
            <div class="status-box" id="status-box">狀態：就緒 (點擊 ▶ 播放)</div>
        </div>

        <!-- Playlist -->
        <div class="playlist-card">
            <div class="playlist-header" id="playlist-title">播放清單 (78 首)</div>
            <div id="playlist-container"></div>
        </div>
    </div>

    <audio id="audio-elem" preload="auto"></audio>

    <script>
        const TRACKS_DATA = """ + json.dumps(mobile_manifest, ensure_ascii=False) + """;

        let localFileBlobMap = {}; // Maps filename to ObjectURL
        let currentFilter = 'ALL';
        let filteredTracks = [...TRACKS_DATA];
        let currentIndex = 0;
        let isPlaying = false;
        let parsedLrc = [];
        let currentLrcLine = -1;

        const audio = document.getElementById('audio-elem');
        const playBtn = document.getElementById('btn-play');
        const lyricsBox = document.getElementById('lyrics-box');
        const progressFill = document.getElementById('progress-fill');
        const timeCurrent = document.getElementById('time-current');
        const timeTotal = document.getElementById('time-total');
        const playerTitle = document.getElementById('player-title');
        const playerDesc = document.getElementById('player-desc');
        const trackBadge = document.getElementById('track-badge');
        const statusBox = document.getElementById('status-box');
        const playlistContainer = document.getElementById('playlist-container');

        function showStatus(msg, type = 'normal') {
            statusBox.textContent = msg;
            statusBox.className = `status-box ${type}`;
        }

        function triggerFilePicker() {
            document.getElementById('local-file-input').click();
        }

        function handleLocalFilesSelected(event) {
            const files = event.target.files;
            if (!files || files.length === 0) return;

            let loadedCount = 0;
            for (let i = 0; i < files.length; i++) {
                const f = files[i];
                const cleanName = f.name;
                localFileBlobMap[cleanName] = URL.createObjectURL(f);
                loadedCount++;
            }

            showStatus(`✅ 成功讀取 ${loadedCount} 個本機檔案！請點擊播放`, 'success');
            document.getElementById('android-notice').style.display = 'none';
            loadTrack(currentIndex);
            playAudio();
        }

        function setFilter(f) {
            currentFilter = f;
            document.querySelectorAll('.filter-btn').forEach(btn => {
                btn.classList.toggle('active', btn.getAttribute('onclick').includes(f));
            });
            if (f === 'ALL') filteredTracks = [...TRACKS_DATA];
            else if (f === 'A') filteredTracks = TRACKS_DATA.filter(t => t.version === 'A' && t.day !== 99);
            else if (f === 'B') filteredTracks = TRACKS_DATA.filter(t => t.version === 'B' && t.day !== 99);
            else if (f === 'BONUS') filteredTracks = TRACKS_DATA.filter(t => t.day === 99);
            
            renderPlaylist();
            loadTrack(0);
        }

        function renderPlaylist() {
            document.getElementById('playlist-title').textContent = `播放清單 (${filteredTracks.length} 首)`;
            playlistContainer.innerHTML = filteredTracks.map((t, idx) => `
                <div class="track-item ${idx === currentIndex ? 'playing' : ''}" onclick="selectTrack(${idx})">
                    <div class="track-item-left">
                        <span class="track-num">${idx + 1}</span>
                        <span class="track-item-name">${t.display_title}</span>
                    </div>
                    <span class="track-item-tag">${t.style_desc}</span>
                </div>
            `).join('');
        }

        function selectTrack(idx) {
            currentIndex = idx;
            loadTrack(currentIndex);
            playAudio();
        }

        function loadTrack(idx) {
            if (!filteredTracks[idx]) return;
            const t = filteredTracks[idx];
            currentIndex = idx;
            
            playerTitle.textContent = t.title;
            trackBadge.textContent = `${t.day_str} ${t.version}版 (${t.take_str})`;
            playerDesc.textContent = `${t.style_desc} (${formatTime(t.duration)})`;

            // Determine audio source: Blob URL (if authorized) or direct relative file
            if (localFileBlobMap[t.mp3_file]) {
                audio.src = localFileBlobMap[t.mp3_file];
            } else {
                audio.src = t.mp3_file; // Direct relative
            }
            audio.load();

            parseLrc(t.lrc_text);
            renderPlaylist();
            updateMediaSession(t);
            showStatus(`已載入：${t.title}`);
        }

        function parseLrc(text) {
            parsedLrc = [];
            currentLrcLine = -1;
            lyricsBox.innerHTML = '';

            if (!text) {
                lyricsBox.innerHTML = '<div class="lyric-line">無動態歌詞</div>';
                return;
            }

            const lines = text.split('\\n');
            const timeReg = /\\[(\\d+):(\\d+(?:\\.\\d+)?)\\](.*)/;

            lines.forEach((line) => {
                const match = line.match(timeReg);
                if (match) {
                    const sec = parseInt(match[1]) * 60 + parseFloat(match[2]);
                    const content = match[3].trim();
                    if (content) {
                        parsedLrc.push({ sec, text: content });
                    }
                }
            });

            if (parsedLrc.length === 0) {
                lyricsBox.innerHTML = '<div class="lyric-line">純音樂 / 演奏版</div>';
                return;
            }

            lyricsBox.innerHTML = parsedLrc.map((item, idx) => `
                <div class="lyric-line" id="lrc-${idx}" onclick="jumpToSec(${item.sec})">${item.text}</div>
            `).join('');
        }

        function jumpToSec(sec) {
            audio.currentTime = sec;
            if (!isPlaying) playAudio();
        }

        function togglePlay() {
            if (isPlaying) pauseAudio();
            else playAudio();
        }

        function playAudio() {
            showStatus('正在播放音訊...');
            const playPromise = audio.play();
            if (playPromise !== undefined) {
                playPromise.then(() => {
                    isPlaying = true;
                    playBtn.textContent = '⏸';
                    showStatus('▶ 正在播放', 'success');
                }).catch(err => {
                    console.warn('[Audio Play Error]:', err);
                    isPlaying = false;
                    playBtn.textContent = '▶';
                    showStatus('⚠️ 播放受限：請點上方按鈕選取隨身包資料夾解除限制', 'error');
                });
            }
        }

        function pauseAudio() {
            audio.pause();
            isPlaying = false;
            playBtn.textContent = '▶';
            showStatus('⏸ 已暫停');
        }

        function playPrev() {
            currentIndex = (currentIndex - 1 + filteredTracks.length) % filteredTracks.length;
            loadTrack(currentIndex);
            playAudio();
        }

        function playNext() {
            currentIndex = (currentIndex + 1) % filteredTracks.length;
            loadTrack(currentIndex);
            playAudio();
        }

        audio.ontimeupdate = () => {
            if (!audio.duration) return;
            const cur = audio.currentTime;
            const dur = audio.duration;
            
            progressFill.style.width = `${(cur / dur) * 100}%`;
            timeCurrent.textContent = formatTime(cur);
            timeTotal.textContent = formatTime(dur);

            // Sync LRC
            let activeIdx = -1;
            for (let i = 0; i < parsedLrc.length; i++) {
                if (cur >= parsedLrc[i].sec) activeIdx = i;
                else break;
            }

            if (activeIdx !== currentLrcLine && activeIdx !== -1) {
                currentLrcLine = activeIdx;
                document.querySelectorAll('.lyric-line').forEach((el, i) => {
                    el.classList.toggle('active', i === currentLrcLine);
                });
                const activeEl = document.getElementById(`lrc-${currentLrcLine}`);
                if (activeEl) {
                    lyricsBox.scrollTo({
                        top: activeEl.offsetTop - lyricsBox.offsetTop - 60,
                        behavior: 'smooth'
                    });
                }
            }
        };

        audio.onerror = (e) => {
            console.error('[Audio Error Details]:', e);
            showStatus('⚠️ 檔案讀取失敗：Android 本地限制，請點上方按鈕選取資料夾', 'error');
        };

        audio.onended = () => playNext();

        function seekAudio(e) {
            const rect = document.getElementById('progress-bg').getBoundingClientRect();
            const pos = (e.clientX - rect.left) / rect.width;
            audio.currentTime = pos * audio.duration;
        }

        function formatTime(s) {
            const m = Math.floor(s / 60);
            const sec = Math.floor(s % 60);
            return `${m < 10 ? '0' + m : m}:${sec < 10 ? '0' + sec : sec}`;
        }

        function updateMediaSession(t) {
            if ('mediaSession' in navigator) {
                navigator.mediaSession.metadata = new MediaMetadata({
                    title: t.title,
                    artist: `2026 東京單車騎旅 (${t.style_desc})`,
                    album: '2026 東京單車騎旅 19日主題曲全集'
                });
                navigator.mediaSession.setActionHandler('play', playAudio);
                navigator.mediaSession.setActionHandler('pause', pauseAudio);
                navigator.mediaSession.setActionHandler('previoustrack', playPrev);
                navigator.mediaSession.setActionHandler('nexttrack', playNext);
            }
        }

        // Init
        renderPlaylist();
        loadTrack(0);
    </script>
</body>
</html>
"""

output_file = PHONE_PACK_DIR / "00_手機離線網頁播放器.html"
with open(output_file, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"[SUCCESS] Rebuilt {output_file} ({len(html_content)} bytes)")
