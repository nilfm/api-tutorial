import requests
from pprint import pprint

TOKEN = "###" # TODO: Modify this


URL = "https://community-open-weather-map.p.rapidapi.com/weather"

querystring = {
    "q": "London,uk",
    "units": "metric",
}

headers = {
    'x-rapidapi-key': TOKEN,
    'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com"
}

response = requests.get(URL, headers=headers, params=querystring)

print(response.url)
pprint(response.json())