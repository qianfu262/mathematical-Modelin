#name=1
#print(name)
a=1
b=2
counter=100#整型变量
miles=1000.0#浮点型变量
var=True#布尔型变量
s="hello world"#字符串

#基本数据类型
a=100.0
#print(type(a))#输出a的类型 

## 字符串

name="alice"
#print(name[1:3])#输出li,字符串左闭右开
#print(name*5) #连续输出五次alice


##
a=3
b=2

#print(a**b)#3 的2次方,次幂运算
#print(a//b)#整除，向下取整
#print(a/b)#除法，保留小数
#print(a>b)#比较运算符

# 成员运算符

string="hello,world"
char="h"
#print( char in string)#判断h是否在字符串中

## 序列数据类型:列表 元组 字典

##列表的创建
list1=[1,2,True,"hello world",3.0]
print(list1)#整个列表
print(list1[1:3])#输出2，True
# 列表可以修改值

##元组的创建 元组不可以修改值
colors=("red","blue","green") ##相当于cpp中的enum
print(colors[0])#输出red

##字典的创建
dict1={"第一个元素":1,"第二个元素":'2',"第三个元素":True,"第四个元素":"hello world"}
print(dict1)#输出1 相当于cpp中的map
print(dict1["第一个元素"])#输出1
## 通过访问key值可以修改字典中的值

## 集合
set0={1,2,3.0,True,"hello world"}#不允许重复的元素,相当于cpp中的set
print(type(set0))
print(set0)#输出1,2,3.0,True,"hello world"


## 运算符加复合数据类型

a=[1,3,4,"2","alice"]
b=[2,3,4,"hello world"]
print(a+b)#输出[1,3,4,"2","alice",2,3,4,"hello world

## 成员运算符
a=[1,2,3,4,"2","alice",[4,"2"]]
b=1
print(b in a)#输出True
c="li"
print(c  in a)#输出false,判断是否在列表中
d=[4,"2"]
print(d in a)#输出True,判断是否在列表中
## 可以在a中加入一个子列表，判断子列表是否在a中

## 对于列表元组,集合,也可以进行强制类型转换
list_example=["hello",1,2,3,5,5,5,"hello"]
set(list_example)#将列表转换为集合
list(list_example)#将集合转换为列表
#print(list_example)#输出list_example

## 循环语句和条件语句
a=1
if a==1:
    print("a=1")
elif a==2:
    print("a=2")
else:
    print("a!=1 and a!=2")
## 循环语句
"""for i in range(5):##后面的语句也可以写成[0,1,2,3,4],输出1~4
    print(i)
    print(i%2)

#for i in "abcdefg": #列表也可以作为循环的条件
    print(i)##输出a,b,c,d,e,f,g
#for i in ["red","blue","green"]:
    print(i)
"""

# while循环
num=0
"""
while num<100:
    num+=1;
    print(num)
    if num==50:
        break
    else:
        continue
"""
#while 1:
#   print("这是一个死循环")

## 猜数
"""target=100 
predict=0
while predict!=target:
    predict=int(input("请输入一个整数:"))#input默认输入的是字符串,需要转换为整数
    if predict>target:
        print("猜大了")
    elif predict<target:
        print("猜小了")
    else:
        print("猜对了")
        break
else:
    print("恭喜猜对")
"""

## 函数

def max(a,b): ##def开头 接着是函数名，后面是参数列表
    if a>b:
        return a
    else:
        return b

## 缺省参数
def multiply(a,b=2):#b的默认值为2
    return a*b
multiply(3)#输出6,b自动赋值为2

## python读写文件

## file.close 关闭文件
## file.read([size]) 读取文件内容,size是读取文件指定的字节数,未给定则读取所有
## file.readline([size]) 读取文件的一行内容(包括\n),size是读取文件指定的字节数,未给定则读取所有
## file.readlines([size]) 读取文件的所有行内容(包括\n
## file.write(str) 向文件写入内容
## file.writelines(sequence) 向文件写入一个序列字符串列表,如果要换行需要自己写入\n
""""""
file_example=open(".vscode\mathematicalModeling\example.txt",mode="r")#打开文件,r表示只读
content=file_example.readlines()
for line in content:
    print(line)
file_example.close()#关闭文件


with open(".vscode\mathematicalModeling\example.txt",mode="a",encoding="utf-8") as file_example:#打开文件,a表示追加r表示只读
    file_example.write("hello everyone! \n")

    #content=file_example.readlines()
    #for line in content:
    #   print(line)
    