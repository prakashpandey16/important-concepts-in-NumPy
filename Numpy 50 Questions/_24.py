# 24. Convert float array to integer array in NumPy
import numpy as np
arr = np.array([10.5,23.4,5.5,10.34,90.45,10.454,100.34])
print(arr)
print(arr.dtype)
arr_int = arr.astype(int)
print(arr_int)
print(arr_int.dtype)