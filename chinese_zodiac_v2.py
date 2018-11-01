# 根据年月日计算生肖和星座
# chinese_zodiac = '鼠牛虎兔龙蛇马羊猴鸡狗猪'
#
# year = int(input("请输入年份")) #input可以在控制台输入内容，int将内容转换为int类型
# zodiac_name = chinese_zodiac[(year - 1900) % 12]
# if zodiac_name == '马':
#     print("好马...")
#
# for cz in chinese_zodiac:
#     print(cz)
#
# for year in range(2010,2019):
#     print('%s 年的属相是 %s' %(year,chinese_zodiac[(year - 1900) % 12]))

number = 5
# while True:
#     print("a")
#     number = number + 1
#     if number > 10:
#         break
import time
while True:
    time.sleep(2)
    number = number + 1
    if number == 10:
        continue
    print(number)
