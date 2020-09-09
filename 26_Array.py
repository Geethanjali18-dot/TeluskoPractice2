from array import *
vals=array('i',[5,9,8,4,2])
vals1=array('i',[5,9,8,4,-2])
#vals=array('i',[5,9,8,4,2.9])
print(vals)
print(vals1)
print(vals.buffer_info()) #address size
print(vals.typecode)
vals.reverse()
print(vals)
print(vals[0])
for i in vals:
    print(i)
vals2=array('u',['a','e','i','o','u'])
for i in vals2:
    print(i)
vals3=array(vals.typecode,(a*a for a in vals))
for i in vals3:
    print(i)
i=0
while i <len(vals3):
    print(vals3[i])
    i+=1


