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

H,W=LI()
if H%3==0 or W%3==0:
	print(0)
	exit()
ans=inf
for h in range(H//2, H):
	items=[(H-h)*W, h*(W//2), h*(W-(W//2))]

	big=max(items)
	sml=min(items)
	ans = min(ans,big-sml)
	items=[(H-h)*W,(h//2)*W, (h-(h//2))*W]
	big=max(items)
	sml=min(items)
	ans = min(ans,big-sml)
	#(((() print(h,big,sml,items)

for w in range(W//2, W):
	items=[(W-w)*H,w*(H//2),w*(H-(H//2))]

	big=max(items)
	sml=min(items)
	ans=min(ans,big-sml)
	
	items=[(W-w)*H,(w//2)*H, (w-(w//2))*H]
	big=max(items)
	sml=min(items)
	ans = min(ans,big-sml)

print(ans)
