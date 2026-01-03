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
    a, b = LS()
    if a == b:
        print("H")
    else:
        print("D")
    return

#B
def B():
    w, a, b = LI()
    a, b = min(a, b), max(a, b)
    if w + a >= b:
        print(0)
        return
    print(b-a-w)
    return

#C
def C():
    n = II()
    x = 0
    for i in range(1, 10 ** 5):
        x += i
        if n <= x:
            print(i)
            return
    return

#D
def D():
    n, k = LI()
    a = LI()
    a.sort()
    ok = n
    ng = -1
    def f(x):
        dp = [False] * (k)
        dp[0] = True
        kx = k - a[x]
        for i in range(n):
            if i == x: continue
            ai = a[i]
            for j in range(k - 1, ai - 1, -1):
                if dp[j - ai]:
                    dp[j] = True
                    if kx <= j:
                        return True
        for j in range(max(0, k - a[x]), k):
            if dp[j]:
                return True
        return False
    while ok - ng > 1:
        mid = (ok + ng) // 2
        if f(mid):
            ok = mid
        else:
            ng = mid
    print(ng + 1)
    return

#Solve
if __name__ == '__main__':
    D()
