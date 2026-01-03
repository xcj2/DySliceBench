def examC():
    N, A = LI()
    x = LI()
    maxNX = max(x)*N
    dp = [[[0]*(maxNX+1) for _ in range(N+1)]for _ in range(N+1)]
    dp[0][0][0] = 1
    for i in range(1,N+1):
        cur = x[i-1]
        for l in range(N+1):
            for j in range(maxNX + 1):
                dp[l][i][j] += dp[l][i - 1][j]
        for l in range(1,N + 1):
            for j in range(cur, maxNX + 1):
                dp[l][i][j] += dp[l-1][i - 1][j - cur]
#    print(dp)
    ans = int(0)
    for i in range(1,min(maxNX//A+1,N+1)):
        ans += dp[i][N][i*A]
    print(ans)


import sys
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def S(): return sys.stdin.readline().strip()
mod = 10**9 + 7
inf = float('inf')

examC()
