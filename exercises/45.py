#### 45. Create random vector of size 10 and replace the maximum value by 0 (★★☆)
import numpy as np

a = np.random.random(10) * 10
print(a)
a = np.where(a == a.max(), np.zeros(a.shape), a)
print(a)
print()
a = np.random.random(10) * 10
print(a)
a[a == a.max()] = 0
print(a)
