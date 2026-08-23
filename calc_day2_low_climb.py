import urllib.request, json, time, math

# Route A: The low-climbing valley route
# Takao Base Camp -> Route 20 Otarumi Pass -> Chigira -> Sagamiko -> Uenohara (Route 20) -> Torisawa / Saruhashi (Route 20) -> Otsuki (Route 20) -> Route 139 (Katsura River Valley) -> Tsuru City (Yukari Ryokan)

waypoints_low_climb = [
    (139.2708, 35.6315), # Takao Base Camp (190m)
    (139.2390, 35.6170), # Otarumi Pass (392m)
    (139.2130, 35.6120), # Chigira
    (139.1880, 35.6135), # Sagamiko
    (139.1550, 35.6150), # Fujino
    (139.1080, 35.6280), # Uenohara (Route 20)
    (139.0150, 35.6130), # Torisawa (Route 20)
    (138.9800, 35.6150), # Saruhashi (Route 20)
    (138.9400, 35.6100), # Otsuki Station (Route 20 -> Route 139 junction)
    (138.9200, 35.5800), # Route 139: Yamura
    (138.9065, 35.5525)  # Tsuru City: Yukari Ryokan (475m)
]

all_coords_a = []
total_dist_a = 0

for i in range(len(waypoints_low_climb) - 1):
    p1 = waypoints_low_climb[i]
    p2 = waypoints_low_climb[i+1]
    url = f"http://router.project-osrm.org/route/v1/bicycle/{p1[0]},{p1[1]};{p2[0]},{p2[1]}?overview=full&geometries=geojson"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req, timeout=10) as resp:
        data = json.loads(resp.read().decode())
        seg_route = data['routes'][0]
        seg_coords = seg_route['geometry']['coordinates']
        if i > 0 and len(seg_coords) > 0:
            seg_coords = seg_coords[1:]
        all_coords_a.extend(seg_coords)
        total_dist_a += seg_route['distance']

dist_km_a = round(total_dist_a / 1000, 1)

def haversine(p1, p2):
    R = 6371000
    lat1, lon1 = math.radians(p1[1]), math.radians(p1[0])
    lat2, lon2 = math.radians(p2[1]), math.radians(p2[0])
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = math.sin(dlat/2)**2 + math.cos(lat1)*math.cos(lat2)*math.sin(dlon/2)**2
    return 2 * R * math.asin(math.sqrt(a))

total_pts = len(all_coords_a)
sample_indices = [int(i * (total_pts - 1) / 74) for i in range(75)]
elevation_profile = []
cumulative_dist = 0.0
elevations = []

for i, idx in enumerate(sample_indices):
    pt = all_coords_a[idx]
    lon, lat = pt[0], pt[1]
    if i == 0:
        c_dist = 0.0
    else:
        prev_idx = sample_indices[i-1]
        seg_d = 0.0
        for k in range(prev_idx, idx):
            seg_d += haversine(all_coords_a[k], all_coords_a[k+1])
        c_dist = round(cumulative_dist + seg_d / 1000, 2)
        cumulative_dist = c_dist
        
    gsi_url = f"https://cyberjapandata2.gsi.go.jp/general/dem/scripts/getelevation.php?lon={lon}&lat={lat}&outtype=JSON"
    try:
        req_gsi = urllib.request.Request(gsi_url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req_gsi, timeout=5) as g_resp:
            g_data = json.loads(g_resp.read().decode())
            ele = g_data.get('elevation', None)
            if ele is None or ele == '-----':
                ele = 190.0
            else:
                ele = round(float(ele), 1)
    except:
        ele = 190.0
        
    elevations.append(ele)
    elevation_profile.append({"km": round(c_dist, 1), "ele": ele})
    time.sleep(0.01)

gain = 0
loss = 0
for k in range(len(elevations)-1):
    diff = elevations[k+1] - elevations[k]
    if diff > 0:
        gain += diff
    else:
        loss += abs(diff)

gain = int(round(gain))
loss = int(round(loss))
start_e = int(round(elevations[0]))
end_e = int(round(elevations[-1]))
peak_e = int(round(max(elevations)))

print(f"Low-Climb Valley Route: Dist={dist_km_a} km, Gain=+{gain} m, Loss=-{loss} m, Start={start_e}m, Peak={peak_e}m, End={end_e}m")
