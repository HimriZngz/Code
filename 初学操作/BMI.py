H = input('请输入你的身高m:')
W = input('请输入你的体重kg:')
w = float(W)
h = float(H)
bmi = w/(h*h)
print('你的BMI指数为:',bmi)
b = float(bmi)
if 0 < b < 18.5:
    print('你的目前体型过轻')
elif 18.5 <= b < 25:
    print('你的目前体型正常')
elif 25 <= b <= 28:
    print('你的目前体型过重')
elif 28 < b <= 32:
    print('你的目前体型肥胖')
elif 32 < b:
    print('你的目前体型严重肥胖')
else:
    print('你的输入好像有误')