#understand instance variables
class Sample:
    def __init__(self):
        self.x =10

    def modify(self):
        self.x+=1

s1=Sample()
s2 =Sample()

print('x is ',s1.x)
print('x is ',s2.x)

s1.modify()
print("modified x")
print('x is',s1.x)