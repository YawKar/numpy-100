#### 5. How to get the documentation of the numpy add function from the command line? 
#### (★☆☆)
import numpy as np

print(np.info("add"))
print(np.info(np.add))

# in bash: python3 -c "import numpy as np; np.info(np.add)"
