# -*- coding: utf-8 -*-
import sys
from collections import deque
from collections import defaultdict
import heapq
import collections
import itertools
import bisect
import copy
import math
sys.setrecursionlimit(10**6)

# lis_of_lis = [[] for _ in range(N)]


def zz(): return list(map(int, sys.stdin.readline().split()))


def z(): return int(sys.stdin.readline())


def S(): return sys.stdin.readline()[:-1]


def C(line): return [sys.stdin.readline() for _ in range(line)]

# a,bの最大公約数


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# a,bの最小公倍数


def lcm(a, b):
    return a * b // gcd(a, b)


def get_sieve_of_eratosthenes(n):
    if not isinstance(n, int):
        raise TypeError('n is int type.')
    if n < 2:
        raise ValueError('n is more than 2')
    prime = []
    limit = math.sqrt(n)
    data = [i + 1 for i in range(1, n)]
    while True:
        p = data[0]
        if limit <= p:
            return prime + data
        prime.append(p)
        data = [e for e in data if e % p != 0]


max_a = pow(10, 6)+5
N = z()
A = zz()
pari_flg = True

set_flg = True
count = [0]*max_a
for i in range(N):
    count[A[i]] += 1
for i in range(2, max_a):
    c = 0
    for j in range(i, max_a, i):
        c += count[j]
        if (c > 1):
            pari_flg = False
res = A[0]
for a in A:
    res = math.gcd(res, a)
if (res != 1):
    set_flg = False

if (pari_flg):
    print('pairwise coprime')
elif (set_flg):
    print('setwise coprime')
else:
    print('not coprime')
