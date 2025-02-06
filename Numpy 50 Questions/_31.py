# 31. Convert a 1D array into a 2D array with 2 rows.
import numpy as np

arr = np.array([1,2,3,4,5,6])
arr_2d = arr.reshape(2,3)
print(arr_2d)