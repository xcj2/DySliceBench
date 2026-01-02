# import numpy as np
import sys, math, heapq
from itertools import permutations, combinations
from collections import defaultdict, Counter, deque
from math import factorial, gcd
from bisect import bisect_left, bisect_right

sys.setrecursionlimit(10 ** 7)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline()[:-1]
pl = lambda x: print(*x, sep="\n")

S = int(input())
num = S // 3
res = 0


fact = [1]
for i in range(1, S + 10):
    fact.append(fact[-1] * i % MOD)


def rev(x):
    return pow(x, MOD - 2, MOD)


def cmb(i, k):
    if i < k:
        return 0
    return fact[i] * rev(fact[k]) * rev(fact[i - k]) % MOD


def cmb2(n, r, p):
    r = min(n - r, r)
    if r == 0:
        return 1
    over = 1
    for i in range(n, n - r, -1):
        over = over * i % p
    under = 1
    for i in range(1, r + 1):
        under = under * i % p
    inv = pow(under, p - 2, p)
    return over * inv % p


def h(i, k):
    return cmb(i + k - 1, k)


for r in range(1, num + 1):
    val = h(r, S - 3 * r)
    # print("r, val", r, val)
    res += val
res %= MOD
print(res)
