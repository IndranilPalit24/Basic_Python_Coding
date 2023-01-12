class A():
    def method(self):
        print("This is in class A")
        #super().method()

class B:
    def method(self):
        print("This is in class B")
        #super().method()

class C:
    def method(self):
        print("This is in method C")

class X(A,B):
    def method(self):
        print("X class method")
        super().method()

class Y(B,C):
    def method(self):
        print("This is in class Y")
        super().method()

class P(X,Y,C):
    def method(self):
        print("This is in class P")
        super().method()

p=P()
p.method()

print(())
