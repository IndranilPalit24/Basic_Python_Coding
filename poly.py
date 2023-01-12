class Dog:
    """Dog class"""
    def bark(self):
        """bark class"""
        print("Bow wow!")

class Human:
    """Human class"""
    def talk(self):
        """talk on human"""
        print("hello Hi!")

class Duck:
    """a Duck class"""
    def talk(self):
        """talk method"""
        print("Quack quack")

def call_talk(obj):
    """a method call"""
    if hasattr(obj,'talk'):
        obj.talk()
    else:
        obj.bark()

x=Human()
call_talk(x)

y=Duck()
call_talk(y)

z=Dog()
call_talk(z)