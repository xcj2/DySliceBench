from collections import defaultdict, deque, Counter
from heapq import heappush, heappop, heapify
import math
import bisect
import random
from itertools import permutations, accumulate, combinations, product
import sys
import string
from bisect import bisect_left, bisect_right
from math import factorial, ceil, floor
from operator import mul
from functools import reduce


sys.setrecursionlimit(2147483647)
INF = 10 ** 20
def LI(): return list(map(int, sys.stdin.buffer.readline().split()))
def I(): return int(sys.stdin.buffer.readline())
def LS(): return sys.stdin.buffer.readline().rstrip().decode('utf-8').split()
def S(): return sys.stdin.buffer.readline().rstrip().decode('utf-8')
def IR(n): return [I() for i in range(n)]
def LIR(n): return [LI() for i in range(n)]
def SR(n): return [S() for i in range(n)]
def LSR(n): return [LS() for i in range(n)]
def SRL(n): return [list(S()) for i in range(n)]
def MSRL(n): return [[int(j) for j in list(S())] for i in range(n)]
mod = 1000000007


l = []
n, k = LI()
X = []
Y = []
ans = INF
for _ in range(n):
  x, y = LI()
  X += [x]
  Y += [y]
  l.append((x,y))

X.sort()
Y.sort()
for xl,xr in combinations(X, 2):
  for yl,yr in combinations(Y, 2):
    cnt = 0
    for x,y in l:
      if xl<=x<=xr and yl<=y<=yr:
        cnt += 1
      if cnt >= k and ans > (xr - xl) * (yr - yl):
         ans = (xr - xl) * (yr - yl)
print(ans)