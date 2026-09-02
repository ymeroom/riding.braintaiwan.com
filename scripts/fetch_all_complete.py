import requests
import json
import sys
import time

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

# Load existing clips from disk if present to preserve what we have
existing_clips_dict = {}
try:
    with open("workspace_clips_raw.json", "r", encoding="utf-8") as f:
        for c in json.load(f):
            cid = c.get("id")
            if cid:
                existing_clips_dict[cid] = c
    print(f"[INFO] Loaded {len(existing_clips_dict)} existing clips from workspace_clips_raw.json")
except Exception:
    pass

# Helper to fetch pages with retry & delay
def fetch_paged_endpoint(base_url, name):
    page = 1
    total_added = 0
    consecutive_empty = 0

    while True:
        url = f"{base_url}&page={page}" if "?" in base_url else f"{base_url}?page={page}"
        print(f"[{name}] Fetching page {page} ...", end=" ", flush=True)

        for attempt in range(5):
            try:
                r = requests.get(url, headers=headers, timeout=15)
                if r.status_code == 200:
                    data = r.json()
                    clips = data.get("clips", []) if isinstance(data, dict) else (data if isinstance(data, list) else [])
                    print(f"-> Got {len(clips)} clips", flush=True)
                    
                    if not clips:
                        consecutive_empty += 1
                        if consecutive_empty >= 2:
                            return
                        break
                    
                    consecutive_empty = 0
                    for c in clips:
                        cid = c.get("id")
                        if cid and cid not in existing_clips_dict:
                            existing_clips_dict[cid] = c
                            total_added += 1
                    
                    # Delay to avoid 429
                    time.sleep(0.6)
                    break
                elif r.status_code == 429:
                    wait_time = (attempt + 1) * 3
                    print(f"[429 Rate Limit - waiting {wait_time}s] ...", end=" ", flush=True)
                    time.sleep(wait_time)
                elif r.status_code == 404:
                    print("-> 404 End of pages", flush=True)
                    return
                else:
                    print(f"-> Status {r.status_code}", flush=True)
                    time.sleep(2)
            except Exception as e:
                print(f"-> Err: {e}", flush=True)
                time.sleep(2)

        page += 1
        if page > 120:
            break

# 1. Fetch from workspace feed
print("\n--- 1. Fetching Workspace Feed ---")
fetch_paged_endpoint(f"https://studio-api.prod.suno.com/api/feed/v2?project_id={wid}", "WorkspaceFeed")

# 2. Fetch from global user feed
print("\n--- 2. Fetching Global Feed ---")
fetch_paged_endpoint("https://studio-api.prod.suno.com/api/feed/", "GlobalFeed")

print(f"\n[DONE] Total unique clips across all sources: {len(existing_clips_dict)}")
with open("workspace_clips_raw.json", "w", encoding="utf-8") as f:
    json.dump(list(existing_clips_dict.values()), f, ensure_ascii=False, indent=2)
