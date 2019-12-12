# 1. 写一个登录豆瓣的客户端
# 这道题可能要难为大家了，因为需要 N 多你没学过的知识！
# 不过我也不打算让你断送希望，下边是一个可行的 Python 2 的代码片段，请修改为 Python 3 版本。


import http.cookiejar as hc
import re
import urllib.request as ur
import urllib.parse as up

loginurl = 'https://www.douban.com/accounts/login'
cookie = hc.CookieJar()
opener = ur.build_opener(ur.HTTPCookieProcessor)

params = {
    "form_email": "your email",
    "form_password": "your password",
    "source": "index_nav"  # 没有的话登录不成功
}

# 从首页提交登录
response = opener.open(loginurl, up.urlencode(params).encode('utf-8'))

# 验证成功跳转至登录页
if response.geturl() == "https://www.douban.com/accounts/login":
    html = response.read().decode()

    # 验证码图片地址
    imgurl = re.search('<img id="captcha_image" src="(.+?)" alt="captcha" class="captcha_image"/>', html)
    if imgurl:
        url = imgurl.group(1)
        # 将图片保存至同目录下
        res = ur.urlretrieve(url, 'v.jpg')
        # 获取captcha-id参数
        captcha = re.search('<input type="hidden" name="captcha-id" value="(.+?)"/>', html)

        if captcha:
            vcode = input('请输入图片上的验证码：')
            params["captcha-solution"] = vcode
            params["captcha-id"] = captcha.group(1)
            params["user_login"] = "登录"
            # 提交验证码验证
            response = opener.open(loginurl, up.urlencode(params).encode('utf-8'))
            ''' 登录成功跳转至首页 '''
            if response.geturl() == "http://www.douban.com/":
                print('login success ! ')
