from collections import defaultdict 
import sys
import heapq
sys.setrecursionlimit(10**8)

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



#N:頂点数 E:辺数 
N,E = map(int,input().split())

#Union-Find
table = [i for i in range(N)]	#木の親 table[x] == x なら根	
rank  = [1 for i in range(N)]	#木の長さ

# 優先度付きキューの作成
q = []
heapq.heapify(q)

#rout辞書
rout = defaultdict(set)
for i in range(E):
	a,b,w = list(map(int,input().split()))
	rout[a].add(b)
	rout[b].add(a)
	heapq.heappush(q,[w,a,b])

weight = 0
	
while q:
	w,a,b = heapq.heappop(q)
	
	if not Check(a,b):
		weight += w
		Union(a,b)
		
print(weight)
