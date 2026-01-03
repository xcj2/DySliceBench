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
    a, b, c = LS()
    if a[-1] == b[0] and b[-1] == c[0]:
        print("YES")
    else:
        print("NO")
    return

#B
def B():
    a, b, c = LI()
    for i in range(1, b):
        if a * i % b == c:
            print("YES")
            return
    print("NO")
    return

#C
def C():
    _, T = LI()
    t = LI()
    ans = 0
    now = t[0]
    for i in t[1:]:
        if now + T <= i:
            ans += T
        else:
            ans += i - now
        now = i
    print(ans + T)

    return

#D
def D():
    n, W = LI()
    wv = LIR(n)
    wv.sort()
    dp = [-inf] * ((3 * n + 1) * n + 1)
    dp[0] = 0
    minw =  wv[0][0]
    if minw <= 3 * n:
        for w, v in wv:
            for i in range((3 * n + 1) * n, w - 1, -1):
                dp[i] = max(dp[i - w] + v, dp[i])
        print(max(dp[:W + 1]))
    else:
        for w, v in wv:
            w -= minw
            for i in range(min(W // minw, n - 1), 0, -1):
                for k in range(3 * n, w - 1, -1):
                    dp[(3 * n + 1) * i + k] = max(dp[(3 * n + 1) * (i - 1) + k - w] + v, dp[(3 * n + 1) * i + k])
        print(max(dp[:W // minw * (3 * n + 1) + W % minw + 1]))
    return

#Solve
if __name__ == '__main__':
    D()
