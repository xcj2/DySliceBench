import sys
import math
import bisect
MAX_INT = int(10e12)
MIN_NUM = -MAX_INT
mod = 1000000007
sys.setrecursionlimit(1000000000)
def IL(): return list(map(int,input().split()))
def SL(): return input().split()
def I(): return int(sys.stdin.readline())
def S(): return input()

import sys
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

N,M = IL()
a = IL()

hpop = heapq.heappop
hpush = heapq.heappush
data = []

for i in a:
    hpush(data, -i)

for i in range(M):
  tmp = math.ceil(hpop(data)/2)
  hpush(data, tmp)
  #print(data)

print(-sum(data))