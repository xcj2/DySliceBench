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
h = list(li())

dp = [0]*n
dp[1] = abs(h[1]-h[0])
for i in range(1,n-1):
    dp[i+1] = min(dp[i-1] + abs(h[i+1]-h[i-1]),
                  dp[i] + abs(h[i+1]-h[i]))
    
print(dp[-1])