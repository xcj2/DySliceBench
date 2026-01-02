import sys
sys.setrecursionlimit(10**8)
def ii(): return int(sys.stdin.readline())
def mi(): return map(int, sys.stdin.readline().split())
def li(): return list(map(float, sys.stdin.readline().split()))
def li2(N): return [list(map(int, sys.stdin.readline().split())) for i in range(N)]
def dp2(ini, i, j): return [[ini]*i for i2 in range(j)]
def dp3(ini, i, j, k): return [[[ini]*i for i2 in range(j)] for i3 in range(k)]
#import bisect #bisect.bisect_left(B, a)
#from collections import defaultdict #d = defaultdict(int) d[key] += value

N = ii()
P = li()

dp = dp2(0, N+1, N)
dp[0][0] = 1 - P[0]
dp[0][1] = P[0]

for i in range(1, N):
    for j in range(i+1):
        dp[i][j] += dp[i-1][j] * (1-P[i])
        dp[i][j+1] += dp[i-1][j] * P[i]

print(sum(dp[N-1][(N//2+1):])) 