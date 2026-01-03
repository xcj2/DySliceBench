#### import ####
import sys
import math
from collections import defaultdict

#### 設定 ####
sys.setrecursionlimit(10**7)
def input():
  return sys.stdin.readline()[:-1]

#### 定数 ####
mod = 10**9 + 7

#### 読み込み ####
def I(): return int(input())
def II(): return map(int, input().split())
def III(): return list(map(int, input().split()))
def Line(N):
  read_all = [tuple(map(int, input().split())) for _ in range(N)]
  return map(list,zip(*read_all))

#################

N,K,L = II()
p,q = Line(K)
r,s = Line(L)

class UF(object):
  def __init__(self, n=1):
    self.par = [i for i in range(n)]
    self.rank = [0 for _ in range(n)]
    self.size = [1 for _ in range(n)]

  def find(self, x):
    """
    x が属するグループを探索
    """
    if self.par[x] == x:
      return x
    else:
      self.par[x] = self.find(self.par[x])
      return self.par[x]

  def union(self, x, y):
    """
    x と y のグループを結合
    """
    x = self.find(x)
    y = self.find(y)
    if x != y:
      if self.rank[x] < self.rank[y]:
        x, y = y, x
      if self.rank[x] == self.rank[y]:
        self.rank[x] += 1
      self.par[y] = x
      self.size[x] += self.size[y]

  def is_same(self, x, y):
    """
    x と y が同じグループか否か
    """
    return self.find(x) == self.find(y)

  def get_size(self, x):
    """
    x が属するグループの要素数
    """
    x = self.find(x)
    return self.size[x]
  
uf1 = UF(N)
uf2 = UF(N)
ans = []

for i in range(K):
  uf1.union(p[i]-1,q[i]-1)

for i in range(L):
  uf2.union(r[i]-1,s[i]-1)

x = []
for i in range(N):
  x.append([uf1.find(i), uf2.find(i)])
y = x[:]
y.sort(key=lambda x:(x[0],x[1]))

from bisect import bisect_left, bisect_right
for i in range(N):
  ans.append(bisect_right(y,x[i])- bisect_left(y,x[i]))

print(*ans)