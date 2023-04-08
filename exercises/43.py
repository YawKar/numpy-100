#### 43. Make an array immutable (read-only) (★★☆)
import numpy as np

a = np.eye(10)
a.flags.writeable = False
a[0][0] = 123 # ValueError: assignment destination is read-only
