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
    n, W_max = map(int, input().strip().split())
    lv = []
    lw = []
    for _ in range(n):
        a, b = map(int, input().strip().split())
        lv.append(a)
        lw.append(b)

    l_maxSumVal = [[-1 for _ in range(n+1)] for _ in range(W_max + 1) ]
    # function to return "max sum of values" (when picking up [i-th Elarger items] into [W-spaced bagage])
    def calc_maxSumVal(i, W):
        if i > n-1: # 
            return 0
        elif l_maxSumVal[W][i] != -1:
            return l_maxSumVal[W][i]
        elif W < lw[i]: #
            l_maxSumVal[W][i+1] = calc_maxSumVal(i + 1, W)
            return l_maxSumVal[W][i+1]
        else: # if [the free space of bagage] is << Elarger than [the weight] (of items now u r looking at) >>
            l_maxSumVal[W - lw[i]][i+1] = calc_maxSumVal(i + 1, W - lw[i]) # [value of the item now u r looking at] + [max sum of values when u picking up items from i-th Elarger ones and put them into bagage whose free space is W - l_w[i]]
            l_maxSumVal[W][i+1] = calc_maxSumVal(i+1, W)
            return max(lv[i] + l_maxSumVal[W - lw[i]][i+1], l_maxSumVal[W][i+1])
    
    #
    print(calc_maxSumVal(0,W_max))

if __name__ == '__main__':
    main()

