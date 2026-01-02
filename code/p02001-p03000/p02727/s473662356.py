from collections import defaultdict, deque, Counter
from heapq import heappush, heappop, heapify
from bisect import bisect_right, bisect_left
import random
from itertools import permutations, accumulate, combinations, product
from re import split
import sys
import string
from bisect import bisect_left, bisect_right
from math import factorial, ceil, floor, gamma, log
from operator import mul
from functools import reduce
from copy import deepcopy
import re

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
mod = 10 ** 9 + 7


x, y, a, b, c = LI()
P = LI()
Q = LI()
R = LI()
L = []
for p in P:
    L += [(p, 0)]

for q in Q:
    L += [(q, 1)]

for r in R:
    L += [(r, 2)]

L.sort(reverse=True)
ret = 0
z = 0
for l, i in L:
    if i == 0 and x:
        x -= 1
        ret += l
    elif i == 1 and y:
        y -= 1
        ret += l
    elif i == 2:
        z += 1
        ret += l
    if x + y == z:
        break


print(ret)


