# -*- coding: utf-8 -*-

def findSet(x):
  if x == parent[x]:
    return x
  else:
    return findSet(parent[x])

def link(x, y):
  if rank[x] < rank[y]:
    parent[x] = y
  else:
    parent[y] = x
    if rank[x] == rank[y]:
      rank[y] += 1

def union(x, y):
  link(findSet(x), findSet(y))

n, q = list(map(int, input().split()))

data = (i for i in range(n))
rank = [0 for i in range(n)]
parent = [i for i in range(n)]

for i in range(q):
  f, x, y = list(map(int, input().split()))
  if f == 0:
    union(x, y)
  else:
    if findSet(x) == findSet(y):
      print(1)
    else:
      print(0)
