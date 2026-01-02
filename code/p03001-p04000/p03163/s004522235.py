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
    
dp = [[0]*(w+1) for _ in range(n+1)]

for item in range(n):
    wi,vi = wv[item]
    for weight in range(w+1):
        if weight - wi >= 0:
            dp[item+1][weight] = max(dp[item][weight],
                                     dp[item][weight-wi] + vi)
            
        else:
            dp[item+1][weight] = dp[item][weight]
            
            
print(dp[n][w])