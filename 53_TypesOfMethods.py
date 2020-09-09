class Student:
    #static variable
    school='Teslusko'
    def __init__(self,m1,m2,m3):
        self.marks1=m1
        self.marks2=m2
        self.marks3=m3
    #instance method
    def average(self):
        return(self.marks1+self.marks2+self.marks3)/3
    def getm1(self):
        return self.marks1
    def setm1(self):
        self.marks1=35
    #class method
    @classmethod
    def getSchool(cls):
        return cls.school
    #static method
    @staticmethod
    def info():
        print("This is student class..in abc module")

s1=Student(23,76,90)
s2=Student(91,14,65)
print(s1.average())
print(s2.average())
print(s1.getSchool())
print(Student.getSchool())
Student.info()