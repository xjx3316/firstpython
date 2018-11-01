#下载页面中的标题
import requests
from bs4 import BeautifulSoup

content = requests.get('http://www.infoq.com/cn/news').text
soup = BeautifulSoup(content, 'lxml')
div_content = soup.find_all('div', class_='news_type_block')
for title_href in div_content:
    print([title.get('title') for title in title_href.find_all('a') if title.get('title')]) # 列表推导式
    # lable_a = title_href.find_all('a')
    # for title in lable_a:
    #     if title.get('title'):
    #         print(title.get('title'))