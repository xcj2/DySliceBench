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

def check(l):
  for i in l:
    if i >= X:
      continue
    else:
      return False
  else:
    return True

N,M,X = IL()
ca = [IL() for i in range(N)]

ans = MAX_INT
for i in range(1 << N):
  x = 0
  rikaido = [0]*M
  for j in range(N):
    if (i >> j) & 1 == 1:
      x += ca[j][0]
      for k in range(1,M+1):
        rikaido[k-1] += ca[j][k]
  else:
    if check(rikaido):
      ans = min(ans, x)
if ans == MAX_INT:
  print(-1)
else:
  print(ans)