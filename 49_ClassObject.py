
class Computer:
    def config(self):
        print("i5,16gb,1TB")

com1=Computer()
print(type(com1))
com1.config()
Computer.config(com1)
a=5
print(a.bit_length())