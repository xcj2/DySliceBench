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
    a,b,c = LI()
    ans = 10 ** 5
    ans = min(ans, a + b)
    ans = min(ans, a + c)
    ans = min(ans, c + b)
    print(ans)
    return

#B
def B():
    n = II()
    w = LI()
    ans = inf
    for i in range(n):
        ans = min(ans, abs(sum(w[:i]) - sum(w[i:])))
    print(ans)
    return

#C
def C():
    n, m = LI()
    a = IR(m)+[inf]
    dp = [0] * (n + 3)
    dp[0] = 1
    for i in range(n + 1):
        if a[bisect_left(a, i + 1)] != i + 1:
            dp[i + 1] += dp[i] % mod
        if a[bisect_left(a, i + 2)] != i + 2:
            dp[i + 2] += dp[i] % mod
    print(dp[n] % mod)
    return

#D
def D():
    h, w = LI()
    s = SR(h)
    dp = [[0] * w for _ in range(h)]
    for x in range(w):
        for y in range(h):
            if s[y][x] == ".":
                dp[y][x] += 1
    for y in range(h):
        x = 0
        q = 0
        while 0 <= x < w:
            if s[y][x] == ".":
                dp[y][x] += q
                q += 1
            else:
                q = 0
            x += 1
        x = w - 1
        q = 0
        while 0 <= x < w:
            if s[y][x] == ".":
                dp[y][x] += q
                q += 1
            else:
                q = 0
            x -= 1
    for x in range(w):
        y = 0
        q = 0
        while 0 <= y < h:
            if s[y][x] == ".":
                dp[y][x] += q
                q += 1
            else:
                q = 0
            y += 1
        y = h - 1
        q = 0
        while 0 <= y < h:
            if s[y][x] == ".":
                dp[y][x] += q
                q += 1
            else:
                q = 0
            y -= 1
    print(max(map(lambda x: max(x), dp)))
    return


#Solve
if __name__ == '__main__':
    D()
