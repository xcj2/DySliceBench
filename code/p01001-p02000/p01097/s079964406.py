import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy,functools
input = sys.stdin.readline
INF = 10**20
EPS = 1.0 / 10**10
MOD = 10**9 + 7
def LI(): return [int(x) for x in input().split()]
def LF(): return [float(x) for x in input().split()]
def LS(): return input().split()
def I(): return int(input())
def F(): return float(input())
def S(): return input()

class Graph:
  def __init__(self, _n):
    self.n = _n
    self.m = 0
    self.g = [[] for i in range(_n)]
  def add_edge(self, s, t, c = 1):
    self.g[s].append((t,c))
    self.g[t].append((s,c))
  def __getitem__(self, v):
    return self.g[v]

def edge_cost(i,j):
  L = [s - abs(ps[i][k]-ps[j][k]) for k in range(3)]
  if len([x for x in L if x <= 0]) > 0:
    return -1
  return 2*(L[0]*L[1]+L[1]*L[2]+L[2]*L[0])

def dfs(v, pv, k):
  if k == 0:
    for e in G[v]:
      if e[0] != pv and used[e[0]]:
        return e[1]
    return 0
  if used[v]:
    return INF
  used[v] = True
  res = INF
  for e in G[v]:
    if e[0] == pv:
      continue
    dd = dfs(e[0],v,k-1)
    if dd < INF:
      res = min(res,dd+e[1])
  used[v] = False
  return res


if __name__ == '__main__':
  while True:
    n,k,s = LI()
    if n == 0:
      break
    ps = [LI() for i in range(n)]

    G = Graph(n)
    for i in range(n-1):
      for j in range(i+1,n):
        c = edge_cost(i,j)
        if c > 0:
          G.add_edge(i,j,-c)

    used = [False] * n
    sub = INF
    for i in range(n):
      sub = min(sub,dfs(i,-1,k-1))
    if sub == INF:
      print(-1)
    else:
      print(6*k*s*s+sub)
