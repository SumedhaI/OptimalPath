import json
from collections import defaultdict
 #creates graph from the dijkstra_data_sample
 # graph is dijkstra_graph.json

with open('dijkstra_data_sample.json','r') as readfile:
    dijkstra_data_list = json.load(readfile)

#print(dijkstra_data_list)
#print(len(dijkstra_data_list))

new_dict={}
for value in dijkstra_data_list:
    if value['ID1'] not in new_dict:
        new_dict[value['ID1']] = {value['ID2']: value['Distance']}
    else:
        new_dict[value['ID1']][value['ID2']] = value['Distance']

print(len(new_dict))

with open('dijkstra_graph.json', 'w') as write_dijkstra_data:
    json.dump(new_dict, write_dijkstra_data)
