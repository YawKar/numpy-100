#### 25. Given a 1D array, negate all elements which are between 3 and 8, in place.
#### (★☆☆)
import numpy as np

a = (np.random.random(30) * 10).round()
a[(a > 3) & (a < 8)] *= -1
print(a)
