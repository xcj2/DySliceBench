from collections import defaultdict,deque
import sys,heapq,bisect,math,itertools,string,queue,datetime
sys.setrecursionlimit(10**8)
INF = float('inf')
mod = 10**9+7
eps = 10**-7
def inpl(): return list(map(int, input().split()))
def inpl_s(): return list(input().split())

N,M = inpl()
lines = defaultdict(set)
for _ in range(M):
	a,b = inpl()
	a,b = a-1,b-1
	lines[a].add(b)
	lines[b].add(a)

ans = 0

def search(s,ed,num):
	global ans

	if num == N:
		ans += 1
	else:
		for t in lines[s]:
			if not ed & (1<<t):
				search(t,ed+(1<<t),num+1)


search(0,1,1)
print(ans)
