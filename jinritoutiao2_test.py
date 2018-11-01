# 下载页面中的图片
import requests
from bs4 import BeautifulSoup
import download_test as dt


url = 'http://www.infoq.com/cn/presentations/'
def getPicture(url):
    content = requests.get(url).text
    soup = BeautifulSoup(content,'lxml')
    # print(soup)
    targ_div = soup.find_all('div',class_='news_type_video')
    for img in targ_div:
        src = img.img['src']
        dt.down(src)

#分页下载
def page(url):
    j = 1
    for i in range(0,37,12):
        print('第 %s 页' %j)
        getPicture(url+str(i))
        j+=1

page(url)
