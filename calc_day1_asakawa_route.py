import urllib.request, json

# Waypoints for Day 1: Akihabara -> Daiichi Keihin -> Rokugo Bridge -> Tamagawa CR -> Fuchu Yotsuya Bridge -> Asakawa CR -> Minamiasakawa Bridge / Ryonan Park -> Mt. Takao Base Camp
waypoints = [
    (139.778496, 35.698425), # Akihabara CycleTrip Base
    (139.7645, 35.6705),     # Ginza
    (139.7390, 35.6260),     # Shinagawa
    (139.7120, 35.5395),     # Rokugo Bridge
    (139.6275, 35.6115),     # Futakotamagawa
    (139.5350, 35.6420),     # Chofu / Tamagawa CR
    (139.4440, 35.6690),     # Fuchu Yotsuya Bridge (Tamagawa -> Asakawa junction)
    (139.3800, 35.6600),     # Asakawa CR (Hino / Hachioji)
    (139.3250, 35.6560),     # Confluence to Minamiasakawa CR (Hachioji City Hall)
    (139.2900, 35.6480),     # Minamiasakawa CR / Ryonan Park / Minamiasakawa Bridge
    (139.2780, 35.6420),     # Takao Station area
    (139.2708, 35.6315)      # Mt. Takao Base Camp
]

coords_str = ";".join([f"{lon},{lat}" for lon, lat in waypoints])
url = f"http://router.project-osrm.org/route/v1/bicycle/{coords_str}?overview=full&geometries=geojson"

req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    with urllib.request.urlopen(req, timeout=15) as resp:
        data = json.loads(resp.read().decode())
        route = data['routes'][0]
        dist_km = round(route['distance'] / 1000, 1)
        coords = route['geometry']['coordinates']
        print(f"OSRM Route Success! Distance: {dist_km} km, Total coordinate points: {len(coords)}")
except Exception as e:
    print(f"OSRM Error: {e}")
