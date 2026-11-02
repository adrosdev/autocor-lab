import time
import requests

def get_with_retry(url, max_attempts=3):
    for attempt in range(1, max_attempts + 1):
        r = requests.get(url, timeout=5)
        if r.status_code not in (429, 403):
            return r

        if "Retry-After" in r.headers:
            wait = int(r.headers["Retry-After"])
        elif "X-RateLimit-Reset" in r.headers:
            wait = int(r.headers["X-RateLimit-Reset"]) - int(time.time())
        else:
            wait = 2 ** attempt

        wait = max(1, min(wait, 60))
        print(f"attempt {attempt}: limited, waiting {wait}s")
        time.sleep(wait)

    raise RuntimeError(f"gave up after {max_attempts} attempts")

r = get_with_retry("https://api.github.com/repos/python/cpython")
print(r.status_code)