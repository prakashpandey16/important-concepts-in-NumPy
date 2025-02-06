# 41. Get the number of days between two dates in NumPy.
import numpy as np

# Define the first date
date1 = np.datetime64('2025-01-18')

# Define the second date
date2 = np.datetime64('2025-07-29')

# Subtract date1 from date2 to find the difference
# This gives a NumPy timedelta64 object representing the difference in days
difference = date2 - date1

# Print the difference (in days)
print(difference)
