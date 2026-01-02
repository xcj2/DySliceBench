import sys
sys.setrecursionlimit(10**5+10)
input = sys.stdin.readline
def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LI2(N): return [list(map(int, sys.stdin.readline().split())) for i in range(N)]
def S(): return sys.stdin.readline()
def LS(): return sys.stdin.readline().split()
def LS2(N): return [sys.stdin.readline().split() for i in range(N)]
def FILL(i,h,w): return [[i for j in range(w)] for k in range(h)]
MOD = 1000000007
INF = float("inf")

H,W = LI()
c = [list(S()) for i in range(H)]
dp = FILL(0,H+1,W+1)
dp[0][0] = 1
for i in range(H):
    for j in range(W):
        if i+1<H:
            if c[i+1][j] == '.':
                dp[i+1][j] += dp[i][j]

        if j+1<W:
            if c[i][j+1] == '.':
                dp[i][j+1] += dp[i][j]

        dp[i][j] %= MOD


print(dp[H-1][W-1])
