import requests
import json

url = "https://api.github.com/repos/python/cpython/contributors"
r = requests.get(url, timeout=5)
print(r.json()["rate"])
