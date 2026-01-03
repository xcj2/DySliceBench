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
A=LI()
l = [0,0,0,0,0,0,0,0]
x=0
for a in A:
	if a <= 399:
		l[0]+=1
	elif a<= 799:
		l[1] += 1
	elif a <= 1199:
		l[2] += 1
	elif a <= 1599:
		l[3] += 1
	elif a <= 1999:
		l[4] += 1
	elif a<= 2399:
		l[5]+=1
	elif a<= 2799:
		l[6]+=1
	elif a<=3199:
		l[7]+=1
	else:
		x+=1
	
ans =sum(1 if i>0 else 0 for i in l)
if ans==0:
	print(1, end=" ")
else:
	print(ans,end=" ")

print(ans+x)
	
		
	
