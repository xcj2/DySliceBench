import sys
import math
from collections import deque
import heapq
import itertools
MAX_INT = int(10e25)
MIN_INT = -MAX_INT
mod = 998244353
sys.setrecursionlimit(1000000)
def IL(): return list(map(int,input().split()))
def SL(): return input().split()
def I(): return int(sys.stdin.readline())
def S(): return input()

N = I()
a = IL()

num = sum(a)
ans = 0
ko = 1
for i in range(N):
  ans += ko
  ko -= a[i]
  num -= a[i]
  ko = min(ko*2, num)

  if ko <= 0:
    print(-1)
    break
else:
  ans += ko
  ko -= a[-1]
  if ko < 0:
    print(-1)
  else:
    print(ans)