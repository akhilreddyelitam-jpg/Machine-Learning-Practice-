import numpy as np
# 1d array 
arr1=np.array([1,2,3,4,5])
print(arr1)
print(type(arr1))
# 2d array
arr2=np.array([[1,2,3,3],[5,6,8,5]])
print(arr2)
print(type(arr2))
#zeros arry
arr3=np.zeros((2,3))
print(arr3)
#arry ones
arr4=np.ones((3,3))
print(arr4)
#array identity
arr5=np.identity(5)
print(arr5)
#array arange
arr6=np.arange(20)
print(arr6)
arr7=np.arange(1,20,2)
print(arr7)
#linspace
arr8=np.linspace(10,20,10)
print(arr8)
arr9=arr8.copy()
print(arr9)