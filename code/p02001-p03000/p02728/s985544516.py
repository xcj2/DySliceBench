from functools import *
from collections import *
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.buffer.readline
 
M = 10**9+7

@lru_cache(maxsize=None)
def mod_inv(x):
  if x == 1:
    return 1
  return M // x * -mod_inv(M%x) % M

@lru_cache(maxsize=None)
def calc_subtree(v):
  ret = 1
  size = 1
  for child in Edge[v]:
    Edge[child].remove(v)
    r, s = calc_subtree(child)
    ret = ret * r % M
    size += s
  ret = ret * size % M
  return ret, size

ans = {}
def set_ans(v, a):
  ans[v] = a
  for child in Edge[v]:
    n = calc_subtree(child)[1]
    set_ans(child, ans[v] * n * mod_inv(N-n) % M)

N = int(input())
Edge = defaultdict(set)
fact = N
for i in range(1, N):
  fact = fact * i % M
  a, b = map(int, input().split())
  Edge[a].add(b)
  Edge[b].add(a)

set_ans(1, mod_inv(calc_subtree(1)[0]) * fact % M)
for i in range(1, N+1):
  print(ans[i])

