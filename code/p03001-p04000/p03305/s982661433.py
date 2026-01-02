#### import ####
import sys
import math
from collections import defaultdict

#### 設定 ####
sys.setrecursionlimit(10**7)
def input():
  return sys.stdin.readline()[:-1]

#### 定数 ####
mod = 10**9 + 7

#### 読み込み ####
def I(): return int(input())
def II(): return map(int, input().split())
def III(): return list(map(int, input().split()))
def Line(N):
  read_all = [tuple(map(int, input().split())) for _ in range(N)]
  return map(list,zip(*read_all))

#################

n,m,s,t = II()
u,v,a,b = Line(m)

from heapq import heappop, heappush
def dijkstra(E,s,n):
  inf=float('inf')
  d=[inf for _ in range(n)]
  d[s]=0
  q=[]
  heappush(q,(0,s))
  while q:
    du, u1 = heappop(q)
    if d[u1]<du: continue
    for v1,weight in E[u1].items():
      alt=du+weight
      if d[v1]>alt:
        d[v1]=alt
        heappush(q, (alt,v1))
  return d

p = [dict() for _ in range(n)]
p2 = [dict() for _ in range(n)]
for i in range(m):
  p[u[i]-1][v[i]-1] = a[i]
  p[v[i]-1][u[i]-1] = a[i]
  p2[u[i]-1][v[i]-1] = b[i]
  p2[v[i]-1][u[i]-1] = b[i]

d = dijkstra(p,s-1,n)
d2 = dijkstra(p2,t-1,n)

ans = [0]*n
ans[0] = d[n-1]+d2[n-1]
for i in range(1,n):
  ans[i] = min(ans[i-1],d[n-1-i]+d2[n-1-i])

for i in ans[::-1]:
  print(10**15-i)