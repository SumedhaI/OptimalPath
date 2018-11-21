import random
import json
#check whether the node is available or not
#generate random number to check availability
#delete nodes from graph if there is no availability
with open('nodes.json','r') as readfile:
    nodes_list = json.load(readfile)

deleted_nodes=[]

for i in range(0,len(nodes_list)):
    node=nodes_list[i]['ID']
    random_num = random.uniform(0, 1)
    if random_num < 0.1:
        deleted_nodes.append(node)

print(deleted_nodes)
print(len(deleted_nodes))