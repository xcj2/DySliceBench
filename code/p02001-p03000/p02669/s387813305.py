from collections import defaultdict, deque, Counter
from heapq import heappush, heappop, heapify
import math
import bisect
import random
from itertools import permutations, accumulate, combinations, product
import sys
import string
from bisect import bisect_left, bisect_right
from math import factorial, ceil, floor, cos, radians, pi, sin
from operator import mul
from functools import reduce
from operator import mul


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


t = I()
for _ in range(t):
    n, a, b, c, d = LI()
    D = defaultdict(int)
    def f(x):
        if D[x]:
            return D[x]
        if x == 0:
            return 0
        if x == 1:
            return d
        ret = INF
        ret = min(ret, f(x // 2) + x % 2 * d + a)
        ret = min(ret, f(x // 3) + x % 3 * d + b)
        ret = min(ret, f(x // 5) + x % 5 * d + c)
        if x % 2:
            ret = min(ret, f(x // 2 + 1) + (2 - x % 2) * d + a)
        if x % 3:
            ret = min(ret, f(x // 3 + 1) + (3 - x % 3) * d + b)
        if x % 5:
            ret = min(ret, f(x // 5 + 1) + (5 - x % 5) * d + c)
        ret = min(ret, x * d)
        D[x] = ret
        return ret

    print(f(n))