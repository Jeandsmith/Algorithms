import numpy as np
import matplotlib.pyplot as plt
import time as t
import random as r
from config import *

from Algorithms import *
# from tqdm import tqdm

times = []
random_data = np.random.randint(DATAMINRANGE, DATAMAXRANGE, DATAMAXRANGE)
x = np.arange(DATAMAXRANGE)

fig, ax = plt.subplots(3, 1)
ax[0].bar(x, ar)
ax[0].set_title('Unsorted Array')

# [101, 201, ..., 10001]
iter = 0
for maxR in range(DATAMINRANGE, DATAMAXRANGE, 100):
    random_data = np.random.randint(DATAMINRANGE, DATAMAXRANGE, maxR)
    x = np.arange(maxR)

    iter += 1
    print(f'\rIter {iter}')
    bsn = selectionsort()
    s = t.time()
    sorted_data = bsn.sort(random_data)
    e = t.time()
    times.append(e - s)
    print(sar)

ax[1].bar(x, sorted_data)
ax[1].set_title('Sorted Array')

ax[2].plot(times)
ax[2].grid(True)
plt.show()

# Additional information
print(f'\n\nSeconds: {t.localtime(e - s).tm_sec} Secs')
print(f'Steps Taken: {bsn.steps_taken()}')
