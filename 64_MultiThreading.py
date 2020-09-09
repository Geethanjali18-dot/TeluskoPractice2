import time
from threading import Thread


class Hello(Thread):
    def run(self):
        for i in range(5):
            print("hello")
            time.sleep(1)
class Hi(Thread):
    def run(self):
        for i in range(5):
            print("hi")
            time.sleep(1)

t1=Hello()
t2=Hi()
#t1.run()
#t2.run()
t1.start() #internally calls run
time.sleep(2)
t2.start()
t1.join()
t2.join()
print("bye")