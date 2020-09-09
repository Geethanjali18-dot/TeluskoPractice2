lst=[1,2,3,4,5,6,7,8,9,11,12,13]


def count(lst):
    even=0
    odd=0
    for i in lst:
        if i%2==0:
            even+=1
        else:
            odd+=1
    return even,odd


even,odd=count(lst)
print(even)
print(odd)
print("even :{} and odd:{}".format(even,odd))