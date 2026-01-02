import sys
import math
from collections import deque
import heapq
MAX_INT = int(10e10)
MIN_INT = -MAX_INT
mod = 1000000007
sys.setrecursionlimit(1000000)
def IL(): return list(map(int,input().split()))
def SL(): return input().split()
def I(): return int(sys.stdin.readline())
def S(): return input()

N = I()
a = IL()
b = []
for i in range(N):
  b.append((a[i], i))
b.sort(reverse=True)

dp = [[0]*(N+1) for i in range(N+1)] # dp[i番目まで][左からj番目]

for i in range(N):
  happy, ID = b[i]
  #print(b[i])
  for l in range(i+1):
    lcnt = l
    rcnt = i - lcnt
    r = N-1 - rcnt
    if i > l-1:
      dp[i+1][l+1] = max(dp[i+1][l+1], dp[i][l] + happy*abs(ID - l))
      dp[i+1][l] = max(dp[i+1][l], dp[i][l] + happy*abs(ID - r))
    else:
      break
    #print(l,r)
    #print(dp)
  #print("---")
print(max(dp[-1]))