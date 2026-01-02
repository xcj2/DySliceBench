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

def ispalindrome(s):
  h = int(math.floor(len(s) / 2))
  #print(s[h+1:], s[:h])
  hh = h+1
  if(len(s)%2==0):
    hh = h
  for a, b in zip(s[hh:], reversed(s[:h])):
    if a != b: return 0
  return 1

#sys.setrecursionlimit(10**7)
#N, Q = map(int, input().split())
#G = [list(input()) for i in range(H)]
#V, E, r = map(int, input().split())
#INF = V * 10001

S = str(input())
ans = "No"
h = int(math.floor(len(S) / 2))

#print(S[5:])

if(ispalindrome(S)==1):
  if(ispalindrome(S[:h])==1):
    ans = "Yes"

print(ans)
