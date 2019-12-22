#  原链接：http://pic.yesky.com/c/6_60201.shtml


import requests
import os
import time
import re
from bs4 import BeautifulSoup


def get_html(url):
    """ 进入初始页面，拿到全页内容 供Bs提取 """
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                            'Chrome/65.0.3314.0 Safari/537.36 SE 2.X MetaSr 1.0'}
    response = requests.get(url, headers=header)
    #  这里不用.text ，因为在读取图片的链接的时候方便直接调用这里的函数
    return response


def get_main_html(url):
    """ 解析主页面，拿到每个小主题的链接以及标题 """
    html = get_html(url).text

    # 准备一个空列表 装每个小主题的小列表
    main_list = []

    soup = BeautifulSoup(html, 'html.parser')
    div = soup.find('div', class_="mode_box")
    dl_tag = div.find_all('dl')
    for dl in dl_tag:
        # 此时的dl就是要找的dl标签，卧槽尼玛的，总算是拿到了
        name = dl.dd.a.get_text()
        link = dl.dd.a['href']
        page = dl.dd.span.get_text()
        page_num = re.findall(r'\d+', page)     # 返回的是像这样的数字：['5']
        each_info = [name, link, page_num]
        main_list.append(each_info)     # 把小列表加到大列表

    # 找一下有没有下一页，有的话，读出链接，准备下次打开
    next_page = soup.find_all('font')
    for i in next_page:
        #  判定链接里有没有下一页按钮，有的话拿到对应链接，准备递归打开读取
        if '下一页'in i.a.get_text():
            link = 'http://pic.yesky.com' + i.a['href']
            # get_main_html(link)
            print('当前位置还有下一页')

    return main_list


def get_img(url):
    """ 依次打开main_list里的全部链接，然后获取次级图片链接 """
    info_list = get_main_html(url)

    main_folder = '天极网图片'
    os.mkdir(main_folder)
    os.chdir(main_folder)

    for number in range(len(info_list)):
        print('总共有%s个栏目在下载' % len(info_list))
        name = info_list[number][0]        # 拿到主图的名称
        link = info_list[number][1]        # 拿到主图的链接
        page = info_list[number][2][0]     # 拿到主图的页数

        fu_name = link.split('.')[-2]      # 先把原本的副名拿到

        if page is 1:
            # 打开一次链接，找到图片链接，打开，存入
            print(name, '正在下载')
            photo = img_data(link)
            os.mkdir(name)
            os.chdir(name)
            with open('000.jpg', 'wb')as f:
                f.write(photo)
            os.chdir('..')
            print(name, '下载好了')

            time.sleep(1)

        else:
            # 把链接依次加入 _x 按次数打开链接
            os.mkdir(name)
            os.chdir(name)
            print(name, '有%s张正在下载' % int(page))
            for num in range(int(page)):
                photo = img_data(link)
                file_name = str(num) + '.jpg'
                with open(file_name, 'wb')as f:
                    f.write(photo)

                count = 2  # 第2页那个就是从_2开始的
                postfix = link.split('.')[-1]
                link = link.replace(link.split('.')[-2], fu_name + '_' + str(count))
                count += 1

            os.chdir('..')
            print(name, '下载好了')

            time.sleep(1)

    print('完毕')


def img_data(url):
    """ 打开图片的次级链接，获取img标签里的链接，打开链接，获取图片二进制数据并返回 """
    web = get_html(url).text
    soup = BeautifulSoup(web, 'html.parser')
    div_tag = soup.find('div', class_='l_effect_img_mid')
    # print(url)
    # print(div_tag)
    img_link = div_tag.a.img['src']      # 此处成功获取次级图片页面的图片单独链接
    img = get_html(img_link).content

    return img


def go():
    # url = 'http://pic.yesky.com/204/862108204_3.shtml'
    # img_data(url)

    url = 'http://pic.yesky.com/c/6_60201_1.shtml'
    get_img(url)


if __name__ == "__main__":
    go()
