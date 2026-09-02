import os
import sys
from pathlib import Path

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
        sys.stderr.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass

STEMS_DIR = Path("stems")

EXPECTED_DAYS = [
    (1, "世界線的起跑線"),
    (2, "峠道狂詩曲"),
    (3, "水鏡神域"),
    (4, "千圓紙幣的晨光"),
    (5, "山獸神之森的休止符"),
    (6, "破風降臨千米疾走"),
    (7, "駿河灣的蔚藍防潮堤"),
    (8, "修善寺竹林幽夢"),
    (9, "熔岩懸崖與伊豆之瞳"),
    (10, "網代夕照的避風港"),
    (11, "海灣夜空的最後花火"),
    (12, "早雲柑橘道與湘南風"),
    (13, "高校前的命運路口"),
    (14, "獨角獸與彩虹之橋"),
    (15, "葛飾下町的昭和人情"),
    (16, "江戶川無重力巡航"),
    (17, "萬棵水杉的黃金童話"),
    (18, "神宮外苑的黃金雨"),
    (19, "776公里的世界線閉環")
]

print("=" * 85)
print(f"{'天數':<7} | {'曲目主題':<16} | {'⚡ A版 STEMS 現狀':<20} | {'🍃 B版 STEMS 現狀':<20}")
print("-" * 85)

for day_num, title in EXPECTED_DAYS:
    day_str = f"Day{day_num:02d}"
    a_folders = list(STEMS_DIR.glob(f"{day_str}_A_*"))
    b_folders = list(STEMS_DIR.glob(f"{day_str}_B_*"))
    
    a_status = f"✅ 有 {len(a_folders)} 組 ({len(a_folders)*12} 軌)" if a_folders else "❌ 無 (Suno未生成)"
    b_status = f"✅ 有 {len(b_folders)} 組 ({len(b_folders)*12} 軌)" if b_folders else "❌ 無 (Suno未生成)"
    
    print(f"{day_str:<7} | {title[:14]:<16} | {a_status:<20} | {b_status:<20}")

print("=" * 85)
