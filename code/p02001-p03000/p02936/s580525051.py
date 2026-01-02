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

if 'LOCAL' in os.environ:
    N = 2* 10** 5
    Q = 2 * 10 ** 5
    AB = [[i, i + 1] for i in range(1, N)]
    PX = [[i, 10] for i in range(Q)]
else:
    N, Q = LI()
    AB = []
    PX = []
    for i in range(N-1):
        AB.append(LI())

    for i in range(Q):
        PX.append(LI())


"""
そもそも各頂点の部分木をdictに入れましょうか？
参照するような形で。
2には3
3には4,5
4,5はNoneだと、参照しやすいか？

カウントを若い順にやっていく
"""
AB = sorted(AB, key=lambda x: x[0])
perr('AB')
perr(AB)
d = {}
for p, x in PX:
    if p not in d.keys():
        d[p] = 0
    d[p] += x
for a, b in AB:
    if b not in d.keys():
        d[b] = 0
    if a not in d.keys():
        d[a] = 0
    d[b] += d[a]
for i in range(1, N+1):
    print(d[i], end=' ')
