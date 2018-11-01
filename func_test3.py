# 上下文管理器
try:
    file = open('name.txt', encoding='UTF-8')
    for i in file:
        print(i)
except Exception as e:
    print(e)
finally:
    file.close()

#使用上下文管理器
with open('name.txt', encoding='UTF-8') as f:
    for i in f:
        print(i)
