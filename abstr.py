from abc import ABC, abstractmethod
class Myclass(ABC):
    
    @abstractmethod
    def calculate(self,x):
        pass

#this is the sub class of the method
class Sub1(Myclass):
    def calculate(self,x):
        print('Square value = ',x*x)

import math
class Sub2(Myclass):
    def calculate(self,x):
       x = math.sqrt(x)
       print("Square root = %.2f"%x)

class Sub3(Myclass):
    def calculate(self,x):
        print('cube root of = ',x**3)

obj1 = Sub1()
obj1.calculate(3)

obj2 = Sub2()
obj2.calculate(3)

obj3 = Sub3()
obj3.calculate(3)