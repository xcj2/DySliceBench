from collections import defaultdict,deque
import sys,heapq,bisect,math,itertools,string,queue,datetime
sys.setrecursionlimit(10**8)
INF = float('inf')
mod = 10**9+7
eps = 10**-7
def inp(): return int(input())
def inpl(): return list(map(int, input().split()))
def inpls(): return list(input().split())

N,M = inpl()
ed = defaultdict(lambda:False)
for i in range(M):
	a,b = inpl()
	if a == 1:
		if ed[b]:
			print('POSSIBLE')
			sys.exit()
		else:
			ed[b] = True
	elif b == N:
		if ed[a]:
			print('POSSIBLE')
			sys.exit()
		else:
			ed[a] = True

print('IMPOSSIBLE')
