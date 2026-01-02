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
    a = list(map(int, input().split()))

    a_pos = []
    n_breaks = 0
    i = 1
    for ai in a:
        if i - ai < 0:
            n_breaks += 1
        else:
            a_pos.append(ai)
            i += 1

    # a[i] - i >= 0 for all i

    # a_ret = []
    if len(a_pos) == 0 or a_pos[0] != 1:
        print(-1)
    else:
        i = 1
        for ai in a_pos:
            if i - ai != 0:
                n_breaks += 1
            else:
                # a_ret.append(ai)
                i += 1
        print(n_breaks)


if __name__ == '__main__':
    main()
