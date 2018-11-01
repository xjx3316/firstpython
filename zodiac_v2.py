zodiac_name = ('水瓶座', '双鱼座', '白羊座', '金牛座', '双子座', '巨蟹座',
               '狮子座', '处女座', '天秤座', '天蝎座', '射手座', '摩羯座')
zodiac_days = (
    (1, 20), (2, 19), (3, 21), (4, 21), (5, 21), (6, 22), (7, 23), (8, 23), (9, 23), (10, 23), (11, 23), (12, 23))

month = int(input("请输入月份"))
day = int(input("请输入几号"))
md = (month, day)

for zd in range(len(zodiac_days)):
    if zodiac_days[zd] >= md:
        print(zodiac_name[zd])
        break
    elif month == 12 and day > 23:
        print(zodiac_name[0])
        break
n = 0
while zodiac_days[n] <= md:
    if month == 12 and day > 23:
        break
    n += 1
print(zodiac_name[n])

# (month, day) = (9, 20)
# zodiac_day = filter(lambda x: x <= (month, day), zodiac_days)
# zodiac_len = len(list(zodiac_day)) % 12
# print(zodiac_name[zodiac_len])
