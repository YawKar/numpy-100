#### 33. How to get the dates of yesterday, today and tomorrow? (★☆☆)
import numpy as np

print(np.datetime64('today') - np.timedelta64(1)) # yesterday
print(np.datetime64('today')) # today
print(np.datetime64('today') + np.timedelta64(1)) # tomorrow
