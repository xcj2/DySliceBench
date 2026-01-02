import math
import functools
import itertools
import numpy as np
import sys
MAX_INT = int(10e10)
MIN_INT = -MAX_INT
mod = 1000000007
sys.setrecursionlimit(1000000)
def IL(): return list(map(int,input().split()))
def SL(): return input().split()
def I(): return int(sys.stdin.readline())
def S(): return input()

def tami(node,cost):
  if visited[node] == True:
    return
  else:
    visited[node] = True
    if cost%2 == 0:
      ans[node-1] = 0
    else:
      ans[node-1] = 1
    for x,c in root[node]:
      tami(x, cost+c)

N = I()
uvw = [IL() for i in range(N-1)]

root = [[] for _ in range(N+1)]
visited = [False]*(N+1)
ans = [0]*N

for u,v,w in uvw:
  root[u].append([v, w])
  root[v].append([u, w])

tami(1, 0)
for i in ans:
  print(i)