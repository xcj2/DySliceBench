def examE(mod):
    N, X, Y, Z = LI()
    L = 2**(X+Y+Z-1)
    XYZ = (1 << (X + Y + Z - 1)) | (1 << (Y + Z - 1)) | (1 << (Z - 1))
    dp = [[0]*L for _ in range(N+1)]
    dp[0][0] = 1
    for i in range(N):
        for j in range(L):
            for k in range(1,11):
                next = (j<<k)|(1<<(k-1))
                if next&XYZ==XYZ:
                    continue
                else:
                    dp[i+1][next%L] += dp[i][j]
                    dp[i + 1][next % L] %=mod
    ans = pow(10,N,mod)-sum(dp[-1])%mod
    if ans<0:
        ans +=mod
    print(ans)

import sys
import copy
import bisect
import heapq
from collections import Counter,defaultdict,deque
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def S(): return sys.stdin.readline().strip()
mod = 10**9 + 7
inf = float('inf')

examE(mod)
