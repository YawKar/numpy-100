#### 18. Create a 5x5 matrix with values 1,2,3,4 just below the diagonal (★☆☆)
import numpy as np

a = np.zeros((5, 5), dtype=np.int32)
for i in range(1, 5):
    a[i][i - 1] = i
print(a)

a = np.diag(np.arange(1, 5), k = -1)
print(a)
