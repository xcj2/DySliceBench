import sys
stdin = sys.stdin

sys.setrecursionlimit(10 ** 7)

def li(): return map(int, stdin.readline().split())
def li_(): return map(lambda x: int(x) - 1, stdin.readline().split())
def lf(): return map(float, stdin.readline().split())
def ls(): return stdin.readline().split()
def ns(): return stdin.readline().rstrip()
def lc(): return list(ns())
def ni(): return int(stdin.readline())
def nf(): return float(stdin.readline())

n, k = li()
MOD = 10**9 + 7

dp = [[[0]*(n*n+1) for _ in range(n+1)] for _ in range(n+1)]

dp[0][0][0] = 1

for x in range(1, n+1):
    for y in range(n+1):
        for z in range(n*n+1):
            dp[x][y][z] = ((2*y + 1) * dp[x-1][y][z-2*y] if z-2*y >= 0 else 0)\
                            + ((y+1)**2 * dp[x-1][y+1][z-2*y] if (z-2*y >= 0 and y+1 <= n) else 0)\
                            + (dp[x-1][y-1][z-2*y] if (z-2*y >= 0 and y-1 >= 0) else 0)
            dp[x][y][z] %= MOD

print(dp[n][0][k])