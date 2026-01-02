import collections
import math
import operator as op
from functools import reduce
import numpy as np
import math
import bisect


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    return a * b // gcd(a, b)


def main():
    N = int(input())
    if N == 0 or N == 1:
        print(0)
        return

    if N % 2 == 1:
        print(0)
        return
    else:
        N //= 2
        n5 = 0
        i = 1
        while 5**i <= N:
            n5 += N // (5**i)
            i += 1

        print(n5)
        return

    # print(min(n2, n5))


if __name__ == '__main__':
    main()
