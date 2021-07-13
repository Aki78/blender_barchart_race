import json
from pprint import pprint as pp

with open("finald2020CovidData.json", "r") as f:
     data = json.load(f)[0]
#print(data[0].keys())

print(data['id'])
print(data['label'])
print(data['children'])

pp(data['children'][0])
