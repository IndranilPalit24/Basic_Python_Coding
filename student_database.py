class Student:
    #this is a constructor
    def __init__(self, name, marks):
        self.name =name
        self.marks=marks

    #this is an instance method
    def display(self):
        print(f"Hi {self.name}. Your marks is {self.marks}")


#constructor is called with arguments
s = Student("Indranil",90)
s.display()
print('----------------------------------')

s1=Student("Norman",50)
s1.display()