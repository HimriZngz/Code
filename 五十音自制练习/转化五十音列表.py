import os

os.chdir(os.curdir)

all_list = []

with open('50y.txt', 'r', encoding='utf-8', errors='ignore')as f, open('50yin.txt', 'w')as e:
    for i in f.readlines():
        a = i.split()
        all_list.append(a)
    for x in all_list:
        e.write(str(x) + ',\n')
    # e.seek(0, 0)
    # e.write('[')
    # e.seek(2, 0)
    # e.write(']')

print(all_list)
