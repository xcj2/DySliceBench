import sys

sys.setrecursionlimit(10**7)
def I(): return int(sys.stdin.readline().rstrip())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))  #空白あり
def LI2(): return list(map(int,sys.stdin.readline().rstrip()))  #空白なし
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())  #空白あり
def LS2(): return list(sys.stdin.readline().rstrip())  #空白なし

H,W,K = MI()
mod = 10**9+7

if W == 1:
    print(1)
    exit()

fib = [1,1,2,3,5,8,13,21,34]

dp = [[0]*(W+1) for _ in range(H+1)]
dp[0][1] = 1
for i in range(1,H+1):
    for j in range(1,W+1):
        if W == 2:
            if j == 1:
                dp[i][j] = dp[i-1][j] + dp[i-1][j+1]
                dp[i][j] %= mod
            else:
                dp[i][j] = dp[i-1][j] + dp[i-1][j-1]
                dp[i][j] %= mod
        else:
            if j == 1:
                dp[i][j] = dp[i-1][j+1]*fib[W-2] + dp[i-1][j]*fib[W-j]
                dp[i][j] %= mod
            elif j == W:
                dp[i][j] = dp[i-1][j-1]*fib[W-2] + dp[i-1][j]*fib[j-1]
                dp[i][j] %= mod
            else:
                dp[i][j] = dp[i-1][j-1]*fib[j-2]*fib[W-j] + dp[i-1][j+1]*fib[j-1]*fib[W-j-1] + dp[i-1][j]*(fib[W-j]*fib[j-1])
                dp[i][j] %= mod

print(dp[H][K])
