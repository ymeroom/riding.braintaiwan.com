import urllib.request, re, sys, json
from bs4 import BeautifulSoup
sys.stdout.reconfigure(encoding='utf-8')

# JMA station codes:
# Tokyo: prec_no=44, block_no=47662
# Kawaguchiko: prec_no=49, block_no=47638
# Mishima: prec_no=50, block_no=47656
# Yokohama: prec_no=46, block_no=47670

stations = {
    "Tokyo": {"prec_no": 44, "block_no": 47662, "name": "東京"},
    "Kawaguchiko": {"prec_no": 49, "block_no": 47638, "name": "河口湖"},
    "Mishima": {"prec_no": 50, "block_no": 47656, "name": "三島/伊豆"},
    "Yokohama": {"prec_no": 46, "block_no": 47670, "name": "橫濱/湘南"}
}

def parse_jma_daily(prec_no, block_no, year, month):
    url = f'https://www.data.jma.go.jp/stats/etrn/view/daily_s1.php?prec_no={prec_no}&block_no={block_no}&year={year}&month={month}&day=&view='
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    daily_data = {}
    try:
        with urllib.request.urlopen(req) as resp:
            html = resp.read().decode('utf-8')
            # Look for table data
            # Format in daily_s1: tr with td cells: day, air_press, precip(total, max1h, max10m), temp(avg, max, min), humidity, wind, sun, weather
            rows = re.findall(r'<tr style="text-align:right;">(.*?)</tr>', html, re.DOTALL)
            for row in rows:
                cols = re.findall(r'<td[^>]*>(.*?)</td>', row, re.DOTALL)
                if cols and len(cols) >= 14:
                    # Clean tags
                    clean_cols = [re.sub(r'<.*?>', '', c).strip() for c in cols]
                    day_str = clean_cols[0]
                    if day_str.isdigit():
                        day = int(day_str)
                        precip = clean_cols[3] # 降水量合計
                        temp_avg = clean_cols[6]
                        temp_max = clean_cols[7]
                        temp_min = clean_cols[8]
                        wind_max = clean_cols[11] if len(clean_cols) > 11 else "--"
                        sun_h = clean_cols[16] if len(clean_cols) > 16 else "--"
                        weather_day = clean_cols[19] if len(clean_cols) > 19 else ""
                        daily_data[day] = {
                            "precip": precip,
                            "temp_avg": temp_avg,
                            "temp_max": temp_max,
                            "temp_min": temp_min,
                            "wind_max": wind_max,
                            "sun_h": sun_h,
                            "weather": weather_day
                        }
    except Exception as e:
        print(f"Error fetching {prec_no}-{block_no}: {e}")
    return daily_data

print("Fetching JMA weather records for Nov 2025 & Dec 2025...")
records_2025_nov = {}
records_2025_dec = {}

for k, v in stations.items():
    records_2025_nov[k] = parse_jma_daily(v["prec_no"], v["block_no"], 2025, 11)
    records_2025_dec[k] = parse_jma_daily(v["prec_no"], v["block_no"], 2025, 12)

