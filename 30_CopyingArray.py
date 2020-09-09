from numpy import*
arr=array([1,2,3,4,5])
arr=arr+5
print(arr)

arr1=array([6,1,9,3,2])
arr3=arr+arr1
print(arr3)

print(sin(arr))
print(cos(arr))
print(log(arr))
print(sqrt(arr))
print(sum(arr))
print(min(arr))
print(max(arr))

#to concatenate 2 arrays
print(concatenate(arr,arr1))

#one array with same id copying values
arr4=arr
print(arr4)
print(arr4)

#shallow copy
arr5=arr.view()
print(arr5)

#deep copy
arr6=arr.copy()
print(arr5)