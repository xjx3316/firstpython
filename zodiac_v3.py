chinese_zodiac = '鼠牛虎兔龙蛇马羊猴鸡狗猪'
zodiac_name = ('水瓶座', '双鱼座', '白羊座', '金牛座', '双子座', '巨蟹座',
               '狮子座', '处女座', '天秤座', '天蝎座', '射手座', '摩羯座')
zodiac_days = (
    (1, 20), (2, 19), (3, 21), (4, 21), (5, 21), (6, 22), (7, 23), (8, 23), (9, 23), (10, 23), (11, 23), (12, 23))

# cz_num = {}
# for i in chinese_zodiac:
#     cz_num[i] = 0
#使用字典推导式
cz_num = {i:0 for i in chinese_zodiac}

# z_num = {}
# for i in zodiac_name:
#     z_num[i] = 0
#使用字典推导式
z_num ={i:0 for i in zodiac_name}

while True:
    year = int(input("请输入年份"))
    month = int(input("请输入月份"))
    day = int(input("请输入日期"))

    y = 1900
    cz_name = chinese_zodiac[(year - y) % 12]  # 获取年份对应的属相
    cz_num[cz_name] += 1  # 对应的属相的数据+1

    zodiac_day = list(filter(lambda x: x <= (month, day), zodiac_days))  # 获取月和日期对应的zodiac_days
    z_name = zodiac_name[len(zodiac_day)]  # 通过zodiac_days获取对应的星座
    z_num[z_name] += 1  # 对应的星座的数据+1

    for each_key in cz_num.keys():
        print("生肖为 %s 出现的次数是 %s 次" % (each_key, cz_num[each_key]))
    for each_key in z_num.keys():
        print('星座为 %s 出现的次数是 %s 次' % (each_key, z_num[each_key]))
