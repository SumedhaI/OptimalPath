from loadData import list_data
import geopy.distance
import json
from pathlib import Path

#this file sample data from open_data.json taking atlanta as centre considering only 5250 charging stations
#creates edge between two charging stations considering distance between charging station must not be more than 400 km
sampled_file = Path("sample_data.json")

if sampled_file.exists():
    print("Sampled file exists")

else:
  number_of_data = len(list_data)
  lat_atl = 33.7507209
  lng_atl = -84.3242866
  coord_atl = (lat_atl, lng_atl)
  distance_from_atl = 950
  sampled_list_data = []

  for x in list_data:
        lat = x['AddressInfo']['Latitude']
        lng = x['AddressInfo']['Longitude']
        coord = (lat, lng)
        distance = geopy.distance.vincenty(coord_atl, coord).km

        if distance <= distance_from_atl:
            sampled_list_data.append(x)

  with open('sample_data.json', 'w') as write_sample_file:
            json.dump(sampled_list_data, write_sample_file)



with open('sample_data.json','r') as readfile:
    sample_data_list = json.load(readfile)


print(len(sample_data_list))
list_dijkstra=[]

number_of_sampled_data=len(sample_data_list)


dijkstra_data=Path("dijkstra_data_sample.json")

if dijkstra_data.exists():
    print("Dijkstra data file exists")


else:
 for i in range(0, number_of_sampled_data):
    id1 = sample_data_list[i]['ID']
    lat1 = sample_data_list[i]['AddressInfo']['Latitude']
    lng1 = sample_data_list[i]['AddressInfo']['Longitude']
    coord1 = (lat1, lng1)
    for j in range(0, number_of_sampled_data):
        if j < i:
            id2 = sample_data_list[j]['ID']
            lat2 = sample_data_list[j]['AddressInfo']['Latitude']
            lng2 = sample_data_list[j]['AddressInfo']['Longitude']
            coord2=(lat2,lng2)
            distance = geopy.distance.vincenty(coord1, coord2).km
            if distance<400:
             list_dijkstra.append({"ID1":id1, "ID2":id2, "Distance":distance})
             list_dijkstra.append({"ID1": id2, "ID2": id1, "Distance": distance})
             #print(list_dijkstra)
             print(len(list_dijkstra))



 with open('dijkstra_data_sample.json', 'w') as write_dijkstra_data:
            json.dump(list_dijkstra, write_dijkstra_data)