from __future__ import print_function

from functools import reduce
from operator import mul
from collections import Counter
from collections import deque
from itertools import accumulate
from queue import Queue
from queue import PriorityQueue as pq
from heapq import heapreplace
from heapq import heapify
from heapq import heappushpop
from heapq import heappop
from heapq import heappush
import heapq
import time
import random
import bisect
import itertools
import collections
from fractions import Fraction
import fractions
import string
import math
import operator
import functools
import copy
import array
import re
import sys
sys.setrecursionlimit(500000)


input = sys.stdin.readline


def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)
    return

# from fractions import gcd
# from math import gcd

# def lcm(n, m):
#     return int(n * m / gcd(n, m))


# def coprimize(p, q):
#     common = gcd(p, q)
#     return (p // common, q // common)


# def find_gcd(list_l):
#     x = reduce(gcd, list_l)
#     return x


def combinations_count(n, r):
    r = min(r, n - r)
    numer = reduce(mul, range(n, n - r, -1), 1)
    denom = reduce(mul, range(1, r + 1), 1)
    return numer // denom


def main():
    #
    s0 = input().strip()
    q = int(input().strip())

    #
    stc1 = []
    stc2 = []
    flag = 0

    # def f(flag1, flag2, val):
    #     if flag1 ^ flag2:
    #         stc1 += val
    #     else:
    #         stc2 += val

    #
    for i in range(q):
        t, *fc = map(lambda x: int(x) if x.isdecimal() else x, input().strip().split())
        # eprint('t,fc ', end=':\n')
        # eprint(t, fc, "\n")

        if t == 2:    # 文字列付加
            # f(fc[0], flag, fc[1])
            if (fc[0]-1)^flag==1:  # fc[0]は前方/後方， flagは非反転/反転，をそれぞれ表す
                stc2.append(fc[1])
            else:
                stc1.append(fc[1])
        else:       # 反転命令
            flag = flag ^ 1

    #
    if flag == 0:
        ans ="".join(stc1[::-1] + list(s0) + stc2)
    else:
        ans ="".join( stc2[::-1] + list(s0)[::-1] + stc1)
    print(ans)
    # eprint(ans[::-1])
    return


if __name__ == '__main__':
    main()
