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

n, x, m = I()

seen = [x]
ans = x
for i in range(1, n):
    now = seen[-1]
    next = (now * now) % m

    if next not in seen:
        seen.append(next)
        ans += next
    else:
        loop = seen[seen.index(next):]
        count = len(loop)
        total = sum(loop)
        remain = n - i
        
        q, r = remain // count, remain % count
        ans += q * total
        ans += sum(loop[:r])
        break
        
print(ans)
