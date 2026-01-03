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
def pf(s): return print(s, flush=True)

N=_I()

def F(A,B):
	return max(len(str(A)),len(str(B)))

#高々10**5まで見れば良い
ans=inf
for i in range(1,min(N+1,10**5+3)):
	if N%i==0:
		ans=min(ans,F(i,int(N/i)))
#ans=min(ans, F(1,N))
print(ans)
	
