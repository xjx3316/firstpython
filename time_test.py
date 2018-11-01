# import time
#
# print(time.time())
# print(time.localtime())
# print(time.strftime('%Y-%m-%d %H:%M:%S')) #获取当前时间
# print(time.strptime('2018-10-26 09:54:42','%Y-%m-%d %H:%M:%S'))

# import datetime
# print(datetime.datetime.now()) #获取当前时间
# delta = datetime.timedelta(minutes=-20) #获取分钟的增量
# print(datetime.datetime.now()+delta) #获取当前时间的增量
# #获取指定的时间的增量
# delta2 = datetime.timedelta(days=10)
# one_day=datetime.datetime(2018,10,26,10,16,25)#获取指定的时间
# print(one_day+delta2)#获取2018-10-26 10:16:25的10天以后的日期

import random

print(random.randint(1, 50))  # 获取1到50中的随机数
print(random.randrange(1, 5))
print(random.choice(('ab', 'cd', 'e')))
print(random.choices(('ab', 'cd', 'e')))
