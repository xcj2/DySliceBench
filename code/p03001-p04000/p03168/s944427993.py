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
dp = [[0]*(n+1) for _ in range(n+1)]

dp[0][0] = 1
for o in range(n):
    for u in range(n):
        if o+u >= n:
            continue
        
        dp[o][u+1] += (1-p[o+u]) * dp[o][u]
        dp[o+1][u] += p[o+u] * dp[o][u]
        
ans = 0
for o in range(n+1):
    u = n-o
    if o > u:
        ans += dp[o][u]
        
print(ans)