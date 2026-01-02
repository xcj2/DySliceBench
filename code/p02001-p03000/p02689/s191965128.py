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
from functools import reduce


sys.setrecursionlimit(2147483647)
INF = 10 ** 13
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


n, m = LI()
G = [[] for _ in range(n)]
H = LI()
for _ in range(m):
    a, b = LI()
    G[a - 1] += [b - 1]
    G[b - 1] += [a - 1]

ans = 0
for i in range(n):
    j = H[i]
    for v in G[i]:
        if H[v] >= j:
            break
    else:
        ans += 1

print(ans)
