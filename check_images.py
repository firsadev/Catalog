import re
import urllib.request

with open('index.html', 'r', encoding='utf-8') as f:
    txt = f.read()

urls = re.findall(r"url\('([^']+)'\)|src=\"(https://[^\"]+)\"", txt)
all_urls = []
for u in urls:
    url = u[0] or u[1]
    if url and url.startswith('http'):
        all_urls.append(url)

all_urls = list(dict.fromkeys(all_urls))  # deduplicate

print(f"Found {len(all_urls)} unique image URLs\n")
for url in all_urls:
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        resp = urllib.request.urlopen(req, timeout=10)
        status = resp.status
        size = len(resp.read())
        print(f"OK ({status}, {size} bytes): {url[:90]}")
    except Exception as e:
        print(f"FAIL: {e} | {url[:90]}")
