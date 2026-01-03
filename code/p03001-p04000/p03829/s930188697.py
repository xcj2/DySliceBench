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
    a, b, c, d = LI()
    print(max(a * b, c * d))
    return

#B
def B():
    _ = II()
    s = S()
    d = {}
    d["I"] = 1
    d["D"] = -1
    ans = 0
    now = 0
    for i in s:
        now += d[i]
        ans = max(ans, now)
    print(ans)
    return

#C
def C():
    def primes2(n):
        """https://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n/3035188#3035188"""
        """ Returns  a list of primes < n """
        sieve = [True] * (n//2)
        for i in range(3,int(n**0.5)+1,2):
            if sieve[i//2]:
                sieve[i*i//2::i] = [False] * ((n-i*i-1)//(2*i)+1)
        return [2] + [2*i+1 for i in range(1,n//2) if sieve[i]]
    n = II()
    prime = primes2(n+1)
    d = []
    for i in prime:
        b = n
        f = 0
        while b:
            b = b // i
            f += b
        d.append(f%mod)
    ans = 1
    for i in d:
        ans *= (i + 1)
        ans %= mod
    print(ans)
    return

#D
def D():
    n, a, b = LI()
    x = LI()
    ans = 0
    for i in range(n - 1):
        ans += min((x[i + 1] - x[i]) * a, b)
    print(ans)
    return

#Solve
if __name__ == '__main__':
    D()
