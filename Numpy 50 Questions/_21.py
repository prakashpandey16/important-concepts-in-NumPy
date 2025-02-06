# 21. Subtract the mean of a random vector from all elements.
import numpy as np

# Creating a random vector (1D array)
arr = np.array([1, 5, 4, 2, 8, 9, 10, 13])
print("Original array:")
print(arr)

# Calculating the mean of the array
mean_of_arr = np.mean(arr)
print("Mean of the array:", mean_of_arr)

# Subtracting the mean from all elements using NumPy's subtract function
subtract_arr = np.subtract(arr, mean_of_arr)

print("Array after subtracting the mean:")
print(subtract_arr)


