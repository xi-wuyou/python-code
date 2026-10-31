#这串代码只是去掉了0到100之间7的倍数
for i in range(1,101):
    if i%7==0:
        continue
    print(i)
#与上面的代码不同，下面的代码去掉了7的倍数，个位是7的数，十位数是7的数
for a in range(1,101):
    if a % 7 == 0 or a % 10 == 7 or a // 10 == 7:
        continue
    else:
        print(a)
        
   