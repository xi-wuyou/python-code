#1
for i in {'a','b','c'}:
    print(i)
#2
#外层循环
for i in range(1,10):
    #内层循环
    for j in range(1,i+1):
        print(f'{i}*{j}={i*j}',end='\t')
    print()
#3
j=0
while j < 10:
    j+=1
    for i in range(1,j+1):
        print(f'{i}*{j}={i*j}',end='\t')
    print()
#4
i=0
while i < 10:
    i+=1
    for j in range(1,i+1):
        print(f'{j}*{i}={i*j}',end='\t')
    print()
    