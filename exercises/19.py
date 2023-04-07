#### 19. Create a 8x8 matrix and fill it with a checkerboard pattern (★☆☆)
import numpy as np

a = np.zeros((8, 8), dtype=np.int32)
for i in range(1, 8, 2):
    a += np.diag(np.ones((8 - i,), dtype=np.int32), k = i)
    a += np.diag(np.ones((8 - i,), dtype=np.int32), k = -i)
print(a)

a = np.zeros((8, 8), dtype=np.int32)
a[::2, ::2] = 1
a[1::2, 1::2] = 1
print(a)
