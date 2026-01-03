import sys
sys.setrecursionlimit(10**6)

class Edge:
	def __init__(self, v1, v2, w):
		self.v1 = v1
		self.v2 = v2
		self.w = w
	def __repr__(self):
		return 'Edges({},{},{})'.format(self.v1, self.v2, self.w)

def dfs(edges, v, visited, i, m, r):
	m[0 if i<r else 1] = min(m[0 if i<r else 1], v[i])
	for edge in edges[i]:
		if visited[edge.v2]:
			if (v[i] + v[edge.v2]) != edge.w:
				return False
			continue
		visited[edge.v2] = True
		v[edge.v2] = edge.w - v[i]
		if not dfs(edges, v, visited, edge.v2, m, r):
			return False
	return True

r, c = map(int, input().split())
edges = [list() for _ in range(r + c)]
v = [0] * (r + c)
visited = [False] * (r + c)
n = int(input())
for _ in range(n):
	ri, ci, ai = map(int, input().split())
	ri, ci = ri-1, ci-1
	edges[ri].append(Edge(ri, r+ci, ai))
	edges[r+ci].append(Edge(r+ci, ri, ai))

flag = True
for i in range(r + c):
	if visited[i]:
		continue
	m = [10**10, 10**10]
	if (not dfs(edges, v, visited, i, m, r)) or sum(m) < 0:
		flag = False
if flag:
	print('Yes')
else:
	print('No')
