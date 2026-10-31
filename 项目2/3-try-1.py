tickle=int(input('0：未购买高铁票/1：购买了高铁票，输入：'))
safe=int(input('0：未通过安检/1：通过了安检，请输入：'))
if tickle==1 and safe==1:
    print('请上车')
elif tickle==1 and safe==0:
    print('你不符合乘车标准')
else:
    print('你未购票')
