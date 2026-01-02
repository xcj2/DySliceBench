from collections import defaultdict
import sys,heapq,bisect,math,itertools,string,queue,datetime
sys.setrecursionlimit(10**8)
INF = float('inf')
mod = 10**9+7
eps = 10**-7
AtoZ = [chr(i) for i in range(65,65+26)]
atoz = [chr(i) for i in range(97,97+26)]

def inpl(): return list(map(int, input().split()))
def inpl_str(): return list(input().split())

def Find(x):	#xの根を返す
	global table

	if table[x] == x:
		return x
	else:
		table[x] = Find(table[x])	#親の更新(根を直接親にして参照距離を短く)
		return table[x]

def Union(x,y):	#xとyを繋げる
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

table = [i for i in range(N)]	#木の親 table[x] == x なら根
rank  = [1 for i in range(N)]	#木の長さ

pp = inpl()

for i in range(M):
	x,y = inpl()
	x -= 1
	y -= 1
	Union(x,y)

ans = 0
for i in range(N):
	if Check(pp[i]-1,i):
		ans += 1

print(ans)