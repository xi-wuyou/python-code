num=[x**2 for x in range(5)]
print(num)
nums=[]
for i in range(5):
    nums.append(i**2)
print(nums)
#筛选偶数1
num2=[x for x in range(10) if x%2==0]
print(num2)
num2_2=[]
#2
for j in range(10):
    if j%2==0:
        num2_2.append(j)
print(num2_2)
#多条件与复杂逻辑（奇数变负数，偶数保留）1
num_3=[x if x%2==0 else -x for x in range(10)]
print(num_3)
#2
number=[]
for y in range(10):
    if y%2!=0:
        number.append(-y)
    else:
        number.append(y)
print(number)