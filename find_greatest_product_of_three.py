from array import ArrayType, array
import numpy as np
import time

from numpy.core.fromnumeric import size
from Algorithms import QuickSort as quicky

def fgpot(Ar):
    g = 0
    steps = 0
    for a in range(len(Ar)):
        for b in range(a + 1, len(Ar)):
            for c in range(b + 1, len(Ar)):
                if g < (Ar[a]*Ar[b]*Ar[c]):
                    g = (Ar[a]*Ar[b]*Ar[c])
                steps += 1
    return (steps, g)

arr = np.random.randint(1, 100, size=100)

ts = time.time()
steps, g = fgpot(arr)
print(g)
print(f"N^3: {steps}")
te = time.time()
print(time.localtime(te-ts).tm_sec)

def quick_mul(A):
    q = quicky()
    arr_len = len(A)
    steps = q.sort(A, 0, arr_len - 1)
    print (A)
    prod = A[arr_len - 1] * A[arr_len - 2] * A[arr_len - 3]
    return (steps, prod)

# Original
# print("Sorted")
# print(arr)
# print("\n")

# Sorted
ts = time.time()
(steps, prod) = quick_mul(arr)
print(prod)
print(f'Steps {steps}')
te = time.time()
# print(time.localtime(te-ts).tm_sec)