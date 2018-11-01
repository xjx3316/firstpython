#读取人物名称
file_name = open('name.txt',encoding='UTF-8')
names = file_name.read()
list_names = names.split('|')
print(list_names)

#读取武器名称
file_weapon = open('weapon.txt',encoding='UTF-8')
i = 1
for line in file_weapon.readlines():
    if i % 2 == 1:
        print(line.strip('\n'))
    i+=1

#读取三国名著
file_sanguo = open('sanguo.txt',encoding='UTF-8')
print(file_sanguo.read().replace('\n',''))