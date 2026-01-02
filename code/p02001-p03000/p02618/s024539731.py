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

def tami(now, ContestType):
  res = c[ContestType] * (now - LastDay[ContestType])
  return res

def nasu(now, x, y, z):
  res = 0
  res += s[now-1][x]
  res += s[now][y]
  res += s[now+1][z]
  if x == y == z:
    res += (D - now) * ((now - LastDay[x]) * c[x])
    now += 1
    res += (D - now) * (1 * c[y])
    now += 1
    res += (D - now) * (1 * c[z])
  elif x == y:
    res += (D - now) * ((now - LastDay[x]) * c[x])
    now += 1
    res += (D - now) * (1 * c[y])
    now += 1
    res += (D - now) * ((now - LastDay[z]) * c[z])
  elif y == z:
    res += (D - now) * ((now - LastDay[x]) * c[x])
    now += 1
    res += (D - now) * ((now - LastDay[y]) * c[y])
    now += 1
    res += (D - now) * (1 * c[z])
  elif x == z:
    res += (D - now) * ((now - LastDay[x]) * c[x])
    now += 1
    res += (D - now) * ((now - LastDay[y]) * c[y])
    now += 1
    res += (D - now) * (2 * c[z])
  else:
    res += (D - now) * ((now - LastDay[x]) * c[x])
    now += 1
    res += (D - now) * ((now - LastDay[y]) * c[y])
    now += 1
    res += (D - now) * ((now - LastDay[z]) * c[z])
  return res

D = I()
c = IL()
s = [IL() for i in range(D)]

LastDay = [0]*26
for i in range(1,D+1-2):
  tmp = ["", 0]
  for x in range(26):
    for y in range(26):
      for z in range(26):
        score = nasu(i, x, y, z)
        if tmp[1] < score:
          tmp = [(x, y, z), score]
  LastDay[tmp[0][0]] = i
  print(tmp[0][0]+1)
else:
  print(tmp[0][1]+1)
  print(tmp[0][2]+1)