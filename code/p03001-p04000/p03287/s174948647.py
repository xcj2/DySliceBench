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
    n, k = LI()
    if n % k:
        print(1)
    else:
        print(0)
    return

#B
def B():
    n = II()
    dp = [0] * (100 + 1)
    dp[4] = 1
    dp[7] = 1
    for i in range(8,n + 1):
        if dp[i - 4] or dp[i - 7]:
            dp[i] = 1
    print(["No", "Yes"][dp[n]])
    return

#C
def C():
    n = II()
    ans = []
    if n == 0:
        print(0)
    while n:
        ans.append("{}".format(n % 2))
        n = (n-1) // -2
    print("".join(ans[::-1]))
    return

#D
def D():
    n, m = LI()
    a = LI()
    a = list(map(lambda x: x % m, a))
    a = [0] + a
    d = defaultdict(int)
    ans = 0
    for i in range(1, n + 1):
        a[i] += a[i - 1]
        a[i] %= m
        d[a[i]] += 1
    d[0] += 1
    for value in d.values():
        ans += value * (value - 1) // 2
    print(ans)
    return

#Solve
if __name__ == '__main__':
    D()
