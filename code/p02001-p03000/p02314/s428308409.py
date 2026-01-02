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
C = li()

'''
# 二次元DP
dp = dp2(float('inf'), N+1, M+1)
dp[0][0] = 0
for i in range(1, M+1):
    for j in range(N+1):
        #if j == 0:
            #dp[i][j] = 0
        dp[i][j] = min(dp[i-1][j], dp[i][j])
        c = C[i-1]
        if j+c <= N:
            dp[i][j+c] = min(dp[i][j]+1, dp[i-1][j+c])
#print(dp)
print(dp[M][N])
'''

# 1次元DP
dp = [float('inf') for i in range(N+1)]
dp[0] = 0

for i in range(M):
    for j in range(N+1):
        c = C[i]
        if j+c <= N:
            dp[j+c] = min(dp[j]+1, dp[j+c])

print(dp[N])
