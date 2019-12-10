# 2. 写一个程序，依次访问文件中指定的站点，并将每个站点返回的内容依次存放到不同的文件中。


import urllib.request as ur
import os


with open('./小甲鱼练习题辅助文档/习题053/urls.txt', 'r')as f:
    file = f.readline()

