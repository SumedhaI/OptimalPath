import json

with open('sample_data.json','r') as readfile:
    sample_data_list = json.load(readfile)
number_of_sampled_data=len(sample_data_list)

nodes_list=[]
for i in range(0, number_of_sampled_data):
    id = sample_data_list[i]['ID']
    lat = sample_data_list[i]['AddressInfo']['Latitude']
    lng = sample_data_list[i]['AddressInfo']['Longitude']

    nodes_list.append({"ID":id, "Latitude":lat, "Longitude":lng})

print(len(nodes_list))

with open('nodes.json', 'w') as write_nodes:
    json.dump(nodes_list, write_nodes)