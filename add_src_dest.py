from random import uniform
import json
import geopy.distance

#add source and destination to the existing graph

src_id='0'
coord_src=(33.753746,-84.386330)
coord_dest=(26.616756, -80.068451)
#coord_src=(uniform(-90, 90),uniform(-180,180))
#coord_dest=(uniform(-90, 90),uniform(-180,180))
dest_id='1'


with open('dijkstra_graph.json', 'r') as readfile:
    graph = json.load(readfile)

with open('nodes.json','r') as readfile:
    nodes_list = json.load(readfile)

for i in range(0,len(nodes_list)):
    node = nodes_list[i]['ID']
    node_lat=nodes_list[i]['Latitude']
    node_lng=nodes_list[i]['Longitude']
    coord_node=(node_lat,node_lng)
    distance_dest = geopy.distance.vincenty(coord_dest, coord_node).km
    distance_src=geopy.distance.vincenty(coord_src,coord_node).km
    if distance_src<400:
        if src_id not in graph:
            graph[str(src_id)] = {str(node): distance_src}
        else:
            graph[str(src_id)][node] = distance_src
    if distance_dest<400:
        #print("nodetodestination",node)
        graph[str(node)].update({dest_id: distance_dest})

    if dest_id not in graph:
        graph[dest_id] = {}


#print(graph['0'])
#print(graph['1'])
print(graph['112250'])








