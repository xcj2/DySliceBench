from sys import exit, setrecursionlimit, stderr
from functools import reduce
from itertools import *
from collections import *
from bisect import *

def read():
  return int(input())
 
def reads():
  return [int(x) for x in input().split()]

INF = 1 << 60

def main():
  N = read()
  rs = []; bs = []
  for i in range(N):
    a, b = reads()
    rs.append((a, b))
  for i in range(N):
    a, b = reads()
    bs.append((a, b))
  
  bi = bipmatch(2 * N)
  for i, j in product(range(N), range(N)):
    if rs[i][0] < bs[j][0] and rs[i][1] < bs[j][1]:
      bi.add_edge(i, N+j)
  ans = bi.count_match()
  print(ans)

class bipmatch:
  def __init__(self, N):
    self.size = N
    self.edges = [[] for _ in range(N)]

  def add_edge(self, u, v):
    self.edges[u].append(v)
    self.edges[v].append(u)

  def dfs(self, match, used, u):
    N = self.size; edges = self.edges
    used[u] = True
    for v in edges[u]:
      w = match[v]
      if w < 0 or not used[w] and self.dfs(match, used, w):
        match[u], match[v] = v, u
        return True
    return False

  def count_match(self):
    N = self.size; edges = self.edges
    res = 0; match = [-1] * N
    for v in range(N):
      if match[v] < 0:
        used = [0] * N
        if self.dfs(match, used, v):
          res += 1
    return res

main()