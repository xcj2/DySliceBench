# Binary Indexed Tree (Fenwick Tree)
from collections import defaultdict
class BIT:
  def __init__(self, n):
    self.n = n
    self.data = [0]*(n+1)
    self.el = [0]*(n+1)
  def sum(self, i):
    s = 0
    while i > 0:
      s += self.data[i]
      i -= i & -i
    return s
  def add(self, i, x):
    # assert i > 0
    self.el[i] += x
    while i <= self.n:
      self.data[i] += x
      i += i & -i
  def get(self, i, j=None):
    if j is None:
      return self.el[i]
    return self.sum(j) - self.sum(i-1)

def solve():
  ans = 0
  N = int(input())
  bit = BIT(N)
  A = list(map(int, input().split()))
  dic = {a:i+1 for i,a in enumerate(sorted(A))}
  for i in range(N):
    A[i] = dic[A[i]]
  for i in range(N):
    ans += i - bit.sum(A[i])
    bit.add(A[i],1)
  return ans
print(solve())
