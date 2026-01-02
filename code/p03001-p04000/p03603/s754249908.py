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


n = I()
P = [-1] + LI()
X = LI()
G = [[] for _ in range(n)]
for i in range(1, n):
    G[P[i] - 1] += [i]
    G[i] += [P[i] - 1]

def check(u):
    total = 0
    bit  = 1
    for v in G[u]:
        if v == P[u] - 1:
            continue
        if len(G[v]) == 1:
            total += X[v]
            bit |= bit << X[v]
        else:
            a, b = check(v)
            total += a + b
            bit =  bit << a | bit << b
    c = bin(bit)
    for j in range(X[u], -1, -1):
        if bit >> j & 1:
            total += X[u] - j
            return X[u], total - X[u]
    else:
        print('IMPOSSIBLE')
        exit()


if check(0):
    print('POSSIBLE')