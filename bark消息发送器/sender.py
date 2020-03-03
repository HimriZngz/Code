import tkinter as tk
import requests
from tkinter import messagebox as msg


def get_api():
    with open('api.txt', 'r')as f:
        api = f.read()

        return api


def call_back():
    sentences = text.get('0.0', 'end')
    word = sentences
    api = get_api()
    url = api + word

    header = {
        'User-Agent': 'Mozilla/5.0 (Android 5.1; Mobile; rv:45.0) Gecko/45.0 Firefox/45.0'}
    response = requests.get(url, headers=header)

    if response.status_code == 200:
        msg.showinfo(title='', message='发送成功')
        text.delete('1.0', 'end')


window = tk.Tk()

# 获取屏幕大小并让窗口居中显示
screen_width = screen_height = window.maxsize()
window_width = 350
window_height = 140
x = (screen_width[0] - window_width) / 2
y = (screen_height[-1] - window_height) / 2
window.geometry('%dx%d+%d+%d' % (window_width, window_height, x, y))

# 此调用方法会禁止根窗体改变大小
window.resizable(False, False)

# 清除边框
window.overrideredirect(True)

text = tk.Text(window, highlightcolor='red', highlightthickness=1, font=('楷体', 15))
text.place(width=340, height=80, x=5, y=5)

send = tk.Button(window, text='发送', width=8, font=('黑体', 13), command=call_back)
send.place(x=10, y=100)

exit = tk.Button(window, text='退出', width=8, font=('黑体', 13), command=window.quit)
exit.place(x=258, y=100)


if __name__ == "__main__":
    window.mainloop()
