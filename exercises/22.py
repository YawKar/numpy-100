#### 22. Normalize a 5x5 random matrix (★☆☆)
import numpy as np

a = np.random.random((5, 5))
std = a.std()
mean = a.mean()
a -= mean
a /= std
print(a)
print(a.std())
print(a.mean())
