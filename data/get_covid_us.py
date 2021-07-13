import requests
import json

dl = requests.get('https://api.covidtracking.com/v2/us/daily.json').json()

with open("us_data.json", "w") as f:
    json.dump(dl, f)
print(dl.keys())
