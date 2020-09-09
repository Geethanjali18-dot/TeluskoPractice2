f=open("demo.txt",'r')
#print(f.read())
#print(f.readline())
#print(f.readline(4))

#f1=open("demo1.txt","w")
#data="MY name is Geetha"
#f1.write(data)

#f1=open("demo1.txt","r")
#print(f1.read())

f2=open("demo1.txt","a")
data1="I am Seetha"
f2.write(data1)
f2=open("demo1.txt","r")
print(f2.read())