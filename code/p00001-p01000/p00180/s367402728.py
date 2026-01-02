# AOJ 0180 Demolition of Bridges
# Python3 2018.6.22

# UNION-FIND library
MAX = 105
id, size = [0]*MAX, [0]*MAX

def init(n):
	for i in range(n): id[i], size[i] = i, 1
	
def root(i):
	while i != id[i]:
		id[i] = id[id[i]]
		i = id[i]
	return i
	
def connected(p, q): return root(p) == root(q)
	
def unite(p, q):
	i, j = root(p), root(q)
	if i == j: return
	if size[i] < size[j]:
		id[i] = j
		size[j] += size[i]
	else:
		id[j] = i
		size[i] += size[j]
# UNION-FIND library

# 最小全域木。V:総ノード数、E:枝情報(a,b,cost)
def kruskal(V, edge):
	ee = sorted(edge, key=lambda x:(x[2]))
	init(V)
	ans = 0
	for e in ee:
		if not connected(e[0], e[1]):
			unite(e[0], e[1])
			ans += e[2]
	return ans;

while 1:
	n, m = map(int, input().split())
	if n == 0: break
	edge = []
	for i in range(m):
		s, t, w = map(int, input().split())
		edge.append((s, t, w))
	print(kruskal(n, edge))
