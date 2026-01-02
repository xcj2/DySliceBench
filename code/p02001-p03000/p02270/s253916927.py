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


# def combinations_count(n, r):
#     r = min(r, n - r)
#     numer = reduce(mul, range(n, n - r, -1), 1)
#     denom = reduce(mul, range(1, r + 1), 1)
#     return numer // denom


# mod=1000000007
# def combinations_count_mod(n, r):
#     r = min(r, n - r)
#     numer = reduce(lambda x,y: x*y%mod, range(n, n - r, -1), 1)
#     denom = pow( reduce(lambda x,y: x*y%mod, range(1, r + 1), 1) , mod-2, mod)
#     return numer * denom % mod

def is_ok(p,n,k,w):
    #
    i_track = 0
    i_w = 0

    # トラックに積めるギリギリ(p)まで積んでいくことを繰り返していって，
    # i_w(w_index) を0 ~ n-1 まで全部積めたら嬉しいねぇ
    # 積載量pが小さすぎるゴミみてぇなトラックだったら先にトラックの数が尽きてしまって悲しいことになります
    # 積載量pが十分大きい素敵なトラックだったら i_w(w_index) = n - 1 まで到達できてとっても嬉しくなれます
    while i_track < k and i_w < n : # トラック全部
        temp=0
        while i_w < n and temp + w[i_w] <= p: #  一時積載tempがpを超えないギリギリを目指していけ
            temp += w[i_w]
            i_w+=1
        # ギリギリまで ，背番号i_trackのトラック ，つまり今見ているトラックに積載したら
        i_track += 1 #次のトラックに進みましょうね〜〜〜

    return i_w == n

def solve(n,k,w):
    # 
    ok = 10000 * 100000  # solve(ok)は解が存在すると分かっているような整数ok
    ng = -1                # solve(ng)は解が存在しない(と分かっているような整数ng
    ans = ok

    # abs(ok-ng) つまり ok と ng の絶対差ですね，これが1未満つまりokとngが等しいということになったらですね，終了するんですね
    while abs( ok - ng ) > 1: #abs(ok-ng) <= 1 というのはokとngがもうなんかね，アレなんですよ
        mid = (ok + ng) // 2
        # 
        if is_ok(mid,n,k,w):
            ok = mid
            ans = ok
        else:
            ng = mid
    return ans

def main():
    n,k  = map(int,input().strip().split())
    w=[]
    for i in range(n):
        w.append(int(input().strip()))
    print(solve(n,k,w))

if __name__ == '__main__':
    main()
