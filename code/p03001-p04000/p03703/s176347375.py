from sys import exit, setrecursionlimit, stderr
from functools import reduce
from itertools import *
from collections import defaultdict
from bisect import bisect
 
def read():
  return int(input())
 
def reads():
  return [int(x) for x in input().split()]

class BIT:
  def __init__(self, n):
    self._size = n
    self._body = [0] * (n+1)
  def __repr__(self):
    return ("BIT([" + ", ".join(str(x) for x in self._body) + "])")
  def size(self):
    return self._size
  def add(self, i, v):
    assert 0 <= i < self.size()
    i += 1
    while(i <= self.size()):
      self._body[i] += v
      i += i & -i
  def sum(self, *args):
    assert 1 <= len(args) <= 2
    if len(args) == 1: # [0, i)の和をとる
      i = args[0]
      assert 0 <= i <= self.size()
      s = 0
      while(i > 0):
        s += self._body[i]
        i -= i & -i
      return s
    else: # [i, j)の和をとる
      (i, j) = args
      return self.sum(j) - self.sum(i)

N, K = reads()
A = []
for _ in range(N):
  a = read()
  A.append(a-K)

psum = [0] + list(accumulate(A))

inv = sorted(set(psum))
L = len(inv)
invd = {inv[i]: i for i in range(L)}
bt = BIT(L)

ans = 0
for s in psum:
  c = invd[s]
  ans += bt.sum(c+1)
  bt.add(c, 1)
print(ans)
