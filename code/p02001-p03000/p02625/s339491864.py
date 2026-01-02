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

import functools
@functools.lru_cache(maxsize=None)
def factrial_memo(n):
  fact = [1, 1]
  for i in range(2, n + 1):
    fact.append((fact[-1] * i) % mod)
  return fact

def permutation(n,r): #nPr
  return fact[n]*pow(fact[n-r],mod-2,mod)%mod
  
def combination(n,r): #nCr
  return permutation(n,r)*pow(fact[r],mod-2,mod)%mod

def homogeneous(n,r): #nHr
  return combination(n+r-1,r)%mod

N,M = IL()

fact = factrial_memo(10**6)

s = 0
for k in range(1,N+1):
  s += combination(N, k) * permutation(M-k, N-k) * (-1)**(k-1)
ans = (permutation(M, N)**2 - s*permutation(M, N)) %mod
print(ans)