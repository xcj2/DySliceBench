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
N = int(input())

#Union-Find
table = [i for i in range(N)]	#木の親 table[x] == x なら根	
rank  = [1 for i in range(N)]	#木の長さ

# 優先度付きキューの作成
q = []
heapq.heapify(q)


rout = []

for i in range(N):
	x,y = list(map(int,input().split()))
	rout.append([i,x,y])
	
# y順ソートルート
rout.sort(key=lambda x:x[2])
for i in range(N-1):	
	n1,x1,y1 = rout[i]
	n2,x2,y2 = rout[i+1]
	w = y2 - y1
	heapq.heappush(q,[w,n1,n2])


# x順ソートルート
rout.sort(key=lambda x:x[1])
for i in range(N-1):	
	n1,x1,y1 = rout[i]
	n2,x2,y2 = rout[i+1]
	w = x2 - x1
	heapq.heappush(q,[w,n1,n2])

	

#総コスト	
weight = 0


while q:
	w,a,b = heapq.heappop(q)
	
	if not Check(a,b):
		weight += w
		Union(a,b)
		
print(weight)