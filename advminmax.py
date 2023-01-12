names= ['harshit','harsh','ab']

#print(min(names, key=lambda item: len(item)))


students2 = [
    {'name':'harshit', 'score':50,'age':24},
    {'name':'harsh','score':40,'age':19},
    {'name':'rohit','score':20,'age':23}
]

#print(max(students2, key=lambda item: item.get('score'))['name'])


students3 = {
    'harshit':{'score':700,'age':40},
    'mohit': {'score':600,'age':30},
    'rohit':{'score':300,'age':20}
}

print(max(students3,key=lambda item: students3[item]['score']))


