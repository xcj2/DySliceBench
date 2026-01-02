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

N = I()
a = IL()
a.sort(reverse=True)

ans = a[0]
i = 1
cnt = 2
while True:
  if cnt == N:
    break
  ans += a[i]
  cnt += 1
  if cnt == N:
    break
  ans += a[i]
  cnt += 1
  i += 1
print(ans)