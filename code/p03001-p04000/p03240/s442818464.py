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
import pprint
sys.setrecursionlimit(10 ** 9)


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


n = I()
X = []
Y = []
H = []
ans = ()
for i in range(n):
    x, y, h = LI()
    if h:
        r = i
    X += [x]
    Y += [y]
    H += [h]




for cx in range(101):
    for cy in range(101):
        x0, y0, h0 = X[r], Y[r], H[r]
        h = h0 + abs(cx - x0) + abs(cy - y0)
        for i in range(n):
            if H[i] != max(h - abs(cx - X[i]) - abs(cy - Y[i]), 0):
                break
        else:
            print(cx, cy, h)
            exit()


