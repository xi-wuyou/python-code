person={'name':'Alice','age':25}
print(person.keys())
print(person.values())
print(person.update({'age':26,'job':'Engineer'}))
print(person.popitem())
del person['age']
person.update({'age':25})
print(person.pop('age'))
for key in person:
    print(key,end='')
for value in person.values():
    print(value,end='')
for k,v in person.items():
    print(f'{k}:{v}',end="")