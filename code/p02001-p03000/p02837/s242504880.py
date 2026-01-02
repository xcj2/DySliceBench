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
l=[]
ans=0
for i in range(a):
  s=ii()
  h=[list(mi()) for _ in range(s)]
  l.append(h)
for k in range(2**a):
  lst=[]
  for p in range(a):
    if k>>p & 1:
      lst.append(p)
  t=True
  for aa in lst:
    for m in l[aa]:
      if m[1]==0:
        if m[0]-1 in lst:
          t=False
          break
      else:
        if not m[0]-1 in lst:
          t=False
          break
  if t:
    ans=max(ans,len(lst))
print(ans)