class Emp:
    #this is a constructor
    def __init__(self, id, name, salary):
        self.name = name
        self.id = id
        self.salary = salary

    def display(self):
        print("Id is ",self.id)
        print("Name is ",self.name)
        print("salary is ",self.salary)


class Myclass:
    @staticmethod
    def mymethod(e):
        e.salary+=1000
        e.display()

e=Emp(200, "Indranil", 20000)
Myclass.mymethod(e)
