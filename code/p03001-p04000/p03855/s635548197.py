import sys
import itertools
from collections import defaultdict

sys.setrecursionlimit(10**8)

def find(x,table):	#xの根を返す	
	if table[x] == x:
		return x
	else:
		table[x] = find(table[x],table)	#親の更新(根を直接親にして参照距離を短く)
		return table[x]

def union(x,y,table,rank):	#xとyを繋げる
	x = find(x,table)	
	y = find(y,table)
	
	if x == y:
		return
	
	if rank[x] > rank[y]:
		table[y] = x
	else:
		table[x] = y
		if rank[x] == rank[y]:
			rank[y] += 1

def check(x,y,table):
	if find(x,table) == find(y,table):
		return True
	else:
		return False

N,K,L = map(int,input().split())

table_car = [i for i in range(N)]	#木の親 table[x] == x なら根	
rank_car  = [1 for i in range(N)]	#木の長さ
table_tr  = [i for i in range(N)] 
rank_tr   = [1 for i in range(N)]

for i in range(0,K):
	a,b = map(int, input().split())
	union(a-1,b-1,table_car,rank_car)
	
for i in range(0,L):
	a,b = map(int, input().split())
	union(a-1,b-1,table_tr,rank_tr)
	
ar = [(find(i,table_car),find(i,table_tr)) for i in range(N)]
dd = defaultdict(int)
for s in ar:
    dd[s] += 1
	
ans =[]
for i in range(N):
    ans.append(dd[ar[i]])
	
print(' '.join(map(str, ans)))
