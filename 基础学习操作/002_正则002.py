import re


def name_of_email(addr):
    # custom2 = re.compile(r'.*?([\w\s]+)')
    # if custom2.match(addr).group(1):
    #     return True
    return re.match(r'.*?([\w\s]+)', addr).group(1)


# 测试:
assert name_of_email('<Tom Paris> tom@voyager.org') == 'Tom Paris'
assert name_of_email('tom@voyager.org') == 'tom'
print('ok')
