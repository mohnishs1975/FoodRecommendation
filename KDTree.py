import pandas as pd
from sklearn.neighbors import KDTree
from scipy import spatial
import math

data = pd.read_csv('zomato.csv',encoding='latin-1')
#print(data.RestaurantName[3])
def cartesian(latitude, longitude, elevation = 0):
    # Convert to radians
    latitude = latitude * (math.pi / 180)
    longitude = longitude * (math.pi / 180)

    R = 6371 # 6378137.0 + elevation  # relative to centre of the earth
    X = R * math.cos(latitude) * math.cos(longitude)
    Y = R * math.cos(latitude) * math.sin(longitude)
    Z = R * math.sin(latitude)
    return (X, Y, Z)

restaurants = []
for index, row in data.iterrows():
    coordinates = [row['Latitude'], row['Longitude']]
    cartesian_coord = cartesian(*coordinates)
    restaurants.append(cartesian_coord)

tree = spatial.KDTree(restaurants)

def find_restaurant(lat, lon):
    temp = []
    cartesian_coord = cartesian(lat, lon)
    closest = tree.query([cartesian_coord], p = 2)
    index = closest[1][0]
    return {
        'name' : data.RestaurantName[index],
        'latitude' : data.Latitude[index],
        'longitude' : data.Longitude[index],
        'Address' : data.Address[index],
        'distance' : closest[0][0]
    }
    #temp.append(data[index])
    


test = find_restaurant(42, 73)

print(test)

