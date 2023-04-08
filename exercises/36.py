#### 36. Extract the integer part of a random array of positive numbers 
#### using 4 different methods (★★☆)
import numpy as np

a = np.random.random(10) * 10
print(a.astype(np.int32))
print(a - a % 1)
print(np.floor(a))
print(np.trunc(a))
