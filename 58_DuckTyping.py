class PyCharm:
    def execute(self):
        print("compiling")
        print("running")
class MyEditor:
    def execute(self):
        print("Spell check")
        print("convention check")
        print("compiling")
        print("running")
class Laptop:
    def code(self,ide):
        ide.execute()

ide=PyCharm()
ide1=MyEditor()
lap1=Laptop()
lap1.code(ide)
lap1.code(ide1)
