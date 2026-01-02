import math, string, itertools, fractions, heapq, collections, re, \
array, bisect, sys, random, time, copy, functools, os, queue, pdb
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


M, D = LI()

"""
20何日
1の位が2以上
30日はだめ
8/24
2*4=8

"""
if D <= 21:
    print(0)
    exit()

ans = 0
for m in range(1, M+1):
    for d in range(22, D+1):
        d10 = str(d)[0]
        d1 = str(d)[1]
        #  print(d10, d1)
        if int(d1) >= 2 and int(d10) * int(d1) == m:
            #  print(d10, d1)
            ans += 1

print(ans)
