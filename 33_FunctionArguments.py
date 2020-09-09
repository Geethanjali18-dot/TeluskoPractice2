def update(x):
    print(id(x))
    x=8
    print(id(x))
    print("x ",x)


def update1(lst):
    print(id(lst))
    lst[1]=25
    print(id(lst))
    print('lst ',lst)


lst=[10,30,20]
update1(lst)
print(id(lst))
a=10
update(a)
print(id(a))
print("a ",a)
