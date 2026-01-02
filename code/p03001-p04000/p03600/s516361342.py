from collections import defaultdict, deque, Counter
from heapq import heappush, heappop, heapify
import math
import bisect
import random
from itertools import permutations, accumulate, combinations, product
import sys
import string
from bisect import bisect_left, bisect_right
from math import factorial, ceil, floor, atan2
from operator import mul
from functools import reduce
sys.setrecursionlimit(10 ** 9)

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


n = I()
G = []
for _ in range(n):
    G += [LI()]


ret = 0
for i in range(n):
    for j in range(i + 1, n):
        flag = 1
        for k in range(n):
            if i == k or j == k:
                continue
            if G[i][j] > G[i][k] + G[k][j]:
                print(-1)
                exit()
            elif G[i][j] == G[i][k] + G[k][j]:
                flag = 0
        if flag:
            ret += G[i][j]


print(ret)