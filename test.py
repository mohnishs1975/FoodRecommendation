import pandas as pd
from sklearn.neighbors import KDTree
from scipy import spatial
import math
import numpy as np
import time


data = pd.read_csv('poi_data_all.csv',encoding='latin-1')
print(data.head())

start_time = time.time()
if __name__ == "__main__":

    tree = spatial.cKDTree(data)
    print("--- %s seconds ---" % ((time.time() - start_time)*1000000))