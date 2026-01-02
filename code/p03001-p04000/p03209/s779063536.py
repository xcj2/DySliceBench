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


n, x = LI()
p = [0] * n
a = [0] * n
a[0] = p[0] = 1
for i in range(1, n):
    a[i] = 2 * a[i - 1] + 3
    p[i] = 2 * p[i - 1] + 1


def f(n, x):
    if x==1:
        return 0 if n else 1
    elif 1 < x <= 1 + a[n - 1]:
        return f(n - 1, x - 1)
    elif x == a[n - 1] + 2:
        return p[n - 1] + 1
    elif x <= 2 * a[n - 1] + 2:
        return f(n - 1, x - a[n - 1] - 2) + p[n - 1] + 1
    else:
        return 2 * p[n - 1] + 1


print(f(n, x))