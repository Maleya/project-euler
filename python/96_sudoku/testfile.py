# testfile

import numpy as np 

r = np.random.randint(0,9,(5,5))

print(r)
a,b = np.where(r==0)

for i,j in zip(a,b):
    print(i,j)