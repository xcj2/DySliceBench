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
F = []
for i in range(N):
    F.append(LI())
P = []
for i in range(N):
    P.append(LI())

"""
各時間帯をon/offで2通り全探索すると、2**10になる。
"""
ans = -10**18
def dfs(l):
    global ans
    if len(l) == 10:
        if all(item == 0 for item in l):
            return
        # 探索終了
        point = 0
        for n in range(N):
            s = sum([f for fidx, f in enumerate(F[n]) if f == l[fidx] == 1])
            point += P[n][s]
        ans = max(ans, point)
        return
    dfs(l + [0])
    dfs(l + [1])

dfs([])
print(ans)
