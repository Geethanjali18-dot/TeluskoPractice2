x=int(input("How many candies you want"))
i=1
av=10 #available
while i<=x:
    if i>av:
        print("out of stock")
        break

    print("candy")
    i+=1
#print("bye")


for j in  range(101):
    if j%3==0 or j%5==0:
        continue
    print(j)
print("bye")

for k in range(1,101):
    if k%2!=0:
        pass
    else:
        print(k)