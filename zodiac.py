# zodiac_name = ('水瓶座', '双鱼座', '白羊座', '金牛座', '双子座', '巨蟹座',
#                '狮子座', '处女座', '天秤座', '天蝎座', '射手座', '摩羯座')
# zodiac_days = (
#     (1, 20), (2, 19), (3, 21), (4, 21), (5, 21), (6, 22), (7, 23), (8, 23), (9, 23), (10, 23), (11, 23), (12, 23))
#
# print(zodiac_days)
# print(zodiac_name)
#
# (month, day) = (9, 20)
# zodiac_day = filter(lambda x: x <= (month, day), zodiac_days)
# # print(zodiac_name[len(list(zodiac_day))])
#
# zodiac_len = len(list(zodiac_day)) % 12
# print(zodiac_name[zodiac_len])

a_list=['abc','xjx']
print(a_list)
a_list.append('xjs')
print(a_list)
a_list.remove('abc')
print(a_list.remove('abc'))