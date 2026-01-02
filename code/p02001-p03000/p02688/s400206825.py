"""
import random
import functools
import copy
import bisect
import array
import re
import collections
import heapq
import fractions
import itertools
import string
import math
from operator import itemgetter as ig
from bisect import bisect_left, bisect_right, insort_left, insort_right
from itertools import permutations, combinations, product, accumulate, groupby
from heapq import heappush, heappop
from collections import deque, defaultdict, Counter
import sys
sys.setrecursionlimit(10 ** 7)
# import numpy as np

inf = 10 ** 20
INF = float("INF")
mod = 10 ** 9 + 7
dd = [(-1, 0), (0, 1), (1, 0), (0, -1)]
ddn = dd + [(-1, 1), (1, 1), (1, -1), (-1, -1)]
ddn9 = ddn + [(0, 0)]
'''for dx, dy in dd:
        nx = j + dx; ny = i + dy
            if 0 <= nx < w and 0 <= ny < h:'''
"""
from operator import itemgetter
from collections import defaultdict
import sys
import math
sys.setrecursionlimit(10 ** 7)


def wi(): return list(map(int, sys.stdin.readline().split()))
# WideIntPoint


def wip(): return [int(x) - 1 for x in sys.stdin.readline().split()]


def ws(): return sys.stdin.readline().split()


def si(): return int(sys.stdin.readline())  # SingleInt


def ss(): return input()


def hi(n): return [si() for _ in range(n)]


def hs(n): return [ss() for _ in range(n)]  # HeightString


def s_list(): return list(input())


def mi(n): return [wi() for _ in range(n)]  # MatrixInt


def mip(n): return [wip() for _ in range(n)]


def ms(n): return [ws() for _ in range(n)]


def num_grid(n): return [[int(i) for i in sys.stdin.readline().split()[
    0]] for _ in range(n)]  # NumberGrid


def grid(n): return [s_list() for _ in range(n)]


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# a/b の切り上げ


def round_up(a, b):
    """ a/b の切り上げ """
    c = (a + b - 1) / b
    return c


def lcm(a, b):
    """a,bの最小公倍数"""
    return a * b // gcd(a, b)


def floor(a, b):
    """floor(a/b) 整数値を返す"""
    c = (a - a % b)/b
    return int(c)


def main():
    n, k = wi()
    d = []
    a = []
    b = []
    cnt = 0
    for i in range(k):
        d = int(input())
        a.append(wi())
    for i in range(k):
        for j in a[i]:
            if j in b:
                continue
            else:
                b.append(j)
                cnt += 1
    print(n-cnt)


if __name__ == '__main__':
    main()
