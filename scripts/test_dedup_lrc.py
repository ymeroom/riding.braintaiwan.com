import re

def clean_and_dedup_lrc(raw_lrc_text):
    """
    Cleans raw LRC text:
    1. Removes prompt/structure instructions (e.g. [Intro], [Verse...], (Final power chord...))
    2. Strips speaker tags: [Male], [Female], [Male & Female], [Duet]
    3. Removes partial syllable fragments where subsequent lines are extensions of the prefix (e.g. 'Suruga Bay, here we' followed by 'Suruga Bay, here we come!')
    4. Removes non-lyric audio noise fragments (e.g. 'ain...', 'ay!', 'i...', 'ji...', 'hearts...')
    5. Formats valid timestamps and removes duplicates.
    """
    lines = raw_lrc_text.splitlines()
    parsed = []
    
    # Noise pattern regex
    instruction_regex = re.compile(
        r'^\s*('
        r'\[(Intro|Verse|Chorus|Pre-Chorus|Bridge|Outro|Guitar Solo|Solo|Instrumental|Drop|Hook|Fade Out|Ending|Interlude|Break|Duet|Male|Female).*?\]|'
        r'\((Final power chord|Dramatic orchestral chord|Temple bell|Cheerful brass|Railroad bell|Synth pulse|Fast shredding|Blazing fast|A highly skilled|Acoustic guitar|Breezy indie|Catchy melodic|Classic 90s|Elegant and emotional|Ending heavy|Energetic dual|Epic neoclassical|Eurobeat|Fading acoustic|Fast rhythmic|Gentle acoustic|Grand final|Jovial and bouncy|Massive emotional|Massive stadium|Passionate and expressive|Playful acoustic|Sawano-style|Instrumental|Guitar solo|Drum fill|Cello solo|Piano solo|Acoustic strumming).*?\)'
        r')\s*$',
        re.I
    )
    inline_tag_regex = re.compile(r'\[(Male & Female|Male|Female|Duet|Both)\]\s*', re.I)
    
    for line in lines:
        line = line.strip()
        if not line or re.match(r'\[(ti|ar|al|by|length|offset):', line, re.I):
            continue
            
        ts_match = re.match(r'^(\[\d+:\d+(?:\.\d+)?\])\s*(.*)', line)
        if not ts_match:
            continue
            
        ts, text = ts_match.group(1), ts_match.group(2).strip()
        
        # Check instruction
        if instruction_regex.match(text):
            continue
        text = inline_tag_regex.sub('', text).strip()
        if re.search(r'^\(.*(?:chord|resonat|silence|fades into|wave sound effect|ambient city|bell chime).*\)$', text, re.I):
            continue
            
        # Ignore tiny 1-3 letter English fragment fragments like 'ain...', 'e!', 'ji...', 'ay!'
        if re.match(r'^[a-z]{1,4}(\.{2,3}|!)?$', text, re.I):
            continue
            
        if not text:
            continue
            
        parsed.append((ts, text))
        
    # Deduplicate prefix fragments: If line A is a prefix of line B and within 2 seconds, keep only line B
    deduped = []
    for i in range(len(parsed)):
        cur_ts, cur_text = parsed[i]
        if i + 1 < len(parsed):
            next_ts, next_text = parsed[i+1]
            # If current text is a prefix of next text (like 'Suruga Bay, here we' is in 'Suruga Bay, here we come!')
            if next_text.startswith(cur_text) and len(cur_text) < len(next_text):
                continue
            # If both lines have identical text, keep the first one
            if cur_text == next_text:
                continue
        deduped.append(f"{cur_ts}{cur_text}")
        
    return "\n".join(deduped)

import sys
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
        sys.stderr.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass

from pathlib import Path
SRC_DIR = Path(r"D:\Suno jazz version")
folders_with_lrc = [f for f in SRC_DIR.iterdir() if f.is_dir() and (f / "lyrics.lrc").exists()]
for folder in folders_with_lrc[:4]:
    raw = (folder / "lyrics.lrc").read_text(encoding="utf-8", errors="replace")
    cleaned = clean_and_dedup_lrc(raw)
    print(f"=== {folder.name} (Before: {len(raw.splitlines())} lines -> After: {len(cleaned.splitlines())} lines) ===")
    print("\n".join(cleaned.splitlines()[:8]))
    print("...\n")
