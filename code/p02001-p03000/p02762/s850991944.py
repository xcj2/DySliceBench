# union fine tree

n, m, k = map(int, input().split())

# init
parent = [i for i in range(n)]
rank = [1] * n
size = [1] * n

def find(x):
	if parent[x] == x:
		return x
	else:
		parent[x] = find(parent[x])
		return parent[x]

def unite(x, y):
	x, y = find(x), find(y)
	if x == y:
		return 
	if rank[x] < rank[y]:
		parent[x] = y
		size[y] += size[x]
	else:
		parent[y] = x
		size[x] += size[y]
		if rank[x] == rank[y]:
			rank[x] += 1

def same(x, y):
	return find(x) == find(y)

def groupSize(x):
	return size[find(x)]

A, B = [0] * m, [0] * m
C, D = [0] * k, [0] * k

net = [[] for _ in range(n)]

for i in range(m):
	a, b = map(int, input().split())
	A[i] = a - 1
	B[i] = b - 1
	net[A[i]].append(B[i])
	net[B[i]].append(A[i])
	unite(A[i], B[i])

for i in range(k):
	c, d = map(int, input().split())
	C[i] = c - 1
	D[i] = d - 1
	if same(C[i], D[i]):
		net[C[i]].append(D[i])
		net[D[i]].append(C[i])

res = [0] * n
for i in range(n):
	res[i] = groupSize(i) - len(net[i]) - 1
print(*res)