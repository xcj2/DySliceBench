#!usr/bin/env python3
from collections import defaultdict,deque
from heapq import heappush, heappop
import sys
import math
import bisect
import random
def LI(): return [int(x) for x in sys.stdin.readline().split()]
def I(): return int(sys.stdin.readline())
def LS():return [list(x) for x in sys.stdin.readline().split()]
def S(): return list(sys.stdin.readline())[:-1]
def IR(n):
    return [I() for i in range(n)]
def LIR(n):
    return [LI() for i in range(n)]
def SR(n):
    return [S() for i in range(n)]
def LSR(n):
    return [LS() for i in range(n)]

sys.setrecursionlimit(1000000)
mod = 1000000007

#A
def A():
    n = I()

    return

#B
def B():
    def dfs(d,x,c):
        if d <= dp[x]:
            return
        dp[x] = d
        if not f[x]:
            f[x] = c
        for y in v[x]:
            dfs(d-1,y,c)
    n,m = LI()
    f = [0]*n
    v = [[] for i in range(n)]
    for i in range(m):
        a,b = LI()
        a -= 1
        b -= 1
        v[a].append(b)
        v[b].append(a)
    dp = defaultdict(lambda : -1)
    q = I()
    l = LIR(q)
    l = l[::-1]
    for x,d,c in l:
        x -= 1
        dfs(d,x,c)
    for i in f:
        print(i)
    return

#C
def C():
    n = I()

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
    B()
