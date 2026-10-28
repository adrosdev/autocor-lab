import os
import requests
from dotenv import load_dotenv

load_dotenv()

url = f"https://{os.getenv('IOSXE_HOST')}/restconf/data/Cisco-IOS-XE-native:native/hostname"
headers = {"Accept" : "application/yang-data+json"}
auth = (os.getenv("IOSXE_USER"), os.getenv("IOSXE_PASS"))

response = requests.get(url, headers=headers, auth=auth, verify=False)
print(response.status_code)
print(response.json())