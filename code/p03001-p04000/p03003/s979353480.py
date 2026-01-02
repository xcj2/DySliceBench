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

n, m = li()
s = list(li())
t = list(li())

MOD = 10**9 + 7

dp = [[0]*(m+1) for _ in range(n+1)]
# for i in range(n+1):
#     dp[i][0] = 1
#
# for j in range(m+1):
#     dp[0][j] = 1

for i in range(n):
    for j in range(m):
        if s[i] == t[j]:
            dp[i+1][j+1] = (dp[i][j+1] + dp[i+1][j] + 1) % MOD
        else:
            dp[i + 1][j + 1] = (dp[i+1][j] + dp[i][j+1] - dp[i][j]) % MOD

print((dp[n][m] + 1) % MOD)
