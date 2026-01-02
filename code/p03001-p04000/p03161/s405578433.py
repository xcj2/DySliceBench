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

n,k = li()
h = list(li())
INF = float('inf')

dp = [INF]*n
dp[0] = 0

for idx in range(n):
    for jdx in range(min(idx, k)):
        dp[idx] = min(dp[idx],
                      dp[idx-jdx-1] + abs(h[idx]-h[idx-jdx-1]))

print(dp[-1])
