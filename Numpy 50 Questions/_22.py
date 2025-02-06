# 22. Sort a random array of size 10.
import numpy as np

# Creating a random array of size 10
arr = np.array([1, 10, 3, 4, 8, 5, 7, 29, 15, 2])
print("Original array:")
print(arr)

# Sorting the array in ascending order using np.sort()
sorted_arr = np.sort(arr)

print("Sorted array:")
print(sorted_arr)
