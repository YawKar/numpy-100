#### 27. Consider an integer vector Z, which of these expressions are legal? (★☆☆)
import numpy as np
Z = (np.random.random(10) * 10).round().astype(dtype=np.int32)

print(Z**Z) # element-wise powering
print(2 << Z) # idk but Z << 2 just left shifts element-wise
print(Z <- Z) # Z < (-Z) 
print(1j*Z) # complex numbers
print(Z/1/1) # casts to floats
# Z<Z>Z illegal truth value is ambiguous
print(Z < Z) # Z < Z
