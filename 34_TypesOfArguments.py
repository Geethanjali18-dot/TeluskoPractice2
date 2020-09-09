#Formal Arguments
#Actual Arguments-position,keyword,default,variable length

def add(a,b):
    c=a+b
    print(c)

add(8,9)

#default age =18
#def person(name,age=18):
def person(name,age):
    print(name,age)

#position
person("Geetha",30)
#keyword
person(age=31,name="Seetha")

#variable length
def sum(a,*b):
    c=a
    for i in b:
        c=c+i
    print(c)

sum(5,6)
sum(1,2,3,4)
