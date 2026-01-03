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

n,ma,mb = li()
drugs = [tuple(li()) for _ in range(n)]

INF = 10**18

dp = [[[INF]*401 for _ in range(401)] for _ in range(41)]
dp[0][0][0] = 0

for i in range(n):
    ai, bi, ci = drugs[i]
    for a in range(401):
        for b in range(401):
            if a+ai <= 400 and b+bi <= 400:
                dp[i+1][a+ai][b+bi] = min(dp[i][a][b] + ci,
                                          dp[i+1][a+ai][b+bi])

            dp[i+1][a][b] = min(dp[i][a][b],
                                dp[i+1][a][b])
            
ans = INF
for ai in range(1,401):
    for bi in range(1,401):
        if ai/bi == ma/mb and dp[n][ai][bi] < INF:
            ans = min(ans, dp[n][ai][bi])
            
print(ans if ans < INF else -1)