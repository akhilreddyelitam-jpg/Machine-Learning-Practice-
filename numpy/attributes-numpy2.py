import numpy as np
arr1=np.array([1,2,3])
print(arr1)
print(type(arr1))
# 2d array shape
arr2=np.array([[1,2,3,3],[5,6,8,5]])
print(arr2)
print(arr1.shape)
print(arr2.shape)
arr3=np.array([[[1,2],[2,3]],[[4,5],[2,5]]])
print(arr3)
print(arr3.shape)
print(arr1.ndim)#ndim it gives n dimensional array
print(arr2.ndim)
print(arr3.ndim)
#size
print(arr1.size)
print(arr2.size)
print(arr3.size)
#itemsize
print(arr1.itemsize)
print(arr2.itemsize)
#dtype
print(arr1.dtype)
arr4=np.array([[2.3,3.4],[1.3,6.4]])
print(arr4)
print(arr4.dtype)
#astype it will covert 1type to given type
print(arr4.astype('int'))
print(arr2.astype('float'))