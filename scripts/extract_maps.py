import re
from urllib.parse import unquote

html = open('index.html', encoding='utf-8').read()
matches = re.findall(r'<a href="https://www\.google\.com/maps/search/\?api=1&amp;query=([^"]+)".*?>(.*?)</a>', html)
if not matches:
    matches = re.findall(r'<a href="https://www\.google\.com/maps/search/\?api=1&query=([^"]+)".*?>(.*?)</a>', html)

with open('map_links.txt', 'w', encoding='utf-8') as f:
    for m in matches:
        f.write(f"{unquote(m[0])} -> {re.sub(r'<[^>]+>', '', m[1])}\n")
