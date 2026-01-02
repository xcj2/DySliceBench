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
    n = I()
    a,b = LI()
    c,d = LI()
    a -= 1
    b -= 1
    c -= 1
    d -= 1
    ans = float("inf")
    for w in range(1,1000):
        ans = min(ans, abs(a%w-b%w)+abs(a//w-b//w)+abs(c%w-d%w)+abs(c//w-d//w))
    print(ans)
    return

#B
def B():
    n = I()
    dp = [-1]*394
    dp[0] = 0
    for i in range(n):
        l,r,p = LI()
        for j in range(l,394):
            for k in range(l,r+1):
                if j-k >= 0:
                    if dp[j-k] >= 0:
                        if dp[j-k]+p > dp[j]:
                            dp[j] = dp[j-k]+p
    m = I()
    ans = [None for i in range(m)]
    for i in range(m):
        k = I()
        if dp[k] == -1:
            print(-1)
            quit()
        ans[i] = dp[k]
    for i in ans:
        print(i)
    return

#C
def C():
    def dfs(x):
        if f[x] != None:
            return f[x]
        res = 0
        for y,c in v[x]:
            res = max(res,dfs(y)+c)
        f[x] = res
        return f[x]
    n,m = LI()
    v = [[] for i in range(n)]
    f = defaultdict(lambda : None)
    f[0] = 0
    for i in range(m):
        a,b,c = LI()
        v[b].append((a,c))
    print(dfs(n-1))
    return

#D
def D():
    return

#E
def E():
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

#I
def I_():
    return

#J
def J():
    return

#Solve
if __name__ == "__main__":
    C()

