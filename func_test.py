# def fun(a, b, c):
#     print('a=%s' % a)
#     print('b=%s' % b)
#     print('c=%s' % c)
#
# # 调用函数时的几种方式 1.按照参数顺序；2.参数名对应
# fun(1, 2, 3)
# fun(1, c=3, b=2)
#
# # ============================================================
# def fun2(first, *other):
#     print('参数的个数为 %s' %(1 + len(other)))
# #first参数必传，other为其他参数
# fun2(123,456,789)

# var = 1
# def fun3():
#     global var
#     var = 2
#     print(var)
#
# fun3()
# print(var)

# list = [1,2,3,4]
# for i in list:
#     print(i)
# #===================
# it = iter(list)
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))

# def frange(start, end, step):
#     x = start
#     while x < end:
#         yield x
#         # print('haha %s' % x)
#         x += step
#
#
# for i in frange(10, 20, 0.5):
#     print('i %s' % i)

# print(list(filter(lambda x: x > 5, range(1, 10))))
# print(list(map(lambda x,y,z:x+y+z,[1,2,3],[4,5,6],(7,8,9))))
# ===============================================
from functools import reduce

# n = 3
# print(reduce(lambda x, y: x * y, range(1, n + 1)))
# 阶乘的迭代实现
# def fun(x):
#     y = x
#     for i in range(1,x):
#         y = i * y
#     return y
# 阶乘的递归实现
# def fun(x):
#     if x == 1:
#         return 1;
#     else:
#         y = x * fun(x - 1)
#         return y
# print(fun(5))
# =================================================
# from functools import reduce
# print(reduce(lambda x,y:x+y,(1,2,3),4))

# print(list(zip([1,2,3],[4,5,6],[7,8,9])))
# a ={'a':1,'b':2}
# print(dict(zip(a.values(),a.keys())))

# # 计算两个数值的和
# def fun():
#     a = 1
#     b = 2
#     return a + b
#
#
# def fun2(a):
#     def fun3(b):
#         return a + b
#     return fun3
#
# print(fun())
# #调用闭包函数
# a = fun2(1)
# print(a(2))
# #或者这样调用
# print(fun2(1)(2))
#
# #写fun3是对函数的引用
# #写fun3()是对函数的调用

# 闭包实现计数器
# def count():
#     a = [0]
#
#     def add():
#         a[0] += 1
#         return a[0]
#
#     return add
#
#
# c = count()
# print(c())
# print(c())
# print(c())

# def cal(a, b, x):
#     return a * x + b
#
# def func(a,b):
#     def func2(x):
#         return a * x + b
#     return func2
#
# print(cal(1,2,3))
# print(func(1,2)(3))

#装饰器
#计算一个函数执行的时间
import time
def timer(func):
    def timer2():
        start = time.time()
        func()
        end = time.time()
        return end-start
    return timer2

@timer
def func():
    time.sleep(3)

print(func())

# start = time.time()
# func()
# end = time.time()
# print(end-start)


