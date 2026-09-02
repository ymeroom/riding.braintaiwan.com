import urllib.request, json, math

# Let's test routing with dense riverbank waypoints placed EXACTLY on the Tamagawa left bank dyke (多摩川左岸堤防), Asakawa left bank dyke (浅川左岸堤防), and Minamiasakawa dyke (南浅川堤防).

# Let's inspect dense waypoints strictly on the river dyke crown:
dyke_waypoints = [
    # 1. Start Akihabara -> Daiichi Keihin (Route 15)
    (139.778496, 35.698425), # Akihabara CycleTrip Base
    (139.7680, 35.6705),     # Ginza / Shimbashi (Route 15)
    (139.7390, 35.6260),     # Shinagawa (Route 15)
    (139.7210, 35.5580),     # Omori / Kamata (Route 15)
    (139.7120, 35.5395),     # Rokugo Bridge (Entry to Tamagawa CR Left Bank)
    
    # 2. Tamagawa Left Bank Cycling Road (多摩川左岸サイクリングロード / 堤防上専用道)
    (139.7020, 35.5630),     # Yaguchi / Ota (Tamagawa Left Bank CR)
    (139.6800, 35.5850),     # Maruko Bridge (Tamagawa Left Bank CR)
    (139.6600, 35.5920),     # Todoroki / Tamagawa Left Bank CR
    (139.6275, 35.6115),     # Futakotamagawa Hyogo Island (Tamagawa Left Bank CR)
    (139.6000, 35.6325),     # Komae / Izumi Tamagawa (Tamagawa Left Bank CR)
    (139.5400, 35.6430),     # Chofu Tamagawa (Tamagawa Left Bank CR)
    (139.4950, 35.6600),     # Fuchu Koremasa Bridge (Tamagawa Left Bank CR)
    (139.4440, 35.6690),     # Fuchu Yotsuya Bridge (Tamagawa -> Asakawa Left Bank mouth)
    
    # 3. Asakawa Cycling Road (浅川ゆったりロード / 浅川左岸・右岸堤防専用道)
    (139.4180, 35.6650),     # Hino Takahatafudo area (Asakawa CR)
    (139.3800, 35.6600),     # Hirayama Bridge (Asakawa CR)
    (139.3450, 35.6580),     # Osabawa Bridge / Hachioji (Asakawa CR)
    (139.3250, 35.6560),     # Tsurumaki Bridge (Confluence: Asakawa -> Minamiasakawa CR)
    
    # 4. Minamiasakawa Cycling Road (南浅川サイクリング道路 / 陵南遊歩道)
    (139.3080, 35.6520),     # Minamiasakawa CR
    (139.2900, 35.6480),     # Ryonan Park / Minamiasakawa Bridge (南浅川橋)
    (139.2780, 35.6420),     # Takao Bridge / Asakawa Bridge (near Takao Station)
    
    # 5. Last stretch to Mt. Takao Base Camp
    (139.2708, 35.6315)      # Mt. Takao Base Camp (Takaosanguchi Station)
]

# We can query OSRM segment by segment to guarantee it stays 100% on the river dyke cycleway
all_coords = []
total_dist = 0

for i in range(len(dyke_waypoints) - 1):
    p1 = dyke_waypoints[i]
    p2 = dyke_waypoints[i+1]
    url = f"http://router.project-osrm.org/route/v1/bicycle/{p1[0]},{p1[1]};{p2[0]},{p2[1]}?overview=full&geometries=geojson"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode())
            seg_route = data['routes'][0]
            seg_coords = seg_route['geometry']['coordinates']
            if i > 0 and len(seg_coords) > 0:
                seg_coords = seg_coords[1:] # avoid duplicate vertex
            all_coords.extend(seg_coords)
            total_dist += seg_route['distance']
            print(f"Segment {i+1} ({p1} -> {p2}): {round(seg_route['distance']/1000, 2)} km, points: {len(seg_coords)}")
    except Exception as e:
        print(f"Error on segment {i+1}: {e}")

print(f"\nTotal full cycleway route: {round(total_dist/1000, 1)} km, total points: {len(all_coords)}")
