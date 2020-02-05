"""
运行失败，目标服务器积极拒绝
"""


import requests
import time
from lxml import etree


def open_url(url):
    """打开链接返回2进制文本网页"""
    proxies = {
        'https': 'https://127.0.0.1:9090',
        'http': 'http://127.0.0.1:9090'
    }
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0'}
    response = requests.get(url, headers=header, proxies=proxies, verify=False)
    text = etree.HTML(response.text)

    return text


def get_all_link(url):
    """拿到全部章节的链接列表"""
    root = open_url(url)
    link = root.xpath('//div[@class="figure_wrapper"]/img/@src')

    return link


def save_img(url):
    link = get_all_link(url)
    for i in link:
        print(i)



if __name__ == "__main__":
    url = 'https://telegra.ph/rioko%E5%87%89%E5%87%89%E5%AD%90---%E5%9C%A3%E8%AF%9E%E8%B4%9D%E5%B0%94%E6%B3%95%E6%96%AF%E7%89%B9-24P-12-24'
    save_img(url)