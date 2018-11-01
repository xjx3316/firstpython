from os import path

# print(path.abspath('.'))  # 获取当前目录的绝对路径
# print(path.abspath('..'))  # 获取上级目录的绝对路径
# print(path.exists('D:\develop2\python.exe'))  # 判断目录是否存在
# print(path.isdir('D:\develop2\python.exe'))  # 判断是否是文件夹
# print(path.isfile('D:\develop2\python.exe'))  # 判断是否是文件
# print(path.join(r'D:\develop2', 'abc'))  # 拼接路径
# print('==================================')
from pathlib import Path

print(Path('.').resolve())  # 获取当前目录的绝对路径
print(Path('..').resolve())  # 获取上级目录的绝对路径
print(Path('D:\develop2\python.exe').exists())  # 判断目录是否存在
print(Path('D:\develop2\python.exe').is_dir())  # 判断是否是文件夹
print(Path('D:\develop2\python.exe').is_file())  # 判断是否是文件
print(Path(r'D:\develop2', 'abc').joinpath())  # 拼接路径
# q = Path(r'D:\\develop2\aaa\bbb')
# Path.mkdir(q,parents=True) #当路径aaa不存在时，属性parents=True就可以自动创建aaa文件夹，然后再创建bbb文件夹
#
# Path.rmdir(q) #删除指定的目录
