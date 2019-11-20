# 输出商品列表，用户输入序号，显示用户选中的商品
#
# 　　商品 商品li=["电脑","显示器",“笔记本”,“机械键盘”]
#
# 　　a.允许用户添加商品
#
# 　　b.用户输入序号显示内容

shop = ["电脑", "显示器", '笔记本', '机械键盘']

print('=' * 10, '当前有', '=' * 10)  # 开始展示内容
for item in shop:
    print(shop[shop.index(item)])
print('=' * 28)

print('')
print('要添加内容吗?')
print('直接按数字并回车,以0开始且不超过', len(shop) - 1, '，0表示添加在最前')
print('直接按回车则不添加')
print('')

while True:
    add = input('在这里输入添加的指定位置，直接回车可以放弃添加：')
    if not add:  # 看看是不是直接回车的
        break
    else:
        try:
            add = int(add)  # 看看是不是输入的数字
            pass
        except ValueError:
            print('\n', '请输入正确的数字', '\n')
            continue
        else:
            if int(add) <= (len(shop) - 1):  # 看看数字对没有
                i = input('你要添加什么?')
                shop.insert(int(add), i)
                print('\n', '=' * 8, '现在的清单为', '=' * 8)
                for item2 in shop:
                    print(item2)
                print('=' * 31, '\n')
            else:
                print('\n', '请输入正确的数字鸭', '\n')
                continue
    break

print('\n')
print('可以输入序号查看商品内容,以0开始且不超过%s，0表示查看第一个' % (len(shop) - 1), '\n', '直接回车则不查看', '\n')
while True:
    view = input('现在输入：')
    if not view:  # 看看是不是直接回车的
        break
    else:
        try:
            add = int(add)  # 看看是不是输入的数字
            pass
        except ValueError:
            print('\n', '请输入正确的数字啊', '\n')
            continue
        else:
            if int(view) <= (len(shop) - 1):  # 看看数字对没有
                print('当前查看的是：%s' % (shop[int(view)]))
            else:
                print('\n', '请输入正确的数字wdnmd', '\n')
                continue
    break