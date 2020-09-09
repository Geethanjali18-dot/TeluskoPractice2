a=10
print(id(a))

def something():
    #global a
    a=9
    x=globals()['a']
    print(id(x))
    a=15
    print("inside func",a)
    globals()['a']=18


something()
print("outside func",a)