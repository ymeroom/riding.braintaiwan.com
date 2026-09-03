"""把散落的資料合併成單一正本 data/trip.json。

來源：
  all_19days_route_data.json  路線節點、住宿、文化、避坑（現行版，與總覽表一致）
  data/navitime_stats.json    NAVITIME 實測距離與爬升
  data/meals.json             實地查證的餐廳（另行維護）
  data/logistics.json         撤退、機械、緊急、預算（另行維護）
"""
import json, io, os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PREF = '坡少'  # NAVITIME 路線偏好：休閒長途以少爬坡為準

STAGES = [
    (1, 6, '第一階段：多摩川水岸出城 ➔ 桂川河谷 ➔ 富士五湖賞楓最盛期'),
    (7, 11, '第二階段：千米長下坡 ➔ 駿河灣海堤 ➔ 伊豆溫泉與熱海花火'),
    (12, 15, '第三階段：湘南海岸巡航 ➔ 鎌倉古都 ➔ 橫濱／東京灣岸'),
    (16, 19, '第四階段：下町水岸漫遊 ➔ 都心金黃銀杏 ➔ 圓滿還車'),
]


def load(path, default=None):
    p = os.path.join(ROOT, path)
    if not os.path.exists(p):
        return default
    return json.load(io.open(p, encoding='utf-8'))


def stage_of(day):
    for a, b, label in STAGES:
        if a <= day <= b:
            return {'no': STAGES.index((a, b, label)) + 1, 'label': label,
                    'first': day == a, 'range': f'Day {a} – Day {b}'}
    return None


def parse_weather(s):
    """'☀️ 晴 ｜ 11.8°C ~ 19.6°C ｜ 0.0mm ｜ 9.4h' -> 結構化"""
    out = {'raw': s, 'icon': '', 'text': '', 'lo': None, 'hi': None, 'rain': None, 'sun': None}
    if not s:
        return out
    m = re.match(r'\s*(\S+)\s*(\S+)?\s*｜', s)
    if m:
        out['icon'], out['text'] = m.group(1), (m.group(2) or '')
    t = re.search(r'([\d.]+)°C\s*~\s*([\d.]+)°C', s)
    if t:
        out['lo'], out['hi'] = float(t.group(1)), float(t.group(2))
    r = re.search(r'([\d.]+)mm', s)
    if r:
        out['rain'] = float(r.group(1))
    h = re.search(r'([\d.]+)h', s)
    if h:
        out['sun'] = float(h.group(1))
    return out


def build_bailout(day, stations_db, lodging_db, rinko):
    """撤退方案。策略依使用者定義：
       A. 沿線有車站 → 裝輪行袋（或搭サイクルトレイン）到下一站
       B. 沒站區 → 在 20 公里內找住宿點
    """
    st = stations_db.get(str(day)) or {}
    stations = st.get('stations') or []
    gaps = st.get('gaps') or []
    if not stations and not gaps:
        return None

    # 適用的上車規定：預設 JR 輪行，加上該日有跑サイクルトレイン的路線
    lines = [dict(rinko['jr_rinko'], key='jr_rinko')]
    for key, v in rinko.items():
        if key.startswith('_') or key == 'jr_rinko':
            continue
        if day in (v.get('days') or []):
            lines.insert(0, dict(v, key=key))

    # 沒站區配上實查住宿
    lodging_by_gap = {}
    for g in (lodging_db.get(str(day)) or []):
        lodging_by_gap[(g['from_km'], g['to_km'])] = g.get('samples') or []
    gaps_out = []
    for g in gaps:
        gaps_out.append({**g, 'samples': lodging_by_gap.get((g['from_km'], g['to_km']), [])})

    strategy = 'B' if not stations else ('A+B' if gaps else 'A')
    return {
        'strategy': strategy,
        'lines': lines,
        'stations': stations,
        'station_count': len(stations),
        'gaps': gaps_out,
    }


