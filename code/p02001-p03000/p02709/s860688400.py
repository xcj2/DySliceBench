import bisect, collections, copy, heapq, itertools, math, string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def MI(): return map(int, sys.stdin.readline().rstrip().split())
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

N = I()
A = LI()
A_tup = [(0, 0)] * N
for i in range(N):
    A_tup[i] = (A[i], i)
A_tup.sort(reverse=True)

dp = [[0] * (N + 1) for i in range(N + 1)]
dp[0][0] = 0
for i in range(N):
    pi = A_tup[i][1]
    for j in range(i + 1):
        k = i - j
        dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j] + (pi - j) * A_tup[i][0])
        dp[i + 1][j] = max(dp[i + 1][j], dp[i][j] + (N - k - 1 - pi) * A_tup[i][0])

ans = 0
for i in range(N):
    ans = max(ans, dp[N][i])
print(ans)