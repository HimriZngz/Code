def num1(*num):
    a = 0
    for i in num:
        a += i
    return a


def avrage1(*num):
    x = len(num)
    # return (num1(*num)) / x
    k = (num1(*num)) / x
    print('%.d' % k)

avrage1(1,2,3,4,5,6,7,8,9)
