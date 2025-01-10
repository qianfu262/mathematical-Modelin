import numpy as np

arr=np.array([1,2,3,4,5])
print(arr)
print(type(arr)) 
arr=np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])#二维数组
print(arr[0])#二维数组打印第一行
print(arr[0:3])#二维数组打印前3行]
print(arr[1][2])

#运算
print(np.array([1,2,3])+np.array([4,5,6]))#对应向量的相加
print(np.array([1,2,3])*np.array([4,5,6]))#对应向量的点乘

# 数组形状操作
arr=np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
print(arr.shape)#(4,3) 4行3列
new_arr=np.reshape(arr,(2,6))#将arr变成2行6列的数组 注意：2*6=4*3,一定要乘积相等
print(new_arr,new_arr.shape)#(2,6)

## 线性代数 进阶使用
arr1=np.array([1,2,3])
arr2=np.array([4,5,6]) 
print(np.dot(arr1,arr2))#1*4+2*5+3*6=32 点乘

print("平均值",np.mean(arr))#平均值
print("方差",np.var(arr))#方差
print("标准差",np.std(arr))#标准差
print("最大值",np.max(arr))#最大值
print("最小值",np.min(arr))#最小值
print("中位数",np.median(arr))#中位数\
print("求和",np.sum(arr))#求和
print("排序",np.sort(arr))#排序
print(arr[(arr<10) & (arr>5)])#大于10的元素 and大于5的元素

# 保存与导入
# npy
print("保存与导入")
print(arr)
np.save("arr.npy",arr)#保存
arr=np.load("arr.npy")
print(arr)#导入