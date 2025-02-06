# 32. Stack two arrays vertically and horizontally. 
import numpy as np

# Creating two 2D NumPy arrays
arr = np.array([[1, 2, 3],
                [4, 5, 6]])

brr = np.array([[7, 8, 9],
                [9, 10, 11]])

# Stacking arrays vertically (adds rows)
arr_vertical = np.vstack((arr, brr))

# Stacking arrays horizontally (adds columns)
arr_horizontal = np.hstack((arr, brr))

# Printing the vertically stacked array
print("Vertical Stack:\n", arr_vertical)
print("\n")

# Printing the horizontally stacked array
print("Horizontal Stack:\n", arr_horizontal)
