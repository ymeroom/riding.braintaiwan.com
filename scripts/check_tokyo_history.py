import urllib.request, re, sys
sys.stdout.reconfigure(encoding='utf-8')

def parse_jma(yr, m):
    url = f"https://www.data.jma.go.jp/stats/etrn/view/daily_s1.php?prec_no=44&block_no=47662&year={yr}&month={m}&day=&view="
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    daily = {}
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            html = resp.read().decode('utf-8')
            rows = re.findall(r'<tr class="mtx" style="text-align:right;">(.*?)</tr>', html, re.DOTALL)
            for r in rows:
                cells = re.findall(r'<td[^>]*>(.*?)</td>', r, re.DOTALL)
                clean = [re.sub(r'<.*?>', '', c).strip() for c in cells]
                if clean and clean[0].isdigit():
                    d = int(clean[0])
                    p = clean[3] if len(clean) > 3 else '0.0'
                    try:
                        p_val = float(p.replace('--', '0.0').replace(']', '').replace(')', ''))
                    except:
                        p_val = 0.0
                    daily[d] = p_val
    except Exception as e:
        print(f"Err {yr}-{m}: {e}")
    return daily

print("=== 日本氣象廳（JMA）過去 5 年（2021～2025）東京市區 11/13 ～ 12/01 實際降雨統計 ===")
for yr in range(2021, 2026):
    nov = parse_jma(yr, 11)
    dec = parse_jma(yr, 12)
    
    rain_days = []
    dry_days = 0
    for d in range(13, 31):
        p = nov.get(d, 0.0)
        if p >= 1.0:
            rain_days.append((f"11/{d}", f"{p}mm"))
        else:
            dry_days += 1
            
    p_dec1 = dec.get(1, 0.0)
    if p_dec1 >= 1.0:
        rain_days.append(("12/01", f"{p_dec1}mm"))
    else:
        dry_days += 1
        
    sunny_rate = round((dry_days / 19) * 100, 1)
    print(f"【{yr} 年】 19天中：晴天/乾燥天數 {dry_days:2d} 天（晴天率 {sunny_rate}%） ｜ 下雨天數 {len(rain_days)} 天 ｜ 雨天詳細: {rain_days}")
