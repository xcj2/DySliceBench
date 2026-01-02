import sys
import math
from collections import deque
import heapq
import itertools
MAX_INT = int(10e10)
MIN_INT = -MAX_INT
mod = 1000000007
sys.setrecursionlimit(1000000)
def IL(): return list(map(int,input().split()))
def SL(): return input().split()
def I(): return int(sys.stdin.readline())
def S(): return input()

def tami(x, cnt):
  if visited[x-1] != -1:
    return [x, visited[x-1], cnt-visited[x-1]]
  else:
    visited[x-1] = cnt
    return tami(a[x-1], cnt+1)

def nasu1(x, cnt):
  if cnt == K:
    return x
  else:
    return nasu1(a[x-1], cnt+1)

def nasu2(x, cnt):
  if cnt == num:
    return x
  else:
    return nasu2(a[x-1], cnt+1)

N,K = IL()
a = IL()

visited = [-1]*N
i, start, roop = tami(1, 0)
if K <= start:
  print(nasu1(1, 0))
else:
  #print(visited)
  num = (K-start)%roop
  #print(start,roop,num)

  print(nasu2(i, 0))