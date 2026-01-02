#import bisect,collections,copy,heapq,itertools,math,numpy,string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
N, M = LI()
A = [I() for _ in range(M)]
md = 10**9+7


dp = [0] * (N+1)
dp[0] = 1
chk = [True] * (N+1)
for a in A:
  chk[a] = False

for now in range(N):
  for next in range(now+1, now+3):
    if next == N:
      dp[next] += dp[now]
      dp[next] %= md
      break
    if not chk[next]:
      continue
    else:
      dp[next] += dp[now]
      dp[next] %= md

print(dp[N])