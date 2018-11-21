import json
from generate_random_availability import deleted_nodes
#delete node from graph if there is o availability
with open('dijkstra_graph.json', 'r') as readfile:
        graph = json.load(readfile)

print(len(graph))

for i in range(0, len(deleted_nodes)):
    node = deleted_nodes[i]
    del graph[str(node)]