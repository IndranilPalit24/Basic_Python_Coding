def to_power(x):
    def square(n):
        return n**x
    return square

square = to_power(3)
print(square(2))