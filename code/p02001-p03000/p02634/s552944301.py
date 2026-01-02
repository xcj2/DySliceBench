import sys
def input():return sys.stdin.readline()[:-1]
def N(): return int(input())
def NM():return map(int,input().split())
def L():return list(NM())
def LN(n):return [N() for i in range(n)]
def LL(n):return [L() for i in range(n)]

a,b,c,d=NM()
dp=[[0]*(d+1) for i in range(c+1)]
dp[a][b]=1
mod=998244353
for i in range(a+1,c+1):
    dp[i][b]=dp[i-1][b]*b%mod
for j in range(b+1,d+1):
    dp[a][j]=dp[a][j-1]*a%mod
for i in range(a+1,c+1):
    for j in range(b+1,d+1):
        dp[i][j]=(dp[i][j-1]*i+dp[i-1][j]*j-(i-1)*(j-1)*dp[i-1][j-1])%mod
print(dp[c][d])