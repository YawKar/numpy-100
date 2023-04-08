#### 30. How to find common values between two arrays? (★☆☆)
import numpy as np

a = np.array(range(10))
b = np.array(range(-100, 100))

print(np.intersect1d(a, b))

