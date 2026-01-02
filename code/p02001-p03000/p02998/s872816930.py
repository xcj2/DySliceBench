import sys
sys.setrecursionlimit(10**7)
from collections import defaultdict
import math
mod = 10**9 + 7
def I(): return int(input())
def II(): return map(int, input().split())
def L(): return list(map(int, input().split()))
def TWO(M):
  L=[0]*M
  R=[0]*M
  for i in range(M):
    L[i],R[i] = II()
  return L, R

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

N = I()
x,y = TWO(N)
G = UF(N)

#座標値をkeyにして辞書を作成
X = defaultdict(list)
Y = defaultdict(list)
for i in range(N):
  X[x[i]].append(i)
  Y[y[i]].append(i)

#xが同じ値のものをunion
for v in X.values():
  if len(v)==1:
    continue
  for i in v[1:]:
    G.union(v[0],i)
  
#yが同じ値のものをunion   
for v in Y.values():
  if len(v)==1:
    continue
  for i in v[1:]:
    G.union(v[0],i)

#同じグループに存在するx,y値
X2 = defaultdict(set)
Y2 = defaultdict(set)
for i in range(N):
  root = G.find(i)
  X2[root].add(x[i])
  Y2[root].add(y[i])

#同じrootの格子点が全て追加される　rootごとにdisjoint
checked = [False]*N
ans = -N
for i in range(N):
  root = G.find(i)
  if checked[root] == True:
    continue
  checked[root] = True
  ans += len(X2[root])*len(Y2[root])
print(ans)