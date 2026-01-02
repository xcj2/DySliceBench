from functools import *
from collections import *
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.buffer.readline
 
M = 10**9+7
N = int(input())

@lru_cache(maxsize=None)
def mod_inv(x):
  if x == 1:
    return 1
  return M // x * -mod_inv(M%x) % M

weight = [0]*(N+1)
size = [0]*(N+1)
def calc_subtree(v):
  W = 1
  S = 1
  for child in Edge[v]:
    Edge[child].remove(v)
    w, s = calc_subtree(child)
    W = W * w % M
    S += s
  weight[v] = W * S % M
  size[v] = S
  return weight[v], size[v]

ans = [0]*(N+1)
def set_ans(v, a):
  ans[v] = a
  for child in Edge[v]:
    n = size[child]
    set_ans(child, ans[v] * n * mod_inv(N-n) % M)

Edge = defaultdict(set)
fact = N
for i in range(1, N):
  fact = fact * i % M
  a, b = map(int, input().split())
  Edge[a].add(b)
  Edge[b].add(a)
  
calc_subtree(1)
set_ans(1, mod_inv(weight[1]) * fact % M)
for i in range(1, N+1):
  print(ans[i])

