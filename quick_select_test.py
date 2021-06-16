from numpy.core.fromnumeric import size
from Algorithms import QuickSort
import numpy as np

target = 25
sample = np.random.randint(100, size=59)
ins = QuickSort()
print(f'Target = {target}')
print(f'Sample Array = {sample}\n')

idx = ins.select(sample, 0, len(sample) -1, target=target)

print(f'Semi Sorted Array = {sample}')
print(f'Returned Value = {target in sample}')
print(f'Index = {idx}')