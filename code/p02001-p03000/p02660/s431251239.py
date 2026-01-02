import sys
import math
from collections import deque
import heapq
import itertools
from decimal import Decimal
import bisect
MAX_INT = int(10e25)
MIN_INT = -MAX_INT
mod = 1000000000+7
sys.setrecursionlimit(1000000)
def IL(): return list(map(int,input().split()))
def SL(): return input().split()
def I(): return int(sys.stdin.readline())
def S(): return input()

def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a

N = I()
a = prime_factorize(N)

d = {}
for i in a:
  if i in d:
    d[i] += 1
  else:
    d[i] = 1

ruiseki = [0]
tmp = 0
for i in range(1,200):
  ruiseki.append(ruiseki[-1]+i)

ans = 0
for i in d.values():
  tmp = bisect.bisect_right(ruiseki, i) -1
  ans += tmp
print(ans)