def main():
    route = load('all_19days_route_data.json')
    nav = load('data/navitime_stats.json', {})
    meals = load('data/meals.json', {})
    logi = load('data/logistics.json', {})
    stations_db = load('data/bailout_stations.json', {})
    lodging_db = load('data/bailout_lodging.json', {})
    rinko = load('data/rinko.json', {})
    support = load('data/support_poi.json', {})
    emergency = load('data/emergency.json', {})
    prefs = load('data/day_prefectures.json', {})

    days = []
    for e in sorted(route, key=lambda x: x['day']):
        d = e['day']
        n = (nav.get(str(d)) or {})
        pref = n.get(PREF) or n.get('短距離') or {}
        subtitle, _, headline = (e.get('title') or '').partition('：')
        days.append({
            'day': d,
            'date': e.get('date'),
            'stage': stage_of(d),
            'subtitle': subtitle,
            'route_line': headline or e.get('title'),
            'nav': {'pref': PREF, **pref, 'variants': n},
            'timeline': [t for t in e.get('timeline', []) if t.get('coord')],
            # 實走里程＝路線節點最末的公里數（本計畫刻意繞走專用道，故常與
            # NAVITIME 最短路徑不同）。標記 mode=train 的節點屬搭車段，不計入。
            'planned_km': next((t['km'] for t in reversed(e.get('timeline', []))
                                if t.get('coord') and t.get('mode') != 'train'), None),
            'hotel': {
                'name': e.get('hotel'), 'addr': e.get('hotel_addr'),
                'url': e.get('hotel_url'), 'booked': str(e.get('booked')) == 'True',
                'bike': e.get('bike_status'), 'tel': (logi.get(str(d), {}) or {}).get('hotel_tel'),
            },
            'weather_hist': parse_weather(e.get('weather')),
            'foliage': e.get('foliage'),
            'expert_tip': e.get('expert_tip'),
            'culture': e.get('culture') or {},
            'meals': meals.get(str(d), {}),
            'logistics': logi.get(str(d), {}),
            'bailout': build_bailout(d, stations_db, lodging_db, rinko),
            'support': support.get(str(d)) or {},
            'prefectures': prefs.get(str(d)) or [],
            'gpx': f'day{d}_track.gpx',
            'map_demo': (f'day{d}_route_map_demo.html'
                         if os.path.exists(os.path.join(ROOT, f'day{d}_route_map_demo.html')) else None),
            'elev_profile': e.get('elev_profile') or [],
        })

    total_km = round(sum(x['nav'].get('km', 0) for x in days), 1)
    total_gain = sum(x['nav'].get('gain', 0) for x in days)
    total_planned = round(sum(x.get('planned_km') or 0 for x in days), 1)
    trip = {
        'meta': {
            'title': '東京・富士五湖・富士宮・伊豆・東京灣 19日秋季單車騎行計畫',
            'start': '2026-11-13', 'end': '2026-12-01', 'days': len(days),
            'total_km': total_km, 'total_gain': total_gain,
            'total_planned_km': total_planned,
            'source': f'NAVITIME 自転車ルート（{PREF}）實測；標高取自 NAVITIME shape API 三維座標',
            'booked': sum(1 for x in days if x['hotel']['booked']),
        },
        'emergency': emergency,
        'stages': [{'no': i + 1, 'from': a, 'to': b, 'label': l} for i, (a, b, l) in enumerate(STAGES)],
        'days': days,
    }
    out = os.path.join(ROOT, 'data/trip.json')
    io.open(out, 'w', encoding='utf-8').write(json.dumps(trip, ensure_ascii=False, indent=1))
    print(f'寫出 {out}')
    print(f"  {len(days)} 天 ｜ NAVITIME {total_km} km ／ 實走 {total_planned} km "
          f"｜ +{total_gain} m ｜ 已訂房 {trip['meta']['booked']} 晚")
    return trip


if __name__ == '__main__':
    main()
