import numpy as np
arr1=np.arange(24).reshape(6,4)
print(arr1)
print(arr1[2:4,1:3])

#iterations
for i in arr1:
    print(i)

for i in np.nditer(arr1):
  print(i)