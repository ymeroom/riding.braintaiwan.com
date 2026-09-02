import urllib.request, json, math, time

# Precise Japanese Road Cyclist route for Day 2:
# Mt. Takao Base Camp -> Route 20 Otarumi Pass -> Chigira (千木良) -> Sagamiko (相模湖) -> Katsuse Bridge (勝瀬橋) / Hizure (日連) -> r76 -> Okumagino (奥牧野 / 縣道35號起點) -> Akiyama Kaido (山梨縣道35號) -> Akiyama Tunnel -> Tsuru City (由加利旅館)

waypoints_d2 = [
    (139.2708, 35.6315), # 1. Start: Mt. Takao Base Camp (高尾山口 190m)
    (139.2390, 35.6170), # 2. Route 20: 大垂水峠 (Otarumi Toge 392m)
    (139.2130, 35.6120), # 3. Route 20: 千木良 (Chigira)
    (139.1880, 35.6135), # 4. Route 20: 相模湖 (Sagamiko / 勝瀬橋入口)
    (139.1750, 35.6020), # 5. 勝瀬橋 (Katsuse Bridge) -> 縣道520號
    (139.1550, 35.5960), # 6. 縣道76號: 日連 / 名倉
    (139.1120, 35.5860), # 7. 奧牧野 / 牧野 (山梨縣道35號・秋山街道起點)
    (139.0600, 35.5830), # 8. 縣道35號: 秋山櫻井 / 秋山溫泉周邊
    (138.9800, 35.5780), # 9. 縣道35號: 無生野 (Muno)
    (138.9400, 35.5720), # 10. 縣道35號: 秋山隧道 (分水嶺標高 612m)
    (138.9065, 35.5525)  # 11. End: ビジネス旅館 由加利 (都留市 475m)
]

all_coords_d2 = []
total_dist_d2 = 0

for i in range(len(waypoints_d2) - 1):
    p1 = waypoints_d2[i]
    p2 = waypoints_d2[i+1]
    url = f"http://router.project-osrm.org/route/v1/bicycle/{p1[0]},{p1[1]};{p2[0]},{p2[1]}?overview=full&geometries=geojson"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req, timeout=10) as resp:
        data = json.loads(resp.read().decode())
        seg_route = data['routes'][0]
        seg_coords = seg_route['geometry']['coordinates']
        if i > 0 and len(seg_coords) > 0:
            seg_coords = seg_coords[1:]
        all_coords_d2.extend(seg_coords)
        total_dist_d2 += seg_route['distance']
        print(f"D2 Seg {i+1}: {round(seg_route['distance']/1000, 2)} km, pts: {len(seg_coords)}")

dist_km_d2 = round(total_dist_d2 / 1000, 1)
print(f"Total Day 2 Distance: {dist_km_d2} km, points: {len(all_coords_d2)}")
