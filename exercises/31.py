#### 31. How to ignore all numpy warnings (not recommended)? (★☆☆)
import numpy as np

np.seterr(all='ignore')
np.ones(1) / 0 # error ignored
