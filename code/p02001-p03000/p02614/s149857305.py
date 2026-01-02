import sys
import time
import math
from collections import deque
import heapq
import itertools
from decimal import Decimal
import bisect
from operator import itemgetter
MAX_INT = int(10e18)
MIN_INT = -MAX_INT
mod = 1000000000+7
sys.setrecursionlimit(1000000)
def IL(): return list(map(int,input().split()))
def SL(): return input().split()
def I(): return int(sys.stdin.readline())
def S(): return input()

def tami(hl, wl):
  cnt = 0
  for h in range(H):
    if h in hl:
      continue
    for w in range(W):
      if w in wl:
        continue
      if grid[h][w] == "#":
        cnt += 1
  if cnt == K:
    return True
  else:
    return False

H,W,K = IL()
grid = [list(S()) for i in range(H)]

ans = 0
for i in range(1<<H):
  a = []
  for ii in range(H):
    if (i >> ii) & 1 == 1:
      a.append(ii)
  for j in range(1<<W):
    b = []
    for jj in range(W):
      if (j >> jj) & 1 == 1:
        b.append(jj)
    if tami(a, b):
      ans += 1
print(ans)