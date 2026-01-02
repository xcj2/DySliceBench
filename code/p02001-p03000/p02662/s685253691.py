import sys
sys.setrecursionlimit(10**7)

readline = sys.stdin.buffer.readline
def readstr():return readline().rstrip().decode()
def readstrs():return list(readline().decode().split())
def readint():return int(readline())
def readints():return list(map(int,readline().split()))
def printrows(x):print('\n'.join(map(str,x)))
def printline(x):print(' '.join(map(str,x)))

n,s = readints()
a = readints()

mod = 998244353

dp = [[0]*(s+1) for i in range(n+1)]
dp[0][0] = 1

for i in range(1,n+1):
    x = a[i-1]
    for j in range(s+1):
        dp[i][j] = dp[i-1][j]*2
        if 0<=j-x:
            dp[i][j] += dp[i-1][j-x]
        dp[i][j]%=mod


print(dp[n][s])


