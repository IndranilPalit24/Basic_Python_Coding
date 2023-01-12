def even(n):
    for i in range(1,n):
        if(i%2==0):
            yield i


numbers = even(7)

for num in numbers:
    print(num)