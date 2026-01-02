from sys import exit, setrecursionlimit, stderr
from functools import reduce
from itertools import *
from collections import defaultdict
from bisect import bisect

setrecursionlimit(10**6)

def read():
  return int(input())

def reads():
  return [int(x) for x in input().split()]

n, m = reads()

d = dict()
edges = [[] for _ in range(n)]

for i in range(m):
  u, v, s = reads()
  u, v = u-1, v-1
  edges[u].append((s, v))
  edges[v].append((s, u))

def quit(x):
  print(x)
  exit()

cond = [[None] * n for _ in range(2)]
cond[0][0] = 0

INF = 10**16

visited = [False] * n

def walk(x):
  if visited[x]:
    return
  visited[x] = True
  for s, y in edges[x]:
    for sig in range(2):
      if cond[sig][x] is not None:
        p = cond[sig][x]
        if cond[1-sig][y] is None or cond[1-sig][y] == s - p:
          cond[1-sig][y] = s - p
        else:
          quit(0)
    walk(y)

walk(0)

for i in range(n):
  if cond[0][i] is not None and cond[1][i] is not None:
    x = (cond[1][i] - cond[0][i]) // 2
    for i in range(n):
      if cond[0][i] is not None and cond[0][i] + x <= 0:
        quit(0)
      if cond[1][i] is not None and cond[1][i] - x <= 0:
        quit(0)
      if cond[0][i] is not None and cond[1][i] is not None and x + cond[0][i] != cond[1][i] - x:
        quit(0)
    quit(1)

pmin = min(p for p in cond[0] if p is not None)
nmin = min(p for p in cond[1] if p is not None)

print(max(0, nmin + pmin - 1))
