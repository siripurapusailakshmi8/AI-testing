import time
import requests

PAGES = ['/', '/restaurants', '/checkout']

def measure(base_url):
    results = {}
    for p in PAGES:
        url = base_url.rstrip('/') + p
        t0 = time.time()
        r = requests.get(url, timeout=10)
        t1 = time.time()
        results[p] = {"status": r.status_code, "elapsed": t1-t0}
    return results

if __name__ == '__main__':
    import os
    base = os.getenv('BASE_URL', 'https://example-app-url')
    print(measure(base))
