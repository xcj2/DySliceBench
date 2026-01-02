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

N = ii()
l = li2(N)


'''
# メモ化再帰
dp = dp2(-1, N, N)
def rec(i, j):
    if dp[i][j] != -1:
        return dp[i][j]
    if i == j:
        dp[i][j] = 0
        return 0
    if j-i == 1:
        dp[i][j] = l[i][0] * l[i][1] * l[j][1]
        return dp[i][j]
    res = float('inf')
    for k in range(i, j):
        res = min(res, rec(i, k) + rec(k+1, j) + l[i][0] * l[k+1][0] * l[j][1])
    dp[i][j] = res
    return res

print(rec(0, N-1))
'''

# 2次元DP

dp = dp2(float('inf'), N, N)

for i in range(N):
    dp[i][i] = 0

for h in range(1, N):
    for i in range(N):
        if i+h < N:
            if h == 1:
                dp[i][i+h] = l[i][0] * l[i][1] * l[i+h][1]
            else:
                #dp[i][i+h] = dp[i][i+h-1] + l[i][0] * l[i+h][0] * l[i+h][1]
                for r in range(i, i+h):
                    dp[i][i+h] = min(dp[i][i+h], dp[i][r]+dp[r+1][i+h]+l[i][0]*l[r+1][0]*l[i+h][1])
#print(dp)
print(dp[0][N-1])
