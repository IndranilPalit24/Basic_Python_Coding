class Father:
    def __init__(self):
        self.height = 1.56


class Mother:
    def __init__(self):
        self.colour= "black"



class child(Father,Mother):
    pass


c=child()
print(c.height)
print(c.colour)

