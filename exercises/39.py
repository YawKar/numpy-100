#### 39. Create a vector of size 10 with values ranging from 0 to 1, both excluded(★★☆)
import numpy as np

a = np.linspace(0, 1, 11, False)[1:]
print(a)
