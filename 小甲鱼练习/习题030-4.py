#  编写一个程序，用户输入关键字，查找当前文件夹内
# （如果当前文件夹内包含文件夹，则进入文件夹继续搜索）所有含有该关键字的文本文件（.txt后缀）
#  要求显示该文件所在的位置以及关键字在文件中的具体位置（第几行第几个字符）

import os


def search_text_in_file(file_dir, text):
    os.chdir(file_dir)

    for item in os.listdir(os.curdir):
        if os.path.splitext(item)[1] == '.txt':
            with open(os.getcwd() + os.sep + item, 'r')as f:
                for i in f.read():
                    if i == text:
                        print('%s在%s文件的第%s个字符处' % (text, os.getcwd() + os.sep + item, f.tell()))

        if os.path.isdir(item):
            search_text_in_file(item, text)
            os.chdir(os.pardir)


file_dir = input('要查询的文件的路径：')
text = input('要查询的文本是：')

search_text_in_file(file_dir, text)
