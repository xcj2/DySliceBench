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
    n, q = map(int, input().strip().split())
    G = [[] for _ in range(n)]
    for i in range(0, n-1):
        temp1, temp2 = map(lambda x: int(x) - 1, input().strip().split())
        G[temp1].append(temp2)
        G[temp2].append(temp1)

    px = [0 for _ in range(n)]
    for _ in range(q):
        temp1, temp2 = map(int, input().strip().split())
        px[temp1-1] += temp2

    #
    # eprint('px ', end=':\n')
    # eprint(px)

    # 木の頂点から順番に頂点を見ていき，頂点j
    # 頂点iについて，その子すべてにカウンタを"配る"
    usedlist = [False for _ in range(n)]
    imos = [0 for _ in range(n)]
    Q = Queue()

    # 木の頂点から順番に頂点を見ていき，頂点j
    Q.put(0)
    while not(Q.empty()):
        v = Q.get()
        usedlist[v] = True
        imos[v] += px[v]
        for u in G[v]:  # uは，「今見ているノード」の「子ノード」を表す
            if usedlist[u] == False:
                imos[u] += imos[v]
                Q.put(u)
    # eprint('imos ', end=':\n')
    # eprint(imos)

    #
    for value in imos:
        print(value, end=" ")


if __name__ == '__main__':
    main()
