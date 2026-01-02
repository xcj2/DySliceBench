#!/usr/bin/python3
# -*- coding:utf-8 -*-

class UnionFindTree:
  def __init__(self, n):
    self.nodes = [-1]*n
    
  def find(self, x):
      parent = self.nodes[x]
      if parent < 0:
        return x
      else:
        self.nodes[x] = self.find(self.nodes[x])
        return self.nodes[x]
  
  def unite(self, x, y):
    xp = self.find(x)
    yp = self.find(y)
    if self.nodes[xp] > self.nodes[yp]:
      xp, yp = yp, xp
    self.nodes[xp] += self.nodes[yp]
    self.nodes[yp] = xp  
  
  def size(self, x):
    return -self.nodes[self.find(x)]


def main():
  n, m = map(int, input().split())
  edges = []
  
  for _ in range(m):
    a, b = map(lambda x:int(x)-1, input().split())
    edges.append((a, b))
  uftree = UnionFindTree(n)
  scores = []
  
  for a, b in edges[::-1]:
    ap = uftree.find(a)
    bp = uftree.find(b)
    if  ap != bp:
      scores.append(uftree.size(ap) * uftree.size(bp))
      uftree.unite(a, b)    
    else:
      scores.append(0)
      
  sum = 0
  for score in scores[::-1]:
    sum += score
    print(sum)

if __name__=='__main__':
  main()

