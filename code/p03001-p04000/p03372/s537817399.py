from collections import defaultdict, deque, Counter
from heapq import heappush, heappop, heapify
import math
import bisect
import random
from itertools import permutations, accumulate, combinations, product
import sys
from pprint import pprint
from copy import deepcopy
import string
from bisect import bisect_left, bisect_right
from math import factorial, ceil, floor
from operator import mul
from functools import reduce
from pprint import pprint


sys.setrecursionlimit(2147483647)
INF = 10 ** 13
def LI(): return list(map(int, sys.stdin.readline().split()))
def I(): return int(sys.stdin.readline())
def LS(): return sys.stdin.buffer.readline().rstrip().decode('utf-8').split()
def S(): return sys.stdin.buffer.readline().rstrip().decode('utf-8')
def IR(n): return [I() for i in range(n)]
def LIR(n): return [LI() for i in range(n)]
def SR(n): return [S() for i in range(n)]
def LSR(n): return [LS() for i in range(n)]
def SRL(n): return [list(S()) for i in range(n)]
def MSRL(n): return [[int(j) for j in list(S())] for i in range(n)]
mod = 1000000007



n, c = LI()
clock_pos = []
value = []
for pos, v in LIR(n):
    clock_pos += [pos]
    value += [v]

r1 = 0
r2 = 0
A1 = [0]
A2 = [0]
for i in range(n):
    r1 += value[i]
    r2 += value[-i - 1]
    A1 += [max(A1[i], r1 - clock_pos[i])]
    A2 += [max(A2[i], r2 - (c - clock_pos[-i-1]))]

ans = 0
for j in range(n-1):
    ans = max(ans, A1[j+1] + A2[n - j - 1] - clock_pos[j], A2[j+1] + A1[n - j - 1] - (c - clock_pos[-j-1]))

print(max(ans, A1[-1], A2[-1]))