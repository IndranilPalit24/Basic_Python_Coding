numbers1 = [2,4,3,8,10]

#print(all([num%2==0 for num in numbers1]))

#print(any([num%2!=0 for num in numbers1]))


def mysum(*args):
    '''This is a function'''
    if all([type(arg)==int or type(arg)==float for arg in args]):
        total=0
        for num in args:
            total+=num
        return total 
    else:
        return "Wrong input"



print(mysum(1,2,3,4,8,9))









