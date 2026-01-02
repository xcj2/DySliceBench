import math, string, itertools, fractions, heapq, collections, re,  array, bisect, sys, random, time, copy, functools
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

N = _I()
A = LI()
B = LI()

"""
左からみていったときの不都合
特になし
"""
all_count = sum(A)
for bidx in range(len(B)):
    diff = min(A[bidx], B[bidx])
    A[bidx] -= diff
    B[bidx] -= diff
    diff = min(A[bidx+1], B[bidx])
    A[bidx+1] -= diff
    B[bidx] -= diff
final_count = sum(A)

#  print(all_count, final_count)
print(all_count - final_count)
