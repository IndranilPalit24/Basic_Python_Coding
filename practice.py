class Practice:
    x=10
    
    @classmethod
    def modify(cls):
        cls.x+=1


p=Practice()

print('p is',p.x)

p.modify()

print('p is', p.x)
