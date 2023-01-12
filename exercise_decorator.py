import time
from functools import wraps

def calculate_time(function):
    @wraps(function)
    def wrapper_func(*args, **kwargs):
        print(f"Executing {function.__name__}")
        t1 = time.time()
        returned_value = function(*args,**kwargs)
        t2 = time.time()
        time_taken = t2-t1
        print(f"This function took {time_taken} in seconds")
        return returned_value
    return wrapper_func

@calculate_time
def square_finder(n):
    return [i**2 for i in range(0,n+1)]

square_finder(100)