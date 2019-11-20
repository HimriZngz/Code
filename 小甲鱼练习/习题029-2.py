# 编写一个程序，用户输入文件名及行数，打印它

# 先手动创建一下
'''
f = open(r'd:/1/习题29-2.txt', 'w')
for i in range(1,11):
     str1 = str('这是第%s行\n' % i)
     f.writelines(str1)
'''

path = input('文件位置：')
li = int(input('行数：'))

with open(path, 'r')as f:
    for i in range(li):
        print(f.readline())