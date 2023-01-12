from functools import wraps
def only_int_allow(function):
    @wraps(function)
    def wrapper_function(*args, **kwargs):
        if all(type(arg)==int for arg in args):
            return function(*args,**kwargs)
        return "Invalid Arguments"

        '''datatypes = []
            for arg in args:
                datatypes.append(type(arg)==int)
            if all(datatypes):
                return function(*args,**kwargs)
            else:
                print("Invalid function)
            '''


    return wrapper_function

@only_int_allow
def addition(*args):
    total = 0
    for i in args:
        total+=i
    return total

print(addition(1,2,3,[1,2,3]))
