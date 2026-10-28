import requests
import json

url = "https://api.github.com/repos/python/cpython/contributors"
r = requests.get(url, params={"per_page": 5}, timeout=5)

all_items = []

while url:
    r = requests.get(url, params={"per_page": 50}, timeout=5)
    r.raise_for_status()
    all_items.extend(r.json())
    url = r.links.get("next", {}).get("url")
    print(f"fetched {len(all_items)} so far")

print(f"total: {len(all_items)}")