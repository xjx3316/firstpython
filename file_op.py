#文件的内建函数
#open():打开文件 read():输入  readline():输入一行
#seek():文件内移    write():输出  close():关闭文件
#'w'表示写入，‘r'表示读取,   'a'表示在原来的内容上继续写入
# tell()方法是获取当前指针位置
#seek(5,0) 文件内偏移指针 第一个参数表示偏移量，第二个参数 0:从开头开始;1:从当前位置开始;2:从结尾开始

#创建文件并且写入内容
# file = open('D:\sanguo.txt','w')
# file.write('诸葛亮')
# file.close()

#读取文件内容
# file2 = open('D:\sanguo.txt','r')
# print(file2.readline())
# file2.close()

#追加内容
# file3 = open('D:\sanguo.txt','a')
# file3.write('刘备')
# file3.close()

#读取一行
# file4 = open('D:\sanguo.txt','r')
# print(file4.readline())

#逐行读取
# file5 = open('D:\sanguo.txt','r')
# for f in file5.readlines():
#     print(f)
# file5.close()

#seek() 移动指针
# file6=open('D:\sanguo.txt','r')
# print('当前指针位置 %s' %(file6.tell())) #tell()方法是获取当前指针位置
# print('读取到的内容为 %s' %(file6.read(1)))
# print('当前指针位置 %s' %(file6.tell()))
# file6.seek(0)
# print('当前指针位置 %s' %(file6.tell()))
# file6.close()