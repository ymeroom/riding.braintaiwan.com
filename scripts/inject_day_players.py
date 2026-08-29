import json, re

# Load tracks
data = json.load(open('songs_manifest.json', encoding='utf-8'))
best_tracks = {}
for day in range(1, 20):
    tracks = [t for t in data.get('tracks', []) if t.get('day') == day]
    if not tracks: continue
    a1 = next((t for t in tracks if t.get('version')=='A' and t.get('take')==1), None)
    if a1: best_tracks[day] = a1
    else:
        any1 = next((t for t in tracks if t.get('take')==1), None)
        best_tracks[day] = any1 if any1 else tracks[0]

css_block = """
<!-- SUNO INLINE PLAYER CSS -->
<style>
.theme-music-player {
    display: flex;
    align-items: center;
    background: var(--primary-light, #f0f0f0);
    border: 1px solid var(--card-border, #ccc);
    border-radius: 8px;
    padding: 10px 14px;
    margin: 12px 0 16px 0;
    gap: 12px;
    box-shadow: 0 2px 4px rgba(0,0,0,0.04);
}
.theme-music-player .player-btn {
    background: var(--primary, #333);
    color: white;
    border: none;
    border-radius: 50%;
    width: 38px;
    height: 38px;
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
    flex-shrink: 0;
    transition: transform 0.1s ease, background 0.2s ease;
}
.theme-music-player .player-btn:active {
    transform: scale(0.95);
}
.theme-music-player .player-btn svg {
    width: 22px;
    height: 22px;
}
.theme-music-player .player-info {
    display: flex;
    flex-direction: column;
    min-width: 0;
    flex: 1;
}
.theme-music-player .player-label {
    font-size: 11px;
    color: var(--primary, #333);
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    margin-bottom: 2px;
}
.theme-music-player .player-title {
    font-size: 14px;
    font-weight: 700;
    color: var(--text-dark, #000);
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
}
.theme-music-player .player-progress-container {
    flex: 1.5;
    height: 6px;
    background: rgba(0,0,0,0.1);
    border-radius: 3px;
    cursor: pointer;
    position: relative;
}
.theme-music-player .player-progress-bar {
    height: 100%;
    background: var(--accent, #666);
    border-radius: 3px;
    width: 0%;
    transition: width 0.1s linear;
}
.theme-music-player .player-time {
    font-size: 12px;
    color: var(--text-muted, #555);
    font-variant-numeric: tabular-nums;
    min-width: 75px;
    text-align: right;
    font-weight: 500;
}
/* Mobile optimization */
@media (max-width: 600px) {
    .theme-music-player {
        flex-wrap: wrap;
        padding: 10px;
    }
    .theme-music-player .player-progress-container {
        flex-basis: 100%;
        order: 4;
        margin-top: 8px;
    }
    .theme-music-player .player-time {
        order: 3;
        flex-basis: auto;
    }
}
</style>
"""

js_block = """
<!-- SUNO INLINE PLAYER JS -->
<script>
let currentlyPlayingAudio = null;
let currentlyPlayingBtn = null;

function toggleThemePlayer(btn) {
    const playerDiv = btn.closest('.theme-music-player');
    const audio = playerDiv.querySelector('audio');
    const playIcon = btn.querySelector('.icon-play');
    const pauseIcon = btn.querySelector('.icon-pause');

    if (audio.paused) {
        if (currentlyPlayingAudio && currentlyPlayingAudio !== audio) {
            currentlyPlayingAudio.pause();
            if (currentlyPlayingBtn) {
                currentlyPlayingBtn.querySelector('.icon-pause').style.display = 'none';
                currentlyPlayingBtn.querySelector('.icon-play').style.display = 'block';
            }
        }
        audio.play();
        playIcon.style.display = 'none';
        pauseIcon.style.display = 'block';
        currentlyPlayingAudio = audio;
        currentlyPlayingBtn = btn;
    } else {
        audio.pause();
        playIcon.style.display = 'block';
        pauseIcon.style.display = 'none';
        currentlyPlayingAudio = null;
        currentlyPlayingBtn = null;
    }
}

function updateThemePlayerProgress(audio) {
    const playerDiv = audio.closest('.theme-music-player');
    const progressBar = playerDiv.querySelector('.player-progress-bar');
    const timeDisplay = playerDiv.querySelector('.player-time');
    if (audio.duration) {
        const percent = (audio.currentTime / audio.duration) * 100;
        progressBar.style.width = percent + '%';
        timeDisplay.innerText = formatTime(audio.currentTime) + ' / ' + formatTime(audio.duration);
    }
}

function seekThemePlayer(event, container) {
    const playerDiv = container.closest('.theme-music-player');
    const audio = playerDiv.querySelector('audio');
    if (audio.duration) {
        const rect = container.getBoundingClientRect();
        const pos = (event.clientX - rect.left) / rect.width;
        audio.currentTime = pos * audio.duration;
    }
}

function formatTime(sec) {
    if (isNaN(sec)) return "0:00";
    const m = Math.floor(sec / 60);
    const s = Math.floor(sec % 60).toString().padStart(2, '0');
    return `${m}:${s}`;
}

function setPlayerDuration(audio) {
    const playerDiv = audio.closest('.theme-music-player');
    const timeDisplay = playerDiv.querySelector('.player-time');
    timeDisplay.innerText = "0:00 / " + formatTime(audio.duration);
}

function resetThemePlayer(audio) {
    const playerDiv = audio.closest('.theme-music-player');
    const btn = playerDiv.querySelector('.player-btn');
    if(btn) {
        btn.querySelector('.icon-pause').style.display = 'none';
        btn.querySelector('.icon-play').style.display = 'block';
    }
    const pb = playerDiv.querySelector('.player-progress-bar');
    if(pb) pb.style.width = '0%';
    audio.currentTime = 0;
}
</script>
"""

