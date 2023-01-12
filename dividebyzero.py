def divide(a,b):
    try:
        divide_num = a/b
        return divide_num

    except ZeroDivisionError:
        return "Please don't divide by zero"
    
    except TypeError:
        return 'Please input numbers only'



#print(divide(4,2))
#print(divide(4,0))

print(divide('4',2))