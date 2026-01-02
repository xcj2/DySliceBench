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

def tami(turu, kame):
  if turu*2 + kame*4 == y:
    #print(turu,kame)
    return True
  else:
    return False

x,y =IL()

for turu in range(x+1):
  kame = x - turu
  if tami(turu, kame):
    print("Yes")
    exit()
else:
  print("No")
