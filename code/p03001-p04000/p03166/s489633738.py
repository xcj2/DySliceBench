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
    for i in range(n):l[i] = SR()
    return l
mod = 1000000007
sys.setrecursionlimit(100000)

#A
def A():
    n = I()
    h = LI()
    dp = [float("inf") for i in range(n)]
    dp[0] = 0
    for i in range(n-2):
        dp[i+1] = min(dp[i+1],dp[i]+abs(h[i+1]-h[i]))
        dp[i+2] = min(dp[i+2],dp[i]+abs(h[i+2]-h[i]))
    dp[n-1] = min(dp[n-1],dp[n-2]+abs(h[n-1]-h[n-2]))
    print(dp[n-1])
#B
def B():
    n,k = LI()
    h = LI()
    dp = [float("inf") for i in range(n)]
    dp[0] = 0
    for i in range(n):
        for j in range(1,min(n-i,k+1)):
            dp[i+j] = min(dp[i+j],dp[i]+abs(h[i+j]-h[i]))
    print(dp[n-1])

#C
def C():
    n = I()
    v = LIR(n)
    dp = [[0,0,0] for i in range(n+1)]
    for i in range(n):
        dp[i+1][0] = max(dp[i+1][0],dp[i][1]+v[i][0],dp[i][2]+v[i][0])
        dp[i+1][1] = max(dp[i+1][1],dp[i][2]+v[i][1],dp[i][0]+v[i][1])
        dp[i+1][2] = max(dp[i+1][2],dp[i][0]+v[i][2],dp[i][1]+v[i][2])
    print(max(dp[n]))

#D
def D():
    n,W = LI()
    g = LIR(n)
    dp = [[0 for i in range(W+1)] for j in range(n+1)]
    for i in range(n):
        for j in range(W+1)[::-1]:
            w,v = g[i]
            if j >= w:
                dp[i+1][j] = max(dp[i][j],dp[i][j-w]+v)
            else:
                dp[i+1][j] = max(dp[i+1][j],dp[i][j])
    print(max(dp[n]))
#E
def E():
    n,W = LI()
    g = LIR(n)
    V = 100000
    dp = [[float("inf") for i in range(V+1)] for j in range(n+1)]
    dp[0][0] = 0
    for i in range(n):
        for j in range(V+1)[::-1]:
            w,v = g[i]
            if j >= v:
                dp[i+1][j] = min(dp[i][j],dp[i][j-v]+w)
            else:
                dp[i+1][j] = min(dp[i+1][j],dp[i][j])

    for i in range(V+1)[::-1]:
        if dp[n][i] <= W:
            print(i)
            quit()

#F
def F():
    s = S()
    t = S()
    dp = [[0 for i in range(len(t)+1)] for j in range(len(s)+1)]
    for i in range(len(s)):
        for j in range(len(t)):
            if s[i] == t[j]:
                dp[i+1][j+1] = max(dp[i][j]+1,dp[i+1][j],dp[i][j+1])
            else:
                dp[i+1][j+1] = max(dp[i+1][j],dp[i][j+1])

    i = len(s)
    j = len(t)
    ans = ""
    while i > 0 and j > 0:
        if dp[i][j] == dp[i-1][j]:i -= 1
        elif dp[i][j] == dp[i][j-1]:j -= 1
        else:
            i -= 1
            j -= 1
            ans = s[i]+ans
    print(ans)
#G
def G():
    def dfs(x):
        if dp[x] != None:
            return dp[x]
        if len(v[x]) == 0:
            dp[x] = 0
            return 0
        else:
            res = 0
            for y in v[x]:
                res = max(res,dfs(y)+1)
            dp[x] = res
            return dp[x]
    n,m = LI()
    dp = [None for i in range(n)]
    v = [[] for i in range(n)]
    for i in range(m):
        x,y = LI()
        v[x-1].append(y-1)
    for i in range(n):
        dfs(i)
    print(max(dp))

#H
def H():
    h,w = LI()
    s = SR(h)
    dp = [[0 for i in range(w)] for j in range(h)]
    dp[0][0] = 1
    for i in range(h-1):
        for j in range(w-1):
            if s[i+1][j] == ".":
                dp[i+1][j] += dp[i][j]
                dp[i+1][j] %= mod
            if s[i][j+1] == ".":
                dp[i][j+1] += dp[i][j]
                dp[i][j+1] %= mod
    for j in range(w-1):
        if s[h-1][j+1] == ".":
            dp[h-1][j+1] += dp[h-1][j]
            dp[h-1][j+1] %= mod
    for i in range(h-1):
        if s[i+1][w-1] == ".":
            dp[i+1][w-1] += dp[i][w-1]
            dp[i+1][w-1] %= mod
    print(dp[h-1][w-1])

#I
def J():
    n = I()
    p = list(map(float, input().split()))
    dp = [[0 for i in range(n+1)] for j in range(n+1)]
    dp[0][0] = 1
    for i in range(n):
        for j in range(n+1):
            dp[i+1][j] = p[i]*dp[i][j-1]+(1-p[i])*dp[i][j]

    ans = 0
    m = math.floor(n/2)
    for i in range(m+1,n+1):
        ans += dp[n][i]
    print(ans)

#J
def K():
    n = I()


#Solve
if __name__ == "__main__":
    G()
