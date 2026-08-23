import urllib.request, json, sys
sys.stdout.reconfigure(encoding='utf-8')

# Waypoints
takao_basecamp = [139.2705, 35.6323]
dest_yukari = [138.90582, 35.55057]

waypoints = [
    takao_basecamp,
    [139.2780, 35.6150],
    [139.2550, 35.5880],
    [139.2080, 35.5810],
    [139.1450, 35.5800],
    [139.0400, 35.5680],
    dest_yukari
]

coord_str = ';'.join([f'{c[0]},{c[1]}' for c in waypoints])
url_osrm = f'http://router.project-osrm.org/route/v1/bicycle/{coord_str}?overview=full&geometries=geojson'
req = urllib.request.Request(url_osrm, headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req) as resp:
    data = json.loads(resp.read().decode('utf-8'))
    coords = data['routes'][0]['geometry']['coordinates']

# Sample points
sampled_pts = coords[::max(1, len(coords)//100)]
elevs = []
for pt in sampled_pts:
    gsi_url = f'https://cyberjapandata2.gsi.go.jp/general/dem/scripts/getelevation.php?lon={pt[0]}&lat={pt[1]}&outtype=JSON'
    try:
        req_gsi = urllib.request.Request(gsi_url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req_gsi, timeout=4) as g_resp:
            g_data = json.loads(g_resp.read().decode('utf-8'))
            elevs.append(float(g_data.get('elevation', 0)))
    except:
        pass

def calc_gain(elev_list, threshold=0):
    gain = 0
    loss = 0
    prev = elev_list[0]
    for e in elev_list[1:]:
        diff = e - prev
        if abs(diff) >= threshold:
            if diff > 0:
                gain += diff
            else:
                loss += abs(diff)
            prev = e
    return gain, loss

gain_raw, loss_raw = calc_gain(elevs, threshold=0)
gain_3m, loss_3m = calc_gain(elevs, threshold=3)
gain_5m, loss_5m = calc_gain(elevs, threshold=5)
gain_10m, loss_10m = calc_gain(elevs, threshold=10)

print(f"採樣點數量: {len(elevs)}")
print(f"起點 (高尾山口 Base Camp): {elevs[0]:.1f} m")
print(f"最低點: {min(elevs):.1f} m")
print(f"最高點 (秋山街道峠口): {max(elevs):.1f} m")
print(f"終點 (都留市 由加利旅館): {elevs[-1]:.1f} m")
print("--------------------------------------------------")
print(f"1. 原始未過濾數值 (Raw DEM，包含橋樑/山谷噪訊微震盪): +{gain_raw:.0f} m")
print(f"2. Strava / Komoot 常用濾波 (3m 閥值): +{gain_3m:.0f} m")
print(f"3. Garmin 碼表標準氣壓濾波 (5m 閥值): +{gain_5m:.0f} m")
print(f"4. 主要地形爬升濾波 (10m 閥值): +{gain_10m:.0f} m")
