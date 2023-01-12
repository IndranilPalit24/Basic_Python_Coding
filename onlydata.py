from functools import wraps
import time
def only_datatype_allowed(datatype):
    def decorator(function):
        @wraps(function)
        def wrapper(*args,**kwargs):
            print(f"You are calling {function.__name__} function")
            print(f"{function.__doc__}")
            if all([type(arg)==datatype for arg in args]):
                t1 = time.time()
                returned_function =  function(*args,**kwargs)
                t2 = time.time()
                print("Time is ",t2-t1)
                return returned_function
            return "Invalid Arguments"
        return wrapper
    return decorator

@only_datatype_allowed(str)
def add_two_strings(*args):
    '''This is a string function concatening two string'''
    string = ''
    for i in args:
        string+=i
    return string


@only_datatype_allowed(int)
def add_integers(*args):
    '''This is a function adding numbers input by the user'''
    total = 0
    for i in args:
        total+=i
    return total

print(add_integers(1,12))