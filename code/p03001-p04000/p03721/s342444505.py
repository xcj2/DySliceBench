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

N,K=LI()
A=[]
B=[]
AB=[]
for i in range(N):
	a,b=LI()
	A.append(a)
	B.append(b)
	AB.append([a,b])
A=list(set(A))
A.sort()
counts={}
for a in A:
	counts[a]=0

for ab in AB:
	counts[ab[0]]+=ab[1]
if K<N/2:
	c=0
	for item in A:
		c+=counts.get(item)
		if c>=K:
			print(item)
			exit()
else:
	c=sum(B)
	for item in reversed(A):
		c-=counts.get(item)
		if c<K:
			print(item)
			exit()
		
	



