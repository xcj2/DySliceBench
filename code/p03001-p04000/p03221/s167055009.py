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

def cmp_vec(u,v):   # u < v なる必要条件を記す
    if u[1] < v[1]:
        return  1
    elif u[1] == v[1]:
        if u[2] < v[2]:
            return 1
        elif u[2]==v[2]:
            return 0
        else:
            return -1
    else:
        return -1

def main():
    #
    n,m = map(int,input().strip().split())  # 市 in 県  # n個の県，m個の市
    l=[]
    for i in range(m):
        p,y = map(int,input().strip().split()) # 市iは県piに属しyi年に誕生した
        p = str(p).zfill(6) # p-=1 # i (y,p) 
        l.append(list((i,p,y)))
    l.sort(key=functools.cmp_to_key(cmp_vec),reverse = True)

    #
    eprint('l (i,p,y)',end=':\n')
    eprint(l)

    #
    cntr=1
    for i in range(m):
        if i>0 and l[i][1] != l[i-1][1]:
            cntr=1
        l[i][2] = str(cntr).zfill(6)
        cntr+=1

    #
    l.sort(key=lambda x:x[0])
    for xx in l:
        print(xx[1]+xx[2])
    #
    # eprint('l (i,p,y)',end=':\n')
    # eprint(l)
    # aaa=["asdfa",32, 15.3, True]
    # eprint('aaa ',end=':\n')
    # eprint(aaa)

if __name__ == '__main__':
    main()