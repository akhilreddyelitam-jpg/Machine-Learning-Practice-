import numpy as np
#reshapeing the array
arr1=np.array([[1,2,3,4],[3,4,5,6]])
print(arr1)
print(arr1.ndim)
print(arr1.ravel())
print(arr1.ndim)
#transpose
print(arr1)
print(arr1.transpose())
#stacking means combing to arrays
print(arr1)
arr2=np.arange(12,20).reshape(2,4)
print(arr2)
arr3= np.hstack((arr1,arr2))
print(arr3)
arr4= np.vstack((arr1,arr2))#vertical stacking
print(arr4)
#spltting
print(arr1)
arr5=np.hsplit(arr1,2)
print(arr5)
arr6=np.vsplit(arr1,2)
print(arr6)