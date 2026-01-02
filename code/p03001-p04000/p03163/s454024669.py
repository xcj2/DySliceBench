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

n,w = li()
dp = [[0]*(w+1) for _ in range(n+1)]

for i in range(1,n+1):
    wi, vi = li()
    for j in range(1,w+1):
        if j-wi >= 0:
            dp[i][j] = max(dp[i-1][j],
                           dp[i-1][j-wi] + vi)
        else:
            dp[i][j] = dp[i-1][j]
            
print(dp[n][w])