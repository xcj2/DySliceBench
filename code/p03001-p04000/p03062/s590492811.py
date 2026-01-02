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
    a, b, t = LI()
    print(b * (t // a))
    return

#B
def B():
    n = II()
    v = LI()
    c = LI()
    ans = 0
    for i in range(n):
        if v[i] > c[i]:
            ans += v[i] - c[i]
    print(ans)
    return

#C
def C():
    def gcd(a, b):
        if b > a: a, b = b, a
        while b:
            a, b = b, a % b
        return a
    n = II()
    a = LI()
    dp1 = [None] * (n - 1)
    dp1[0] = a[0]
    dp2 = [None] * (n - 1)
    dp2[-1] = a[-1]
    for i in range(1, n - 1):
        dp1[i] = gcd(dp1[i - 1], a[i])
        dp2[-i - 1] = gcd(dp2[-i], a[-i - 1])
    ans = 0
    dp1.insert(0, dp2[0])
    dp2.append(dp1[-1])
    for i in range(n):
        ans = max(ans, gcd(dp1[i], dp2[i]))
    print(ans)
    return

#D
def D():
    n = II()
    a = LI()
    positive = []
    negative = []
    for ai in a:
        if ai >= 0:
            positive.append(ai)
        else:
            negative.append(ai)
    positive.sort()
    negative.sort()
    ans = sum(positive) + sum(map(lambda x: abs(x), negative))
    if len(negative) & 1:
        ans -= 2 * min(positive[0] if positive else inf, abs(negative[-1]))
    print(ans)
    return

#Solve
if __name__ == '__main__':
    D()
