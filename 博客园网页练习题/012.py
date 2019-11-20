# 编写程序，统计如下各个字符串个数

string = "hello world god is always busy"
# 比如："hello world" 字符串统计的结果为： h:1 e:1 l:3 o:2 d:1 r:1 w:1


import re

# del_ = re.compile(r'\s+')             # 下面sub替换模式的提前书写
str_ = re.sub(r'\s+', '', string)           # 以指定模式替换掉空格
# print(str_)         # 输出 helloworldgodisalwaysbusy ,空格已经删除

l = set()           # 先定义空集
for i in str_:
    if i not in l:
        l.add(i)
        print(i, ':', str_.count(i))
