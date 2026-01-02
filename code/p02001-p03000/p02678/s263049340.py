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
    n, m = map(int, input().strip().split())
    g = [[] for _ in range(n)]
    for i in range(m):
        a_temp,b_temp = map(lambda x: int(x) - 1, input().strip().split())
        g[a_temp].append(b_temp)
        g[b_temp].append(a_temp)
    
    usedlist=[-100 for _ in range(n)]
    Q=Queue()

    #
    Q.put(0)
    usedlist[0] = -1
    while not(Q.empty()):
        u=Q.get()
        for v in g[u]:
            if usedlist[v]==-100:
                usedlist[v] = u # usedlist[u] + 1
                Q.put(v)
            else:
                pass
    eprint('g ',end=':\n')
    eprint(g)
    eprint('usedlist ',end=':\n')
    eprint(usedlist)
    print("Yes")
    for i in range(1,n):
        print( usedlist[i]+1)
    
        

if __name__ == '__main__':
    main()
