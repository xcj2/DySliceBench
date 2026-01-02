import math

def Next(): return input()
def NextInt(): return int(Next())
def NextInts(): return map(int,input().split())
def Nexts(): return map(str,input().split())
def NextIntList(): return list(map(int,input().split()))
def RowInts(n): return [input() for i in range(n)]

n,k = NextInts()
da = NextIntList()
for i in range(n):
    da[i]-=1

dp = [[0 for i in range(n)] for i in range(61)]

dp[0] = da

for i in range(60):
    for j in range(n):
        dp[i+1][j] = dp[i][dp[i][j]]

ans = 0
for i in range(61):
    if k&1:
        ans = dp[i][ans]
    k >>= 1
print(ans+1)