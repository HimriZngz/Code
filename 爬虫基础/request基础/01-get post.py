import requests

# get方式
'''
url = "http://httpbin.org/get"
data = {'name': 'zhangsan', 'age': '25'}
response = requests.get(url, params=data)
print(response.url)
print(response.text)
'''

# post方式
# '''
url = "http://httpbin.org/post"
data = {'name': 'zhangsan', 'age': '25'}
response = requests.post(url, data=data)
print(response.url)
print(response.text)
# '''


# 带header访问逼乎首页
'''
url = "https://www.zhihu.com"
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3314.0 Safari/537.36 SE 2.X MetaSr 1.0'}
response = requests.get(url, headers=header)
print(response.text)
'''