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
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def pf(s): return print(s, flush=True)

N = I()
A = sorted(LI())
B = sorted(LI())
C = sorted(LI())

BC = []
for b in B:
    idx = bisect.bisect_right(C, b)
    BC.append(len(B)-idx)

b_ac = [0]
for b in reversed(BC):
    b_ac.append(b+b_ac[-1])
b_ac.sort(reverse=True)
#  print(b_ac)
result = 0
for a in A:
    idx = bisect.bisect_right(B, a)
    result += b_ac[idx]
print(result)
