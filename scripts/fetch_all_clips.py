import requests
import json
import sys

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
        sys.stderr.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass

token = """eyJhbGciOiJSUzI1NiIsImtpZCI6InN1bm8tYXBpLXJzMjU2LWtleS0xIiwidHlwIjoiSldUIiwieC1hYmx5LXRva2VuIjoibnYzNlZ3LklDZ0gwaWhTbDlhU1JuWGViMXd2M3h5XzlXdTNENUJWWUdkYmJlS3VhVWV3TEhKVGU2blcyRmVfdV9acEtrQ24yZ3AySEhNcEpqVmthN2N5Y2hzVFFkQ3JmQzE0c04zWHZMM2M5TnFhODF0Wi0xcVFhWUF4ejVXRXhqYlY4eTNUSWllX1lLNWRtRlRoeFlKM3lYSVFpUkNySHFvWm45YXRnVU92djVHMXhRVkVNalNVRkhwUVdXUS1VRk1VWk1fM3NQWkQ1NHNZMjVhbFRNZTdnaGt0cS1wLTRJZGhNTjdfRktOeHdzY1ZGTUlvIn0.eyJzdW5vLmNvbS9jbGFpbXMvdXNlcl9pZCI6IjA1NmIxM2Y0LWY2NWUtNGUwYS1hOGQwLTE2YjY3YzBhMmJkYSIsImh0dHBzOi8vc3Vuby5haS9jbGFpbXMvY2xlcmtfaWQiOiIwNTZiMTNmNC1mNjVlLTRlMGEtYThkMC0xNmI2N2MwYTJiZGEiLCJzdW5vLmNvbS9jbGFpbXMvdG9rZW5fdHlwZSI6ImFjY2VzcyIsInN1bm8vZGlkIjoxMzgyMjczODUsImV4cCI6MTc4NzYzMjc5MywiYXVkIjoic3Vuby1hcGkiLCJzdWIiOiIwNTZiMTNmNC1mNjVlLTRlMGEtYThkMC0xNmI2N2MwYTJiZGEiLCJhenAiOiJodHRwczovL3N1bm8uY29tIiwiZnZhIjpbMCwtMV0sImlhdCI6MTc4NzYyOTE5MywiaXNzIjoiaHR0cHM6Ly9hdXRoLnN1bm8uY29tIiwiaml0IjoiZTgxNDlhMDYtMzkzNy00MjBjLTk3M2YtOGRkNTE3ZGFjYzc5IiwicGxhbiI6IjNlYWViZWYzLWVmNDYtNDQ2YS05MzFjLTNkNTBjZDE1MTRmMTptb250aDoiLCJzdW5vL2pvaW5lZCI6MTc4Mzc2ODc3OCwic2lkIjoic2Vzc2lvbl85ODA4NjI2MjEwZWU0NDI4YmI3ZGNiIiwic3Vuby5jb20vY2xhaW1zL2VtYWlsIjoieW1lcm9vbUBnbWFpbC5jb20iLCJodHRwczovL3N1bm8uYWkvY2xhaW1zL2VtYWlsIjoieW1lcm9vbUBnbWFpbC5jb20iLCJzdW5vL2hhbmRsZSI6ImJyYWludGFpd2FuIiwic3Vuby91c2VyX2lkIjoiMTY4OTI1MTY3Iiwic3Vuby91c2VybmFtZSI6InltZXJvb21AZ21haWwuY29tIn0.MzDvniM3ZczrUc32wSHB12crp81S7pV4eBbQ2xC2JbrbUTPGBu3-Iy5F0n8k-7_x12PrR80iqGjRerrj4NKdzKG8-wbLbavXSu1qmpsFUN_BZ2pLtu6HV-lVMruk2x6g2Dp0jG3Gi-CgKPszgjMS2CfJnaPg-8Bnij6wa3aB2wXS3t1KPvsTXBYbsDhS2VKPZ0CROwrjHYulFQ7KyDim09aXufi6DgLo-7jS4Vmk-g6zVMd62l22nV9yTTIuh42DI0_el0Ct6O4FTYR4F7jTLHF6fPrZNUs3b7zS7GSNe3-gIlAViz6E81Cr52IQZ7z2GYKw-q2FAeJIy-UDq3vZOw""".strip()

headers = {
    "Authorization": f"Bearer {token}",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
    "Accept": "application/json, text/plain, */*",
    "Referer": "https://suno.com/",
    "Origin": "https://suno.com"
}

wid = "9e6e1488-d6d1-47ef-8ee4-b2ebe788f58b"
all_clips = []
page = 1

while True:
    url = f"https://studio-api.prod.suno.com/api/feed/v2?project_id={wid}&page={page}"
    r = requests.get(url, headers=headers)
    if r.status_code != 200:
        print(f"Page {page} failed: {r.status_code}")
        break
    data = r.json()
    clips = data.get("clips", [])
    if not clips:
        print(f"No more clips at page {page}.")
        break
    all_clips.extend(clips)
    print(f"Page {page}: Got {len(clips)} clips (Total so far: {len(all_clips)})")
    
    # Check if there are more
    if len(clips) < 20 or not data.get("has_more", True):
        print("Reached end of clips.")
        break
    page += 1

print(f"\n[SUMMARY] Total clips fetched: {len(all_clips)}")
with open("workspace_clips_raw.json", "w", encoding="utf-8") as f:
    json.dump(all_clips, f, ensure_ascii=False, indent=2)
