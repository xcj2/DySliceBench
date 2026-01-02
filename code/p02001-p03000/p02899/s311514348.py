import math, string, itertools, fractions, heapq, collections, re,  array, bisect, sys, random, time, copy, functools, os, pdb
sys.setrecursionlimit(10**7)
from queue import PriorityQueue
inf = 10 ** 20
eps = 1.0 / 10**10
mod = 10**9+7
dd = [(-1, 0), (0, 1), (1, 0), (0, -1)]
ddn = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def _I(): return int(sys.stdin.readline())
def _F(): return float(sys.stdin.readline())
def _pf(s): return print(s, flush=True)
def perr(s): return print(s, file=sys.stderr)
"""
"""
N = _I()
A = LI()

A = [[i, idx+1] for idx, i in enumerate(A)]
#  print(A)
A.sort(key=lambda x: x[0])
A = [str(i[1]) for i in A]
print(' '.join(A))
