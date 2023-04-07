#### 15. Create a 2d array with 1 on the border and 0 inside (★☆☆)
import numpy as np

a = np.zeros((5, 5))
a[:1] = 1
a[-1:] = 1
a[:, 0] = 1
a[:, -1] = 1
print(a)

a = np.ones((5, 5))
a[1:-1, 1:-1] = 0
print(a)
