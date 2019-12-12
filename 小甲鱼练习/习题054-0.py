# 0. 配合 EasyGui，给“下载一只猫“的代码增加互动：
#    让用户输入尺寸；
#    如果用户不输入尺寸，那么按默认宽400，高600下载喵；
#    让用户指定保存位置。


import easygui as Eg
import urllib.request as Ur
import os
import time


def user_in():
    e = Eg.multenterbox(msg='请输入要下载的图片尺寸', title='下载一只喵', fields=('宽：', '高：'), values=(400, 600))
    #  返回的e是一个宽高的list
    return e


def choice_save():
    f = Eg.diropenbox(msg='请选择存放喵的位置', title='随便选', default=os.curdir)
    #  返回的f是一个文件夹位置的字符串
    return f


def get_data():
    #  通过Eg输入获得宽高
    pic = user_in()
    width = pic[0]
    heigth = pic[1]
    #  把宽高带入到链接进去，读出byte数据
    url = 'http://placekitten.com/' + width + '/' + heigth
    response = Ur.urlopen(url)
    data = response.read()
    return data


def save():
    #  加载数据要费点时间，打印个提示
    print('获取数据中，请等待...')
    data = get_data()
    folder = choice_save()
    #  用时间戳来给文件命名，保证绝不会出现重名
    path = folder + '/kitten_' + str(time.time()) +'.jpg'
    with open(path, 'wb')as f:
        try:
            f.write(data)
        except IOError:
            Eg.msgbox('出错了，没存起')
        else:
            Eg.msgbox('保存完毕')


if __name__ == "__main__":
    save()
