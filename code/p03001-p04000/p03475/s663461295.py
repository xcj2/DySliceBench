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
INF = 10 ** 18
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


n = I()
R = []
D = []
interval = []
for _ in range(n - 1):
    c, s, f = LI()
    R += [c]
    D += [s]
    interval += [f]


for start in range(n - 1):
    t = 0
    for j in range(start, n - 1):
        d, r, f = D[j], R[j], interval[j]
        if t <= D[j]:
            t = D[j] + R[j]
        else:
            t = D[j] + (t - D[j]) // interval[j] * interval[j] + bool((t - D[j]) % interval[j]) * interval[j] + R[j]
    print(t)
print(0)

