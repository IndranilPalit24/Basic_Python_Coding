class Person:
    count_instance = 0
    
    #constructor
    def __init__(self):
        Person.count_instance +=1

p1 = Person()
p2 = Person()
p3 = Person()


print(Person.count_instance)