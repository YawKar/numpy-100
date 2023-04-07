#### 20. Consider a (6,7,8) shape array, what is the index (x,y,z) of the 100th element?
#### (★☆☆)
import numpy as np

a = np.empty((6, 7, 8), dtype=np.int32)
elementIndex = 99
print(np.unravel_index(elementIndex, (6, 7, 8)))
