import math, string, itertools, fractions, heapq, collections, re,  array, bisect, sys, random, time, copy, functools, os, pdb
sys.setrecursionlimit(10**7)
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
N = _I()
B = LI()

"""
Bの値は、A, A+1の最大値
2 5 なら
A[1]は2でなくてはならない
? 2 ?
なんでも 2 5と決まる
2 2 5


3なら
3 3

5
 0 153 10 10 23なら
6
0 0 10 10 10 23

0 0 ? ? ? ?
0 0 10 10 ? ?
0 0 10 10 10 ?
0 0 10 10 10 23
最小値から決めていく
"""

A = [None] * N
#  print('a', A)
while any(a == None for a in A):
    min_idx = B.index(min(B))
    #  print(min_idx)
    if A[min_idx] is None:
        A[min_idx] = B[min_idx]
    if A[min_idx+1] is None:
        A[min_idx+1] = B[min_idx]
    B[min_idx] = inf

#  print(A)
print(sum(A))
