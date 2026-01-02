import sys
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

def tami(date, LastDay, type, score):
  res = score
  res += s[date-1][type]
  for i in range(26):
    if i == type:
      continue
    res -= (date - LastDay[i]) *c[i]
  return res

def nasu():
  res = []
  for d in range(1,D+1):
    tmp1 = ["", 0]
    tmp2 = ["", 0]
    for i in range(26):
      if tmp1[1] < (d - LastDay[i]) * c[i]:
        tmp1 = [i, (d - LastDay[i]) * c[i]]
      if tmp2[1] < s[d-1][i]:
        tmp2 = [i, s[d-1][i]]
    if tmp1[1] > tmp2[1]:
      res.append(tmp1[0])
    else:
      res.append(tmp2[0])
    LastDay[res[-1]] = d
  return res

D = I()
c = IL()
s = [IL() for i in range(D)]

LastDay = [0]*26
score = 0
ans = nasu()

for i in ans:
  print(i+1)

"""
for d in range(D):
  score = tami(d+1, LastDay, ans[d]-1, score)
  LastDay[ans[d]-1] = d+1
  print(score)
"""