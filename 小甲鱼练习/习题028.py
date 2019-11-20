# 尝试将音频文件打印到屏幕上

with open(r'd:/1/m001.wav', 'rb') as f:
    # print(f.readline())
    print((f.read(20)))


# 然后尝试将这个音频文件保存为txt

with open(r'd:/1/m001.wav', 'rb') as f:
    with open(r'd:/1/m001.txt', 'w') as f2:
        f2.write(str(f.read(20)))