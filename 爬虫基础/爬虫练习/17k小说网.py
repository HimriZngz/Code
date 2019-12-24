# 原链接：https://www.17k.com/list/2994136.html

'''
只能爬到前100个章节，后面的div标签没有捕捉到，还有登录甚至vip才可查看的部分
'''

import requests
import time
from lxml import etree


def open_url(url):
    """打开链接返回2进制文本网页"""
    header = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 '
                            '(KHTML, like Gecko) Chrome/65.0.3314.0 Safari/537.36 SE 2.X MetaSr 1.0'}
    response = requests.get(url, headers=header)
    text = etree.HTML(response.content)     # 用content转成2进制文本以便xpath获取文本时候不会转码错误

    return text


def get_all_link(url):
    """拿到全部章节的链接列表"""
    root = open_url(url)
    link = root.xpath('/html/body/div[5]/dl[2]/dd/a[@target="_blank"][contains(@href, "chapter")]/@href')

    return link


def get_info(url):
    """拿到文章标题、作者、作者的个人页面链接"""
    root = open_url(url)
    title = root.xpath('/html/body/div[5]/h1/text()')[0]
    author = root.xpath('/html/body/div[5]/div[@class="Author"]/a/text()')[0]
    author_link = 'https:' + root.xpath('/html/body/div[5]/div[@class="Author"]/a/@href')[0]
    info = [title, author, author_link]

    return info


# def time_goes(func):
#     def times():
#         t1 = time.time()
#         func()
#         t2 = time.time()
#         t = t2 - t1
#         s = t % 60
#         m = t // 60
#         h = m // 60
#         d = h // 24
#         print('用时%d天%d小时%d分%d秒' % (d, h, m, s))
#
#     return times
#
#
# @time_goes
def get_text(url):
    """依次打开每个章节的链接，拿到需要的文字，写入文件"""
    info = get_info(url)
    file_name = info[0]     # 文章标题作为文件名
    author = info[1]        # 作者
    author_link = info[2]   # 作者的个人链接
    n = '\n'*2

    with open('17K小说《' + file_name + '》.txt', 'a', errors='ignore')as f:
        f.write('作者个人页面————' + author_link + n)

        perfix = 'https://www.17k.com'
        link_list = get_all_link(url)
        print('《%s》共有%d章' % (file_name, len(link_list)))

        for item in range(len(link_list)):
            print('正在写入第%d章，总进度%.2f%%' % (item+1, ((item+1)/len(link_list))*100))
            time.sleep(1)
            link = perfix + link_list[item]
            # print(link)
            root = open_url(link)
            chapter = root.xpath('//div[@class="readAreaBox content"]/h1/text()')[0]
            author = root.xpath('//div[@class="chapter_update_time"]/text()')[0]
            paragraph = root.xpath('//div[@class="p"]/p/text()')
            say_1 = root.xpath('//div[@class="author-say"]/strong/text()')
            say_2 = root.xpath('//div[@class="author-say"]/text()')

            f.write(n)
            f.write(chapter)
            f.write(n)
            f.write(author.strip())
            f.write(n)

            for i in range(len(paragraph)-2):
                f.write(paragraph[i])
                f.write('\n')

            f.write(n)

            if say_1 and say_2:
                f.write(say_1[0])
                f.write(say_2[1].strip())
            f.write(n)

    print('《%s》下载完毕' % file_name)


if __name__ == "__main__":

    # url = 'https://www.17k.com/list/2994136.html'
    # url = 'https://www.17k.com/list/3054274.html'
    url = 'https://www.17k.com/list/1601685.html'
    t1 = time.time()
    get_text(url)
    t2 = time.time()
    t = t2 - t1
    s = t % 60
    m = t // 60
    h = m // 60
    d = h // 24
    print('用时%d天%d小时%d分%d秒' % (d, h, m, s))

