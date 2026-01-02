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

z = pow(2,mod-2,mod)

a.sort()

dp = [[0]*(s+1) for i in range(n+1)]
for i in range(n+1):
    dp[i][0] = pow(2,n,mod)

for i in range(1,n+1):
    x = a[i-1]
    for j in range(1,s+1):
        if 0<=j-x:
            dp[i][j] += (dp[i-1][j-x]*z + dp[i-1][j])%mod
        else:
            dp[i][j] += dp[i-1][j]


print(dp[n][s]%mod)


