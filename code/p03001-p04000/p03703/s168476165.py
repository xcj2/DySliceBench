# Binary Indexed Tree (Fenwick Tree)
class BIT:
  def __init__(self, n):
    self.n = n
    self.bit = [0]*(n+1)
    self.el = [0]*(n+1)
  def sum(self, i):
    s = 0
    while i > 0:
      s += self.bit[i]
      i -= i & -i
    return s
  def add(self, i, x):
    # assert i > 0
    self.el[i] += x
    while i <= self.n:
      self.bit[i] += x
      i += i & -i

N, K = map(int, input().split())
A = [int(input())-K for _ in range(N)]
from itertools import groupby, accumulate, product, permutations, combinations
cum = [0]+list(accumulate(A))
comp = lambda arr: {e: i+1 for i, e in enumerate(sorted(set(arr)))}
compcum = comp(cum)
for i in range(N+1):
  cum[i] = compcum[cum[i]]
bit = BIT(N+1)
ans = 0
for i in range(N+1):
  ans += bit.sum(cum[i])
  bit.add(cum[i],1)
print(ans)

