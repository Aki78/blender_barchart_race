import json
from pprint import pprint as pp

with open("us_data.json", "r") as f:
     data = json.load(f)
#print(data.keys())

#print(data['meta'])
#print(data['links'])
#print(data['data'])

#pp(data['data'])
pp(data['data'][0])
pp(data['data'][0].keys())

for i, s in enumerate(data['data']):
    pp(data['data'][i]['states'])
    
    pp(data['data'][0].keys())
