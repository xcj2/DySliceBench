import sys
stdin = sys.stdin
 
sys.setrecursionlimit(10**5) 
 
def li(): return map(int, stdin.readline().split())
def li_(): return map(lambda x: int(x)-1, stdin.readline().split())
def lf(): return map(float, stdin.readline().split())
def ls(): return stdin.readline().split()
def ns(): return stdin.readline().rstrip()
def lc(): return list(ns())
def ni(): return int(stdin.readline())
def nf(): return float(stdin.readline())

from itertools import accumulate

n,k = li()
a = list(li())
MOD = 10**9+7

dp = [[0]*(k+1) for _ in range(n+1)]
for i in range(k+1):
    if i <= a[0]:
        dp[1][i] = 1

if n > 1:   
    dp[1] = list(accumulate(dp[1]))
        
for i in range(1,n+1):
    dp[i][0] = 1
    
for i in range(2,n+1):
    for m in range(1,k+1):
        if m-a[i-1] > 0:
            dp[i][m] = dp[i-1][m] - dp[i-1][m-a[i-1]-1]
        else:
            dp[i][m] = dp[i-1][m]
        dp[i][m] %= MOD
    
    if i < n:
        dp[i] = list(accumulate(dp[i]))
        
print(dp[n][k])