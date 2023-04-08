#### 34. How to get all the dates corresponding to the month of July 2016? (★★☆)
import numpy as np

print(np.arange(np.datetime64('2016-07'), 
                np.datetime64('2016-08'), 
                dtype='datetime64[D]'))
