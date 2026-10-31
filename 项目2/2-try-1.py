x=float(input("请输入数字:"))
y=float(input('再输入'))
z=(input('请输入运算方式:'))
if z=='+':
    result=x+y
    print(f"结果为：{x}+{y}={result}")
if z=='-':
    result=x-y
    print(f'结果为:{x}-{y}={result}')
if z=='*':
    result=x*y
    print(f'结果为:{x}*{y}={result}')
if z=='/':
    result=x/y
    print(f'结果为:{x}/{y}={result:-^15.3f}')


