#a = int(input())
#b,c = map(int,input().split())
#s = input()
#list_s = list(input())
#list_int = list(map(int,input().split()))

#list = [0 for i in range(n)]
#dp = [[0 for i in range(A)] for j in range(B)]

#list_int 並べて出力 print (' '.join(map(str,ans_li)))
#list_str 並べて出力 print (' '.join(list))

# 2進数 format(10, 'b') # '1010'

# aa=[int(input()) for i in range(n)]

#for i,name in enumerate(list)

''' 二次元配列を一列ずつ
for i in ans:
	print(*i)
'''
''' heapq
queue = []
heapq.heapify(queue) #heapqの作成
heapq.heappush(queue,num) #numのpush(値の追加)
pop = heapq.heappop(queue) #numのpop(最小値の出力)
pop = heapq.heappushpop(queue,num) #push -> pop

'''

from collections import defaultdict
import sys,heapq,bisect,math,itertools,string
sys.setrecursionlimit(10**8)
INF = float('inf')
mod = 10**9+7
AtoZ = [chr(i) for i in range(65,65+26)]
atoz = [chr(i) for i in range(97,97+26)]

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



N = int(input())


#Union-Find
table = [i for i in range(N)]	#木の親 table[x] == x なら根
rank  = [1 for i in range(N)]	#木の長さ

# 優先度付きキューの作成
q = []
heapq.heapify(q)


xys = [list(map(int,input().split()))+[i] for i in range(N)]
xys.sort()
for i in range(N-1):
	xa,ya,a = xys[i]
	xb,yb,b = xys[i+1]
	heapq.heappush(q,[xb-xa,a,b])

xys.sort(key=lambda x:x[1])
for i in range(N-1):
	xa,ya,a = xys[i]
	xb,yb,b = xys[i+1]
	heapq.heappush(q,[yb-ya,a,b])

#総コスト
weight = 0


while q:
	w,a,b = heapq.heappop(q)

	if not Check(a,b):
		weight += w
		Union(a,b)

print(weight)
