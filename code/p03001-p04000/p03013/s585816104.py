#!usr/bin/env python3
from collections import defaultdict
from collections import deque
from heapq import heappush, heappop
import sys
import math
import bisect
import random
def LI(): return list(map(int, sys.stdin.readline().split()))
def I(): return int(sys.stdin.readline())
def LS():return list(map(list, sys.stdin.readline().split()))
def S(): return list(sys.stdin.readline())[:-1]
def IR(n):
    l = [None for i in range(n)]
    for i in range(n):l[i] = I()
    return l
def LIR(n):
    l = [None for i in range(n)]
    for i in range(n):l[i] = LI()
    return l
def SR(n):
    l = [None for i in range(n)]
    for i in range(n):l[i] = S()
    return l
def LSR(n):
    l = [None for i in range(n)]
    for i in range(n):l[i] = LS()
    return l
sys.setrecursionlimit(1000000)
mod = 1000000007

#A
def A():
    p,q,r = LI()
    print(p+q+r-max(p,q,r))
    return

#B
def B():
    n = I()
    w = LI()
    ans = float("inf")
    for i in range(n):
        m = sum(w[:i])
        l = sum(w[i:])
        ans = min(ans,abs(m-l))
    print(ans)
    return

#C
def C():
    n,m = LI()
    f = defaultdict(lambda : 1)
    for i in range(m):
        a = I()
        f[a] = 0
    dp = [0 for i in range(n+1)]
    dp[0] = 1
    for i in range(1,n+1):
        if f[i]:
            dp[i] = dp[i-1]+dp[i-2]
            dp[i] %= mod
    print(dp[n])
    return

#D
def D():
    n = I()

    return

#E
def E():
    n = I()

    return

#F
def F():
    n = I()

    return

#Solve
if __name__ == "__main__":
    C()
