import sys
from collections import defaultdict as dd
mod = pow(10, 9) + 7
mod2 = 998244353
inf = int(1e20)
def data(): return sys.stdin.readline().strip()
def out(*var, end="\n"): sys.stdout.write(" ".join(map(str, var))+end)
def l(): return list(sp())
def sl(): return list(ssp())
def sp(): return map(int, data().split())
def ssp(): return map(str, data().split())
def l1d(n, val=0): return [val for i in range(n)]
def l2d(n, m, val=0): return [l1d(n, val) for j in range(m)]


n = int(data())
arr = list(map(float, data().strip().split()))
dp = dd(lambda: dd(float))
dp[0][0] = 1
for i in range(1, n+1):
    dp[i][0] = dp[i-1][0] * (1.0 - arr[i-1])
answer = 0.0
for i in range(1, n+1):
    for j in range(1, n+1):
        dp[i][j] = arr[i-1] * dp[i-1][j-1] + (1.0 - arr[i-1]) * dp[i-1][j]
        if j >= n//2+1 and i == n:
            answer += dp[i][j]
out(answer)
