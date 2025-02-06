# 47. Count the occurrences of a unique value in an array.
import numpy as np

# Create an array with some repeating values
arr = np.array([1, 4, 4, 1, 5, 8, 10, 5, 8, 23, 32, 23, 32])

# Print the original array
print("Original Array:", arr)

# Use np.unique() to get the unique elements and their counts
# return_counts=True returns the counts of each unique value in the array
unique_values, counts = np.unique(arr, return_counts=True)

# Print the unique values and their corresponding counts
print("Unique values:", unique_values)
print("Counts of unique values:", counts)
