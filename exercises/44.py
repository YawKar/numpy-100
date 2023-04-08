#### 44. Consider a random 10x2 matrix representing cartesian coordinates,
#### convert them to polar coordinates (★★☆)
import numpy as np

cartesian = np.random.randint(0, 1000, (10, 2))
print(cartesian)
x, y = cartesian[:, 0], cartesian[:, 1]
r = np.sqrt(x**2 + y ** 2)
phi = np.arctan2(y, x)
print(r)
print(phi)
