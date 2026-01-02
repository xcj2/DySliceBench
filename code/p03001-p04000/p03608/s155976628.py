#!/usr/bin/python3r
# -*- coding:utf-8 -*-

from itertools import permutations

def main():
  n, m, nr = map(int, input().split())
  lr = list(map(lambda x:int(x)-1, input().split()))
  edges = [[10**9]*n for _ in range(n)]
  for i in range(n):
    edges[i][i] = 0
  for _ in range(m):
    a, b, c = map(int, input().split())
    a, b = a - 1, b - 1
    edges[a][b] = edges[b][a] = c
    
  def wf():
    for k in range(n):
      for i in range(n):
        for j in range(n):
          edges[i][j] = min(edges[i][j], edges[i][k] + edges[k][j])
  wf()
          
  def calc_cost(path):
    cost = 0
    for i in range(nr-1):
      cost += edges[path[i]][path[i+1]]
    return cost
  
  print(min([calc_cost(path) for path in permutations(lr)]))

if __name__=='__main__':
  main()