# Itinerary day mappings
itinerary = [
    {"day": 1, "date": "11/13", "m": 11, "d": 13, "st": "Tokyo", "loc": "秋葉原 ➔ 府中", "type": "騎行 50.4km"},
    {"day": 2, "date": "11/14", "m": 11, "d": 14, "st": "Tokyo", "loc": "府中 ➔ 高尾 ➔ 都留", "type": "騎行 68.5km (爬升+580m)"},
    {"day": 3, "date": "11/15", "m": 11, "d": 15, "st": "Kawaguchiko", "loc": "都留 ➔ 山中湖", "type": "騎行 33.3km (爬升+530m)"},
    {"day": 4, "date": "11/16", "m": 11, "d": 16, "st": "Kawaguchiko", "loc": "山中湖 ➔ 河口湖", "type": "短騎 26.5km (賞楓)"},
    {"day": 5, "date": "11/17", "m": 11, "d": 17, "st": "Kawaguchiko", "loc": "西湖/精進湖/本棲湖巡禮", "type": "騎行 49.2km (環湖)"},
    {"day": 6, "date": "11/18", "m": 11, "d": 18, "st": "Kawaguchiko", "loc": "河口湖/新倉山淺間", "type": "【緩衝/休整日】短騎 15.4km"},
    {"day": 7, "date": "11/19", "m": 11, "d": 19, "st": "Kawaguchiko", "loc": "河口湖 ➔ 朝霧 ➔ 富士宮 ➔ 三島", "type": "大長坡騎行 72.5km (下降-1010m)"},
    {"day": 8, "date": "11/20", "m": 11, "d": 20, "st": "Mishima", "loc": "三島 ➔ 狩野川 ➔ 修善寺", "type": "短騎 21.9km (溫泉賞楓)"},
    {"day": 9, "date": "11/21", "m": 11, "d": 21, "st": "Mishima", "loc": "修善寺 ➔ 冷川峠 ➔ 城崎海岸", "type": "騎行 42.2km (越嶺+510m)"},
    {"day": 10, "date": "11/22", "m": 11, "d": 22, "st": "Mishima", "loc": "伊豆高原 ➔ 伊東 ➔ 熱海", "type": "騎行 31.5km (海線波浪)"},
    {"day": 11, "date": "11/23", "m": 11, "d": 23, "st": "Mishima", "loc": "熱海 ➔ 縣道740 ➔ 小田原", "type": "短騎 23.5km (柑橘山線)"},
    {"day": 12, "date": "11/24", "m": 11, "d": 24, "st": "Yokohama", "loc": "小田原 ➔ 湘南海岸 ➔ 江之島", "type": "平路騎行 38.7km"},
    {"day": 13, "date": "11/25", "m": 11, "d": 25, "st": "Yokohama", "loc": "江之島 ➔ 鎌倉 ➔ 橫濱", "type": "景點騎行 33.5km"},
    {"day": 14, "date": "11/26", "m": 11, "d": 26, "st": "Tokyo", "loc": "橫濱 ➔ 羽田 ➔ 豐洲 ➔ 台場", "type": "都會騎行 41.3km"},
    {"day": 15, "date": "11/27", "m": 11, "d": 27, "st": "Tokyo", "loc": "台場 ➔ 葛西 ➔ 荒川右岸 ➔ 赤羽", "type": "河濱騎行 38.0km"},
    {"day": 16, "date": "11/28", "m": 11, "d": 28, "st": "Tokyo", "loc": "赤羽 ➔ 川越小江戶 ➔ 折返", "type": "景點騎行 56.5km"},
    {"day": 17, "date": "11/29", "m": 11, "d": 29, "st": "Tokyo", "loc": "荒川 ➔ 水元公園 ➔ 上野/淺草", "type": "景點騎行 36.4km"},
    {"day": 18, "date": "11/30", "m": 11, "d": 30, "st": "Tokyo", "loc": "上野 ➔ 東大 ➔ 神宮外苑 ➔ 秋葉原", "type": "市區短騎 18.4km (黃金銀杏)"},
    {"day": 19, "date": "12/01", "m": 12, "d": 1, "st": "Tokyo", "loc": "秋葉原還車 ➔ 機場", "type": "【收官日】市區 8.0km"}
]

results = []
for item in itinerary:
    m = item["m"]
    d = item["d"]
    st = item["st"]
    st_name = stations[st]["name"]
    if m == 11:
        data = records_2025_nov.get(st, {}).get(d, {})
    else:
        data = records_2025_dec.get(st, {}).get(d, {})
    
    results.append({
        "day": item["day"],
        "date": item["date"],
        "loc": item["loc"],
        "type": item["type"],
        "station": st_name,
        "precip": data.get("precip", "--"),
        "temp_max": data.get("temp_max", "--"),
        "temp_min": data.get("temp_min", "--"),
        "sun_h": data.get("sun_h", "--"),
        "weather": data.get("weather", "--")
    })

print(json.dumps(results, ensure_ascii=False, indent=2))
