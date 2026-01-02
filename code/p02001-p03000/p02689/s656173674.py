from __future__ import print_function

import sys
sys.setrecursionlimit(500000)

import re
import array
import copy
import functools
import operator

import math
import string
import fractions
from fractions import Fraction

import collections
import itertools
import bisect

import random
import time

import heapq
from heapq import heappush
from heapq import heappop
from heapq import heappushpop
from heapq import heapify
from heapq import heapreplace
from queue import PriorityQueue as pq
from queue import Queue

from itertools import accumulate

from collections import deque
from collections import Counter

from operator import mul
from functools import reduce

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
    n,m = map(int,input().strip().split()) # nコの展望台，m本の道
    h = list(map(int, input().strip().split())) # h[i]は展望台iの「高さ」
    # g=[]
    S=set([i for i in range(n)])
    for i in range(m): # 「m本の道」についてのループ # 道 j は展望台 Aj と展望台 Bj を結んでいる
        a,b = map(lambda x:int(x)-1,input().strip().split())
        if h[a]>h[b]:
            S.discard(b)
        elif h[a]<h[b]:
            S.discard(a)
        else:
            S.discard(a); S.discard(b)
    print(len(S))

if __name__ == '__main__':
    main()