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
from operator import mul


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


n, m, x = LI()
L = []
C = []
for _ in range(n):
    c, *A = LI()
    C += [c]
    L += [A]

ans = INF

for i in range(2 ** n):
    B = [0] * m
    ret = 0
    for j in range(n):
        if i >> j & 1:
            ret += C[j]
            for k in range(m):
                B[k] += L[j][k]
    for b in B:
        if b < x:
            break
    else:
        ans = min(ans, ret)

print(-1 if ans == INF else ans)