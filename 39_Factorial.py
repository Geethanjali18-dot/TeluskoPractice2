n=int(input("enter the number"))

def fact(n):
    f=1
    while n!=0:
        f=f*n
        n-=1
    return f




result=fact(n)
print(result)