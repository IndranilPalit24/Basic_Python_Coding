#def outer_func():
#    def inner_func():
 #       print("message is here!")

  #  return inner_func

#var = outer_func()
#var()


def outer_func(message):
    def inner_func():
        print(f"your message is {message}")
    return inner_func()


var = outer_func("Hi")
var


