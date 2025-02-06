import numpy as np  # Importing the NumPy library

# Creating a 1D NumPy array with both positive and negative values
arr = np.array([1, 3, 4, 2, -10, -20, -30])

# Printing the original array before any modification
print("Original Array:")
print(arr)

# Replacing negative elements in the array with 0
# arr[arr < 0] selects all negative values and assigns them a value of 0
arr[arr < 0] = 0

# Printing the updated array after replacing negative values with 0
print("\nUpdated Array (Negative Values Replaced with 0):")
print(arr)
