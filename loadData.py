import json
import requests
from pathlib import Path
import geopy.distance

#this file loads data from api and saves in ope_data.json file

my_file = Path("open_data.json")

if my_file.exists():
    print("File exists")

else:
    response = requests.get("https://api.openchargemap.io/v2/poi/?output=json&countrycode=US&maxresults=20000&compact=true&verbose=false").json()
    with open('open_data.json', 'w') as writefile:
        json.dump(response, writefile)


with open('open_data.json','r') as readfile:
    list_data = json.load(readfile)

with open('dijkstra_graph.json', 'r') as readfile:
        graph = json.load(readfile)

print(type(graph))
print(graph['112251']['112250'])
print(len(graph))
for line in graph:
    print(line)










