from collections import defaultdict, deque, Counter
from heapq import heappush, heappop, heapify
import math
import bisect
import random
from itertools import permutations, accumulate
import sys



def LI(): return list(map(int, sys.stdin.readline().split()))
def I(): return int(sys.stdin.readline())
def LIM(): return list(map(lambda x:int(x) - 1, sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def S(): return sys.stdin.readline()
def IR(n): return [I() for i in range(n)]
def LIR(n): return [LI() for i in range(n)]
def LIRM(n): return [LIM() for i in range(n)]
def SR(n): return [S() for i in range(n)]
def LSR(n): return [LS() for i in range(n)]
def SRL(n): return [list(S()) for i in range(n)]
mod = 1000000007



n, x = LI()
a, p = [1], [1]
for i in range(n):
    a += [a[i] * 2 + 3]
    p += [p[i] * 2 + 1]


def f(n, x):
    if n == 0:
        return x
    elif x == a[n]:
        return p[n]
    elif x <= 1:
        return 0
    elif 1 < x <= 1 + a[n - 1]:
        return f(n - 1, x - 1)
    else:
        return p[n - 1] + 1 + f(n - 1, x - a[n - 1] - 2)



print(f(n, x))
