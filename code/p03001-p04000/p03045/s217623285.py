# /usr/bin/python
# -*- coding: utf-8 -*-
import math



class UnionFind():
  def __init__(self, size):
    self.par = [-1]*size
      
  def root(self,x):
    if self.par[x] < 0:
      return x
    else:
      return self.root(self.par[x])
      
  def issame(self,x,y):
    if self.root(x)==self.root(y):
      return True
    else:
      return False
  
  def merge(self,x,y):
    x, y = [self.root(x), self.root(y)]
    if x == y:
      return False
    if self.par[x] > self.par[y]:
      x, y = y, x
    self.par[x] += self.par[y]
    self.par[y] = x
    return True

  def get_list(self):
    return self.par


def main():
  N,M = map(int, input().split())
  uf = UnionFind(N)
  for _ in range(M):
    x,y,z = map(int, input().split())
    uf.merge(x-1,y-1)

  ret = 0
  for p in list(uf.get_list()):
    if p < 0:
      ret += 1
  return ret


if __name__ == "__main__":
  print(main())