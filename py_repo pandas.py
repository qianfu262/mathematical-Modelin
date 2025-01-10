import pandas as pd
import numpy as np
file_path = "C:\python vscode\mathematicalModeling\\test.xlsx"
df=pd.read_excel(file_path, sheet_name="Sheet1",engine="openpyxl")
print(df.head())
print(df.info())
arr=np.array([1,3,4])
df={'样本号':[1,2,3],'萼片长':[8,2.1,4.5],'类型_num':[0,0,1]}
datadf=pd.DataFrame(df)
print(datadf)#输出一个类似于excel的表格


# 数据清洗和过滤
"""
print(df[df['萼片长'] > 5])#输出萼片长大于5的行 中括号里面就是筛选条件
lb=df['花瓣宽'].mean()-3*df['花瓣宽'].std
ub=df['花瓣宽'].mean()+3*df['花瓣宽'].std
print(df[(df['花瓣宽'] > lb) & (df['花瓣宽'] < ub)])#输出花瓣宽在均值加减三倍标准差之间的行 清洗掉许多不合理的数据
"""

