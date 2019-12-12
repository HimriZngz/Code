# 1. 写一个程序，检测指定 URL 的编码。


import urllib.request as ur
import chardet


def detect():
    url = input('请输入URL：')

    response = ur.urlopen(url)
    encode = chardet.detect(response.read())    # detect返回的是一个字典，下面例子

    print('该网页使用的编码是:%s' % encode['encoding'])


if __name__ == '__main__':
    detect()


"""
chardet 模块用法：

非常简单，使用该模块的 detect() 函数即可：

import urllib.request
response = urllib.request.urlopen("http://bbs.fishc.com").read()
import chardet
chardet.detect(response)
{'confidence': 0.99, 'encoding': 'GB2312'}

confidence 是可信度的意思……

0.99 就是 99% 确定是 'GB2312'！


"""