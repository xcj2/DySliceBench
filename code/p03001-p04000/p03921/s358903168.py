from collections import defaultdict,deque
import sys,heapq,bisect,math,itertools,string,queue,datetime
sys.setrecursionlimit(10**8)
INF = float('inf')
mod = 10**9+7
eps = 10**-7
def inp(): return int(input())
def inpl(): return list(map(int, input().split()))
def inpls(): return list(input().split())

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

table = [i for i in range(N+M)]	#木の親 table[x] == x なら根
rank  = [1 for i in range(N+M)]	#木の長さ

for i in range(N):
	tmp = inpl()
	for k in range(tmp[0]):
		l = tmp[k+1]
		Unite(i,l+N-1)

tmp = Find(0)
for i in range(N):
	if tmp != Find(i):
		print('NO')
		sys.exit()
print('YES')
