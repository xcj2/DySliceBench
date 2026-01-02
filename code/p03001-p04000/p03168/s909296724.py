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

n = ni()
p = list(lf())

dp = [0]*(n+1)
dp[0] = 1-p[0]
dp[1] = p[0]
for i in range(2,n+1):
    for j in range(i, 0, -1):
        dp[j] = p[i-1]*dp[j-1] + (1-p[i-1])*dp[j]
        
    dp[0] *= (1-p[i-1])
    
print(sum(dp[(n+1)//2:]))