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
    img_src = soup.find_all('img', src=re.compile('.image$'))

    for i in img_src:
        link = i['src']
        img_url.append(link)

    return img_url


def save_img(img_url):
    """ 依次打开图片的对应链接然后写入文件 """

    for img in img_url:
        filename = img.split('/')[-1].replace('.image', '.jpg')
        with open(filename, 'wb')as f:
            img_data = open_url(img).content    # .content返回的是bytes型也就是二进制的数据
            f.write(img_data)


def download(folder='./小甲鱼练习题辅助文档/056_ooxx'):
    """ 主程序 """

    os.mkdir(folder)
    os.chdir(folder)

    url = "https://bcy.net/coser/toppost100?type=newPeople&date=20191220"
    i = get_page(url)
    save_img(i)
    print('保存完毕')


if __name__ == "__main__":
    download()



