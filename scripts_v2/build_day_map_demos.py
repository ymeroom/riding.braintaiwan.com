"""由 day1_route_map_demo.html 當母版，生成 Day 3–19 的逐日行程地圖 Demo。

Day 1、Day 2 是手工打造（標高取自 GSI 1m DEM、逐句在地解析），不由此腳本覆蓋。
Day 3–19 的內容全部來自既有資料：
  data/trip.json          route_line / subtitle / stage / nav / timeline / elev_profile / expert_tip
  day{N}_track.gpx        實際路線幾何（trkpt）

母版的 CSS、5 主題切換列、Leaflet／Chart.js 邏輯原封不動，只換掉逐日的資料與文案。
"""
import json, io, os, re, html

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'day1_route_map_demo.html')
GEN_DAYS = range(3, 20)

WEEK = {0: '一', 1: '二', 2: '三', 3: '四', 4: '五', 5: '六', 6: '日'}


def esc(s):
    return html.escape(str(s or ''), quote=True)


def gpx_coords(path):
    """<trkpt lat lon> -> [[lon, lat], ...]，座標取 5 位小數（約 1 m）。"""
    txt = io.open(path, encoding='utf-8').read()
    pts = re.findall(r'<trkpt\s+lat="(-?\d+\.?\d*)"\s+lon="(-?\d+\.?\d*)"', txt)
    return [[round(float(lon), 5), round(float(lat), 5)] for lat, lon in pts]


def ride_time(km):
    lo, hi = km / 18.0, km / 15.0
    return f'~{lo:.1f} – {hi:.1f} hr' if hi - lo >= 0.2 else f'~{lo:.1f} hr'


def build(day, tmpl):
    d = day
    n = d['nav']
    date = d['date']                       # "11/15（日）"
    daynum = d['day']
    route = d['route_line']
    title_route = re.sub(r'\s*\(.*?\)\s*$', '', route)
    subtitle = d.get('subtitle') or ''
    stage = (d.get('stage') or {}).get('label') or ''

    coords = gpx_coords(os.path.join(ROOT, f'day{daynum}_track.gpx'))
    geojson = {"type": "Feature", "geometry": {"type": "LineString", "coordinates": coords}}

    tl = d.get('timeline') or []
    ep = d.get('elev_profile') or []
    chart_labels = [f'{p["km"]:.1f}km' for p in ep]
    chart_data = [p['ele'] for p in ep]

    out = tmpl

    # viewport：拿掉縮放鎖（與 index.html 一致）
    out = out.replace(
        '<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no, viewport-fit=cover">',
        '<meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">')

    # <title>
    out = re.sub(r'<title>.*?</title>',
                 f'<title>Day {daynum} 行程地圖 Demo ｜ {esc(title_route)}</title>', out, count=1)

    # <h1>
    out = re.sub(r'(<h1>)Day 1:.*?(</h1>)',
                 lambda m: f'{m.group(1)}Day {daynum}: {esc(title_route)}{m.group(2)}', out, count=1)

    # 副標
    out = re.sub(r'<p>🚴 2026/11/13（五）第一階段出城熱身 ｜ 日本國土地理院 GSI 1m DEM 數值高程模型實測</p>',
                 f'<p>🚴 2026/{esc(date)}　{esc(subtitle)}　｜ {esc(stage)} ｜ NAVITIME 三維座標標高實測</p>', out, count=1)

    # GPX 連結（3 處）與按鈕文字
    out = out.replace('href="day1_track.gpx" download="day1_track.gpx"',
                      f'href="day{daynum}_track.gpx" download="day{daynum}_track.gpx"')
    out = out.replace('💾 下載 Day 1 GPX 軌跡', f'💾 下載 Day {daynum} GPX 軌跡')

    # 統計列
    stats = f'''    <div class="stats-bar">
        <div class="stat-box">
            <div class="val">{n['km']} km</div>
            <div class="lbl">NAVITIME 實測里程</div>
        </div>
        <div class="stat-box">
            <div class="val">+{n['gain']} m / -{n['loss']} m</div>
            <div class="lbl">累積爬升 / 下降</div>
        </div>
        <div class="stat-box">
            <div class="val">{n['min_e']}m ➔ {n['max_e']}m</div>
            <div class="lbl">海拔區間 (最低 ➔ 最高)</div>
        </div>
        <div class="stat-box">
            <div class="val">{len(tl)}</div>
            <div class="lbl">關鍵節點</div>
        </div>
        <div class="stat-box">
            <div class="val">{ride_time(n['km'])}</div>
            <div class="lbl">純騎乘時間 (15–18 km/h)</div>
        </div>
    </div>'''
    out = re.sub(r'    <div class="stats-bar">.*?\n    </div>', lambda m: stats, out, count=1, flags=re.S)

    # 標高圖標題
    out = out.replace(
        '<span>📈 GSI 國土地理院 1m 高精度海拔高程剖面圖</span>\n            <span style="font-size: 12px; color: #10B981;">多摩川＋淺川水岸極緩升（平均坡度 +0.3%，極度舒適）</span>',
        f'<span>📈 NAVITIME 三維座標海拔高程剖面圖</span>\n            <span style="font-size: 12px; color: #10B981;">起點 {n["min_e"]}m ／ 最高 {n["max_e"]}m ／ 總爬升 +{n["gain"]}m</span>')
    out = out.replace('國土地理院海拔', 'NAVITIME 標高')

    # 在地解析卡（trip.json 的 expert_tip 已是完整 HTML）
    tip = d.get('expert_tip') or ''
    out = re.sub(r'<div class="tip-callout">\n.*?\n    </div>',
                 lambda m: f'<div class="tip-callout">\n        {tip}\n    </div>', out, count=1, flags=re.S)

    # footer
    out = out.replace(
        '<p>東京・富士五湖・富士宮・伊豆・東京灣 19日秋季單車騎行計畫 ｜ Day 1 具體地圖 Demo 互動儀表板</p>',
        f'<p>東京・富士五湖・富士宮・伊豆・東京灣 19日秋季單車騎行計畫 ｜ Day {daynum} 行程地圖 Demo</p>')

    # 逐日 JS 資料（整行替換，避開母版單行 megaline 的內容）
    for var, value in (('routeGeojson', geojson), ('timelineData', tl),
                       ('chartLabels', chart_labels), ('chartData', chart_data)):
        literal = 'const %s = %s;' % (var, json.dumps(value, ensure_ascii=False))
        out = re.sub(r'^const %s = .*$' % var, lambda m, lit=literal: lit,
                     out, count=1, flags=re.M)
    return out


def main():
    trip = json.load(io.open(os.path.join(ROOT, 'data/trip.json'), encoding='utf-8'))
    tmpl = io.open(TEMPLATE, encoding='utf-8').read()
    by_day = {d['day']: d for d in trip['days']}
    made = []
    for num in GEN_DAYS:
        d = by_day[num]
        gpx = os.path.join(ROOT, f'day{num}_track.gpx')
        if not os.path.exists(gpx):
            print(f'  ⚠ Day {num}: 缺 day{num}_track.gpx，略過')
            continue
        page = build(d, tmpl)
        dest = os.path.join(ROOT, f'day{num}_route_map_demo.html')
        io.open(dest, 'w', encoding='utf-8').write(page)
        made.append(num)
        print(f'  Day {num:>2} → day{num}_route_map_demo.html  ({len(page):,} 字元)')
    print(f'生成 {len(made)} 頁（Day {made[0]}–{made[-1]}）；Day 1、2 為手工版不覆蓋。')


if __name__ == '__main__':
    main()
