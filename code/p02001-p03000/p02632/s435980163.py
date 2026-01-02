#!/usr/bin/env python3
from collections import defaultdict,deque
from heapq import heappush, heappop
from bisect import bisect_left, bisect_right
import sys, itertools, math
sys.setrecursionlimit(10**5)
input = sys.stdin.readline
sqrt = math.sqrt
def LI(): return list(map(int, input().split()))
def LF(): return list(map(float, input().split()))
def LI_(): return list(map(lambda x: int(x)-1, input().split()))
def II(): return int(input())
def IF(): return float(input())
def S(): return input().rstrip()
def LS(): return S().split()
def IR(n):
    res = [None] * n
    for i in range(n):
        res[i] = II()
    return res
def LIR(n):
    res = [None] * n
    for i in range(n):
        res[i] = LI()
    return res
def FR(n):
    res = [None] * n
    for i in range(n):
        res[i] = IF()
    return res
def LFR(n):
    res = [None] * n
    for i in range(n):
        res[i] = IF()
    return res
def LIR_(n):
    res = [None] * n
    for i in range(n):
        res[i] = LI_()
    return res
def SR(n):
    res = [None] * n
    for i in range(n):
        res[i] = S()
    return res
def LSR(n):
    res = [None] * n
    for i in range(n):
        res[i] = LS()
    return res
mod = 1000000007
inf = float('INF')
fact = [i for i in range(2 * 10 ** 6 + 1)]
fact[0] = 1
for i in range(2 * 10 ** 6):
    fact[i + 1] *= fact[i]
    fact[i + 1] %= mod
invfact = fact[:]
invfact[-1] = pow(invfact[-1], mod - 2, mod)
for i in range(2 * 10 ** 6, 0, -1):
    invfact[i - 1] = i * invfact[i]
    invfact[i - 1] %= mod

def combination_mod(n, k, mod):
    """ power_funcを用いて(nCk) mod p を求める """ 
    """ nCk = n!/((n-k)!k!)を使用 """
    from math import factorial
    if n < 0 or k < 0 or n < k: return 0
    if n == 0 or k == 0: return 1
    a = fact[n]
    b = invfact[k]
    c = invfact[n - k]
    return (a * b * c) % mod

#solve
def solve():
    k = II()
    s = S()
    ans = pow(26, len(s) + k, mod)
    sk = len(s) + k
    for i in range(len(s)):
        ans -= combination_mod(sk, i, mod) * pow(25, sk - i, mod)
        ans %= mod
    print(ans)
    return


#main
if __name__ == '__main__':
    solve()
