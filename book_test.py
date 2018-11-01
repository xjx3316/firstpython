# 下载页面中的图片
import requests
from bs4 import BeautifulSoup

url = 'https://read.qidian.com/chapter/GVTb_Xs_43QPfAGvZBg6QQ2/i2EvUJ_HeQ9p4rPq4Fd4KQ2'


def getPicture(url):
    content = requests.get(url).text
    soup = BeautifulSoup(content, 'lxml')
    book_div = soup.find('div', class_='read-content j_readContent')
    print(book_div)
    text = str(book_div)
    write(text)

def write(obj):
    file = open('D:\\xiaoshuo.html', 'w')
    file.write(obj)
    file.close()

getPicture(url)
