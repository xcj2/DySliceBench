import sys, math
input = sys.stdin.readline
rs = lambda: input().strip()
ri = lambda: int(input())
rl = lambda: list(map(int, input().split()))
mod = 10**9 + 7

import sys
sys.setrecursionlimit(1000000)

import collections

N, M, P = rl()
E = []
edges = collections.defaultdict(list)
redges = collections.defaultdict(list)
for i in range(M):
	a, b, c = rl()
	E.append((a-1, b-1, P-c))
	edges[a-1].append(b-1)
	redges[b-1].append(a-1)

visited = {}
def dfs(n):
	if n in visited: return
	visited[n] = 1
	for e in edges[n]:
		dfs(e)
rvisited = {}
def rdfs(n):
	if n in rvisited: return
	rvisited[n] = 1
	for e in redges[n]:
		rdfs(e)

dfs(0)
rdfs(N-1)
ok = [False] * N
for n in range(N):
	if n in visited and n in rvisited:
		ok[n] = True
V = list(range(N))

def belmanford(V, E, s=0):
	D = [float('inf')] * len(V)
	D[s] = 0
	P = [None] * len(V)
	update = True
	step = 0
	while update:
		update = False
		for u, v, c in E:
			if not ok[u]: continue
			if not ok[v]: continue
			if D[v] > D[u] + c:
				D[v] = D[u] + c
				P[v] = (u, c)
				update = True
		step += 1
		if step > N:
			return None, None
	return D, P

D, P = belmanford(V, E)
if D == None:
	print(-1)
else:
	print(max(-D[N-1], 0))
