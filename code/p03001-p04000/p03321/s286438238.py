from sys import exit, setrecursionlimit, stderr
from functools import reduce
from itertools import *
from collections import defaultdict
from bisect import bisect
 
def read():
  return int(input())
 
def reads():
  return [int(x) for x in input().split()]

N, M = reads()
orig_edges = set()
for _ in range(M):
  A, B = reads()
  A, B = A-1, B-1
  orig_edges.add((A, B))
  orig_edges.add((B, A))

edges = [[] for _ in range(N)]
for A, B in combinations(range(N), 2):
  if (A, B) not in orig_edges:
    edges[A].append(B)
    edges[B].append(A)

remain = set(range(N))
color = [-1] * N

def walk(u, c, ctr, remain):
  if u in remain:
    remain.remove(u)
  if color[u] >= 0:
    if color[u] != c:
      print(-1); exit()
    return ctr

  color[u] = c; ctr[c] += 1
  for v in edges[u]:
    walk(v, 1-c, ctr, remain)
  return ctr

ps = []
while len(remain) > 0:
  s = remain.pop()
  p = walk(s, 0, [0, 0], remain)
  ps.append(p)

dp = set([0])
for a, b in ps:
  d = b - a
  dp = {x - d for x in dp} | {x + d for x in dp}
m = min(abs(x) for x in dp)
a, b = (N + m) // 2, (N - m) // 2
print(a*(a-1)//2 + b*(b-1)//2)
