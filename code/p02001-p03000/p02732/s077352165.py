from __future__ import print_function

import array
import bisect
import collections
import copy
import fractions
import functools
import heapq
import itertools
import math
import operator
import random
import re
import string
import sys
import time
from collections import Counter, deque
from fractions import Fraction
from functools import reduce
from heapq import heapify, heappop, heappush, heappushpop, heapreplace
from itertools import accumulate
from operator import mul
from queue import PriorityQueue as pq
from queue import Queue

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
    if r>n:
        return 0
    r = min(r, n - r)
    numer = reduce(mul, range(n, n - r, -1), 1)
    denom = reduce(mul, range(1, r + 1), 1)
    return numer // denom


def main():
    n = int(input().strip())
    a = list(map(int, input().strip().split()))
    C=Counter()
    for i in range(n):
        C[a[i]]+=1
    ans_temp=0
    X=[0 for _ in range(n+1)]
    for key, value in C.items():
        X[key] = combinations_count(value, 2)
        ans_temp += X[key]
    for k in range(n):
        print( ans_temp - X[a[k]] + combinations_count(C[a[k]]-1,2) )


if __name__ == '__main__':
    main()
