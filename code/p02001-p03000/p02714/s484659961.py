import sys
from math import ceil as C, floor as F, sqrt, gcd as G
from collections import defaultdict as D, Counter as CNT
from functools import reduce as R
import heapq as HQ
from operator import mul

class Heap:
  def __init__(self, data, reverse=False):
    self.reverse = -1 if reverse else 1
    self.data = [self.reverse * d for d in data]
    HQ.heapify(self.data)
  def push(self, x): return HQ.heappush(self.data, self.reverse * x)
  def pop(self): return self.reverse * HQ.heappop(self.data) 

ALP = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alp = 'abcdefghijklmnopqrstuvwxyz'
def prod(list): return R(mul, list, 1)
def _X(): return sys.stdin.readline().rstrip().split(' ')
def _S(ss): return tuple(ss) if len(ss) > 1 else ss[0]
def S(): return _S(_X())
def Ss(): return list(S())
def _I(ss): return tuple([int(s) for s in ss]) if isinstance(ss, tuple) else int(ss)
def I(): return _I(S())
def _Is(ss): return list(ss) if isinstance(ss, tuple) else [ss]
def Is(): return _Is(I())

n = I()
rgb = S()

cnt = CNT(list(rgb))
ans = prod([cnt[c] for c in ['R', 'G', 'B']])

for i, r in enumerate(rgb):
    for j, g in enumerate(rgb[i+1:], start=i+1):
        k = j + (j - i)
        if k < len(rgb):
            if r != g and g != rgb[k] and r != rgb[k]:
                ans -= 1

print(ans)
        
