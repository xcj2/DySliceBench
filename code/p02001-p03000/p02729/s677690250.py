# coding:utf-8

import sys
import math
import time
#import numpy as np
import collections
from collections import deque
import queue
import copy
import bisect
import heapq


def dfs(s, prev, pre):
  val[s] += Ope[s] + prev
  for i in G[s]:
    if(i == pre):
      continue
    dfs(i, val[s], s)

def bfs(sx, sy, n):
  que = deque([[sy,sx]])
  while que:
    y,x = que.popleft()
    for i,j in D:
      if(x+i<0 or y+j<0 or x+i>W-1 or y+j>H-1):
        continue
      dist = G[y+j][x+i]
      if(G[y+j][x+i] != "X"):
        if(type(G[y+j][x+i]) is str):
          G[y+j][x+i] = G[y][x]+1
          que.append([y+j,x+i])
        elif(dist>G[y][x]+1):
          G[y+j][x+i] = G[y][x]+1
          que.append([y+j,x+i])
        

def combinations_count(n, r):
  return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

#sys.setrecursionlimit(10**7)
#N, Q = map(int, input().split())
#G = [list(input()) for i in range(H)]
#V, E, r = map(int, input().split())
#INF = V * 10001

N, M = map(int, input().split())
ans = 0

if(N>1):
  ans += combinations_count(N, 2)
if(M>1):
  ans += combinations_count(M, 2)


print(int(ans))
