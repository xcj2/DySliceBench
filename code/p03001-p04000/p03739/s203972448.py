import numpy as np
import bisect
from operator import itemgetter
import math
import functools
import itertools
import numpy as np
import sys
MAX_INT = int(10e10)
MIN_INT = -MAX_INT
mod = 1000000007
sys.setrecursionlimit(1000000)
def IL(): return list(map(int,input().split()))
def SL(): return input().split()
def I(): return int(sys.stdin.readline())
def S(): return input()

N = I()
a = IL()

l = []
tmp = 0
for i in range(N):
  tmp += a[i]
  l.append(tmp)

ans1 = 0
cnt = 0
tmp = 0
for i in range(N):
  if i%2 == 0:
    if l[i]+tmp > 0:
      continue
    else:
      cnt = -(l[i]+tmp) +1
      tmp += cnt
      ans1 += abs(cnt)
  else:
    if l[i]+tmp < 0:
      continue
    else:
      cnt = -(l[i]+tmp) -1
      tmp += cnt
      ans1 += abs(cnt)

ans2 = 0
cnt = 0
tmp = 0
for i in range(N):
  if i%2 == 0:
    if l[i]+tmp < 0:
      continue
    else:
      cnt = -(l[i]+tmp) -1
      tmp += cnt
      ans2 += abs(cnt)
  else:
    if l[i]+tmp > 0:
      continue
    else:
      cnt = -(l[i]+tmp) +1
      tmp += cnt
      ans2 += abs(cnt)


print(min(ans1,ans2))