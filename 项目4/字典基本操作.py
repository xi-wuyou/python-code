#访问元素
person={'name':'Alice','age':25}
print(person['name'])
#安全访问（键不存在时返回None或默认值）
print(person.get('name'))
print(person.get('address'))
print(person.get('address','不存在'))
#修改/添加元素
person['age']=26
person['address']='beijing'
#in，检测键是否存在
print('name in person')
print('address' not in person)
#删除元素
print('\n删除前：\n',person)
del person['age']
print('删除后：\n',person)
age=person.pop('age')
print('\n删除的值为：',age,'\n删除后字典为：\n',person)
person.clear()