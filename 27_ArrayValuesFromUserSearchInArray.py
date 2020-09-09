from array import *
arr=array('i',[])
n=int(input("Enter the size  or length of array"))
for i in range(n):
    x=int(input("Enter the value of array"))
    arr.append(x)
print(arr)

k=0 #index
search=int(input("enter the element to search"))
for i in range(len(arr)):
    if i==search:
        print("found at index ",k)
        break
    k += 1
print(arr.index(search))

