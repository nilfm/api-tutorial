import requests
from pprint import pprint

URL = "http://127.0.0.1:5000"

# Request the list of available user names
users = requests.get(f"{URL}/users").json()
pprint(users)

# Request info on each user
for user in users:
    info = requests.get(f"{URL}/user/{user}").json()
    pprint(info)

# What happens if we request a non-existent user?
req = requests.get(f"{URL}/user/nonexistent")
print(req)
# We expect a 404 code
print(f"Status code: {req.status_code}")
