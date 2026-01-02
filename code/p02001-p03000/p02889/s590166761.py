import math
import sys
MAX_INT = int(10e10)
MIN_INT = -MAX_INT
mod = 1000000007
sys.setrecursionlimit(1000000)
def IL(): return list(map(int,input().split()))
def SL(): return input().split()
def I(): return int(sys.stdin.readline())
def S(): return input()

N, M, L = IL()
abc = [IL() for _ in range(M)]
Q = I()
q = [IL() for _ in range(Q)]

dp1 = [[MAX_INT]*N for _ in range(N)]
for a, b, c in abc:
  dp1[a - 1][b - 1] = c
  dp1[b - 1][a - 1] = c

for k in range(N):
  for i in range(N):
    for j in range(N):
      if i == j:
        dp1[i][j] = 0
      else:
        dp1[i][j] = min(dp1[i][j], dp1[i][k] + dp1[k][j])

dp2 = [[MAX_INT]*N for _ in range(N)]
for i in range(N):
  for j in range(N):
    if dp1[i][j] <= L:
      dp2[i][j] = 1

for k in range(N):
  for i in range(N):
    for j in range(N):
      if i == j:
        dp2[i][j] = 0
      else:
        dp2[i][j] = min(dp2[i][j], dp2[i][k] + dp2[k][j])

for s, t in q:
  if dp2[s - 1][t - 1] == MAX_INT:
    print(-1)
  else:
    print(dp2[s - 1][t - 1] - 1)