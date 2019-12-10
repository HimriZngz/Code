# 0. 下载鱼C工作室首页（http://www.fishc.com），并打印前三百个字节。


import urllib.request as ur

response = ur.urlopen("http://www.fishc.com")
html = response.read()

print(html[:300])
