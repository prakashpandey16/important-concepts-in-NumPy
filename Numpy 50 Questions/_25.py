# 25. Swap two rows in a 2D NumPy array.

import numpy as np

# Creating a 2D NumPy array
arr = np.array([[12, 3, 4], 
                [9, 8, 7], 
                [14, 19, 18]])

# Printing the original array
print("Original Array:")
print(arr)

# Swapping row 0 with row 2
arr[[0, 2]] = arr[[2, 0]]  

# Printing the array after swapping rows
print("Array After Swapping Rows 0 and 2:")
print(arr)

# Swapping column 0 with column 2
arr[:, [2, 0]] = arr[:, [0, 2]]  

# Printing the array after swapping columns
print("Array After Swapping Columns 0 and 2:")
print(arr)
