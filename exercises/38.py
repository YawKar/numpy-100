#### 38. Consider a generator function that generates 10 integers and use 
#### it to build an array (★☆☆)
import numpy as np

def gen():
    for i in range(10):
        yield i

print(np.fromiter(gen(), dtype=np.int32, count=4))
