import requests
from lxml import etree

url = 'http://photo.chengdu.cn/?g=Square&tag=17'

header = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 '
                        '(KHTML, like Gecko) Chrome/65.0.3314.0 Safari/537.36 SE 2.X MetaSr 1.0'}

response = requests.get(url, headers=header)

html = response.text

root = etree.HTML(html)


a = root.xpath('//a[@class="name f-trans"]/@href')
for i in a:
    print(i)