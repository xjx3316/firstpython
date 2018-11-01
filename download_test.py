import requests
import os

# url = "http://img.cnu.cc/uploads/images/flow/1810/07/b8b8b320f2a23b458f0cc58c741a4c54.jpg"
def down(url):
    root = "D:\pictureDownload//"
    path = root + url.split("/")[-1]
    try:
        if not os.path.exists(root):
            os.mkdir(root)
        if not os.path.exists(path):
            r = requests.get(url)
            r.raise_for_status()
        # 使用with语句可以不用自己手动关闭已经打开的文件流
            with open(path, "wb") as f:
                # 开始写文件，wb代表写二进制文件
                f.write(r.content)
                print("爬取完成")
        else:
            print("文件已存在")
    except Exception as e:
        print("爬取失败:" + str(e))

# down('http://img.cnu.cc/uploads/images/flow/1810/05/2d98c3c237003ddaa02d7ff8a4e23667.jpg')