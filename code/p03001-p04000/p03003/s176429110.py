#!usr/bin/env python3
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
    x, a = LI()
    if x < a:
        print(0)
    else:
        print(10)
    return

#B
def B():
    n, x = LI()
    L = LI()
    ans = 0
    c = 1
    for i in L:
        ans += i
        if ans <= x:
            c += 1
            continue
        break
    print(c)
    return

#C
def C():
    W, H, x, y = LI()
    a = W * H / 2
    b = 0
    if W/2 == x and H/2 == y:
        b = 1
    print(a,b)
    return

#D
def D():
    n, k = LI()
    a = LI()
    dp = [0] * (n)
    for i in range(n):
        dp[i] += dp[i - 1] + a[i]
    ans = 0
    dp.insert(0, 0)
    #print(dp)
    for i in range(1,n+1):
        ai = bisect_left(dp, k + dp[i-1])
        ans += n+1 - ai
        #print(ai, i, k + dp[i-1])
    print(ans)

    return

#E
def E():
    n, m = LI()
    s = LI()
    t = LI()
    dp = [[0] * (m+1) for i in range(n+1)]
    for i in range(n+1):
        dp[i][0] = 1
    for k in range(m + 1):
        dp[0][k] = 1
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s[i - 1] == t[j - 1]:
                dp[i][j] += (dp[i-1][j]+dp[i][j-1])%mod
            else:
                dp[i][j] += (dp[i-1][j]+dp[i][j-1]-dp[i-1][j-1])%mod
    print(dp[n][m])
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
    E()
