# 50. Create a function that applies a rolling window mean to an array. 
import numpy as np
import pandas as pd

# Create the array
arr = np.arange(0, 10).reshape(2, 5)
print("Original Array:")
print(arr)

# Convert the NumPy array to a Pandas DataFrame
df = pd.DataFrame(arr)

# Apply rolling window mean with a window size of 3
window_size = 3
rolling_mean = df.rolling(window=window_size).mean()

print(f"\nRolling Window Mean (Window Size = {window_size}):")
print(rolling_mean)
