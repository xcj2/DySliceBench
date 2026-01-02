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


def main():
    K, N = wi()
    A = wi()
    for i in range(len(A)):
        if i == 0:
            ans = min(K-abs(A[i]+K-A[-1]), K - abs(A[i]-A[i+1]))
        elif i == N - 1:
            ans = min(ans, min(K-abs(K-A[i]+A[0]), K - abs(A[i]-A[i-1])))
        else:
            ans = min(ans, min(K-abs(A[i]-A[i+1]), K - abs(A[i]-A[i-1])))
    print(ans)


if __name__ == '__main__':
    main()
