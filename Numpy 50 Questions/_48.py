# 48. Convert a NumPy array to a Python list
import numpy as np

# Create a NumPy array
arr = np.array([1, 2, 3, 4, 4, 3, 2, 1, 10, 12, 3, 4, 53])
print("NumPy Array:", arr)

# Convert the NumPy array to a Python list using the tolist() method
arr_list = arr.tolist()

# Print the resulting Python list
print("Converted Python List:", arr_list)
