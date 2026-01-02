import sys
import math
import itertools
import bisect
from copy import copy
from collections import deque,Counter
from decimal import Decimal
def s(): return input()
def i(): return int(input())
def S(): return input().split()
def I(): return map(int,input().split())
def L(): return list(input().split())
def l(): return list(map(int,input().split()))
def lcm(a,b): return a*b//math.gcd(a,b)
sys.setrecursionlimit(10**9)
INF = 10**9
mod = 10**9+7

class UnionFind:
  def __init__(self,n):
    self.n=[-1]*n
    self.r=[0]*n
  def find_root(self,x):
    if self.n[x]<0:
      return x
    else:
      self.n[x]=self.find_root(self.n[x])
      return self.n[x]
  def unite(self,x,y):
    x=self.find_root(x)
    y=self.find_root(y)
    if x==y:return
    elif self.r[x]>self.r[y]:
      self.n[x]+=self.n[y]
      self.n[y]=x
    else:
      self.n[y]+=self.n[x]
      self.n[x]=y
      if self.r[x]==self.r[y]:
        self.r[y]+=1
  def root_same(self,x,y):
    return self.find_root(x)==self.find_root(y)
  def count(self,x):
    return -self.n[self.find_root(x)]

N,M = I()
u = UnionFind(N)
for i in range(M):
    a,b = I()
    u.unite(a-1,b-1)
ans = 0
for i in range(N):
    ans = max(ans,u.count(i))
print(ans)