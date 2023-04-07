#### 13. Create a 10x10 array with random values and find the minimum and maximum values
#### (★☆☆)
import numpy as np

a = np.random.random((10, 10))
minimum = a.min()
maximum = a.max()
print(minimum)
print(maximum)