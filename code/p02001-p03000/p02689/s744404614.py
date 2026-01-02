import sys
import math
from collections import deque
import heapq
MAX_INT = int(10e10)
MIN_INT = -MAX_INT
mod = 1000000007
sys.setrecursionlimit(1000000)
def IL(): return list(map(int,input().split()))
def SL(): return input().split()
def I(): return int(sys.stdin.readline())
def S(): return input()

def tami(n):
  if len(edge[n]) == 0:
    top[n-1] = True
  else:
    num = h[n-1]
    for x in edge[n]:
      if num <= h[x-1]:
        break
    else:
      top[n-1] = True

N,M = IL()
h = IL()
ab = [IL() for i in range(M)]

edge = [[] for i in range(N+1)]
for a,b in ab:
  edge[a].append(b)
  edge[b].append(a)

top = [False]*N
for i in range(1,N+1):
  tami(i)

ans = 0
for i in top:
  if i == True:
    ans += 1
print(ans)