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
    S = input().strip()
    n = len(S)

    #
    temp = 0
    cnt = 0
    for i in range(n):
        if S[i] == 'R':
            temp += 1
        else:
            cnt = max(cnt, temp)
            temp = 0
    for i in range(n):
        if S[i] == 'L':
            temp += 1
        else:
            cnt = max(cnt, temp)
            temp = 0

    #
    T = [0 for _ in range(n)]
    #
    stack = 0
    ### 0 <= i < n
    for i in range(0, n):
        if S[i] == 'L':
            # if cnt % 2 == 1:    # 移動回数が奇数の場合
                T[i-1] += - (-stack//2)
                T[i] += stack//2
                stack = 0
            # else:               # 移動回数が偶数の場合
                # T[i-1] += stack//2
                # T[i] += -(-stack//2)
                # stack = 0
        else:
            stack += 1
    eprint(T)
    #
    stack = 0
    TT=[0 for _ in range(n)]
    for i in range(0, n)[::-1]:
        if S[i] == 'R':
            # if cnt % 2 == 1:    # 移動回数が奇数の場合
                TT[i] += stack//2
                TT[i+1] += - (-stack//2)
                stack = 0
            # else:               # 移動回数が偶数の場合
                # TT[i] += -(-stack//2)
                # TT[i+1] += stack//2
                # stack = 0
        else:
            stack += 1
    eprint(TT)

    for x in [(T[i] + TT[i]) for i in range(n)]:
        print(x,end=" ")

if __name__ == '__main__':
    main()
