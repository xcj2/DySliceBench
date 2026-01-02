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
    a = LI()
    a.sort()
    a, b, c = a
    print(int(str(c)+str(b))+a)
    return

#B
def B():
    _, _, X, Y = LI()
    x = LI()
    y = LI()
    x.append(X)
    y.append(Y)
    x.sort()
    y.sort()
    print("No " * (x[-1] < y[0]) + "War")
    return

#C
def C():
    s = S()
    t = S()
    ds = defaultdict(int)
    dt = defaultdict(int)
    for i in range(len(s)):
        if ds[s[i]]:
            if ds[s[i]] == ord(t[i]):
                continue
            print("No")
            return
        if dt[t[i]]:
            if dt[t[i]] == ord(s[i]):
                continue
            print("No")
            return
        ds[s[i]] = ord(t[i])
        dt[t[i]] = ord(s[i])
    print("Yes")
    return

#D
def D():
    n, m = LI()
    if m == 1:
        print(1)
        return
    def combination_mod(n, k, mod):
        """ powを用いて(nCk) mod p を求める """ 
        """ nCk = n!/((n-k)!k!)を使用 """
        a = factorial[n]
        b = factorial[k] 
        c = factorial[n - k]
        return (a * pow(b, mod - 2, mod) * pow(c, mod - 2, mod)) % mod

    factorial = [None for i in range(200001)]
    factorial[0] = 1
    for i in range(1, 200001):
        factorial[i] = factorial[i - 1] * i
        if factorial[i] >= mod:
            factorial[i] %= mod
    def factorize(n):
        if n < 4:
            return {n:1}
        lis = {}
        i = 2   
        m = n
        while i**2 <= m:
            if m%i == 0:
                lis[i] = 0
                while m%i == 0:
                    m //= i
                    lis[i] += 1
            i += 1
        if m != 1:
            lis[m] = 1
        return lis
    d = factorize(m)
    ans = 1
    for a in d.values():
        ans *= combination_mod(a + n - 1, a, mod)
        if ans >= mod:
            ans %= mod
    print(ans)

    return

#Solve
if __name__ == '__main__':
    D()
