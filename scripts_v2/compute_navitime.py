"""從 NAVITIME shape GeoJSON 計算每日距離與累積爬升。

NAVITIME 的 /maps/route/shape 端點回傳的座標是 [lon, lat, ele] 三元組，
標高即其標高剖面圖的資料源。route_no 1~5 對應網頁上五個路線偏好分頁。
爬升用 3 公尺遲滯門檻累加（Garmin / Strava 慣用做法），濾掉 DEM 雜訊。
"""
import json, math, collections, io, os, sys

NAMES = {'1': '短距離', '2': '坡少', '3': '坡多', '4': '主要道路', '5': '後街'}
THRESHOLD = 3.0


def haversine(a, b):
    R = 6371000.0
    p1, p2 = math.radians(a[1]), math.radians(b[1])
    h = (math.sin((p2 - p1) / 2) ** 2
         + math.cos(p1) * math.cos(p2) * math.sin(math.radians(b[0] - a[0]) / 2) ** 2)
    return 2 * R * math.asin(math.sqrt(h))


def summarise(pts, threshold=THRESHOLD):
    dist = sum(haversine(pts[i], pts[i + 1]) for i in range(len(pts) - 1)) / 1000
    gain = loss = 0.0
    last = pts[0][2]
    for c in pts[1:]:
        diff = c[2] - last
        if abs(diff) >= threshold:
            if diff > 0:
                gain += diff
            else:
                loss += -diff
            last = c[2]
    ele = [c[2] for c in pts]
    return dict(km=round(dist, 1), gain=round(gain), loss=round(loss),
                min_e=round(min(ele)), max_e=round(max(ele)))


def variants(path):
    geo = json.load(io.open(path, encoding='utf-8'))
    by = collections.defaultdict(list)
    for f in geo['features']:
        by[f['properties']['route_no']].append(f)
    out = {}
    for no in sorted(by):
        pts = []
        for f in by[no]:
            for c in f['geometry']['coordinates']:
                if not pts or pts[-1] != c:
                    pts.append(c)
        out[NAMES[no]] = summarise(pts)
    return out


def main(src, dest):
    res = {str(d): variants(os.path.join(src, 'day%d.json' % d)) for d in range(1, 20)}
    io.open(dest, 'w', encoding='utf-8').write(json.dumps(res, ensure_ascii=False, indent=1))
    return res


if __name__ == '__main__':
    src = sys.argv[1]
    res = main(src, 'data/navitime_stats.json')
    pref = '坡少'
    print(f"{'D':>3} {'距離':>8} {'爬升':>7} {'下降':>7} {'標高':>12}")
    tk = tg = 0
    for d in range(1, 20):
        s = res[str(d)][pref]
        tk += s['km']; tg += s['gain']
        print(f"{d:>3} {s['km']:>6.1f}km +{s['gain']:>5}m -{s['loss']:>5}m {s['min_e']:>5}~{s['max_e']:<5}m")
    print(f"{'合計':>3} {tk:>6.1f}km +{tg:>5}m   （偏好：{pref}）")
