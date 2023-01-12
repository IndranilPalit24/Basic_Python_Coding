class Student:
    def __init__(self, name=" ", marks=0):
        self.name=name
        self.marks=marks

    def greet(self):
        print('Hi ',self.name)
        print("Your Marks are ", self.marks)

    def calculate(self):
        if(self.marks>=600):
            print("You have got Grade A")
        
        elif(self.marks<=500 and self.marks>=300):
            print("You have got grade B")

        else:
            print("You have failed")


n = int(input("How many student?: "))

i=0
while(i<n):
    name = input("Enter your name: ")
    marks =  int(input("Enter your marks: "))

    s1 = Student(name,marks)
    s1.greet()
    s1.calculate()
    i+=1
    print("----------------------")
