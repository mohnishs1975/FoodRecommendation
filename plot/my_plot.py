import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def draw_kdtree(X,Y,Z):
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