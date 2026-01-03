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

n, a = li()
x = list(li())

dp = [[[0]*(50*50+1) for _ in range(n+1)] for _ in range(n+1)]
dp[0][0][0] = 1

for i in range(1, n+1):
    for j in range(n+1):
        for k in range(50*50 + 1):
            dp[i][j][k] += (dp[i-1][j-1][k-x[i-1]] if (j-1 >= 0 and k-x[i-1] >= 0) else 0)\
                            + dp[i-1][j][k]

ans = 0
for i in range(1, n+1):
    ans += dp[n][i][a*i]

print(ans)