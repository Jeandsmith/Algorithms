from Datastructs import *
import numpy as np
import matplotlib.pyplot as plt
import time as t
import random as r
from config import *

from Algorithms import *
# from tqdm import tqdm

# times = []
# random_data = np.random.randint(DATAMINRANGE, 100, 100)
# x = np.arange(DATAMAXRANGE)
A = [50, 29, 93, 34, 13, 92, 47, 4, 86, 70, 11, 20, 95, 31, 40, 57, 70, 82, 71, 67, 94,  2, 53, 31,
 64, 18, 90, 90, 48, 76,  6,  9, 45, 14, 10, 85, 56, 93, 92, 64, 54, 54,  9, 27, 66, 33, 16, 99,
 33, 16, 77, 76, 72, 45, 97, 79, 37, 89, 64, 22, 40, 21, 13, 75, 74, 93, 52, 62, 50,  3,  9, 18,
 23, 37, 38,  6, 32, 42, 42,  9, 12, 40, 24, 15, 96, 51, 25,  6, 10,  1, 20, 35, 98, 22, 71, 73,
 13, 87,  9, 55]
g = BinarySearchTree()

#  Insert to the tree
for val in A:
    # print(val)
    g.insert(val)

print(A)
print(g.max_value())
