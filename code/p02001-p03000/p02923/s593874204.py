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
H = LI()

# どこからはじめるか
compare_list = []
for i in range(N-1):
    if H[i] >= H[i+1]:
        compare_list.append(True)
    else:
        compare_list.append(False)

perr(compare_list)

streak = 0
ans = 0
for idx, i in enumerate(compare_list):
    if i == True:
        streak = streak + 1
        ans = max(ans, streak)
    else:
        streak = 0
print(ans)
