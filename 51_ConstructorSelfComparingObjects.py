class Computer:
    def __init__(self):
        self.name="Geetha"
        self.age=18
    def update(self):
        self.age=30
    def compare(self,other):
        if self.age==other.age:
            return True
        else:
            return False

c1=Computer()
print(id(c1)) #heap memory
c2=Computer()
print(id(c2))
print(c1.name)
print(c2.name)
c1.name="rashi"
print(c1.name)
c1.age=12
print(c1.age)
c1.update()
print(c1.age)
#if c1==c2:
#    print("they are same")

if c1.compare(c2):
    print("they are same")
else:
    print("they are not same")