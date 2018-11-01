import re


def find_item(hero):
    with open('sanguo.txt', encoding='UTF-8') as f:
        data = f.read().replace('\n', '')
        number = re.findall(hero, data)
        print('%s 出现的次数为 %s' % (hero, len(number)))
        return number


# 读取兵器信息
weapon_dict = {}
with open('weapon.txt', encoding='UTF-8') as f:
    i = 1
    for line in f.readlines():
        if i % 2 == 1:
            weapon = line.strip('\n')
        i += 1
        number = find_item(weapon)
        weapon_dict[weapon] = len(number)
    print('结果为 %s ' % weapon_dict)

# 读取人物的信息
name_dict = {}
with open('name.txt', encoding='UTF-8') as f:
    for line in f:
        names = line.split('|')
        for name in names:
            number = find_item(name)
            name_dict[name] = len(number)
    name_sorted = sorted(name_dict.items(), key=lambda iteam: iteam[1], reverse=True)
    print(name_sorted[0:10])
    # print('结果为 %s ' % name_dict)
