import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
x=np.linspace(0,10,100) #三个给参数分别是start stop num 左右边界和个数
print(x)
y=np.sin(x)
plt.plot(x,y)
plt.title('y=sin(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
##

x2=np.linspace(0,10,100)
y2=np.sin(x2)
plt.scatter(x,y,marker='*',color='r',label='数据集')
plt.plot(x2,y2,linestyle='--',label='拟合曲线')
plt.legend()#调用legend才可以显示图例
plt.show()
##
fig,axes=plt.subplots(1,2)
axes[0].scatter(x,y,marker='*',color='r',label='数据集')
axes[0].set_xlabel('x1')
axes[0].set_ylabel('y')
axes[1].plot(x2,y2,linestyle='--',label='拟合曲线')
axes[1].set_xlabel('x2')
plt.show()


                        