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
def pf(s): return print(s, flush=True, end="")

sx,sy,tx,ty=LI()

for i in range(abs(ty-sy)):
	pf("U")

for i in range(abs(sx-tx)):
	pf("R")

for i in range(abs(ty-sy)):
	pf("D")
	
for i in range(abs(sx-tx)):
	pf("L")

pf("L")

for i in range(abs(ty-sy)):
	pf("U")
pf("U")
pf("R")

for i in range(abs(sx-tx)):
	pf("R")
	
pf("D")

pf("R")

for i in range(abs(ty-sy)):
	pf("D")
pf("D")
pf("L")
for i in range(abs(tx-sx)):
	pf("L")
pf("U")