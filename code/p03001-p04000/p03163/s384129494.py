import sys,io
from functools import lru_cache
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10**8)
def read():
  return int(readline())
def reads():
  return map(int, readline().split())
def mp(arg):
  return map(int,arg.split())
N,W=reads()
weight,value=[0]*N,[0]*N
for i in range(N):
    weight[i],value[i]=reads()
dp=[[ 0 for _ in  range(W+1) ] for _ in range(N+1)]
for i in range(N):
  for k in range(W+1):
    if (k >= weight[i]) :dp[i+1][k] = max(dp[i][k-weight[i]] + value[i], dp[i][k])
    else :dp[i+1][k] = dp[i][k]
print("{}".format(dp[N][W]))