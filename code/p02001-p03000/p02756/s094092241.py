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
from collections import defaultdict
import sys
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


def main():
    s = input()
    q = int(input())
    Q = []
    cnt = 0
    head = []
    tail = []
    for _ in range(q):
        Q.append(list(map(str, input().split())))
    # print(Q)
    for i in range(q):
        if Q[i][0] == '1':
            cnt += 1
            head, tail = tail, head

        else:
            if Q[i][1] == '1':
                head.append(Q[i][2])
            else:
                tail.append(Q[i][2])
    print("".join(head[::-1]) + (s[::-1] if cnt %
                                 2 == 1 else s) + "".join(tail))


if __name__ == '__main__':
    main()
