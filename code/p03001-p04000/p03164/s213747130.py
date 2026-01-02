import sys
stdin = sys.stdin
 
sys.setrecursionlimit(10**8) 
 
def li(): return map(int, stdin.readline().split())
def li_(): return map(lambda x: int(x)-1, stdin.readline().split())
def lf(): return map(float, stdin.readline().split())
def ls(): return stdin.readline().split()
def ns(): return stdin.readline().rstrip()
def lc(): return list(ns())
def ni(): return int(stdin.readline())
def nf(): return float(stdin.readline())

INF = pow(10,15)
SIZE = pow(10,5)+1

n,w = li()
wv = [tuple(li()) for _ in range(n)]

dp = [[INF]*(SIZE + 10) for _ in range(n+1)]
for i in range(n+1):
    dp[i][0] = 0

for idx in range(n):
    wi, vi = wv[idx]
    for val in range(SIZE):
        if val - vi < 0:
            dp[idx+1][val] = min(dp[idx+1][val],
                                 dp[idx][val])
            
        else:
            dp[idx+1][val] = min(dp[idx+1][val],
                                 dp[idx][val-vi]+wi,
                                 dp[idx][val])
        

ans = 0     
for val in range(SIZE):
    if dp[n][val] <= w:
        ans = val
        
print(ans)
    