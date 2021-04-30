import pandas as pd
from sklearn.neighbors import KDTree
from scipy import spatial
import math
import numpy as np
import time
import random

def cartesian(latitude, longitude, elevation = 0):
    # Convert to radians
    latitude = latitude * (math.pi / 180)
    longitude = longitude * (math.pi / 180)

    R = 6371 # 6378137.0 + elevation  # relative to centre of the earth
    X = R * math.cos(latitude) * math.cos(longitude)
    Y = R * math.cos(latitude) * math.sin(longitude)
    return (X, Y)

def rand_coords():
    lat = random.randint(-90,90)
    lon = random.randint(-180,180)
    return (lat,lon)



if __name__ == "__main__":

    data = pd.read_csv('poi_data_all.csv',encoding='latin-1')
    tree = spatial.cKDTree(data)

    for x in range(10):
        [X, Y] = rand_coords()
        cartesian_coord = cartesian(X, Y)
        start_time = time.time()
        dist, ind = tree.query([cartesian_coord], p = 2, k = 10)
        print("--- %s microseconds ---" % ((time.time() - start_time)*1000000))