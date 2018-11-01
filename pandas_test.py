import pandas as pd
from pandas import Series, DataFrame

# obj = Series([12,35,-8,100])
# print(obj)
# print('==============')
# print(obj.keys())
# print(obj.values)

# 创建Series数据时，可以指定key
# obj2 = Series([12,35,-8,100],index=('a','b','c',1))
# print(obj2)
#
# #通过key修改value
# obj2['b'] = 'hehe'
# print(obj2)
#
# #判断key是否存在
# print('c' in obj2)

# 将字典类型的数据转换为Series类型
# object3 = {'bejing':100,'shanghai':200,'guangzhou':300,'shenzhen':400}
# print(object3)
# object4 = Series(object3)
# print(object4)

# 修改Series类型数据的key值
# object4.index = ('bj','sh','gz','sz')
# print(object4)

# DateFrame 处理多维数组
# object6 = {
#     'city':['beijing','shanghai','guangzhou','shenzhen'],
#     'year':[2015,2016,2017,2018],
#     'pop':[100,200,300,400]
# }
# df = DataFrame(object6)
# print(df)

# 可以根据key进行排序
# df2 = DataFrame(object6,columns=('year','city','pop'))
# print(df2)

# 提取二维数据方式
# print(df2['year'])
# print('================')
# print(df2.get('year'))
# print('================')
# print(df2.year)

object7 = {
    'city': ['beijing', 'shanghai', 'guangzhou', 'beijing'],
    'year': [2015, 2016, 2017, 2018],
    'pop': [100, 200, 300, 400]
}
df3 = DataFrame(object7)

# 添加新的列
# df3['food'] = '豆浆'
# print(df3)
# 添加新的列,如果city为beijing的为True
# df3['cap'] = df3['city'] == 'beijing'
# print(df3)

# 二维数据
# object8 = {
#     'beijing': {'2016': '100'},
#     'shanghai': {'2017': '200'}
# }
# df4 = DataFrame(object8)
# print(df4)
# print(df4.T)

# 还可以通过索引对数据进行排序
# object9 = Series([1,2,3,4],index=['a','b','c','d'])
# print(object9)
# print('=================')
# #在进行排序操作时，如果新加的索引本来不存在，值是NAN，也可以通过fill_value指定值
# object10 = object9.reindex(['d','c','b','a','e'],fill_value=0)
# print(object10)

# object11 = Series(['yello', 'blue', 'orange'], index=['0', '2', '4'])
# # print(object11)
# # print('=============')
# print(object11.reindex(range(6), method='ffill'))

# 如果值为空，就忽略
from numpy import nan as NA

# data = Series([1,NA,2])
# print(data)
# print(data.dropna())

data2 = DataFrame([[1, 2, 3], [1.1, NA, 3.3], [NA, NA, NA]])
# print(data2)
# print('==============')
# print(data2.dropna())

# 当全为缺失值的时候才忽略
# print(data2.dropna(how='all'))

# 当整列为缺失值时忽略
# data2[4] = NA
# print(data2)
# print('========')
# print(data2.dropna(axis=1, how='all'))

# 层次化索引
import numpy as  np

data3 = Series(np.random.rand(9),
               index=[['a', 'a', 'a', 'b', 'b', 'b', 'c', 'c', 'd'],
                      [1, 2, 3, 1, 2, 3, 1, 2, 2]])

print(data3)

print('=================')
#转换成DataFrame结构
print(data3.unstack())
#再转成Series数据
print(data3.unstack().stack())
