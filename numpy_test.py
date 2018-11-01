import numpy as np

# #定义数据
# array1 = np.array([1, 2, 3])
# array2 = np.array([1.1, 2.3, 4.5])
# #查看数据类型
# print(array1.dtype)
# print(array2.dtype)
# #做运算
# print(array1 + array2)
# print(array1 - array2)
# print(array1 * array2)
# print(array1 / array2)
# print(array1 % array2)
# print(array2 * 10)
# print('================')
# #将二维数组转换为np的二维矩阵
# data = [[1,2,3],[4,5,6]]
# array3 = np.array(data)
# print(array3)
# print('=======================')
# print(np.zeros(5))
# print(np.zeros((2,3)))
# print('====================')
# print(np.ones((2,3,4)))#三维

array4 = np.arange(10)
# print(array4)
# print(array4[2])  # 获取下标为2的数据
# print(array4[2:5])  # 获取下标为2到5的数据
# array4[5:8] = 10  # 将下标为5,6,7的数据改为10
# print(array4)
#如果不想改变原来数据的值，可以用复制的方法
copy_array4 = array4.copy()
print(copy_array4)
copy_array4[2:4] = 99
print(array4)
print(copy_array4)