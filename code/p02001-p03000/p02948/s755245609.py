#### import ####
import sys
import math
from collections import defaultdict

#### 設定 ####
sys.setrecursionlimit(10**7)

#### 定数 ####
mod = 10**9 + 7

#### 読み込み ####
def I(): return int(input())
def II(): return map(int, input().split())
def III(): return list(map(int, input().split()))
def Line(N):
  read_all = [tuple(map(int, input().split())) for _ in range(N)]
  return map(list,zip(*read_all))

#################

N,M = II()
A,B = Line(N)
a = []
for i in range(N):
  a.append([A[i],B[i]])
a.sort(key = lambda x:(x[0],x[1]))

b = []
for i in range(N):
  b.append([-a[i][1], a[i][0]])

from bisect import bisect_left, bisect_right
import heapq

ans = 0
h = []

for i in range(1,M+1):
  left = bisect_left(a,[i,0])
  right = bisect_right(a,[i,float('inf')])-1
  if right-left>=0:
    for i in range(left,right+1):
      heapq.heappush(h,b[i])
    x = heapq.heappop(h)
    ans += -x[0]
  else:
    if h:
      x = heapq.heappop(h)
      ans += -x[0]

print(ans)