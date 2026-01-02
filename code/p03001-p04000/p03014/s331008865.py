from collections import defaultdict, deque, Counter
from heapq import heappush, heappop, heapify
import math
import bisect
import random
from itertools import permutations, accumulate, combinations
import sys
import string
from bisect import bisect_left, bisect_right
from math import factorial, ceil, floor
from functools import reduce



INF = float('inf')
def LI(): return list(map(int, sys.stdin.readline().split()))
def I(): return int(sys.stdin.readline())
def LS(): return sys.stdin.readline().split()
def S(): return sys.stdin.readline().strip()
def IR(n): return [I() for i in range(n)]
def LIR(n): return [LI() for i in range(n)]
def SR(n): return [S() for i in range(n)]
def LSR(n): return [LS() for i in range(n)]
def SRL(n): return [list(S()) for i in range(n)]
def MSRL(n): return [[int(j) for j in list(S())] for i in range(n)]
mod = 1000000007


h, w = LI()
L = SR(h)
u = [[0]*w for _ in range(h)]
d = [[0]*w for _ in range(h)]
l = [[0]*w for _ in range(h)]
r = [[0]*w for _ in range(h)]
for y in range(h):
    l[y][0] = 1 if L[y][0] == '.' else 0
    for x in range(1, w):
        if L[y][x] == '.':
            l[y][x] = l[y][x-1] + 1



for y in range(h):
    r[y][w-1] = 1 if L[y][w-1] == '.' else 0
    for x in range(w-2, -1, -1):
        if L[y][x] == '.':
            r[y][x] = r[y][x+1] + 1



for x in range(w):
    u[0][x] = 1 if L[0][x] == '.' else 0
    for y in range(1, h):
        if L[y][x] == '.':
            u[y][x] = u[y-1][x] + 1


for x in range(w):
    d[h-1][x] = 1 if L[h-1][x] == '.' else 0
    for y in range(h-2, -1, -1):
        if L[y][x] == '.':
            d[y][x] = d[y+1][x] + 1



print(max([u[y][x] + d[y][x] + l[y][x] + r[y][x] for y in range(h) for x in range(w)]) - 3)