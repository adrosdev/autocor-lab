import os
import requests
from dotenv import load_dotenv
import time

load_dotenv()

host = os.getenv('IOSXE_HOST')
headers = {"Accept" : "application/yang-data+json"}
auth = (os.getenv("IOSXE_USER"), os.getenv("IOSXE_PASS"))

session = requests.Session()
session.auth = auth
session.headers.update(headers)
session.verify=False

start = time.perf_counter()
try:
    r1 = session.get(f"https://{host}/restconf/data/Cisco-IOS-XE-native:native/hostname", timeout=5)
    r1.raise_for_status()
    print(r1.json())
except requests.HTTPError as e:
    print(f"\nRequest error: {e}")
except requests.ConnectionError as e:
    print(f"\nCould not reach the device: {e}")
except requests.Timeout as e:
    print(f"\nDevice did not answer in 5 seconds: {e}")


print(f"\n{time.perf_counter() - start:.2f}s")
