import re

string = r'<div class="grid-item work-thumbnail"><a href="http://www.cnu.cc/works/306635" class="thumbnail" target="_blank"><div class="title">余昼</div><div class="author">拍照的古德卡特</div><img src="http://img.cnu.cc/uploads/images/flow/1810/10/6f61750858f837e8b144ec957a953ac7.jpg?width=4000&amp;height=2964" alt=" 余昼     "></a></div>'

match = re.compile(r'<img src="(.*?)width.*?alt="(.*?)"></a', re.S)
result = re.findall(match, string)
print(result)
for i in result:
    url, name = i
    print(re.sub('\?', '', url), re.sub('/s', '', name))
