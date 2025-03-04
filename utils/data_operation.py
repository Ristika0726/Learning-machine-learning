import math
import numpy as np

x1=[1,2,3]
x2 = [3,5,6]

def euclidean_distance(x1, x2):
    # Eulidean distance between 2 points
    return math.sqrt(math.sum((x1-x2)**2))


