#!/usr/bin/env python3
from collections import defaultdict
from collections import deque
from heapq import heappush, heappop
import sys
import math
import bisect
import random
import itertools
sys.setrecursionlimit(10**5)
stdin = sys.stdin
bisect_left = bisect.bisect_left
bisect_right = bisect.bisect_right
def LI(): return list(map(int, stdin.readline().split()))
def LF(): return list(map(float, stdin.readline().split()))
def LI_(): return list(map(lambda x: int(x)-1, stdin.readline().split()))
def II(): return int(stdin.readline())
def IF(): return float(stdin.readline())
def LS(): return list(map(list, stdin.readline().split()))
def S(): return list(stdin.readline().rstrip())
def IR(n): return [II() for _ in range(n)]
def LIR(n): return [LI() for _ in range(n)]
def FR(n): return [IF() for _ in range(n)]
def LFR(n): return [LI() for _ in range(n)]
def LIR_(n): return [LI_() for _ in range(n)]
def SR(n): return [S() for _ in range(n)]
def LSR(n): return [LS() for _ in range(n)]
mod = 1000000007
inf = float('INF')

#A
def A():
    s = S()
    b = list(set(s))
    a = len(list(set(s)))
    if a == 2 and s.count(b[0]) == s.count(b[1]) == 2:
        print("Yes")
    else:
        print("No")
    return

#B
def B():
    n = II()
    p = LI()
    ans = 0
    for i in range(1,n-1):
        if (p[i - 1] < p[i] and p[i] < p[i + 1]) or (p[i + 1] < p[i] and p[i] < p[i - 1]):
            ans += 1
    print(ans)
    return

#C
def C():
    n = II()
    d = LI()
    d.sort()
    ans = 0
    for i in range(10**5+1):
        if n // 2 == bisect_left(d, i):
            ans += 1
    print(ans)
    return


def combination_mod(n, k, mod):
    # power_funcを用いて(nCk) mod p を求める 
    # nCk = n!/((n-k)!k!)を使用

    from math import factorial
    if n < 0 or k < 0 or n < k: return 0
    if n == 0 or k == 0: return 1
    a = factorial(n) % mod
    b = factorial(k) % mod
    c = factorial(n - k) % mod
    return (a * power_func(b, mod - 2, mod) * power_func(c, mod - 2, mod)) % mod
    
def power_func(a, b, mod):
    # a^b mod p を求める
    # bを2進数分解して高速累乗

    if b == 0: return 1
    if b % 2 == 0:
        d = power_func(a, b // 2, mod)
        return d * d % mod
    if b % 2 == 1:
        return (a * power_func(a, b - 1, mod)) % mod

#D
def D():
    n, k = LI()
    ans = 0
    for i in range(1,k+1):
        a = combination_mod(n - k + 1, i, mod)
        b = combination_mod(k - 1, i - 1, mod)
        print((a*b)%mod)
    return

#E
def E():
    return

#F
def F():
    return

#G
def G():
    return

#H
def H():
    return

#Solve
if __name__ == '__main__':
    B()
