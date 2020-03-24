import os
import uuid
import requests
import time
import tkinter.filedialog as tf


def download(url):
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                            'Chrome/65.0.3314.0 Safari/537.36 SE 2.X MetaSr 1.0'}
    response = requests.get(url, headers=header).content
    name = str(uuid.uuid4()) + '.jpg'
    with open(name, 'wb') as f:
        f.write(response)
        print(name, '\t已下载完成')


# 选择文件
path_ = tf.askopenfilename()
# 准备磁盘地址
# desktop = 'C:/Users/Estonteco/Desktop'
desktop = 'E:/Pic/bcy/'
# 准备文件夹名
folder = path_.split('/')[-1].split('.')[0]
# 合成文件夹名
position = desktop + folder
# 尝试创建文件夹
if os.path.exists(position):
    print('文件夹已存在，看看是不是下载过了')
    time.sleep(3)
else:
    os.mkdir(position)
    # 进入文件夹
    os.chdir(position)
    print('保存在：', position)
    # 开始遍历下载
    with open(path_)as f:
        links = f.readlines()
        print('共%s个' % len(links))
        for url in links:
            download(url)
            time.sleep(0.5)

        print('全部下载完成，程序自动关闭')
        time.sleep(1)
