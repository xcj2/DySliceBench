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
s = [S() for i in range(N)]

d = [0]*4
for i in range(N):
  if s[i] == "AC":
    d[0] += 1
  elif s[i] == "WA":
    d[1] += 1
  elif s[i] == "TLE":
    d[2] += 1
  else:
    d[3] += 1

print("AC x",d[0])
print("WA x",d[1])
print("TLE x",d[2])
print("RE x",d[3])