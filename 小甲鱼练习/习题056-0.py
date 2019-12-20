# 煎蛋网爬点图片
# http://jandan.net/ooxx

import requests
import os
import re
from bs4 import BeautifulSoup


def open_url(url):
    """ 预先写出(打开网页并返回未编码的网页资源的)打开动作 """

    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 '
                            '(KHTML, like Gecko) Chrome/65.0.3314.0 Safari/537.36 SE 2.X MetaSr 1.0'}
    response = requests.get(url, headers=header)
    return response


def get_page(url):
    """然后打开指定的网页并搜索需要的图片的链接"""

    img_url = []
    html = open_url(url).text
    soup = BeautifulSoup(html, 'html.parser')
    # 找到 有以.jpg结尾的值的 src属性 的 img标签
    img_src = soup.find_all('img', src=re.compile('.jpg$'))

    for i in img_src:
        # 此刻的i的类型是 <class 'bs4.element.Tag'>  它的内容是这样的：
        # <img referrerpolicy="no-referrer" src="//wx2.sinaimg.cn/mw600/0076BSS5ly1ga2h0y8fjwj318z0u0n22.jpg"/>

        # 因此要分离出需要的链接来

        # 通过字典键值获得src的值，然后加上前缀http:
        link = 'http:' + i['src']
        # 此刻link就成了能直接访问的图片链接：
        # http://wx2.sinaimg.cn/mw600/0076BSS5ly1ga2h0y8fjwj318z0u0n22.jpg

        img_url.append(link)

    return img_url


def get_next_page(url):
    pass


def find_img(url):
    pass


def save_img(img_url):
    """ 依次打开图片的对应链接然后写入文件 """

    for img in img_url:
        filename = img.split('/')[-1]
        with open(filename, 'wb')as f:
            img_data = open_url(img).content    # .content返回的是bytes型也就是二进制的数据
            f.write(img_data)


def download(folder='./小甲鱼练习题辅助文档/056_ooxx'):
    """ 主程序 """

    os.mkdir(folder)
    os.chdir(folder)

    url = "http://jandan.net/ooxx"
    i = get_page(url)
    save_img(i)
    print('保存完毕')


if __name__ == "__main__":
    download()
