import requests
import json

token = """eyJhbGciOiJSUzI1NiIsImtpZCI6InN1bm8tYXBpLXJzMjU2LWtleS0xIiwidHlwIjoiSldUIiwieC1hYmx5LXRva2VuIjoibnYzNlZ3LklDZ0gwaWhTbDlhU1JuWGViMXd2M3h5XzlXdTNENUJWWUdkYmJlS3VhVWV3TEhKVGU2blcyRmVfdV9acEtrQ24yZ3AySEhNcEpqVmthN2N5Y2hzVFFkQ3JmQzE0c04zWHZMM2M5TnFhODF0Wi0xcVFhWUF4ejVXRXhqYlY4eTNUSWllX1lLNWRtRlRoeFlKM3lYSVFpUkNySHFvWm45YXRnVU92djVHMXhRVkVNalNVRkhwUVdXUS1VRk1VWk1fM3NQWkQ1NHNZMjVhbFRNZTdnaGt0cS1wLTRJZGhNTjdfRktOeHdzY1ZGTUlvIn0.eyJzdW5vLmNvbS9jbGFpbXMvdXNlcl9pZCI6IjA1NmIxM2Y0LWY2NWUtNGUwYS1hOGQwLTE2YjY3YzBhMmJkYSIsImh0dHBzOi8vc3Vuby5haS9jbGFpbXMvY2xlcmtfaWQiOiIwNTZiMTNmNC1mNjVlLTRlMGEtYThkMC0xNmI2N2MwYTJiZGEiLCJzdW5vLmNvbS9jbGFpbXMvdG9rZW5fdHlwZSI6ImFjY2VzcyIsInN1bm8vZGlkIjoxMzgyMjczODUsImV4cCI6MTc4NzYzMjc5MywiYXVkIjoic3Vuby1hcGkiLCJzdWIiOiIwNTZiMTNmNC1mNjVlLTRlMGEtYThkMC0xNmI2N2MwYTJiZGEiLCJhenAiOiJodHRwczovL3N1bm8uY29tIiwiZnZhIjpbMCwtMV0sImlhdCI6MTc4NzYyOTE5MywiaXNzIjoiaHR0cHM6Ly9hdXRoLnN1bm8uY29tIiwiaml0IjoiZTgxNDlhMDYtMzkzNy00MjBjLTk3M2YtOGRkNTE3ZGFjYzc5IiwicGxhbiI6IjNlYWViZWYzLWVmNDYtNDQ2YS05MzFjLTNkNTBjZDE1MTRmMTptb250aDoiLCJzdW5vL2pvaW5lZCI6MTc4Mzc2ODc3OCwic2lkIjoic2Vzc2lvbl85ODA4NjI2MjEwZWU0NDI4YmI3ZGNiIiwic3Vuby5jb20vY2xhaW1zL2VtYWlsIjoieW1lcm9vbUBnbWFpbC5jb20iLCJodHRwczovL3N1bm8uYWkvY2xhaW1zL2VtYWlsIjoieW1lcm9vbUBnbWFpbC5jb20iLCJzdW5vL2hhbmRsZSI6ImJyYWludGFpd2FuIiwic3Vuby91c2VyX2lkIjoiMTY4OTI1MTY3Iiwic3Vuby91c2VybmFtZSI6InltZXJvb21AZ21haWwuY29tIn0.MzDvniM3ZczrUc32wSHB12crp81S7pV4eBbQ2xC2JbrbUTPGBu3-Iy5F0n8k-7_x12PrR80iqGjRerrj4NKdzKG8-wbLbavXSu1qmpsFUN_BZ2pLtu6HV-lVMruk2x6g2Dp0jG3Gi-CgKPszgjMS2CfJnaPg-8Bnij6wa3aB2wXS3t1KPvsTXBYbsDhS2VKPZ0CROwrjHYulFQ7KyDim09aXufi6DgLo-7jS4Vmk-g6zVMd62l22nV9yTTIuh42DI0_el0Ct6O4FTYR4F7jTLHF6fPrZNUs3b7zS7GSNe3-gIlAViz6E81Cr52IQZ7z2GYKw-q2FAeJIy-UDq3vZOw""".strip()

headers = {
    "Authorization": f"Bearer {token}",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
    "Content-Type": "application/json",
    "Accept": "application/json, text/plain, */*",
    "Referer": "https://suno.com/",
    "Origin": "https://suno.com"
}

sample_id = "2f5332d6-d190-4d1d-b8d5-08a53a273aa7"

tests = [
    ("POST", "https://studio-api.prod.suno.com/api/gen_video/", {"clip_id": sample_id}),
    ("POST", "https://studio-api.prod.suno.com/api/gen_video", {"clip_id": sample_id}),
    ("POST", f"https://studio-api.prod.suno.com/api/gen_video/{sample_id}/", {}),
    ("POST", f"https://studio-api.prod.suno.com/api/gen_video/{sample_id}", {}),
    ("POST", f"https://studio-api.prod.suno.com/api/audio/export/wav", {"clip_id": sample_id}),
    ("POST", f"https://studio-api.prod.suno.com/api/export/wav", {"clip_id": sample_id}),
    ("POST", f"https://studio-api.prod.suno.com/api/export/video", {"clip_id": sample_id}),
    ("POST", f"https://studio-api.prod.suno.com/api/clips/export/wav", {"clip_id": sample_id}),
    ("POST", f"https://studio-api.prod.suno.com/api/clips/export/video", {"clip_id": sample_id}),
]

for method, url, body in tests:
    try:
        r = requests.post(url, headers=headers, json=body, timeout=5)
        print(f"{url} -> {r.status_code}")
        if r.status_code != 404:
            print("   ->", r.text[:200])
    except Exception as e:
        print(f"Err {url}: {e}")
