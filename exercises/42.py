#### 42. Consider two random array A and B, check if they are equal (★★☆)
import numpy as np

a = np.random.random(10)
b = a.copy()

print(np.allclose(a, b))
print(np.array_equal(a, b))
