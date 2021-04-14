import pandas as pd
from sklearn.neighbors import KDTree
from scipy import spatial
import math
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def cartesian(latitude, longitude, elevation = 0):
    # Convert to radians
    latitude = latitude * (math.pi / 180)
    longitude = longitude * (math.pi / 180)

    R = 6371 # 6378137.0 + elevation  # relative to centre of the earth
    X = R * math.cos(latitude) * math.cos(longitude)
    Y = R * math.cos(latitude) * math.sin(longitude)
    Z = R * math.sin(latitude)
    return (X, Y, Z)

def find_restaurant(lat, lon, kin = 1):
    temp = []
    cartesian_coord = cartesian(lat, lon)
    dist, ind = tree.query([cartesian_coord], p = 2, k = kin)
    for i in range(ind[0].size):                                        # the index of closest one                             
        index = ind[0][i]
        distance = dist[0][i]
        one_result =  {
            'name' : data.RestaurantName[index],
            'latitude' : data.Latitude[index],
            'longitude' : data.Longitude[index],
            'Address' : data.Address[index],
            'distance' : distance                               # the distance between target pos and the closest one
        }
        temp.append(one_result)
    return temp
    
def draw_kdtree():
    #dist, ind = sktree.query(restaurants[:1], k=10)
    #print(dist)
    #print(ind)  # indices of 3 closest neighbors
    #sk_arr = sktree.get_arrays()
    #print(sk_arr)
    #plt.scatter(X, Y, s=9, marker=".")
    #plt.xlabel("X")
    #plt.ylabel("Y")
    #plt.title("restaurants")
    #plt.show()

    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(111, projection="3d")
    ax.scatter(X, Y, Z, marker='.', s=10)
    
    #set label and title
    ax.set_xlabel('x',size=15)
    ax.set_ylabel('y',size=15)
    ax.set_zlabel('z',size=15)
    ax.set_title("restaurants", weight='bold', size=20)
    
    plt.show()

if __name__ == "__main__":
    data = pd.read_csv('zomato.csv',encoding='latin-1')
    #print(data.RestaurantName[3])

    # prepare for reading 3D cord
    index_max = 0
    for index, row in data.iterrows():
        index_max += 1
    X = np.zeros([index_max,1])
    Y = np.zeros([index_max,1])
    Z = np.zeros([index_max,1])

    restaurants = []

    for index, row in data.iterrows():
        coordinates = [row['Latitude'], row['Longitude']]
        cartesian_coord = cartesian(*coordinates)
        restaurants.append(cartesian_coord)
        X[index] = cartesian_coord[0]
        Y[index] = cartesian_coord[1]
        Z[index] = cartesian_coord[2]

    tree = spatial.KDTree(restaurants)

    test = find_restaurant(42, 73,5)
    print(test)
    
    draw_kdtree()