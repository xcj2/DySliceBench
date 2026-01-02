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

N,M = IL()
a = [I() for i in range(M)]

dp = [0]*(N+1)
dp[0] = 1

for i in a:
  dp[i] = -1

for i in range(N+1):
  if dp[i] == -1:
    continue
  if i+1 <= N:
     if dp[i+1] != -1:
      dp[i+1] += dp[i]
  if i+2 <= N:
    if dp[i+2] != -1:
      dp[i+2] += dp[i]
      
print(dp[N]%mod)