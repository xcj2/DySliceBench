from functools import *
from itertools import *
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.buffer.readline
 
M = 10**9+7
N = int(input())

@lru_cache(maxsize=None)
def mod_inv(x):
  return 1 if x == 1 else M // x * -mod_inv(M%x) % M

Weight = [0]*(N+1)
Size = [0]*(N+1)
def calc_subtree(v):
  W, S = 1, 1
  for child in Edge[v]:
    Edge[child].remove(v)
    calc_subtree(child)
    W = W * Weight[child] % M
    S += Size[child]
  Weight[v] = W * S % M
  Size[v] = S

Ans = [0]*(N+1)
def calc_ans(v, a):
  Ans[v] = a
  for child in Edge[v]:
    n = Size[child]
    calc_ans(child, a * n * mod_inv(N-n) % M)

Edge = [set() for i in range(N+1)]
fact = N
for i in range(1, N):
  fact = fact * i % M
  a, b = map(int, input().split())
  Edge[a].add(b)
  Edge[b].add(a)
  
calc_subtree(1)
calc_ans(1, mod_inv(Weight[1]) * fact % M)

for a in islice(Ans, 1, None):
  print(a)

