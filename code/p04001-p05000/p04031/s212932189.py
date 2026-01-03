import math, string, itertools, fractions, heapq, collections, re,  array, bisect, sys, random, time, copy, functools,pdb
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

"""
全数字を例えば1に変える場合など、試していけば良い
"""

ans = []
for i in range(min(A), max(A)+1):
    tmp = 0
    for a in A:
        tmp += abs(a - i) ** 2
    ans.append(tmp)

print(min(ans))

