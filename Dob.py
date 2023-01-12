class Person:
    def __init__(self,name,dd,mm,yy) :
        self.name = name
        self.Db = self.Dob(dd,mm,yy)

    def display(self):
        print("Hi ", self.name)


    class Dob:
        def __init__(self,dd,mm,yy):
            self.dd = dd
            self.mm = mm
            self.yy = yy

        def display(self):
            print(f"DOB = {self.dd}/{self.mm}/{self.yy}")


#p= Person("Norah",20,10,1996)
#p.display()

#x=p.Db
#x.display()


#create Dob class as sub object to person class object
y = Person("Indranil",20,10,1996).Dob(20,10,1996)
y.display()
print(y.yy)

