import sys
from math import ceil as C, floor as F, sqrt, gcd as G
from collections import defaultdict as D, Counter as CNT
from functools import reduce as R
import heapq as HQ

class Heap:
  def __init__(self, data, reverse=False):
    self.reverse = -1 if reverse else 1
    self.data = [self.reverse * d for d in data]
    HQ.heapify(self.data)
  def push(self, x): return HQ.heappush(self.data, self.reverse * x)
  def pop(self): return self.reverse * HQ.heappop(self.data) 

ALP = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alp = 'abcdefghijklmnopqrstuvwxyz'
def _X(): return sys.stdin.readline().rstrip().split(' ')
def _S(ss): return tuple(ss) if len(ss) > 1 else ss[0]
def S(): return _S(_X())
def Ss(): return list(S())
def _I(ss): return tuple([int(s) for s in ss]) if isinstance(ss, tuple) else int(ss)
def I(): return _I(S())
def _Is(ss): return list(ss) if isinstance(ss, tuple) else [ss]
def Is(): return _Is(I())

a, b, c = I()
j, k, l = I()
x, y, z = I()

seen = {}
n = I()
for _ in range(n):
    d = I()
    seen[d] = 1

if a in seen and b in seen and c in seen:
    print('Yes')
elif j in seen and k in seen and l in seen:
    print('Yes')
elif x in seen and y in seen and z in seen:
    print('Yes')
elif a in seen and j in seen and x in seen:
    print('Yes')
elif b in seen and k in seen and y in seen:
    print('Yes')
elif c in seen and l in seen and z in seen:
    print('Yes')
elif a in seen and k in seen and z in seen:
    print('Yes')
elif x in seen and k in seen and c in seen:
    print('Yes')
else:
    print('No')

