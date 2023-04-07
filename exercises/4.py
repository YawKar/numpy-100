#### 4. How to find the memory size of any array (★☆☆)
import numpy as np

zeros = np.zeros(10)
numberOfElements = zeros.size
byteSizeOfAnElement = zeros.itemsize
print("Total size: {}".format(numberOfElements * byteSizeOfAnElement))
