import time
import requests

class ApiClient:
    def __init__(self, base_url, auth=None, headers=None, verify=True):
        self.base_url = base_url.rstrip("/")
        self.session = requests.Session()
        self.session.auth = auth
        self.session.verify = verify
        if headers:
            self.session.headers.update(headers)

    def get(self, path, params=None, max_attempts=3):
        url = f"{self.base_url}/{path.lstrip('/')}"
        for attempt in range(1, max_attempts + 1):
            r = self.session.get(url, params=params, timeout=5)
            if r.status_code not in (429, 403):
                if not r.ok:
                    raise requests.HTTPError(f"{r.status_code} {r.reason}: {r.text}", response=r)
                return r
            wait = self._wait_time(r, attempt)
            print(f"attempt {attempt}: limited, waiting {wait}s")
            time.sleep(wait)
        raise RuntimeError(f"gave up after {max_attempts} attempts")

    @staticmethod
    def _wait_time(r, attempt):
        if "Retry-After" in r.headers:
            wait = int(r.headers["Retry-After"])
        elif "X-RateLimit-Reset" in r.headers:
            wait = int(r.headers["X-RateLimit-Reset"]) - int(time.time())
        else:
            wait = 2 ** attempt
        return max(1, min(wait, 60))

    def paginate(self, path, params=None):
        items = []
        r = self.get(path, params=params)
        while True:
            items.extend(r.json())
            next_url = r.links.get("next", {}).get("url")
            if not next_url:
                return items
            r = self.session.get(next_url, timeout=5)
            r.raise_for_status()
