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


mod=1000000007
def combinations_count_mod(n, r):
    r = min(r, n - r)
    numer = reduce(lambda x,y: x*y%mod, range(n, n - r, -1), 1)
    denom = pow( reduce(lambda x,y: x*y%mod, range(1, r + 1), 1) , mod-2, mod)
    return numer * denom % mod


def solve():
    pass

# def f_rec(g, h): # あとg個のグループに分けるとき，h番目に仕切りを入れると考えたとき
#     # i:[ 3*g , 2000 - 3*(g-1)]
#     for i in range():
        


def main():
    ans=0
    S = int(input().strip())
    if S<3:
        print(0)
        return
    group = S//3
    # amari = S%3

    ans+=1
    eprint(ans)
    for g in range(2,group+1): # gは何グループあるか
        配る数 = S - g*3
        temp=combinations_count(配る数+ g-1,g-1)
        eprint(temp)
        ans=temp+ans
    
    print(ans%mod)
    # # S//3個に分けるとき
    # if amari==0:
    #     ans+=1
    # elif amari == 1:
    #     ans += S//3
    # else:
    #     ans += combinations_count(S//3,2)

    # for i in range(S//3):   # iはS個の玉を何個のグループに分けるか
    #     ans += # 


if __name__ == '__main__':
    main()