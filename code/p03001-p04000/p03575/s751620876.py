import sys

if sys.platform =='ios':
	sys.stdin=open('Untitled.txt')
input = sys.stdin.readline
def INT(): return int(input())
def MAP(): return [int(s) for s in input().split()]

def dfs(G, v):
	seen[v] += 1
	#print('v :', v)
	
	for nv in G[v]:
		if seen[nv]: continue
		#print('v nv :', v, nv, 'Recursion')
		dfs(G, nv)

N, M = MAP()
A = [MAP() for _ in range(M)]

#print(A)

ans = 0
for i in range(M):
	G = [[] for _ in range(N)]
	for j, m in enumerate(A):
		# i!=jのとき辺を追加しない
		if i != j:
			a, b = m
			G[a-1].append(b-1)
			G[b-1].append(a-1)
		
	seen = [0] * N
	dfs(G, 1)
	#print(i, j, seen)
	
	if sum(seen) != N: ans += 1

print(ans)