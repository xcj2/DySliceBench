mod=10**9+7
import math
import sys
from collections import deque
import heapq
import copy
import itertools
from itertools import permutations
from itertools import combinations
import bisect
def mi() : return map(int,sys.stdin.readline().split())
def ii() : return int(sys.stdin.readline().rstrip())
def i() : return sys.stdin.readline().rstrip()
a=ii()
l=list(mi())
x=[1]*31
y=[[] for _ in range(a)]
for i in range(a):
  for j in range(31):
    if l[i]>>j & 1:
      x[j]=x[j]*(-1)
      y[i].append(-1)
    else:
      y[i].append(1)
c=0
for k in range(a):
  co=0
  for j in range(31):
    if x[j]!=y[k][j]:
      co+=2**j
  print(co,end=' ')