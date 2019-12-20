# 豆瓣电影top250
# https://movie.douban.com/top250?start=0


import requests
import os
import re
from bs4 import BeautifulSoup


def open_url(url):
    """ 打开链接的动作 """

    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 '
                            '(KHTML, like Gecko) Chrome/65.0.3314.0 Safari/537.36 SE 2.X MetaSr 1.0'}
    response = requests.get(url, headers=header)
    return response.text


def get_text(url):
    """ 找需要的标签的文本 """

    html = open_url(url)
    soup = BeautifulSoup(html, 'html.parser')
    movie = []  # 拿来存全部的信息

    li = soup.find_all('div', class_='item')
    # 找到全部的class为item的li标签，然后迭代进行内容获取
    for i in li:
        info = []   # 拿来存一部的信息
        rank = i.find('em').get_text() + '\n'
        # 获取排名
        title = i.find('span', class_='title').get_text() + '\n'
        # 获取片名
        staff = i.find('p', class_='').get_text().strip() + '\n'
        # 获取职员表
        rate = i.find('span', class_='rating_num').get_text() + '\n'
        # 获取得分
        sentence = i.find('span', class_='inq').get_text() + '\n'
        # 获取精华影评
        tag_a = i.find('a', href=re.compile('^https://movie.douban.com/subject.'))
        link = tag_a['href'] + '\n'
        # 获取链接

        info.extend([rank, title, staff, rate, sentence, link])
        movie.append(info)

    return movie


def write(url):
    """ 把爬到的文本写进txt """
    os.chdir(os.curdir)
    file = './小甲鱼练习题辅助文档/习题056爬豆瓣/'
    if not os.path.exists(file):
        # 得预先生成文件夹，否则报错
        os.mkdir(file)

    text = get_text(url)
    for i in range(25):
        # 把全部信息写入txt
        with open(file + 'movie.txt', 'a', encoding='utf-8')as f:
            f.writelines(text[i])
            f.write('\n'*2)


def go():
    p = 0

    # 每页25个，共10页所以每次+25，主要是网页是以0开始的，25递增
    while p <= 225:
        url = 'https://movie.douban.com/top250?start=' + str(p)
        write(url)

        p += 25
    print('弄好了')


if __name__ == "__main__":
    go()
