import requests
import re
from PIL import Image
from io import BytesIO
import download_test as dt

# url = 'http://v3boss.docker.sspaas.net/project/queryBasicopration'
# response=requests.get(url)
# print(response.text)
# print('=========================')
# print(response.json())

content = requests.get('http://www.cnu.cc/discoveryPage/hot-人像').text
print(content)

# match = re.compile(r'<a href="(.*?)".*?title">(.*?)</div>',re.S)
# result = re.findall(match,content)

match = re.compile(r'title">(.*?)</div>.*?<img src="(.*?)width',re.S)
result = re.findall(match,content)

# print(result)
for i in result:
    name,url=i
    # print(re.sub('\s','',name),re.sub('\?','',url))
    # 将图片显示出来
    dt.down(re.sub('\?','',url))
    # response = requests.get(url)
    # image = Image.open(BytesIO(response.content))
    # image.show()