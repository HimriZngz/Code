#  编写一个程序，计算当前文件夹下所有文件的大小

import os

os.chdir('E:/杂项')

for item in os.listdir(os.curdir):
    if os.path.isfile(item):
        print('文件[ %s ]的大小为%sBytes' % (os.path.split(item)[1], os.path.getsize(item)))
