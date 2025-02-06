import numpy as np

# Create an array of dates for the month of February 2025
# np.arange() generates an array of dates starting from '2025-02-01' to '2025-03-01'
# The 'dtype="datetime64[D]"' ensures that the generated array consists of date objects (without time)
feb_arr = np.arange('2025-02-01', '2025-03-01', dtype="datetime64[D]")

# Iterate through the generated array of dates
# For each date in the array, print it
for date in feb_arr:
    print(date)
