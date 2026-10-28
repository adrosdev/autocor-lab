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
r1 = session.get(f"https://{host}/restconf/data/Cisco-IOS-XE-native:native/hostname")
r2 = session.get(f"https://{host}/restconf/data/Cisco-IOS-XE-native:native/hostname")
print(f"\n{time.perf_counter() - start:.2f}s")
print("\n")
print(r1.json())
print(r2.json())
