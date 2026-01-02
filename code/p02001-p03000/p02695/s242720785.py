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
    # 
    n,m,q = map(int,input().strip().split())
    abcd = []
    for i in range(q):
        # a,bはindexの次元，cは値， dはポイント
        temp_a,temp_b,temp_c,temp_d = map(int,input().strip().split())
        abcd.append((temp_a - 1, temp_b - 1, temp_c, temp_d ))

    # 
    eprint('n,m,q ',end=':\n')
    eprint(n,m,q)
    eprint('abcd ',end=':\n')
    eprint(abcd)

    #
    ans=0
    ll=[i for i in range(1,m+1)]
    # # ll=[i for i in range(1,m+1)]+[i for i in range(1,m+1)]+[i for i in range(1,m+1)]+[i for i in range(1,m+1)]
    # A=[]
    # rep(n)
    # for a1 in range(1,m+1):
    #     for a2 in range(p,m+1):
    #         for a3 in range(j,m+1):
    #             for a4 in range(k,m+1):
    #                 for a5 in range(k,m+1):
    #                     for a6 in range(k,m+1):
    #                         for a7 in range(k,m+1):
    #                             for a8 in range(k,m+1):
    #                                 for a9 in range(k,m+1):
    #                                     if :
    #                                         pass
    #                     pass
    #                 A=[p,j,k,l]
    #                 point = 0
    #                 for i in range(q):
    #                     a=abcd[i][0]
    #                     b=abcd[i][1]
    #                     c=abcd[i][2]
    #                     d=abcd[i][3]
    #                     if A[b] - A[a] == c:
    #                         point+=d
    #                 ans = max(point,ans)
    # print(ans)   
    for A in itertools.combinations_with_replacement(ll,n):
        #
        eprint('A ',end=':\n')
        eprint(A)

        point = 0
        for i in range(q):
            a=abcd[i][0]
            b=abcd[i][1]
            c=abcd[i][2]
            d=abcd[i][3]
            if A[b] - A[a] == c:
                point+=d
        ans = max(point,ans)
    print(ans)

if __name__ == '__main__':
    main()