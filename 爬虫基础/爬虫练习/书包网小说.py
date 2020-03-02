# 原链接：https://www.bookbao8.com/book/201909/21/id_XNjA2NjYz.html

'''
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
    link = root.xpath('/html/body/div[@class="wp b2 info_chapterlist"]/ul/li/a/@href')

    return link


def get_info(url):
    """拿到文章标题、作者、文章类型"""
    root = open_url(url)
    title = root.xpath('/html/body/div[5]/div[2]/div[2]/h1/text()')[0]
    author = root.xpath('/html/body/div[5]/div[2]/div[2]/p[1]/a/text()')[0]
    type = root.xpath('/html/body/div[5]/div[2]/div[2]/p[2]/a/text()')[0]
    info = [title, author, type]

    return info


def get_text(url):
    """依次打开每个章节的链接，拿到需要的文字，写入文件"""
    info = get_info(url)
    file_name = info[0]     # 文章标题作为文件名
    author = info[1]        # 作者
    leixing = info[2]       # 文章类型
    n = '\n'

    with open('《' + file_name + '》.txt', 'a', errors='ignore')as f:
        f.write('作者: ' + author + n)
        f.write('类型: ' + leixing + n)
        f.write('本文链接: ' + url + n)

        perfix = 'https://www.bookbao8.com'
        link_list = get_all_link(url)
        print('《%s》共有%d章' % (file_name, len(link_list)))

        for item in range(len(link_list)):
            # print('正在写入第%d章，总进度%.2f%%' % (item+1, ((item+1)/len(link_list))*100))
            time.sleep(0.5)
            link = perfix + link_list[item]
            root = open_url(link)

            chapter = root.xpath('/html/body/div[3]/div[2]/dl/dd[1]/h1/text()')
            paragraph = root.xpath('//dd[@id="contents"]/text()')
            if chapter:
                print('%s 正在写入中，全文总进度%.2f%%' % (chapter[0], ((item+1)/len(link_list))*100))
                f.write(n+n)
                f.write(chapter[0])
                f.write(n+n)
            else:
                print('错了 这篇没对')

            for i in range(len(paragraph)):
                f.write(paragraph[i])
                # f.write(n)

            # f.write(n)

    print('《%s》下载完毕' % file_name)


if __name__ == "__main__":


    # url = 'https://www.bookbao8.com/book/201909/21/id_XNjA2NjYz.html'
    url = 'https://www.bookbao8.com/book/201912/26/id_XNjE1OTI3.html'

    t1 = time.time()

    get_text(url)

    t2 = time.time()

    t = t2 - t1
    s = t % 60
    m = t // 60
    h = m // 60
    print('用时%d小时%d分%d秒' % (h, m, s))

    # d = h // 24
    # print('用时%d天%d小时%d分%d秒' % (d, h, m, s))

