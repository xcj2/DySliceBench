from sys import exit, setrecursionlimit, stderr
from functools import reduce
from itertools import *
from collections import defaultdict, deque
from bisect import bisect
from random import *

def read():
  return int(input())
 
def reads():
  return [int(x) for x in input().split()]

INF = 1 << 60
def bfs(K):
  result = [INF] * K
  result[1] = 1
  que = deque([(1, 1)])
  while len(que) > 0:
    (d, u) = que.popleft()
    if result[u] < d:
      continue
    v0 = (10 * u) % K
    if d < result[v0]:
      result[v0] = d
      que.appendleft((d, v0))
    v1 = (u + 1) % K
    if d + 1 < result[v1]:
      result[v1] = d+1
      que.append((d+1, v1))
  return result

def solve(k):
  return bfs(k)[0]

K = read()
print(solve(K))