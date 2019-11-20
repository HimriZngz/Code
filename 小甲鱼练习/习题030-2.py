#  编写一个程序，用户输入文件名以及开始搜索的路径，搜索该文件是否存在。如遇到文件夹，则进入文件夹继续搜索

import os


def search_in_disk(local_dir, aim_file):
    os.chdir(local_dir)    # 切换执行目录到目标目录
    for item in os.listdir(os.curdir):
        if item == aim_file:
            print(os.getcwd() + os.sep + item)

        if os.path.isdir(item):     # 查找文件夹
            search_in_disk(item, aim_file)     # 递归调用
            os.chdir(os.pardir)     # 递归后返回上一级目录


local_dir = input('请输入待查找的初始目录(如：D:/A/B)：')
aim_file = input('请输入待查找的目标文件(如：File.ext)：')
print('文件查找结果：\n')

search_in_disk(local_dir, aim_file)
