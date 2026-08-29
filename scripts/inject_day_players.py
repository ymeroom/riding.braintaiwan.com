import json, re

# Load tracks
try:
    data = json.load(open('songs_manifest.json', encoding='utf-8'))
except FileNotFoundError:
    print("No songs_manifest.json found")
    exit()

best_tracks = {}
for day in range(1, 20):
    tracks = [t for t in data.get('tracks', []) if t.get('day') == day]
    if not tracks: continue
    a1 = next((t for t in tracks if t.get('version')=='A' and t.get('take')==1), None)
    if a1: best_tracks[day] = a1
    else:
        any1 = next((t for t in tracks if t.get('take')==1), None)
        best_tracks[day] = any1 if any1 else tracks[0]

def process_html(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            html = f.read()
    except FileNotFoundError:
        return

    # 1. Clean ALL existing players globally BEFORE injecting
    html = re.sub(r'<div class="theme-music-player".*?</audio>\s*</div>', '', html, flags=re.DOTALL)

    # 2. Inject players for each day
    for day, track in best_tracks.items():
        song_id = track['id']
        raw_title = track.get('title', f'Day {day} Theme Song')
        title = raw_title.split('_')[-1].replace('(Take1)', '').replace('(Take2)', '').replace('(', '').strip()
        if not title: title = f'Day {day} Theme Song'
        
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
            <audio src="https://audiopipe.suno.ai/?item_id={song_id}" preload="none" ontimeupdate="updateThemePlayerProgress(this)" onloadedmetadata="setPlayerDuration(this)" onended="resetThemePlayer(this)"></audio>
        </div>'''

        # We want to inject inside <div class="day-card" id="day-X">, after the <div class="day-stats" ...> ... </div>
        # Use regex to find the end of the day-stats div.
        pattern = rf'(<div class="day-card" id="day-{day}">.*?<div class="day-stats"[^>]*>.*?</div>)'
        
        if re.search(pattern, html, flags=re.DOTALL):
            html = re.sub(pattern, r'\1' + player_html, html, count=1, flags=re.DOTALL)
        else:
            # Fallback to right after day-card
            fallback = rf'(<div class="day-card" id="day-{day}">)'
            html = re.sub(fallback, r'\1' + player_html, html, count=1)

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Processed {filename}")

process_html('index.html')
process_html('tokyo_fuji_cycling_itinerary_19days_v2.html')
