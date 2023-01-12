'''def outer_func(any_func):
    def inner_func():
        print("This is inner func")
        any_func
    return inner_func

def func1():
    print("This is awesome func")


var = outer_func(func1)
var()'''

'''def outer_func(any_func):
    def inner_func():
        print("inside inner func")
        any_func()
    return inner_func

@outer_func
def func1():
    print('This is func1')

func1()'''



'''def outer_func(any_func):
    def inner_func(*args):
        print("Inside inner func")
        any_func(*args)
    return inner_func

#def func1(a):
 #   print(f"This is a function with argument {a}")

#func1(7)

def add(a,b):
    return a+b

print(add(5,3))'''




from functools import wraps
def outer_func(any_func):
    #@wraps(any_func)
    def inner_func(*args):
        '''This is the inner function'''
        print("awesome")
        any_func(*args)
    return inner_func

def add(a,b):
    '''This is addition function'''
    return a+b

print(add.__doc__)





