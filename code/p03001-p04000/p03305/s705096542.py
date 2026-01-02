from sys import exit, setrecursionlimit, stderr
from functools import reduce
from itertools import *
from collections import defaultdict
from bisect import bisect
from heapq import heappush, heappop

setrecursionlimit(10**6)

def read():
  return int(input())

def reads():
  return [int(x) for x in input().split()]

n, m, s, t = reads()
s, t = s-1, t-1
esyen = [[] for _ in range(n)]
essnk = [[] for _ in range(n)]

for _ in range(m):
  u, v, a, b = reads()
  u, v = u-1, v-1
  esyen[u].append((a, v))
  esyen[v].append((a, u))
  essnk[u].append((b, v))
  essnk[v].append((b, u))

INF = 10**15

def dijkstra(s, edges):
  que = []
  d = [INF] * n
  d[s] = 0
  heappush(que, (0, s))

  while len(que) > 0:
    (c, v) = heappop(que)
    if d[v] < c:
      continue
    for (cc, w) in edges[v]:
      if d[w] > d[v] + cc:
        d[w] = d[v] + cc
        heappush(que, (d[w], w))
  
  return d

ds = dijkstra(s, esyen)
dt = dijkstra(t, essnk)

scores = [0] * n
for i in range(n):
  scores[i] = 10**15 - (ds[i] + dt[i])

amax = [10**15] * n
amax[-1] = scores[-1]
for i in range(n-2, -1, -1):
  amax[i] = max(amax[i+1], scores[i])

for i in range(n):
  print(amax[i])