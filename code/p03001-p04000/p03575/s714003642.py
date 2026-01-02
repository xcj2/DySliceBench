from collections import defaultdict
import sys,heapq,bisect,math,itertools,string,queue,datetime
sys.setrecursionlimit(10**8)
INF = float('inf')
mod = 10**9+7
eps = 10**-7
AtoZ = [chr(i) for i in range(65,65+26)]
atoz = [chr(i) for i in range(97,97+26)]

def inpl(): return list(map(int, input().split()))
def inpl_s(): return list(input().split())


def Find(x):	#xの根を返す
	global table

	if table[x] == x:
		return x
	else:
		table[x] = Find(table[x])	#親の更新(根を直接親にして参照距離を短く)
		return table[x]

def Unite(x,y):	#xとyを繋げる
	x = Find(x)
	y = Find(y)

	if x == y:
		return

	if rank[x] > rank[y]:
		table[y] = x
	else:
		table[x] = y
		if rank[x] == rank[y]:
			rank[y] += 1

def Check(x,y):
	if Find(x) == Find(y):
		return True
	else:
		return False

N,M = inpl()

lines = [inpl() for i in range(M)]
ans = 0
for j in range(M):
	table = [_ for _ in range(N+1)]
	rank  = [1 for _ in range(N+1)]
	for i in range(M):
		if i == j:
			continue
		x,y = lines[i]
		Unite(x,y)
	x,y = lines[j]

	if not Check(x,y):
		ans += 1

print(ans)
