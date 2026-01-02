import sys
from math import ceil as C, floor as F, sqrt, gcd as G, factorial as FAC
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

def ncr(n, r): return FAC(n) // FAC(r) // FAC(n-r)

s = I()
max_buckets = s // 3
mod = 10 ** 9 + 7

ans = 0
for i in range(1, max_buckets+1):
    n = s - 3 * i
    ans += ncr(n+i-1, i-1)
    ans %= mod

print(ans)
    
