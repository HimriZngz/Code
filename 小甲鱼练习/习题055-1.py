import urllib.request as ur
import urllib.parse as up
import re
from bs4 import BeautifulSoup


word = input('输入关键词：')
keyword = up.urlencode({'word': word})
response = ur.urlopen('http://baike.baidu.com/search/word?%s' % keyword)
html = response.read()
soup = BeautifulSoup(html, 'html.parser')

for each in soup.find_all(href=re.compile(r'view')):
    contend = ''.join([each.text])
    print(contend)
    url2 = ''.join(['http://baike.baidu.com/', each['href']])
    print(url2)

    # response2 = ur.urlopen(url2)
    # html2 = response2.read()
    # soup2 = BeautifulSoup(html2, 'html.parser')
    # print(soup2.h2)


