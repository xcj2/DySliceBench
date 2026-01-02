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


def main():
    a, b, c, d = map(int, input().strip().split())
    ans=-1*sys.maxsize
    for x in [a, b]:
        for y in [c, d]:
            ans = max(ans, x * y)
    print(ans)


if __name__ == '__main__':
    main()
