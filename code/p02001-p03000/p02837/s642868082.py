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

N = _I()
X=[]
for i in range(N):
	x=[]

	for j in range(_I()):
		x.append(LI())
	X.append(x)
	
#print(X)
ans=[]

#2の15乗通りしかないので、全部見る
def dfs(idx, ls):
	if idx == N:
		# あってるか確認
		ok = True
		#print("ls",ls)
		for lidx, l in enumerate(ls):
			#print(lidx , l)
		
			if l != 1: continue
			for x in X[lidx]:
				#print("x",x)
			
				if ls[x[0]-1] != x[1]:
					ok=False
					break
		if ok:
			#print("ok", ls)
		
			ans.append(sum(ls))
		
			
		
		
		return
	# 通りを作る
	dfs(idx+1, ls+[0])
	dfs(idx+1, ls+[1])

dfs(0, [])
print(max(ans))

				
			
		
	
		
	
	
