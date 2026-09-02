import subprocess, os, shutil

chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
if not os.path.exists(chrome_path):
    chrome_path = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"

html_url = "file:///C:/Users/ymero/Downloads/day2_route_map_demo.html"
out_download = r"C:\Users\ymero\Downloads\day2_map_demo_snapshot.png"
out_workspace = r"d:\2026東京單車騎旅\day2_map_demo_snapshot.png"
out_artifact = r"C:\Users\ymero\.gemini\antigravity\brain\a6311675-6d02-45ba-9aec-e8b72dc7842d\day2_map_demo_snapshot.png"

cmd = [
    chrome_path,
    "--headless=new",
    f"--screenshot={out_download}",
    "--window-size=1280,1050",
    "--virtual-time-budget=2000",
    "--hide-scrollbars",
    html_url
]

print("Running chrome screenshot...")
res = subprocess.run(cmd, capture_output=True, text=True)
print("Return code:", res.returncode)

if os.path.exists(out_download):
    shutil.copyfile(out_download, out_workspace)
    shutil.copyfile(out_download, out_artifact)
    print("Screenshot saved to all 3 paths successfully!")
else:
    print("Screenshot failed to generate.")
