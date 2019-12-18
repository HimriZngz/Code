# 0. 编写一个爬虫，爬百度百科“网络爬虫”的词条（链接 -> http://baike.baidu.com/view/284853.htm）
# 将所有包含“view”的链接打印出来


from bs4 import BeautifulSoup
import requests
import urllib.request as UR
import re


def go():
    url = 'http://baike.baidu.com/view/284853.htm'
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, '
                            'like Gecko) Chrome/65.0.3314.0 Safari/537.36 SE 2.X MetaSr 1.0'}

    # response = requests.get(url, headers=header).text
    response = UR.urlopen(url).read()

    soup = BeautifulSoup(response, "html.parser")

    links = soup.find_all(href=re.compile(r'view'))
    for link in links:
        print(link.text, "->", ''.join(["http://www.baike.baidu.com", link['href']]))


if __name__ == "__main__":
    go()
