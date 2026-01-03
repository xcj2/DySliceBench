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
    n = II()
    k = II()
    x = II()
    y = II()
    ans = 0
    for i in range(n):
        if i >= k:
            ans += y
        else:
            ans += x
    print(ans)
    return

#B
def B():
    w = S()
    d = defaultdict(int)
    for s in w:
        d[s] += 1
    for di in d.values():
        if di % 2:
            print("No")
            return
    print("Yes")
    return

#C
def C():
    n, a = LI()
    x = LI()
    sumx = [0] * n
    for i in range(n):
        sumx[i] = sumx[i - 1] + x[i]
    dp = [[[0] * (n+1) for i in range(sumx[-1] + 1)] for i in range(n)]
    for i in range(n):
        dp[i][x[i]][1] = 1
    for i in range(1, n):
        for s in range(sumx[i] + 1):
            for k in range(1, i + 2):
                if  s >= x[i]:
                    dp[i][s][k] += dp[i - 1][s - x[i]][k - 1]
                dp[i][s][k] += dp[i - 1][s][k]
    ans = 0
    for i in range(1, n + 1):
        if a * i > sumx[-1]:
            break
        ans += dp[-1][a * i][i]
    print(ans)
    return

#D
def D():
    return


#Solve
if __name__ == '__main__':
    C()
