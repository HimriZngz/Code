# import re
#
# a = 'DATE:2020-03-13 10:03:58  共28张'
#
# regex = '.*?共(\d+)张'
# match = re.match('.*?共(\d+)张', a)
# print(match.group(1))


# l = 'http://www.mmonly.cc/mmtp/xgmn/316821.html'
#
# for i in range(2, 42):
#     t = '_%s.html' % i
#     l2 = l.replace('.html', t)
#     print(l2)


ll = 'http://www.mmonly.cc/mmtp/xgmn/317520_12.html'
ww = '317520_2.html'
add = ll.split('/')[-4:-1]
new_next_page = 'http://%s/%s/%s/%s' % (add[0], add[1], add[2], ww)

print(new_next_page)