import requests
from lxml import etree


def open_url(url):
    header = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:56.0) Gecko/20100101 Firefox/56.0'}
    response = requests.get(url, headers=header)
    web_text = etree.HTML(response.content)

    return web_text


def get_text(url):
    response = open_url(url)

    link = response.xpath('//div[@class="item game_right_dirk"]/div/p/a/@href')
    title = response.xpath('//div[@class="item game_right_dirk"]/div/p/a/text()')
    platform = response.xpath('//div[@class="item game_right_dirk"]/div/div/span[@class="source2"]/text()')

    # print(link)
    # print(title)

    tv_list = []
    for num in range(len(link)):
        l_num = (link[num].split('/')[-1]).split('?')[0]
        tv_list.append(platform[num] + ' ' + title[num] + ' ' + l_num)
    # print(tv_list)

    return tv_list


def save(url):
    text = get_text(url)
    with open('狗仔直播地址.txt', 'a+')as f:
        for item in text:
            try:
                f.write(item + '\n')
                print('写入完成')
            except UnicodeEncodeError as E:
                print('错误:', item, '\n', E)
    # for i in text:
    #     print(i)


def get_url():
    url = 'https://zhibo.sogou.com/search.whtml?query=影视&page='

    for i in range(1, 15):
        url_num = url + str(i)
        # https://zhibo.sogou.com/search.whtml?query=影视&page=1
        save(url_num)


if __name__ == "__main__":

    get_url()
