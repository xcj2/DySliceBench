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
def _I(): return int(input())
def _F(): return float(sys.stdin.readline())
def pf(s): return print(s, flush=True)

N=_I()
A=LI()

Aac=[A[0]]

for aidx in range(1,N):
	Aac.append(Aac[aidx-1]+A[aidx])
ans=10**18
for a in Aac[:-1]:
	ans=min(ans,abs((Aac[-1]-a)-a))
print(ans)