# 20. Create a structured NumPy array with x, y coordinates covering [0,1] x [0,1]
import numpy as np

# Define the number of points along each axis
num_points = 10

# Create arrays of x and y values in the range [0, 1]
x = np.linspace(0, 1, num_points)
y = np.linspace(0, 1, num_points)

# Create a structured array with 'x' and 'y' fields
dtype = [('x', float), ('y', float)]
coordinates = np.array([(xi, yi) for xi in x for yi in y], dtype=dtype)

# Print the structured array
print(coordinates)
