from bs4 import BeautifulSoup
import requests

html = requests.get('http://www.cnu.cc/discoveryPage/hot-人像').text
soup = BeautifulSoup(html,'lxml') # 将网页内容导入BeautifulSoup中

print(soup.prettify()) #将html页面代码格式化
print(soup.title) #找到title标签
print(soup.title.text) #获取title标签的内容
print(soup.a) #找到第一个a标签
print(soup.find_all('a')) #找到所有a标签
print(soup.a.div['id']) #获取a标签下的div标签下的id
print(soup.find(id='recommendForm')) #获取id为recommendForm的标签
print(soup.get_text)# 找到所有的文本内容