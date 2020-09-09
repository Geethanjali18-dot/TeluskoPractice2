

def fib(n):
    a, b = 0, 1
    print(a)
    print(b)
    for i in range(n):

        if i<n:
            c=a+b
            print(c)
            a,b=b,c




fib(5)