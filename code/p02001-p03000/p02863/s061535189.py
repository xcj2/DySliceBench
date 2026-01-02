import sys
from operator import itemgetter
from heapq import heapify, heappop, heappush
MAX_INT = int(10e15)
MIN_INT = -MAX_INT
mod = 1000000007
sys.setrecursionlimit(1000000)
def IL(): return list(map(int,input().split()))
def SL(): return input().split()
def I(): return int(sys.stdin.readline())
def S(): return input()

N, T = IL()
ab = [IL() for i in range(N)]
ab.sort(key=itemgetter(0))
#print(ab)

dp = [[0]*(T+1+3000+1) for _ in range(N+1)]
ans = 0
for i in range(N):
  for j in range(T+1+3000+1):
    time, deli = ab[i]
    if 0 <= j-time < T:
      dp[i + 1][j] = max(dp[i][j], dp[i][j - time] + deli)
    else:
      dp[i + 1][j] = dp[i][j]
    ans = max(ans, dp[i + 1][j])
print(ans)

#print(dp)
