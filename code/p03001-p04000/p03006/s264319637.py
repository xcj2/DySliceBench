import bisect
from operator import itemgetter
import math
import collections
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
xy = [IL() for i in range(N)]

if N == 1 or N == 2:
  print(1)
else:
  data = []
  cnt = 0
  for i in itertools.combinations(xy,2):
    rex,rey = i[0]
    x,y = i[1]
    if rex > x:
      rex,rey,x,y = x,y,rex,rey
    if rex == x:
      if rey > y:
        rex,rey,x,y = x,y,rex,rey
    data.append(str(x-rex)+str(y-rey))
  else:
    d = collections.Counter(data)
    cnt = max(cnt,d.most_common()[0][1])
  
  print(N-cnt)