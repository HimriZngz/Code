#  编写一个程序，统计当前目录下每个文件类型的文件数

import os

os.chdir('E:/杂项')

d = dict()

for item in os.listdir(os.curdir):
    if os.path.isdir(item):
        d.setdefault('文件夹', 0)
        d['文件夹'] += 1
    else:
        (name, ext) = os.path.splitext(item)
        d.setdefault(ext, 0)
        d[ext] += 1

for key in d.keys():
    print('该文件夹下 %s 的文件有%d个' % (key, d[key]))

