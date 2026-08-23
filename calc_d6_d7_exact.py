import urllib.request, json, sys
sys.stdout.reconfigure(encoding='utf-8')

# Day 6: Motosuko -> Asagiri -> Shiraito Falls -> Fujinomiya
motosuko = [138.564758, 35.473095] # 905m
asagiri = [138.5750, 35.4000] # 830m
shiraito = [138.5880, 35.3120] # 450m
fujinomiya = [138.6150, 35.2220] # 120m

# Day 7: Fujinomiya -> Urui River CR -> Tagonoura Port -> Senbonmatsubara Coastal CR -> Numazu Port -> Mishima
tagonoura = [138.6950, 35.1420] # 2m
senbon = [138.8000, 35.1050] # 3m
numazu_port = [138.8580, 35.0830] # 3m
mishima = [138.9150, 35.1220] # 25m

def get_stats(wps, name):
    coord_str = ';'.join([f'{c[0]},{c[1]}' for c in wps])
    url = f'http://router.project-osrm.org/route/v1/bicycle/{coord_str}?overview=full&geometries=geojson'
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req) as resp:
        data = json.loads(resp.read().decode('utf-8'))
        r = data['routes'][0]
        dist_km = round(r['distance'] / 1000.0, 1)
        coords = r['geometry']['coordinates']

    sampled = coords[::max(1, len(coords)//40)]
    elevs = []
    for pt in sampled:
        gsi_url = f'https://cyberjapandata2.gsi.go.jp/general/dem/scripts/getelevation.php?lon={pt[0]}&lat={pt[1]}&outtype=JSON'
        try:
            req_gsi = urllib.request.Request(gsi_url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req_gsi, timeout=4) as g_resp:
                g_data = json.loads(g_resp.read().decode('utf-8'))
                elevs.append(float(g_data.get('elevation', 0)))
        except:
            pass

    gain = sum([max(0, elevs[i]-elevs[i-1]) for i in range(1, len(elevs)) if abs(elevs[i]-elevs[i-1])>=4])
    loss = sum([max(0, elevs[i-1]-elevs[i]) for i in range(1, len(elevs)) if abs(elevs[i-1]-elevs[i])>=4])
    return dist_km, round(gain), round(loss), round(elevs[0]), round(max(elevs)), round(elevs[-1])

d6_dist, d6_gain, d6_loss, d6_s, d6_m, d6_e = get_stats([motosuko, asagiri, shiraito, fujinomiya], 'Day 6')
d7_dist, d7_gain, d7_loss, d7_s, d7_m, d7_e = get_stats([fujinomiya, tagonoura, senbon, numazu_port, mishima], 'Day 7')

print(f"Day 6 (本棲湖 ➔ 朝霧 ➔ 白糸 ➔ 富士宮): 里程={d6_dist}km, 爬升=+{d6_gain}m, 下降=-{d6_loss}m, 海拔: {d6_s}m ➔ {d6_e}m")
print(f"Day 7 (富士宮 ➔ 潤井川CR ➔ 田子の浦 ➔ 千本松原海堤 ➔ 沼津 ➔ 三島): 里程={d7_dist}km, 爬升=+{d7_gain}m, 下降=-{d7_loss}m, 海拔: {d7_s}m ➔ {d7_e}m")
