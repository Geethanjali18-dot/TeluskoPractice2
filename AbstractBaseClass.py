from abc import ABC, abstractmethod


class Computer(ABC):
    @abstractmethod
    def process(self):
        #print("Running")
        pass

class Laptop(Computer):
    #pass
    def process(self):
        print("its running")
class Whiteboard:
    def write(self):
        print("its writing")
class Programmer:
    def work(self,com):
        print("solving bugs")
        com.process()

#com=Computer()
#com.process()
com1=Laptop()
com1.process()
com2=Whiteboard()

prog1=Programmer()
prog1.work(com1)
#prog1.work(com2)