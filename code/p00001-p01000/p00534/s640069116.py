import sys
sys.setrecursionlimit(10**8)
def ii(): return int(sys.stdin.readline())
def mi(): return map(int, sys.stdin.readline().split())
def li(): return list(map(int, sys.stdin.readline().split()))
def li2(N): return [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
def dp2(ini, i, j): return [[ini]*i for _ in range(j)]
def dp3(ini, i, j, k): return [[[ini]*i for _ in range(j)] for _ in range(k)]
#import bisect #bisect.bisect_left(B, a)
#from collections import defaultdict #d = defaultdict(int) d[key] += value
#from itertools import accumulate #list(accumulate(A))

N, M = mi()
C = [ii() for _ in range(N)]
W = [ii() for _ in range(M)]

dp = dp2(float('inf'), N+1, M+1)
dp[0][0] = 0

for i in range(M):
    for j in range(N+1):
        if j+1 <= N:
            dp[i+1][j+1] = min(dp[i][j]+W[i]*C[j], dp[i+1][j+1])
        dp[i+1][j] = min(dp[i][j], dp[i+1][j])

print(dp[M][N])
