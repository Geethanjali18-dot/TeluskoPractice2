from functools import reduce
nums=[1,2,3,4,5,6,7,8,9,10]


evens=list(filter(lambda a: a%2==0 ,nums))

mapEx=list(map(lambda x:x*2,evens))
reduceEx=reduce(lambda a,b:a+b,mapEx)
print(evens)
print(mapEx)
print(reduceEx)