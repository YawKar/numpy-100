#### 10. Find indices of non-zero elements from [1,2,0,0,4,0] (★☆☆)
import numpy as np

a = np.array([1,2,0,0,4,0])
# print(a != 0)
print(*a.nonzero())
