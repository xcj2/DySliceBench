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

L, R = LI()

#LRの差が2019以上の場合、答えは絶対0になる。
#例えば、2019*10098は余り0になる
if R - L >= 2019 or L == 0:
    print(0)
    exit()

# 差が2019未満の場合、全部確かめる。

result = inf
for i in range(L, R):
    for j in range(i + 1, R+1):
        result = min(result, (i*j)%2019)
print(result)
