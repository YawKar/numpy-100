#### 37. Create a 5x5 matrix with row values ranging from 0 to 4 (★★☆)
import numpy as np

print(np.tile(np.arange(0, 5), 5).reshape((5, 5)))
print(np.zeros((5, 5)) + np.arange(0, 5))
