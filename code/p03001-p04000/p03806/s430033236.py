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
drugs = []
for _ in range(n):
    drugs.append(tuple(li()))
    
dp = [[[10**10]*(401) for _ in range(401)] for _ in range(n+1)]
dp[0][0][0] = 0

for i in range(n):
    ca, cb, cc = drugs[i]
    for aa in range(401):
        for bb in range(401):
            if 0 <= aa - ca <= 400 and 0 <= bb - cb <= 400:
                dp[i+1][aa][bb] = min(dp[i][aa-ca][bb-cb] + cc,
                                      dp[i][aa][bb])
                
            else:
                dp[i+1][aa][bb] = dp[i][aa][bb]

ans = 10**10     
for aa in range(1,401):
    for bb in range(1,401):
        if (aa/bb) == (ma/mb):
            ans = min(ans, dp[n][aa][bb])
            
if ans == 10**10:
    print(-1)
else:
    print(ans)