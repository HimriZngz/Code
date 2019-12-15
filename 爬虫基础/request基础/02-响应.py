import requests

'''
response = requests.get("http://www.baidu.com")
print('打印请求页面的状态码:', response.status_code, type(response.status_code))
print('打印请求网址的header信息:', response.headers, type(response.headers))
print('打印请求网址的cookie信息:', response.cookies, type(response.cookies))
print('打印请求网址的地址:', response.url, type(response.url))
print('打印请求网页的历史记录(列表的形式):', response.history, type(response.history))
'''


# 使用request内置的字母判断状态码
response = requests.get("http://www.jianshu.com/404.html")
# 如果返回的是非正常的就打印404
if response.status_code != requests.codes.ok:
    print('404')


# 如果页面状态码是正常的(即200)就打印200
response2 = requests.get("http://www.baidu.com")
if response2.status_code == 200:
    print('200')
