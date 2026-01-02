#!/usr/bin/env python3
from collections import defaultdict,deque
from heapq import heappush, heappop
from bisect import bisect_left, bisect_right
import sys, random, itertools, math
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
def IR(n): return [II() for _ in range(n)]
def LIR(n): return [LI() for _ in range(n)]
def FR(n): return [IF() for _ in range(n)]
def LFR(n): return [LI() for _ in range(n)]
def LIR_(n): return [LI_() for _ in range(n)]
def SR(n): return [S() for _ in range(n)]
def LSR(n): return [LS() for _ in range(n)]
mod = 1000000007
inf = float("INF")

#solve
def solve():
    n, k = LI()
    a = LI()
    a.sort(key=abs, reverse=True)
    ans = 1
    if n - a.count(0) < k:
        print(0)
        return
    t = 0
    L = None
    R= inf
    for ai in a[:k]:
        if ai < 0:
            t ^= 1
            L = ai
        if ai > 0:
            R = ai
        ans *= ai
        ans %= mod
    if k == n:
        print(ans)
        return
    if t:
        if max(a) <= 0:
            ans = 1
            for i in range(k):
                ans *= a[-i - 1]
                ans %= mod
            print(ans)
        else:
            A = min(a[k:])
            B = max(a[k:])
            if A >= 0:
                ans *= pow(L, mod - 2, mod)
                ans *= B
            else:
                if A * L > B * R:
                    ans *= pow(R, mod - 2, mod)
                    ans *= A
                else:
                    ans *= pow(L, mod - 2, mod)
                    ans *= B
            print(ans % mod)
    else:
        print(ans)
    return


#main
if __name__ == '__main__':
    solve()
