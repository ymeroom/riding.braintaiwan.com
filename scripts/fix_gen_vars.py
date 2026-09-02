import urllib.request, json, sys, time

# Fix the loop in generate_19days_data.py
with open("d:/2026東京單車騎旅/generate_19days_data.py", "r", encoding="utf-8") as f:
    code = f.read()

# Replace the loop call section
old_section = '''    r_data = fetch_osrm_with_retry(url)
    if not r_data:
        continue'''

new_section = '''    r_data = fetch_osrm_with_retry(url)
    if not r_data:
        continue
    dist_km = round(r_data['distance'] / 1000.0, 1)
    coords = r_data['geometry']['coordinates']'''

code = code.replace(old_section, new_section)

with open("d:/2026東京單車騎旅/generate_19days_data.py", "w", encoding="utf-8") as f:
    f.write(code)

print("Fixed variable assignment in generate_19days_data.py!")
