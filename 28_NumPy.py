#import numpy
#array
#linspace
#logspace
#arange
#zeros
#ones
from array import array

arr=array([1,2,3,4,5],int)
print(arr.dtype)
print(arr)

#linspace
arr1=linspace(0,15,16) #16 parts #by default 50 parts
print(arr1)

#arange
arr2=array([1,15,2]) #2 steps

#logspace
arr3=logspace([1,40,5]) #10^1 10^40 5 parts
print('%2f' %arr[4])

#zeros
arr4=zeros(5) #5 zeros
print(arr4)

#ones
arr5=ones(5) ##5 ones
print(arr5)

