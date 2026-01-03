
def examD():
    N, W = LI()
    w = [0]*N
    v = [0]*N
    w[0], v[0] = LI()
    wbasic = w[0]
    for i in range(1,N):
        a, b = LI()
        w[i] = a-wbasic
        v[i] = b
    w[0] = 0
    dp =[[[0]*(3*N+1) for _ in range(N+1)]for _ in range(N+1)]
    for i in range(N):
        for j in range(N+1):
            for k in range(3*N+1):
                dp[i+1][j][k] = max(dp[i][j][k], dp[i+1][j][k])
                if w[i]<=k and j>=1:
                    if j*wbasic+k<=W:
                        dp[i+1][j][k] = max(dp[i][j-1][k-w[i]]+v[i], dp[i+1][j][k])
    ans = 0
    for v in dp[N]:
        ans = max(ans,max(v))
#        print(v)
    print(ans)


import sys
import copy
import bisect
from collections import Counter,defaultdict,deque
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def S(): return sys.stdin.readline().strip()
mod = 10**9 + 7
inf = float('inf')

examD()
