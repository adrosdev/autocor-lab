import os
from dotenv import load_dotenv
from client import ApiClient


load_dotenv("../.env")

meraki = ApiClient(
    "https://api.meraki.com/api/v1",
    headers={"Authorization": f"Bearer {os.getenv('MERAKI_API_KEY')}"},
)

org_id = meraki.get("organizations").json()[0]["id"]

nets = meraki.paginate(f"organizations/{org_id}/networks", params={"perPage": 3})
print(len(nets))
for n in nets:
    print(n["id"], n["name"])