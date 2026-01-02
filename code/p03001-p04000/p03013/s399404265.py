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
a = [ni() for _ in range(m)]
aset = set(a)

MOD = 10**9+7

dp = [0]*(n+1)
dp[0] = 1

for i in range(n):
    if i+1 in aset:
        continue

    if i == 0:
        dp[1] = 1

    else:
        dp[i+1] = dp[i] + dp[i-1]
        dp[i+1] %= MOD

print(dp[n])