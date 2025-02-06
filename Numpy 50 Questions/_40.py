# 40. Find the day of the week for each day in a NumPy date range.
import numpy as np
week = np.arange('2025-02-01','2025-02-08',dtype="datetime64[D]")

for date in week:
    day_of_week = np.datetime64(date).astype('datetime64[D]').astype('O').strftime('%A')
    print(f"{date} is a {day_of_week}")
    