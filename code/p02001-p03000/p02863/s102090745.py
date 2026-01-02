def examE():
    N, T = LI()
    A, B = [0] * N, [0] * N
    for i in range(N):
        A[i], B[i] = LI()
    dp = [[0 for _ in range(T+ 1)] for _ in range(N + 1)]
    dp2 = [[0 for _ in range(T+ 1)] for _ in range(N + 1)]
    for i in range(N):
        for j in range(A[i],T+1):
            dp[i + 1][j] = max(dp[i + 1][j], dp[i][j - A[i]] + B[i])
            dp2[i + 1][j] = max(dp2[i + 1][j], dp2[i][j - A[i]] + B[i])
        for j in range(1,T+1):
            dp2[i+1][j] = max(dp2[i+1][j], dp[i][j-1] + B[i], dp2[i][j])
            dp[i + 1][j] = max(dp[i + 1][j], dp[i][j])
#    print(dp[N][T])
    ans = dp2[N][T]
    print(ans)

import sys,copy,bisect,itertools
from heapq import heappop,heappush,heapify
from collections import Counter,defaultdict,deque
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def S(): return sys.stdin.readline().strip()
mod = 10**9 + 7
inf = float('inf')

examE()
