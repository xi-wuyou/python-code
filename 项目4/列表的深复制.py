import copy
a=[1,[2,3]]
b=copy.deepcopy(a)
a[1][1]=5
b[1][1]=6
print(a)
print(b)