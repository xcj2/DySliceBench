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


mod = 1000000007


def combinations_count_mod(n, r):
    r = min(r, n - r)
    numer = reduce(lambda x, y: x * y % mod, range(n, n - r, -1), 1)
    denom = pow(reduce(lambda x, y: x * y % mod, range(1, r + 1), 1), mod - 2, mod)
    return numer * denom % mod


def solve():
    pass


def solve01():
    n = int(input().strip())
    L = []
    Xmin, Ymin, Xmax, Ymax = (sys.maxsize, sys.maxsize, -100, -100)

    for i in range(n):
        a, b = map(int, input().strip().split())
        L.append((a, b))
        Xmin, Ymin, Xmax, Ymax = (min(Xmin, a), min(Ymin, b), max(Xmax, a), max(Ymax, b))
    A, B, C, D = ((Xmin, Ymax), (Xmin, Ymin), (Xmax, Ymin), (Xmax, Ymax))

    flag = 1
    for i in range(len(L) - 1):
        flag *= (L[i] == L[i + 1])
    if flag == 1:
        try:
            raise ValueError("error!")
        except ValueError as e:
            eprint(e)

    if Xmax == Xmin or Ymax == Ymin:
        try:
            raise ValueError("error!")
        except ValueError as e:
            eprint(e)

    # 対角線ACについて
    d_MinDistFromA = sys.maxsize    # 点Aからの距離が最小であるような，その最小の距離の値を求める
    for a, b in L:
        d_MinDistFromA = min(d_MinDistFromA, abs(a - Xmin) + abs(b - Ymax))

    d_MinDistFromC = sys.maxsize    # 点Cからの距離が最小であるような，その最小の距離の値を求める
    for a, b in L:
        d_MinDistFromC = min(d_MinDistFromC, abs(a - Xmax) + abs(b - Ymin))
    ans1 = abs(A[0] - C[0]) + abs(A[1] - C[1]) - (d_MinDistFromA + d_MinDistFromC)  #

    # 対角線BDについて
    d_MinDistFromB = sys.maxsize    # 点Bからの距離が最小であるような，その最小の距離の値を求める
    for a, b in L:
        d_MinDistFromB = min(d_MinDistFromB, abs(a - Xmin) + abs(b - Ymin))

    d_MinDistFromD = sys.maxsize    # 点Dからの距離が最小であるような，その最小の距離の値を求める
    for a, b in L:
        d_MinDistFromD = min(d_MinDistFromD, abs(a - Xmax) + abs(b - Ymax))
    ans2 = abs(B[0] - D[0]) + abs(B[1] - D[1]) - (d_MinDistFromB + d_MinDistFromD)

    # 出力
    # eprint('ans1,ans2 ', end=':\n')
    # eprint(ans1, ans2)
    print(max(ans1, ans2))


def solve00():
    n = int(input().strip())
    L = []
    Xmin = sys.maxsize
    Ymin = sys.maxsize
    Xmax = -100
    Ymax = -100
    for i in range(n):
        a, b = map(int, input().strip().split())
        L.append((a, b))
        Xmin = min(Xmin, a)
        Ymin = min(Ymin, b)
        Xmax = max(Xmax, b)
        Ymax = max(Ymax, b)

    A = (Xmin, Ymax)
    B = (Xmin, Ymin)
    C = (Xmax, Ymin)
    D = (Xmax, Ymax)

    # 対角線ACについて
    d_MinDistFromA = sys.maxsize    # 点Aからの距離が最小であるような，その最小の距離の値を求める
    for a, b in L:
        d_MinDistFromA = min(d_MinDistFromA, abs(a - Xmin) + abs(b - Ymax))

    d_MinDistFromC = sys.maxsize    # 点Cからの距離が最小であるような，その最小の距離の値を求める
    for a, b in L:
        d_MinDistFromC = min(d_MinDistFromC, abs(a - Xmax) + abs(b - Ymin))
    ans1 = abs(A[0] - C[0]) + abs(A[1] - C[1]) - (d_MinDistFromA + d_MinDistFromC)  #

    # 対角線BDについて
    d_MinDistFromB = sys.maxsize    # 点Bからの距離が最小であるような，その最小の距離の値を求める
    for a, b in L:
        d_MinDistFromB = min(d_MinDistFromB, abs(a - Xmin) + abs(b - Ymin))

    d_MinDistFromD = sys.maxsize    # 点Dからの距離が最小であるような，その最小の距離の値を求める
    for a, b in L:
        d_MinDistFromD = min(d_MinDistFromD, abs(a - Xmax) + abs(b - Ymax))
    ans2 = abs(B[0] - D[0]) + abs(B[1] - D[1]) - (d_MinDistFromB + d_MinDistFromD)

    # 出力
    # eprint('ans1,ans2 ', end=':\n')
    # eprint(ans1, ans2)
    print(max(ans1, ans2))


def main():
    solve01()


if __name__ == '__main__':
    main()
