class Myclass:
    #calculate power value by a static method
    @staticmethod
    def powervalue(x,y):
        result =  x**y
        print(f'The power of {x} is the power value in {y} is {result}')

p = Myclass.powervalue(5,4)
