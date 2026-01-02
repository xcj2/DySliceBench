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


def gcd(x, y):
    while y:
        x, y = y, x % y
    return x


t = I()
for i in range(t):
    a, b, c, d = LI()
    g = gcd(b, d)
    if b > d or a < b:
        print('No')
    elif c >= b - 1:
        print('Yes')
    elif (a - (b - 1) - 1) // g != (a - (c + 1)) // g:
        print('No')
    else:
        print('Yes')