# 异常
try:
    year = int(input("请输入年份"))
except ValueError as v:
    print(v)
finally:
    print('始终会执行')

try:
    a = 123
    a.append()
except Exception as e:
    print(e)
