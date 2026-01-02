import sys

sys.setrecursionlimit(10**8)

def find(x):	#xの根を返す
	global table
	global diff_weight
	
	if table[x] == x:
		return x
	else:
		root = find(table[x])
		diff_weight[x] += diff_weight[table[x]] #親の更新に伴う 重みの更新
		table[x] = root	#親の更新(根を直接親にして参照距離を短く)
		return table[x]

def union(x,y,w):	#xとyを diff(x,y)=w で繋げる
	w = w - weight(y) + weight(x) 
	x = find(x)	
	y = find(y)
	
	if x == y:
		return
	
	if rank[x] < rank[y]:
		x,y = y,x
		w = -w
	
	table[y] = x
	diff_weight[y] = w
	
	if rank[x] == rank[y]:
			rank[y] += 1

def check(x,y): #xとyか繋がっているか -> return bool
	if find(x) == find(y):
		return True
	else:
		return False

def weight(x):
	find(x)	#経路圧縮
	return diff_weight[x]
		
def diff(x,y): # weight(y)-weight(x)  (繋がってる前提)
	return (weight(y) - weight(x))

		
N,M = map(int,input().split())

table = [i for i in range(N)]	#木の親 table[x] == x なら根	
rank  = [1 for i in range(N)]	#木の長さ
diff_weight = [0 for i in range(N)]


for i in range(M):
	a,b,D = (map(int,input().split()))
	a -= 1
	b -= 1
	if check(a,b):
		if diff(a,b) != D:
			print('No')
			sys.exit()
	else:
		union(a,b,D)
	
	
print ('Yes')