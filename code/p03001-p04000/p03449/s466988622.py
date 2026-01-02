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
    n = int(input().strip())
    a1 = list(map(int, input().strip().split()))
    a2 = list(map(int, input().strip().split()))
    g = [a1,a2]
    memo = [[0 for _ in range(n)], [0 for _ in range(n)]]

    #
    memo[0][0] = g[0][0]
    memo[1][0] = g[1][0] + g[0][0]
    for i in range(1,n):
        memo[0][i] = memo[0][i-1] + g[0][i]
    for i in range(1,n):
        memo[1][i] = max(  (memo[0][i] + g[1][i])  ,  (memo[1][i-1] + g[1][i])  )
    
    #
    print(memo[1][n-1])
    

if __name__ == '__main__':
    main()
