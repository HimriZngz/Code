# 1. 10 以内的素数之和是：2 + 3 + 5 + 7 = 17，那么请编写程序，计算 2000000 以内的素数之和？

from math import sqrt


def Pn(num):
    if num <= 1:
        return False
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


def cac():
    add = 0
    for i in range(2000000):
        if Pn(i):
            add += i

    print(add)


cac()


"""
参考答案：

import math

def is_prime(number):
    if number > 1:
        if number == 2:
            return True
        if number % 2 == 0:
            return False
        for current in range(3, int(math.sqrt(number) + 1), 2):
            if number % current == 0:
                return False
        return True
    return False

def get_primes(number):
    while True:
        if is_prime(number):
            yield number
        number += 1

def solve():
    total = 2
    for next_prime in get_primes(3):
        if next_prime < 2000000:
            total += next_prime
        else:
            print(total)
            return

if __name__ == '__main__':
    solve()


"""