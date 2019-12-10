# 2. 写一个程序，依次访问文件中指定的站点，并将每个站点返回的内容依次存放到不同的文件中。


import urllib.request as ur
import os
import chardet

os.chdir(os.curdir)

with open('./小甲鱼练习题辅助文档/习题053/urls.txt', 'r')as f:
    file = f.readlines()

    for site in file:
        # strip() 默认删除字符前后的\n
        site = site.strip()

        # 以域名的 . 作为分隔符，把主名提出来当下面要写的文件名
        count = site.split('.')[1]
        file_path = './小甲鱼练习题辅助文档/习题053/urls_' + count + '.txt'

        # 开始打开指定地址的网页
        response = ur.urlopen(site)

        # 获取该网页的编码格式
        # encode = chardet.detect(response.read())
        # encode_encode = encode['encoding']
        """
        这里用识别的编码来解码会返回418错误 所以注释掉
        """

        # 读一下获取的response，然后以原编码格式解码，准备写入txt
        html = response.read().decode('utf-8')

        with open(file_path, 'w', errors='ignore')as e:
            # 写入txt，编码有错误忽略 ↑↑↑↑↑↑↑
            e.write(html)


"""
参考答案：

import urllib.request
import chardet

def main():
    i = 0
    
    with open("urls.txt", "r") as f:
        # 读取待访问的网址
        # 由于urls.txt每一行一个URL
        # 所以按换行符'\n'分割
        urls = f.read().splitlines()
        
    for each_url in urls:
        response = urllib.request.urlopen(each_url)
        html = response.read()

        # 识别网页编码
        encode = chardet.detect(html)['encoding']
        if encode == 'GB2312':
            encode = 'GBK'
        
        i += 1
        filename = "url_%d.txt" % i

        with open(filename, "w", encoding=encode) as each_file:
            each_file.write(html.decode(encode, "ignore"))

if __name__ == "__main__":
    main()

"""