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
    S = input().strip()
    R = []
    G = []
    B = set()
    for i in range(n):
        if S[i] == 'R':
            R.append(i)
        elif S[i] == 'G':
            G.append(i)
        elif S[i] == 'B':
            B.add(i)
    R.sort()
    G.sort()

    #
    n_all = len(R)*len(G)*len(B)
    cnt = 0
    for i in R:
        for j in G:
            high = 2*i - j
            low = 2*j - i
            if (i+j) % 2 == 0:
                mid = (i+j) // 2
            else:
                mid = -1
            cnt += (high in B) + (low in B) + (mid in B)
    eprint('n_all, cnt ',end=':\n')
    eprint(n_all, cnt)
    print(n_all - cnt)


if __name__ == '__main__':
    main()
