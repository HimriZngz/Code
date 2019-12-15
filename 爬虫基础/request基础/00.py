#  本文网址：https://www.cnblogs.com/lei0213/p/6957508.html

import requests

response = requests.get("https://www.baidu.com")
print(type(response))
print(response.status_code)     # 状态码 200即为正常
# print(response.text)    # 网页的2进制字符串
print(type(response.text))

response.encoding = "utf-8"
# print(response.text)    # 此时，网页内容已编码为utf-8

print(response.cookies)

print(response.content.decode("utf-8"))
