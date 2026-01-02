import sys
sys.setrecursionlimit(10**8)
def ii(): return int(sys.stdin.readline())
def mi(): return map(int, sys.stdin.readline().split())
def li(): return list(map(int, sys.stdin.readline().split()))
def li2(N): return [list(map(int, sys.stdin.readline().split())) for i in range(N)]
def dp2(ini, i, j): return [[ini]*i for i2 in range(j)]
def dp3(ini, i, j, k): return [[[ini]*i for i2 in range(j)] for i3 in range(k)]
#import bisect #bisect.bisect_left(B, a)
#from collections import defaultdict #d = defaultdict(int) d[key] += value

H, W = mi()
A = [input() for i in range(H)]

dp = dp2(float("inf"), W, H)
dp[0][0] = 1
INF = 10**9+7

for i in range(H):
    for j in range(W):
        if i==0 and j == 0:
            dp[0][0] = 1
            continue
        if A[i][j] == '.':
            dp[i][j] = 0
            if i > 0 and A[i-1][j] == '.':
                dp[i][j] = (dp[i][j] + dp[i-1][j]) % INF
            if j > 0 and A[i][j-1] == '.':
                dp[i][j] = (dp[i][j] + dp[i][j-1]) % INF

print(dp[H-1][W-1])