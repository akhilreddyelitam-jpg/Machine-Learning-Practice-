import numpy as np
import sys
import time



lista=range(100)
arr1=np.arange(100)
print(lista)
print(arr1)
print(sys.getsizeof(87)*len(lista))
print(arr1.itemsize*arr1.size)

x=range(100000)
y=range(100000,200000)
start_time=time.time()
c=[(x,y)for x,y in zip(x,y)]
print(time.time()-start_time)

#np.arange
a=np.arange(100000)
b=np.arange(100000,200000)
start=time.time()
c=a+b
print(time.time()-start)