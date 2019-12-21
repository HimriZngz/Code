#  原链接：http://pic.yesky.com/c/6_60201.shtml


import requests
import os
import time
import re
from bs4 import BeautifulSoup


def has_a_and_has_span(tag):
    return tag.has_attr('a') and tag.has_attr('span')


def get_html(url):
    """ 进入初始页面，拿到全页内容 供Bs提取 """
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                            'Chrome/65.0.3314.0 Safari/537.36 SE 2.X MetaSr 1.0'}
    response = requests.get(url, headers=header)
    text = response.text
    return text


def get_main_html(url):
    """ 解析主页面，拿到每个小主题的链接以及标题 """
    html = get_html(url)

    # 准备一个空列表 装每个小主题的字典，字典里键是标题，值是链接
    main_list = []

    soup = BeautifulSoup(html, 'html.parser')
    div = soup.find_all('div', class_='mode_box')
    for item in div:
        dl_tag = item.dl
        print(dl_tag)
        # for dt_dd in dl_tag:
        #     link = dt_dd.dt.a['href']
        #     name = dt_dd.dd.a.get_text()
        #     page = dt_dd.dd.span.get_text()
        #     print(link, name, page)





    # 找一下有没有下一页，有的话，读出链接，准备下次打开(递归)，没有就不动
    next_page = soup.find_all('font')
    for i in next_page:
        #  判定链接里有没有下一页按钮，有的话拿到对应链接，准备递归打开读取
        if '下一页'in i.a.get_text():
            link = 'http://pic.yesky.com' + i.a['href']
            # get_main_html(link)


def go():
    url = 'http://pic.yesky.com/c/6_60201.shtml'
    get_main_html(url)


if __name__ == "__main__":
    go()
