import requests

url = "http://httpbin.org/post"
file = {'files': open('./03.bmp', 'rb')}
response = requests.post(url, files=file)
print(response.text)
