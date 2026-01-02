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

D = I()
c = IL()
s = [IL() for i in range(D)]

for i in range(1,D+1):
  tmp = ["", 0]
  for j in range(26):
    if tmp[1] < s[i-1][j]:
      tmp = [j, s[i-1][j]]
  print(tmp[0]+1)