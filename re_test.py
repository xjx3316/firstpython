# 正则匹配
import re

# content1 = 'xujianxiong'
# content2 = '2017-1-1 12:02'
# content3 = '2018-1-1 12:03'

# a = re.compile('c[bcd]t')
# print(a.match('cat'))
# print(a.match('cbt'))
# print(a.match('cct'))
# print(a.match('cdt'))

# pattern = re.compile('\d{2}:\d{2}')
# result1 = re.sub(pattern, '', content1)
# result2 = re.sub(pattern, '', content2)
# result3 = re.sub(pattern, '', content3)
# print(result1, result2, result3)

# 匹配年月日
# 2018-10-25
# a = re.compile('\d{4}-\d{1,2}-\d{1,2}')
# # print(a.match('2018-10-25'))
# b = a.search(a,'我的生日是2018-10-25')
# print(b)
# string = '2018-10-25'
# string2 = '我的生日是2018-10-25'
# a = re.compile('(\d{4})-(\d{1,2})-(\d{1,2})')
#
# b= a.search(string2)
# print(b)
# year,month,day  = a.search(string2).groups()
# print('%s %s %s' %(year,month,day))

# b = a.match(string)
# print(b)
# year,month,day = a.match(string).groups()
# print('%s %s %s' %(year,month,day))

string1 = '123-456-789 #这是注释'
string2 = 's'
a = re.sub(r'#.*$','',string1)
print(a)
c = re.sub('\D','',a)
print(c)

# s = '123wohshi456'
# a = re.compile('\d')
# print(a.findall(s))
# re._compile()



