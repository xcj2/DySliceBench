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


def add_temp_to_T(p, temp, T ):
    if p % 2 == 0:
        T[p-1] += temp[1]
        T[p] += temp[0]
    else:
        T[p-1] += temp[0]
        T[p] += temp[1]
    return 0


def main():
    S = input().strip()
    n = len(S)

    i = 0
    T=[0 for _ in range(n)]
    while i<n:
        temp = [0, 0]
        while i<n and S[i] == 'R':
            temp[i % 2] += 1
            i += 1
        p = i
        while i<n and S[i] == 'L':
            temp[i % 2] += 1
            i += 1
        add_temp_to_T(p, temp, T)
    del i
    print(" ".join(map(str,T)))

if __name__ == '__main__':
    main()
