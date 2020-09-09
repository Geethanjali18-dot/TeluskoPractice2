from numpy import *

arr1=array([ [1,2,3]
             [4,5,6]
    ])

print(arr1.ndim) #dimensions
print(arr1.shape) #no of rows no of columns

print(arr1.size)

#converting 2D array to 1D array
arr2=arr1.flatten()
print(arr2)

#to convert to 1D from 2D
arr3=arr2.reshape(3,4) #3 rows 4 cols
print(arr3)

#to convert to 2D from 3D
arr4=arr2.reshape(2,2,3) #3D array having 2 2D arrays
print(arr4)

m=matrix(arr1)
print(m)

m1=matrix('1,2:3,4:5,6:7,8')
m2=matrix('1,2,12:3,4:5,6,11:7,8,9')
m3=matrix('1,2,12:3,4:5,6,11:7,8,9')
print(diagonal(m2))
print(m.min())
print(m.max())

print(m2+m3)
print(m2*m3)