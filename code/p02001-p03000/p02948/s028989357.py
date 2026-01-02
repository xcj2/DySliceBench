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
  a.append([A[i],-B[i]])
a.sort(key = lambda x:(x[0]))

from bisect import bisect_left, bisect_right
import heapq

ans = 0
p = 0
h = []

for i in range(1,M+1):
  while p<N and a[p][0]==i:
    heapq.heappush(h,a[p][1])
    p += 1
  if h:
    x = heapq.heappop(h)
    ans += -x

print(ans)