import pandas as pd
from sklearn.neighbors import KDTree
from scipy import spatial
import math
import numpy as np


def cartesian(latitude, longitude, elevation = 0):
    # Convert to radians
    latitude = latitude * (math.pi / 180)
    longitude = longitude * (math.pi / 180)

    R = 6371 # 6378137.0 + elevation  # relative to centre of the earth
    X = R * math.cos(latitude) * math.cos(longitude)
    Y = R * math.cos(latitude) * math.sin(longitude)
    Z = R * math.sin(latitude)
    return (X, Y, Z)

def find_restaurant(lat, lon, threshold, kin = 1):
    temp = []
    cartesian_coord = cartesian(lat, lon)
    dist, ind = tree.query([cartesian_coord], p = 2, k = kin)
    for i in range(ind[0].size):                                        # the index of closest one                             
        index = ind[0][i]
        distance = dist[0][i]
        if distance <= threshold:
            one_result =  {
                'name' : cuisine.RestaurantName[index],
                'latitude' : cuisine.Latitude[index],
                'longitude' : cuisine.Longitude[index],
                'Address' : cuisine.Address[index],
                'distance' : distance                               # the distance between target pos and the closest one
            }
            temp.append(one_result)
    return temp

def filter(parameter, index):
    filtered = []
    filtered = data[data[parameter].str.contains(index) == True]
    return filtered

if __name__ == "__main__":
    data = pd.read_csv('zomato.csv',encoding='latin-1')
    
    cuisine = []
    cuisine = filter("Cuisines", "Chinese")
    cuisine = cuisine.reset_index()

    # preparing 3D cord
    index_max = 0
    for index, row in cuisine.iterrows():
        index_max += 1
    X = np.zeros([index_max,1])
    Y = np.zeros([index_max,1])
    Z = np.zeros([index_max,1])

    restaurants = []

    for index, row in cuisine.iterrows():
        coordinates = [row['Latitude'], row['Longitude']]
        cartesian_coord = cartesian(*coordinates)
        restaurants.append(cartesian_coord)
        X[index] = cartesian_coord[0]
        Y[index] = cartesian_coord[1]
        Z[index] = cartesian_coord[2]

    tree = spatial.KDTree(restaurants)

    # try query by Latitude, Longitude and number of results wanted
    test = find_restaurant(31, 77, 50, 10)
    for r in test:
        print(r)

    # plot 3D graph of data
    # draw_kdtree(X,Y,Z)
