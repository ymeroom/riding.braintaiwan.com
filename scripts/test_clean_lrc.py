import sys
import re

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
        sys.stderr.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass

def clean_lrc_content(raw_lrc_text):
    """
    Cleans raw LRC text:
    1. Removes prompt instructions:
       - Structure markers: [Intro], [Verse 1 - ...], [Guitar Solo], [Chorus...], [Bridge...], [Outro...], [Male], [Female], [Duet]
       - Sound effect / instrument direction brackets: (Final power chord...), (Synth pulse...), (Temple bell...), (Acoustic guitar arpeggio...)
    2. Keeps genuine sung lyrics:
       - Chinese lines, Japanese lines, mixed lines
       - Genuine English sung phrases (El Psy Kongroo, Fly away together, etc.)
       - Japanese chorus/echo in parentheses: e.g. (ペダルを踏み込め、新たな世界線へ！)
    3. Normalizes timestamps and removes empty lines.
    """
    cleaned_lines = []
    
    # Instruction patterns to filter out completely
    instruction_regex = re.compile(
        r'^\s*(\[\d+:\d+(?:\.\d+)?\])?\s*('
        r'\[(Intro|Verse|Chorus|Pre-Chorus|Bridge|Outro|Guitar Solo|Solo|Instrumental|Drop|Hook|Fade Out|Ending|Interlude|Break|Duet|Male|Female).*?\]|'
        r'\((Final power chord|Dramatic orchestral chord|Temple bell|Cheerful brass|Railroad bell|Synth pulse|Fast shredding|Blazing fast|A highly skilled|Acoustic guitar|Breezy indie|Catchy melodic|Classic 90s|Elegant and emotional|Ending heavy|Energetic dual|Epic neoclassical|Eurobeat|Fading acoustic|Fast rhythmic|Gentle acoustic|Grand final|Jovial and bouncy|Massive emotional|Massive stadium|Passionate and expressive|Playful acoustic|Sawano-style|Instrumental|Guitar solo|Drum fill|Cello solo|Piano solo).*?\)'
        r')\s*$',
        re.I
    )

    # Inline tag stripper (e.g., "[Male] 秋葉原晨光..." -> "秋葉原晨光...")
    inline_tag_regex = re.compile(
        r'\[(Male & Female|Male|Female|Duet|Both)\]\s*',
        re.I
    )

    lines = raw_lrc_text.splitlines()
    for line in lines:
        line = line.strip()
        if not line:
            continue
            
        # Ignore metadata tags like [ti:], [ar:], etc. if any
        if re.match(r'\[(ti|ar|al|by|length|offset):', line, re.I):
            continue

        # Check if entire line is an instruction/prompt bracket
        if instruction_regex.match(line):
            continue

        # Check timestamp
        ts_match = re.match(r'^(\[\d+:\d+(?:\.\d+)?\])\s*(.*)', line)
        if not ts_match:
            continue

        ts, text = ts_match.group(1), ts_match.group(2).strip()

        # Strip inline speaker tags like [Male], [Female], [Male & Female]
        text = inline_tag_regex.sub('', text).strip()

        # Check if text is just an English direction like "(Final power chord resonating into silence)"
        if re.search(r'^\(.*(?:chord|resonat|silence|fades into|wave sound effect|ambient city|bell chime).*\)$', text, re.I):
            continue

        # Check if text is empty
        if not text:
            continue

        cleaned_lines.append(f"{ts}{text}")

    return "\n".join(cleaned_lines)

# Test on Day 1 A
sample = """[00:00.71]El Psy Kongroo... 踏上未知的世界線！
[00:05.98]踏板旋轉，心跳超頻，出發！
[00:31.67](ペダルを踏み込め、新たな世界線へ！)
[00:31.67]秋葉原晨光染亮了電器街的窗
[00:36.22]鎖定碼表歸零，跨上破風的車把
[00:41.40]穿過銀座的喧囂，第一京濱筆直伸展
[00:45.71]六鄉橋下，多摩川的秋芒如海浪般翻湧
[00:51.70]秋葉原の朝焼け背に受けて
[00:54.97]ペダルを踏み込めば 始まるプロローグ
[01:01.75]多摩川の風が 頬を撫でてゆく
[01:07.50]シン・ゴジラの足跡、丸子橋を越えて
[01:12.12]八王子的空へ、道は続いてる
[01:18.67]Fly away together!
[01:32.63]Fly away together!
[01:32.73]天狗の羽扇が 秋の合図を送る
[01:36.31]明日は大垂水峠、未知の坂道へ
[01:39.89]Fly away together!
[01:40.36]車輪旋轉出無畏的光芒，踏破所有未知的阻擋！
[01:45.71]Fly away together!
[01:52.10]Fly into the twilight sky!
[02:14.52]天狗の羽扇が 秋の合図を送る
[02:19.30]明日は大垂水峠、未知の坂道へ
[02:25.13]車輪旋轉出無畏的光芒，踏破所有未知的阻擋！
[02:25.13]秋葉原到高尾山，八十九公里的序章
[02:27.92]エル・プサイ・コングルゥ、明日も走るんだ！
[02:30.71]走吧！奔向命運的世界線！(夢の彼方へ 駆け抜けろ！)
[02:36.70]雙輪畫出的軌跡，是無可取代的自由 (ペダルを回せ、自由の風になれ)
[02:45.71]這不是巧合，是命運石之門的指引 (運命の扉を 開く旅立ち)
[03:03.66]エル・プサイ・コングルゥ、明日も走るんだ！
[03:12.28]Fly away together!
[03:13.48](Final power chord resonating into silence)"""

print("=== Cleaned LRC Sample Output ===")
print(clean_lrc_content(sample))
