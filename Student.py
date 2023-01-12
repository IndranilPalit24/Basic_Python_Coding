class Student:
    def setname(self, naam):
        self.naam = naam

    def getname(self):
        return self.naam

    def setMarks(self, ank):
        self.ank = ank

    def getmarks(self):
        return self.ank

stu = Student()

name = input("Enter your name: ")
stu.setname(name)

marks = int(input("Enter your marks: "))
stu.setMarks(marks)

print("Hi ",stu.getname())
print("Your marks are ",stu.getmarks())
