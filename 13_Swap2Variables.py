a=5
b=6

temp=a
a=b
b=temp
print(a,b)

x=11
y=12
x=x+y
y=x-y
x=x-y
print(x,y)

#no wastage of extra bit
p=14
q=15
p=p^q
q=p^q
p=p^q
print(p,q)

n=9
m=4
n,m=m,n
print(n,m)