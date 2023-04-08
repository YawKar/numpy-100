#### 35. How to compute ((A+B)*(-A/2)) in place (without copy)? (★★☆)
import numpy as np

a = np.ones(10)
b = np.ones(10)
np.add(a, b, out=b)
np.divide(a, 2, out=a)
np.negative(a, out=a)
np.multiply(b, a, out=a)

print(a)
