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
from decimal import Decimal

mod = 10 ** 9 + 7
INF = 10 ** 13
sys.setrecursionlimit(2147483647)
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


n = I()
A = []
B = []
for _ in range(n):
    a, b = LI()
    A += [a]
    B += [b]

A.sort()
B.sort()
if n % 2:
    print(B[n // 2] - A[n // 2] + 1)
else:
    print((B[n // 2] + B[n // 2 - 1]) - (A[n // 2] + A[n // 2 - 1]) + 1)