# 列表推导式
# 计算从1到10的所有偶数的2次幂

# 第一种方式
alist = []  # 定义一个存放2次幂的列表
for i in range(1, 11):
    if i % 2 == 0:
        alist.append(i * i)
print(alist)

# 第二种方式,使用列表推导式
blist = [i * i for i in range(1, 11) if i % 2 == 0]
print(blist)
