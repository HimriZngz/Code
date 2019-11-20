# 0. 编写一个程序，接受用户的输入并保存为新的文件

file_name = input('请输入文件名：')


name = '习题029-0_' + file_name + '.txt'

print(r'请输入内容,输入 :w 则结束输入并保存：')

f = open(name, 'w')

while 1:
    file_text = input()

    if file_text != ':w':
        f.write('%s\n' % file_text)
    else:
        break

f.close()
