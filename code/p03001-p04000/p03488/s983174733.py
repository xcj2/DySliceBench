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



s = S()
x, y = LI()
components = [len(i) for i in s.split('T')]
initial_x = components[0]
components = components[1:]
y_component = [j for j in components[::2] if j]
x_component = [j for j in components[1::2] if j]
x_len = len(x_component)
y_len = len(y_component)
x_D = defaultdict(int)
y_D = defaultdict(int)


x_D[initial_x] = 1
for i in range(x_len):
    nxt_x_D = defaultdict(int)
    for pos in x_D.keys():
        nxt_x_D[pos + x_component[i]] = nxt_x_D[pos - x_component[i]] = 1
    x_D = nxt_x_D


y_D[0] = 1
for i in range(y_len):
    nxt_y_D = defaultdict(int)
    for pos in y_D.keys():
        nxt_y_D[pos + y_component[i]] = nxt_y_D[pos - y_component[i]] = 1
    y_D = nxt_y_D



if x_D[x] and y_D[y]:
    print('Yes')
else:
    print('No')