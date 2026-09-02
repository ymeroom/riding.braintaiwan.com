import urllib.request, json, sys, time

# Read generate_19days_data.py
with open("d:/2026東京單車騎旅/generate_19days_data.py", "r", encoding="utf-8") as f:
    code = f.read()

# Add retry function for OSRM
retry_helper = '''def fetch_osrm_with_retry(url, retries=3):
    for attempt in range(retries):
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req, timeout=12) as resp:
                return json.loads(resp.read().decode('utf-8'))['routes'][0]
        except Exception as e:
            print(f"OSRM retry {attempt+1}/{retries} due to: {e}")
            time.sleep(1.5)
    return None
'''

if "def fetch_osrm_with_retry" not in code:
    code = retry_helper + "\n" + code
    old_call = '''    with urllib.request.urlopen(req, timeout=10) as resp:
        r_data = json.loads(resp.read().decode('utf-8'))['routes'][0]'''
    new_call = '''    r_data = fetch_osrm_with_retry(url)
    if not r_data:
        continue'''
    code = code.replace(old_call, new_call)

with open("d:/2026東京單車騎旅/generate_19days_data.py", "w", encoding="utf-8") as f:
    f.write(code)

print("Added robust retry to generate_19days_data.py!")
