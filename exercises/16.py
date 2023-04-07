#### 16. How to add a border (filled with 0's) around an existing array? (★☆☆)
import numpy as np

a = np.ones((5, 5))
bordered = np.zeros((7, 7))
bordered[1:-1, 1:-1] = a
print(bordered)

a = np.ones((5, 5))
print(np.pad(a, 1))
