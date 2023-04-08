#### 29. How to round away from zero a float array ? (★☆☆)
import numpy as np

a = np.random.uniform(-10, 10, 10)
absoluteCeiled = np.ceil(np.abs(a))
print(np.copysign(absoluteCeiled, a))

print(np.where(a > 0, np.ceil(a), np.floor(a))) # if elemnt > 0, then return ceiled,
                                                # otherwise floored
