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
wv = []
for _ in range(n):
    wv.append(tuple(li()))
    
MAX = 10**15
SIZE = 10**5+1
UPPER = 10**12
    
dp = [[MAX]*SIZE for _ in range(n+1)]
for item in range(n):
    dp[item][0] = 0

for item in range(n):
    wi, vi = wv[item]
    for value in range(1, SIZE):
        if value - vi >= 0:
            if 0 <= dp[item][value-vi] + wi <= w:
                dp[item+1][value] = min(dp[item][value],
                                        dp[item][value-vi] + wi)
                
            else:
                dp[item+1][value] = dp[item][value]
            
        else:
            dp[item+1][value] = dp[item][value]
        

ans = 0
for value in range(SIZE):
    if dp[n][value] <= UPPER:
        ans = max(ans, value)
        
print(ans)
            