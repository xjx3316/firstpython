from urllib import request, parse

# url = 'http://www.baidu.com'
# data = request.urlopen(url, timeout=2)
# print(data.read().decode('UTF-8'))

url = 'http://v3boss.docker.sspaas.net/project/queryBasicopration'
req = request.Request(url=url,method='GET')
#参数要进行编码
# data = bytes(parse.urlencode({'phone': '18533739365', 'password': 'xjx123456'}),encoding='utf-8')
try:
    response_data = request.urlopen(req, timeout=1)
    print(response_data.read().decode('utf-8'))
except Exception as e:
    print('超时')