def process_html(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            html = f.read()
    except FileNotFoundError:
        return

    if '<!-- SUNO INLINE PLAYER CSS -->' not in html:
        html = html.replace('</head>', css_block + '\n</head>')
    if '<!-- SUNO INLINE PLAYER JS -->' not in html:
        html = html.replace('</body>', js_block + '\n</body>')

    for day, track in best_tracks.items():
        song_id = track['id']
        raw_title = track.get('title', f'Day {day} Theme Song')
        title = raw_title.split('_')[-1].replace('(Take1)', '').replace('(Take2)', '').replace('(', '').strip()
        if not title: title = f'Day {day} Theme Song'
        
        # Suno audio endpoint can be m4a or mp3. m4a usually works well via CDN.
        # But wait, cdn1.suno.ai uses `{song_id}.mp3` typically, or `{song_id}.m4a`?
        # Actually, standard is `{song_id}.mp3` for Suno CDN. Let's try .mp3.
        
        player_html = f'''
        <div class="theme-music-player" data-track="{song_id}">
            <button class="player-btn" onclick="toggleThemePlayer(this)" aria-label="Play Day {day} Theme">
                <svg class="icon-play" viewBox="0 0 24 24"><path fill="currentColor" d="M8 5v14l11-7z"/></svg>
                <svg class="icon-pause" viewBox="0 0 24 24" style="display:none;"><path fill="currentColor" d="M6 19h4V5H6v14zm8-14v14h4V5h-4z"/></svg>
            </button>
            <div class="player-info">
                <div class="player-label">🎵 Day {day} Theme Song</div>
                <div class="player-title">{title}</div>
            </div>
            <div class="player-progress-container" onclick="seekThemePlayer(event, this)">
                <div class="player-progress-bar"></div>
            </div>
            <div class="player-time">0:00 / 0:00</div>
            <audio src="https://cdn1.suno.ai/{song_id}.mp3" preload="none" ontimeupdate="updateThemePlayerProgress(this)" onloadedmetadata="setPlayerDuration(this)" onended="resetThemePlayer(this)"></audio>
        </div>
        '''

        # Clean existing player if present to avoid duplication
        html = re.sub(r'<div class="theme-music-player".*?</audio>\s*</div>', '', html, flags=re.DOTALL)
        
        # Inject right after <h3 class="day-title" ...> inside <div class="day-card" id="day-X">
        h3_pattern = rf'(<div class="day-card" id="day-{day}">\s*<h3[^>]*>.*?</h3>)'
        if re.search(h3_pattern, html, flags=re.DOTALL):
            html = re.sub(h3_pattern, r'\1' + player_html, html, flags=re.DOTALL, count=1)
        else:
            fallback = rf'(<div class="day-card" id="day-{day}">)'
            html = re.sub(fallback, r'\1' + player_html, html, count=1)

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Processed {filename}")

process_html('index.html')
process_html('tokyo_fuji_cycling_itinerary_19days_v2.html')
