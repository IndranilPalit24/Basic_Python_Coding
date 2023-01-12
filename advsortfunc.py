#fruits = ['grapes','mango','apple']

#fruits.sort()
#print(fruits)



#fruits2 = ('grapes','apples','mangoes')
#sorted(fruits2)
#print(fruits2)

guitars = [
    {'model': 'yamaha310' , 'price':840000},
    {'model':'fatih neptune', 'price':500000},
    {'model':'faith apollo','price':350000}
]

print(sorted(guitars,key=lambda item: item['price']))