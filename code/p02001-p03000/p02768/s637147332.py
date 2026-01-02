import sys, bisect, math, itertools, heapq, collections
from operator import itemgetter
# a.sort(key=itemgetter(i)) # i番目要素でsort
from functools import lru_cache
# @lru_cache(maxsize=None)
sys.setrecursionlimit(10**8)
input = sys.stdin.readline
INF = float('inf')
mod = 10**9 + 7
eps = 10**-7


def inp():
    '''
    一つの整数
    '''
    return int(input())


def inpl():
    '''
    一行に複数の整数
    '''
    return list(map(int, input().split()))


def comb(n, r):
    if n - r < r:
        r = n - r
    res = 1
    for i in range(r):
        res *= (n - i) % mod
        res %= mod
        res *= pow(r - i, mod - 2, mod)
        res %= mod
    return res


n, a, b = inpl()
All = pow(2, n, mod) - 1
ans = All - comb(n, a) - comb(n, b)
print(ans % mod)
