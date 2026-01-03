import bisect
from operator import itemgetter
import math
import copy
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

def judge(x):
  res = np.ceil((hp - B*x)/(A-B))
  cnt = res[res > 0].sum()
  if cnt <= x:
    return True
  else:
    return False

# 二分探索 #
def nibutan(n):
  left = 0
  right = n
  while left+1 != right:
    middle = (left+right)//2
    if judge(middle):
      right = middle
    else:
      left = middle
  return right

N,A,B = IL()
hp = np.array([I() for i in range(N)])
hp.sort()
n = hp[-1]//B+1

ans = nibutan(n)

print(ans)