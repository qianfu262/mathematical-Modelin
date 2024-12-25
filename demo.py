#实例:猜数

target=100 
predict=0
cnt=0
while predict!=target:
    predict=int(input("请输入一个整数:"))#input默认输入的是字符串,需要转换为整数
    if predict>target:
        print("傻逼,猜大了")
    elif predict<target:
        print("傻逼,猜小了")
    else:
        print("猜对了")
        break
    cnt+=1
    if cnt>=8:
        print("傻逼,二分不会吗")
