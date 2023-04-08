#### 28. What are the result of the following expressions? (★☆☆)
import numpy as np

print(np.array(0) / np.array(0)) # nan + warning
print(np.array(0) // np.array(0)) # zero + warning
print(np.array([np.nan]).astype(int).astype(float)) # ~zero + warning
