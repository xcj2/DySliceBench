# 入力
import sys
stdin = sys.stdin

def li(): return [int(x) for x in stdin.readline().split()]
def li_(): return [int(x)-1 for x in stdin.readline().split()]
def lf(): return [float(x) for x in stdin.readline().split()]
def ls(): return stdin.readline().split()
def ns(): return stdin.readline().rstrip()
def lc(): return list(ns())
def ni(): return int(ns())
def nf(): return float(ns())

n, ma, mb = li()
a,b,c = list(), list(), list()
for _ in range(n):
    ai,bi,ci = li()
    a.append(ai)
    b.append(bi)
    c.append(ci)
    
INF = 10**5
dp = [[[INF for _ in range(10*n+1)] for _ in range(10*n+1)] for _ in range(n+1)]
dp[0][0][0] = 0

for dr in range(n):
    for wa in range(10*n+1):
        for wb in range(10*n+1):
            dp[dr+1][wa][wb] = min(dp[dr][wa][wb], dp[dr][wa-a[dr]][wb-b[dr]] + c[dr])
            
ans = INF
k = 1
while k*ma <= 10*n and k*mb <= 10*n:
    ans = min(ans, dp[n][k*ma][k*mb])
    k += 1
    
if ans == INF:
    print(-1)
else:
    print(ans)