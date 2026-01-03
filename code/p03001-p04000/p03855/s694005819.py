from itertools import accumulate
from math import*
from collections import deque
from collections import defaultdict
from itertools import permutations
import heapq
import bisect
from collections import Counter
from itertools import*
from bisect import bisect_left,bisect_right
from copy import deepcopy
inf = 10**10
from functools import reduce

class UnionFind:
  def __init__(self, n):
    self.tree = [-1] * n

  def union(self, a, b):
    a = self.root(a)
    b = self.root(b)
    if(a == b):
      return
    if(self.size(a) < self.size(b)):
      a, b = b, a
    self.tree[a] += self.tree[b]
    self.tree[b] = a

  def root(self, a):
    if(self.tree[a] < 0):
      return a
    res = self.root(self.tree[a])
    self.tree[a] = res
    return res

  def size(self, a):
    return -self.tree[self.root(a)]

n,k,l = map(int,input().split())
uf1 = UnionFind(n)
uf2 = UnionFind(n)
for i in range(k):
    p,q = map(int,input().split())
    p -= 1
    q -= 1
    uf1.union(p,q)
for i in range(l):
    r,s = map(int,input().split())
    r -= 1
    s -= 1
    uf2.union(r,s)
ab = [(uf1.root(i),uf2.root(i)) for i in range(n)]
c = Counter(ab)
print(" ".join(map(str,[c[i] for i in ab])))