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
    n, k = map(int, input().strip().split())  # """ 街数n, 移動回数k """
    a = list(map(lambda x: int(x) - 1, input().strip().split()))  # """ 転送先 : 街i から街a[i]"""

    #
    eprint("a", end=':\n')
    eprint(a)
    #
    path = []
    visitedlist = [False for _ in range(n)]
    pos = 0
    cnt=0   # 現在位置posに来るまでの，「移動回数」

    while True:
        if cnt==k:
            print(pos+1)
            return
        if visitedlist[pos]:
            start = pos
            break
        cnt+=1
        path.append(pos)
        visitedlist[pos] = True
        pos = a[pos]

    eprint('path ', end=':\n')
    eprint(path)

    for i in range(len(path)):
        if path[i] == start:
            cycle = path[i:]

    eprint('cycle ',end=':\n')
    eprint(cycle)

    m=len(cycle)
    cnt1=k-cnt
    cnt2=cnt1%m
    print(cycle[cnt2]+1)


if __name__ == '__main__':
    main()
